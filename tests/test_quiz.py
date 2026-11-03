"""Isolated synthetic fixtures: never written into the real question bank."""
import copy
import importlib.util
import json
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))


def engine():
    assert importlib.util.find_spec("quiz"), "quiz engine is not implemented"
    import quiz
    return quiz


def fixture_bank():
    bank = []
    for exam in ("A", "B"):
        for domain, prefix, count, objectives in (
            ("essential", "E", 19, 8),
            ("infrastructure", "I", 20, 10),
            ("operations", "O", 11, 4),
        ):
            for i in range(count):
                answer = "ABCD"[i % 4]
                bank.append({
                    "id": f"{prefix}-{i + (0 if exam == 'A' else count) + 1:03}",
                    "exam": exam, "domain": domain,
                    "objective": f"{prefix}{i % objectives + 1:02}",
                    "question": f"Synthetic isolated fixture {exam} {domain} {i}?",
                    "choices": {x: f"Choice {x}" for x in "ABCD"},
                    "answer": answer, "explanation": "Justification française de test.",
                    "distractors": {x: f"Pourquoi {x} est faux." for x in "ABCD" if x != answer},
                    "source_ids": [1], "difficulty": "scenario",
                })
    return bank


def fixture_sources():
    return {1: {"id": 1, "title": "Source de test", "url": "https://example.org/evidence"}}


def write_fixture(root):
    (root / "questions").mkdir()
    (root / "sources").mkdir()
    bank = fixture_bank()
    for domain in ("essential", "infrastructure", "operations"):
        (root / "questions" / f"{domain}.json").write_text(json.dumps([q for q in bank if q["domain"] == domain]), encoding="utf-8")
    (root / "sources" / "ledger.json").write_text(json.dumps({"version": 1, "sources": list(fixture_sources().values())}), encoding="utf-8")
    return bank


def test_validate_bank_accepts_contract():
    assert engine().validate_bank(fixture_bank(), fixture_sources()) is None


@pytest.mark.parametrize("mutation,match", [
    (lambda b: b[1].update(id=b[0]["id"]), "identifiant"),
    (lambda b: b[0].update(answer="E"), "answer"),
    (lambda b: b[0].update(distractors={"A": "wrong"}), "distractors"),
    (lambda b: b[0].update(source_ids=[999]), "source"),
    (lambda b: b[0].update(source_ids=[True]), "source"),
    (lambda b: b[0].update(choices={"A": "only one"}), "choices"),
    (lambda b: b[0].update(choices={x: "identical" for x in "ABCD"}), "choices"),
    (lambda b: b[0].update(answer=["A"]), "answer"),
    (lambda b: b[0].update(objective=["E01"]), "objective"),
    (lambda b: b[0].update(domain=["essential"]), "domaine"),
    (lambda b: b[0].update(question=""), "question"),
    (lambda b: b[0].update(objective="E99"), "objective"),
    (lambda b: b[0].update(difficulty="hard"), "difficulty"),
    (lambda b: b[0].update(exam="C"), "Examen"),
    (lambda b: b.pop(), "questions"),
    (lambda b: b[0].update(domain="operations"), "questions"),
    (lambda b: [q.update(objective="E01") for q in b if q["domain"] == "essential"], "objectifs"),
    (lambda b: b.append(copy.deepcopy(b[0])), "questions"),
])
def test_invalid_bank_rejected(mutation, match):
    bank = fixture_bank()
    mutation(bank)
    with pytest.raises(ValueError, match=match):
        engine().validate_bank(bank, fixture_sources())


def test_unsafe_source_url_rejected():
    sources = fixture_sources()
    sources[1]["url"] = "javascript:alert(1)"
    with pytest.raises(ValueError, match="URL"):
        engine().validate_bank(fixture_bank(), sources)


def test_load_select_score_and_seed(tmp_path):
    write_fixture(tmp_path)
    quiz = engine()
    bank, sources = quiz.load_bank(tmp_path)
    assert sources == fixture_sources()
    selected = quiz.select_exam(bank, "B", seed=42)
    assert len(selected) == 50
    assert selected == quiz.select_exam(bank, "B", seed=42)
    assert selected != quiz.select_exam(bank, "B", seed=43)
    assert all(q["exam"] == "B" for q in selected)
    correct = {q["id"]: q["answer"] for q in selected}
    report = quiz.score(selected, correct)
    assert report["correct"] == report["total"] == 50
    assert report["percent"] == 100
    assert report["domains"] == {d: {"correct": n, "total": n} for d, n in quiz.DOMAIN_COUNTS.items()}
    report = quiz.score(selected, {selected[0]["id"]: selected[0]["answer"]})
    assert report["correct"] == 1
    assert report["unanswered"] == 49
    assert quiz.score(selected, {})["correct"] == 0


