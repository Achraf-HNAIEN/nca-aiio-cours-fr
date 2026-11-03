#!/usr/bin/env python3
"""Generate a standalone file:// quiz from the validated production bank."""
import argparse
import json
from pathlib import Path
import sys

from quiz import load_bank

TEMPLATE = '''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>Entraînement NCA-AIIO — indépendant</title>
<style>
:root{font-family:system-ui,sans-serif;color:#172536;background:#eef3f6;line-height:1.6}
*{box-sizing:border-box}body{margin:0}main{max-width:900px;margin:auto;padding:1.2rem}
h1{line-height:1.2;font-size:clamp(1.6rem,5vw,2.3rem)}section,.panel{background:white;border:1px solid #c6d1dc;border-radius:12px;padding:1.2rem;margin:1rem 0}
button,select{font:inherit;padding:.65rem .9rem;border:1px solid #526b82;border-radius:7px;max-width:100%;background:white;color:#172536}
button{cursor:pointer}button.primary{background:#154c71;color:white}button:disabled{opacity:.5;cursor:not-allowed}
:focus-visible{outline:3px solid #bd5800;outline-offset:3px}.row{display:flex;flex-wrap:wrap;gap:.7rem;align-items:center}
fieldset{border:0;padding:0;margin:1rem 0;min-width:0}legend{font-weight:650;margin-bottom:.7rem;overflow-wrap:anywhere}
.choice{display:flex;gap:.7rem;padding:.8rem;border:1px solid #b2c1cf;border-radius:7px;margin:.55rem 0;align-items:flex-start}
.choice input{margin-top:.5rem;flex-shrink:0}.choice span{overflow-wrap:anywhere}#timer{font-variant-numeric:tabular-nums;font-weight:700}
#status{min-height:1.6em}#feedback:empty{display:none}.correction{border-left:4px solid #326982;padding:.6rem 1rem;margin:.8rem 0}
a,p,summary{overflow-wrap:anywhere}summary{cursor:pointer;font-weight:600}[hidden]{display:none!important}
.note{font-size:.92rem;color:#3d5265}#results h2:focus{outline:none}
</style></head><body><main>
<h1>Entraînement NCA-AIIO</h1>
<p>Questions originales <strong>non officielles</strong> : énoncés et choix en anglais, explications en français. Ni examen NVIDIA ni garantie de réussite.</p>
<p class="note">Hors ligne : aucune connexion nécessaire sauf pour ouvrir les sources. Aucune donnée envoyée ou sauvegardée. Recharger ferme la session.</p>
<noscript>Activez JavaScript pour utiliser ce quiz, ou consultez les examens Markdown dans questions/.</noscript>
<section id="setup" aria-label="Configuration">
<div class="row"><label for="exam">Série</label><select id="exam"><option value="A">Examen A</option><option value="B">Examen B</option></select>
<label for="mode">Mode</label><select id="mode"><option value="exam">Examen — 60 minutes</option><option value="learn">Apprentissage — sans limite</option></select>
<button id="start" class="primary">Commencer</button></div>
<p>50 questions : Essential 19 (38 %), Infrastructure 20 (40 %), Operations 11 (22 %). Une seule bonne réponse. Aucun seuil officiel de réussite n’est supposé.</p>
<p>Validez chaque réponse. En examen, vous pouvez la modifier avant de terminer ; aucun corrigé ne s’affiche avant la clôture. En apprentissage, la validation révèle le corrigé et verrouille cette question.</p>
</section>
<div class="row"><span id="timer" role="timer" aria-label="Temps restant" hidden>60:00</span><button id="restart" hidden>Recommencer (effacer la session)</button></div>
<p id="status" role="status" aria-live="polite"></p>
<section id="session" hidden aria-label="Question en cours">
<p id="progress" aria-live="polite"></p><p id="metadata" class="note"></p>
<fieldset id="options"><legend id="question" lang="en" tabindex="-1"></legend><div id="choices" lang="en"></div></fieldset>
<div class="row"><button id="submit-answer" class="primary">Valider ma réponse</button><button id="previous">Précédente</button><button id="next">Suivante</button><button id="finish">Terminer et corriger</button></div>
<div id="feedback" aria-live="polite"></div></section>
<section id="results" hidden aria-label="Résultats et corrigé"></section>
<script id="quiz-data" type="application/json">__PAYLOAD__</script>
<script>
'use strict';
(() => {
const data = JSON.parse(document.getElementById('quiz-data').textContent);
const $ = id => document.getElementById(id);
let questions = [], answers = {}, index = 0, mode = 'exam', active = false, deadline = null, interval = null;
function element(tag, text, parent) {
  const node = document.createElement(tag);
  if (text !== undefined) node.textContent = text;
  if (parent) parent.append(node);
  return node;
}
function correction(q, parent) {
  const box = element('div', undefined, parent); box.className = 'correction';
  element('p', 'Réponse correcte : ' + q.answer + '. ' + q.explanation, box);
  for (const letter of 'ABCD') if (letter !== q.answer) element('p', letter + ' — ' + q.distractors[letter], box);
  const list = element('ul', undefined, box);
  for (const sid of q.source_ids) {
    const source = data.sources[sid], item = element('li', undefined, list);
    const link = element('a', '[' + sid + '] ' + (source.title || source.url), item);
    link.href = source.url; link.target = '_blank'; link.rel = 'noopener noreferrer';
  }
}
function allowed() {
  if (!active) return false;
  if (deadline !== null && Date.now() >= deadline) { finish(true); return false; }
  return true;
}
function tick() {
  if (!active || deadline === null) return;
  const remaining = Math.max(0, Math.ceil((deadline - Date.now()) / 1000));
  $('timer').textContent = String(Math.floor(remaining / 60)).padStart(2, '0') + ':' + String(remaining % 60).padStart(2, '0');
  if (remaining === 0) finish(true);
}
function render() {
  const q = questions[index], locked = mode === 'learn' && Object.hasOwn(answers, q.id);
  $('progress').textContent = 'Question ' + (index + 1) + '/50 — ' + Object.keys(answers).length + ' réponse(s)';
  $('metadata').textContent = q.domain + ' · ' + q.objective + ' · ' + q.id;
  $('question').textContent = q.question; $('choices').replaceChildren(); $('feedback').replaceChildren();
  for (const letter of 'ABCD') {
    const label = element('label', undefined, $('choices')); label.className = 'choice';
    const radio = element('input', undefined, label); radio.type = 'radio'; radio.name = 'answer'; radio.value = letter;
    radio.checked = answers[q.id] === letter; radio.disabled = locked || !active;
    element('span', letter + '. ' + q.choices[letter], label);
    radio.addEventListener('change', () => { if (!allowed()) radio.checked = false; });
  }
  $('submit-answer').disabled = locked || !active;
  $('previous').disabled = index === 0 || !active; $('next').disabled = index === questions.length - 1 || !active;
  if (locked) correction(q, $('feedback'));
}
function finish(expired = false) {
  if (!active) return;
  active = false; clearInterval(interval); interval = null;
  if (expired) $('timer').textContent = '00:00';
  for (const id of ['submit-answer', 'previous', 'next', 'finish']) $(id).disabled = true;
  $('options').disabled = true; $('session').hidden = true;
  $('status').textContent = expired ? 'Temps écoulé : réponses verrouillées. Corrigé disponible.' : 'Session terminée : réponses verrouillées.';
  const results = $('results'); results.replaceChildren(); results.hidden = false;
  let correct = 0; const domains = {};
  for (const q of questions) {
    domains[q.domain] ||= {correct: 0, total: 0}; domains[q.domain].total++;
    if (answers[q.id] === q.answer) { correct++; domains[q.domain].correct++; }
  }
  const heading = element('h2', 'Résultat : ' + correct + '/50 (' + (correct * 2) + ' %)', results); heading.tabIndex = -1;
  element('p', 'Sans réponse validée : ' + (50 - Object.keys(answers).length) + '. Ce score d’entraînement n’est pas un seuil officiel.', results);
  const list = element('ul', undefined, results);
  for (const [domain, counts] of Object.entries(domains)) element('li', domain + ' : ' + counts.correct + '/' + counts.total, list);
  element('h3', 'Corrigé complet', results);
  questions.forEach((q, i) => {
    const detail = element('details', undefined, results);
    element('summary', 'Question ' + (i + 1) + ' — ' + q.id + ' — réponse : ' + (answers[q.id] || 'sans réponse') + (answers[q.id] === q.answer ? ' — correcte' : ' — à revoir'), detail);
    const stem = element('p', q.question, detail); stem.lang = 'en';
    for (const letter of 'ABCD') { const choice = element('p', letter + '. ' + q.choices[letter], detail); choice.lang = 'en'; }
    correction(q, detail);
  });
  heading.focus();
}
function reset() {
  clearInterval(interval); interval = null; active = false; deadline = null;
  questions = []; answers = {}; index = 0;
  $('setup').hidden = false; $('session').hidden = true; $('results').hidden = true;
  $('results').replaceChildren(); $('feedback').replaceChildren(); $('choices').replaceChildren();
  $('question').textContent = ''; $('progress').textContent = ''; $('metadata').textContent = '';
  $('status').textContent = ''; $('timer').textContent = '60:00'; $('timer').hidden = true;
  $('restart').hidden = true; $('options').disabled = false;
  for (const id of ['submit-answer', 'previous', 'next', 'finish']) $(id).disabled = true;
  $('start').focus();
}
$('start').addEventListener('click', () => {
  clearInterval(interval); answers = {}; index = 0;
  questions = data.questions.filter(q => q.exam === $('exam').value);
  mode = $('mode').value; active = true; deadline = mode === 'exam' ? Date.now() + 3600000 : null;
  $('setup').hidden = true; $('results').hidden = true; $('results').replaceChildren();
  $('session').hidden = false; $('restart').hidden = false; $('timer').hidden = false;
  $('timer').textContent = mode === 'exam' ? '60:00' : 'Sans limite de temps';
  $('status').textContent = ''; $('finish').disabled = false; $('options').disabled = false;
  render(); $('question').focus();
  if (deadline !== null) interval = setInterval(tick, 250);
});
$('submit-answer').addEventListener('click', () => {
  if (!allowed()) return;
  const q = questions[index];
  if (mode === 'learn' && Object.hasOwn(answers, q.id)) return;
  const checked = document.querySelector('input[name="answer"]:checked');
  if (!checked) { $('status').textContent = 'Choisissez une réponse avant de valider, ou passez à la suivante.'; return; }
  answers[q.id] = checked.value; $('status').textContent = 'Réponse enregistrée.'; render();
});
$('previous').addEventListener('click', () => { if (allowed() && index > 0) { index--; render(); $('question').focus(); } });
$('next').addEventListener('click', () => { if (allowed() && index < questions.length - 1) { index++; render(); $('question').focus(); } });
$('finish').addEventListener('click', () => { if (allowed()) finish(); });
$('restart').addEventListener('click', reset);
document.addEventListener('visibilitychange', tick);
})();
</script></main></body></html>
'''


def build_site(root=None, output=None):
    root = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    bank, sources = load_bank(root)
    used = {sid for q in bank for sid in q["source_ids"]}
    public_sources = {sid: {"id": sid, "title": sources[sid].get("title", ""), "url": sources[sid]["url"]} for sid in sorted(used)}
    payload = json.dumps({"questions": bank, "sources": public_sources}, ensure_ascii=True)
    # Escape script-end tags, HTML metacharacters and JS line separators in data.
    for char, escaped in (("<", r"\u003c"), (">", r"\u003e"), ("&", r"\u0026")):
        payload = payload.replace(char, escaped)
    target = Path(output) if output is not None else root / "site/quiz.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEMPLATE.replace("__PAYLOAD__", payload), encoding="utf-8")
    return target


def main(argv=None):
    parser = argparse.ArgumentParser(description="Construire le quiz HTML autonome à partir de la banque validée.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, help="Par défaut : ROOT/site/quiz.html.")
    args = parser.parse_args(argv)
    try:
        target = build_site(args.root, args.output)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"Erreur de construction : {exc}", file=sys.stderr)
        return 2
    print(f"Quiz autonome généré : {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
