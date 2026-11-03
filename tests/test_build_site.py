"""Build and optional real Chromium tests; synthetic bank stays in tmp_path."""
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

import pytest

from test_quiz import ROOT, fixture_sources, write_fixture


def builder():
    assert importlib.util.find_spec("build_site"), "site builder is not implemented"
    import build_site
    return build_site


def test_build_embeds_real_data_without_network_or_evidence_paths(tmp_path):
    bank = write_fixture(tmp_path)
    ledger_path = tmp_path / "sources/ledger.json"
    ledger = json.loads(ledger_path.read_text())
    ledger["sources"][0]["quotes"] = [{"from": "/private/secret", "text": "not public"}]
    ledger_path.write_text(json.dumps(ledger))
    output = tmp_path / "quiz.html"
    builder().build_site(tmp_path, output)
    html = output.read_text(encoding="utf-8")
    payload = json.loads(re.search(r'<script id="quiz-data" type="application/json">(.*?)</script>', html, re.S).group(1))
    assert sorted(payload["questions"], key=lambda q: q["id"]) == sorted(bank, key=lambda q: q["id"])
    assert payload["sources"]["1"] == fixture_sources()[1]
    assert "/private/secret" not in html
    assert "fetch(" not in html
    assert "<html lang=\"fr\"" in html
    result = subprocess.run([sys.executable, str(ROOT / "tools/build_site.py"), "--root", str(tmp_path), "--output", str(output)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_embedded_json_cannot_close_script_or_inject_html(tmp_path):
    bank = write_fixture(tmp_path)
    dangerous = '</script><img src=x onerror="alert(1)">&\u2028\u2029'
    bank[0]["question"] = dangerous
    (tmp_path / "questions/essential.json").write_text(json.dumps([q for q in bank if q["domain"] == "essential"]))
    output = tmp_path / "quiz.html"
    builder().build_site(tmp_path, output)
    html = output.read_text()
    assert dangerous not in html
    payload = re.search(r'<script id="quiz-data" type="application/json">(.*?)</script>', html, re.S).group(1)
    assert "<" not in payload and "&" not in payload
    assert json.loads(payload)["questions"][0]["question"] == dangerous


def test_build_refuses_incomplete_bank(tmp_path):
    write_fixture(tmp_path)
    (tmp_path / "questions/operations.json").write_text("[]")
    output = tmp_path / "quiz.html"
    with pytest.raises(ValueError, match="questions"):
        builder().build_site(tmp_path, output)
    assert not output.exists()


@pytest.fixture
def page(tmp_path):
    playwright = pytest.importorskip("playwright.sync_api", reason="Tests navigateur facultatifs : installer playwright et Chromium.")
    chromium = shutil.which("chromium") or shutil.which("chromium-browser")
    if not chromium:
        pytest.skip("Chromium absent ; tests Python disponibles sans navigateur.")
    write_fixture(tmp_path)
    target = builder().build_site(tmp_path, tmp_path / "quiz.html")
    from playwright._impl._driver import compute_driver_executable
    driver_node, driver_cli = compute_driver_executable()
    if not Path(driver_node).is_file() or not Path(driver_cli).is_file():
        pytest.skip("Installation Playwright incomplète : utiliser pip install playwright dans un venv.")
    with playwright.sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chromium, headless=True, args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": 390, "height": 844}, offline=True)
        page.set_default_timeout(1500)
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(target.as_uri())
        yield page
        browser.close()
        assert not errors


def start(page, mode="exam", exam="A"):
    page.locator("#mode").select_option(mode)
    page.locator("#exam").select_option(exam)
    page.locator("#start").click()


def test_browser_exam_no_feedback_until_finish_then_locked(page):
    start(page)
    assert page.locator("#timer").inner_text() == "60:00"
    assert page.locator("#progress").inner_text() == "Question 1/50 — 0 réponse(s)"
    assert "Justification" not in page.locator("body").inner_text()
    page.locator('input[value="A"]').check()
    page.locator("#submit-answer").click()
    assert "Justification" not in page.locator("body").inner_text()
    page.locator("#next").click()
    page.locator("#previous").click()
    assert page.locator('input[value="A"]').is_checked()
    page.locator("#finish").click()
    assert "1/50" in page.locator("#results").inner_text()
    assert "essential : 1/19" in page.locator("#results").inner_text()
    assert "infrastructure : 0/20" in page.locator("#results").inner_text()
    assert "operations : 0/11" in page.locator("#results").inner_text()
    assert page.locator("#results .correction").count() == 50
    assert page.locator("#results a").first.get_attribute("href") == "https://example.org/evidence"
    assert not page.locator("#session").is_visible()
    assert page.locator("#finish").is_disabled()


def test_browser_learning_feedback_and_restart_clear_everything(page):
    start(page, "learn", "B")
    assert "Sans limite" in page.locator("#timer").inner_text()
    page.locator('input[value="B"]').check()
    assert "Justification" not in page.locator("#feedback").inner_text()
    page.locator("#submit-answer").click()
    assert "Justification" in page.locator("#feedback").inner_text()
    assert "Pourquoi B est faux" in page.locator("#feedback").inner_text()
    assert page.locator('input[value="B"]').is_disabled()
    page.locator("#restart").click()
    assert page.locator("#setup").is_visible()
    assert page.locator("#results").inner_text() == ""
    start(page, "exam", "A")
    assert page.locator("#timer").inner_text() == "60:00"
    assert "0 réponse(s)" in page.locator("#progress").inner_text()
    assert page.locator("input:checked").count() == 0
    assert page.locator("#feedback").inner_text() == ""


def test_browser_expiry_locks_even_between_timer_ticks(page):
    # Advance the real browser's clock, not a substitute JS implementation.
    page.clock.install()
    start(page)
    page.locator('input[value="A"]').check()
    page.clock.fast_forward(3_600_001)
    assert "Temps écoulé" in page.locator("#status").inner_text()
    assert "0/50" in page.locator("#results").inner_text()
    assert page.locator("#timer").inner_text() == "00:00"
    assert page.locator("#submit-answer").is_disabled()
    assert page.locator("#finish").is_disabled()
    page.locator("#restart").click()
    start(page, "exam", "B")
    assert page.locator("#timer").inner_text() == "60:00"
    assert "0 réponse(s)" in page.locator("#progress").inner_text()
    page.clock.fast_forward(1000)
    assert page.locator("#timer").inner_text() == "59:59"


def test_browser_mobile_fits_and_content_is_english(page):
    start(page)
    assert page.locator("#question").get_attribute("lang") == "en"
    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
    assert page.locator("fieldset legend").inner_text()


def test_browser_action_guard_rejects_late_submit_before_interval(page):
    start(page)
    page.locator('input[value="A"]').check()
    page.evaluate("""() => {
      const realNow = Date.now;
      Date.now = () => realNow() + 3600001;
      document.getElementById('submit-answer').click();
    }""")
    assert "Temps écoulé" in page.locator("#status").inner_text()
    assert "0/50" in page.locator("#results").inner_text()


def test_browser_render_uses_text_not_html(page, tmp_path):
    path = tmp_path / "questions/essential.json"
    questions = json.loads(path.read_text())
    dangerous = '</script><img src=x onerror="window.injected=true">&'
    questions[0]["question"] = dangerous
    path.write_text(json.dumps(questions))
    target = builder().build_site(tmp_path, tmp_path / "escaped.html")
    page.goto(target.as_uri())
    start(page)
    assert page.locator("#question").inner_text() == dangerous
    assert page.locator("img").count() == 0
    assert page.evaluate("window.injected === undefined")