def run_cli(root, *args, data=None):
    import subprocess
    return subprocess.run([sys.executable, str(ROOT / "tools/quiz.py"), "--root", str(root), *args], input=data, text=True, capture_output=True, timeout=15)


def test_check_and_markdown_export(tmp_path):
    write_fixture(tmp_path)
    checked = run_cli(tmp_path, "--check")
    assert checked.returncode == 0, checked.stderr
    assert "100 questions" in checked.stdout
    target = tmp_path / "export.md"
    exported = run_cli(tmp_path, "--exam", "A", "--seed", "42", "--export", str(target))
    assert exported.returncode == 0, exported.stderr
    text = target.read_text(encoding="utf-8")
    assert text.count("### ") == 50
    assert "Justification" not in text
    assert "Réponse correcte" not in text
    assert "non officielles" in text
    with_answers = run_cli(tmp_path, "--exam", "B", "--export", str(target), "--with-answers")
    assert with_answers.returncode == 0
    assert "https://example.org/evidence" in target.read_text(encoding="utf-8")
    both = run_cli(tmp_path, "--export-markdown", str(tmp_path / "printed"))
    assert both.returncode == 0, both.stderr
    for letter in "AB":
        printed = (tmp_path / "printed" / f"examen-{letter}.md").read_text(encoding="utf-8")
        assert printed.count("### Question ") == 50
        assert printed.endswith("\n") and not printed.endswith("\n\n")
        assert "## Corrigé" in printed
        assert printed.index("Justification") > printed.index("## Corrigé")


def test_cli_exam_defers_feedback_learning_is_immediate(tmp_path):
    write_fixture(tmp_path)
    exam = run_cli(tmp_path, "--exam", "A", "--mode", "exam", data="A\n" * 50)
    assert exam.returncode == 0, exam.stderr
    assert exam.stdout.index("Justification") > exam.stdout.index("Résultat")
    assert "essential" in exam.stdout and "/50" in exam.stdout
    learn = run_cli(tmp_path, "--exam", "A", "--mode", "learn", data="A\n" * 50)
    assert learn.returncode == 0, learn.stderr
    assert learn.stdout.index("Justification") < learn.stdout.index("Question 2/50")


def test_missing_bank_is_actionable_error(tmp_path):
    result = run_cli(tmp_path, "--check")
    assert result.returncode == 2
    assert "Erreur" in result.stderr
    assert "Traceback" not in result.stderr


def test_cli_timeout_rejects_a_late_answer(monkeypatch, capsys):
    quiz = engine()
    moments = iter([0, 0, 0, 3601])
    monkeypatch.setattr(quiz.time, "monotonic", lambda: next(moments))
    monkeypatch.setattr(quiz, "timed_input", lambda *_: "A")
    questions = quiz.select_exam(fixture_bank(), "A")
    report = quiz.run_session(questions, fixture_sources(), "exam")
    assert report["correct"] == 0
    assert report["unanswered"] == 50
    output = capsys.readouterr().out
    assert "Temps écoulé" in output
    assert output.index("Justification") > output.index("Temps écoulé")


def test_timed_input_does_not_wait_forever(monkeypatch):
    import threading
    quiz = engine()
    release = threading.Event()
    monkeypatch.setattr("builtins.input", lambda _: release.wait(1))
    try:
        with pytest.raises(TimeoutError):
            quiz.timed_input("", timeout=0.01)
    finally:
        release.set()
    with pytest.raises(TimeoutError):
        quiz.timed_input("", timeout=0)


def test_cli_no_answer_and_invalid_input(tmp_path):
    write_fixture(tmp_path)
    result = run_cli(tmp_path, "--exam", "B", "--mode", "exam", data="invalid\n\nFIN\n")
    assert result.returncode == 0, result.stderr
    assert "Choisir A" in result.stdout
    assert "Résultat : 0/50" in result.stdout
    assert "Sans réponse : 50" in result.stdout


@pytest.mark.parametrize("ledger", [[], {"version": 1, "sources": None}, {"version": 2, "sources": []}])
def test_malformed_ledger_is_controlled_error(tmp_path, ledger):
    write_fixture(tmp_path)
    (tmp_path / "sources/ledger.json").write_text(json.dumps(ledger))
    result = run_cli(tmp_path, "--check")
    assert result.returncode == 2
    assert "Traceback" not in result.stderr
    assert "Registre" in result.stderr
