#!/usr/bin/env python3
"""Offline original NCA-AIIO practice. Python standard library only."""
from collections import Counter
import argparse
import json
from pathlib import Path
import queue
import random
import re
import sys
import threading
import time
from urllib.parse import urlsplit

DOMAIN_COUNTS = {"essential": 19, "infrastructure": 20, "operations": 11}
OBJECTIVES = {"essential": {f"E{i:02}" for i in range(1, 9)},
              "infrastructure": {f"I{i:02}" for i in range(1, 11)},
              "operations": {f"O{i:02}" for i in range(1, 5)}}


def validate_bank(bank, sources):
    """Raise ValueError when the bank violates the shared production contract."""
    if not isinstance(bank, list):
        raise ValueError("La banque doit être une liste.")
    if any(not isinstance(q, dict) for q in bank):
        raise ValueError("Chaque question doit être un objet.")
    for q in bank:
        if q.get("exam") not in ("A", "B"):
            raise ValueError("Examen A ou B requis ; 50 questions par examen.")
        if not isinstance(q.get("domain"), str) or q["domain"] not in DOMAIN_COUNTS:
            raise ValueError("domaine invalide pour les questions.")
    counts = Counter((q.get("exam"), q.get("domain")) for q in bank)
    for exam in ("A", "B"):
        for domain, count in DOMAIN_COUNTS.items():
            if counts[exam, domain] != count:
                raise ValueError(f"Examen {exam}, {domain} : {count} questions requises.")
    if len(bank) != 100:
        raise ValueError("100 questions requises.")
    seen = set()
    for q in bank:
        ident = q.get("id")
        prefix = {"essential": "E", "infrastructure": "I", "operations": "O"}[q["domain"]]
        if not isinstance(ident, str) or not re.fullmatch(prefix + r"-\d{3}", ident) or ident in seen:
            raise ValueError(f"identifiant invalide ou dupliqué : {ident!r}")
        seen.add(ident)
        for field in ("question", "explanation"):
            if not isinstance(q.get(field), str) or not q[field].strip():
                raise ValueError(f"{ident}: {field} doit être un texte non vide.")
        choices = q.get("choices")
        if not isinstance(choices, dict) or set(choices) != set("ABCD") or any(not isinstance(v, str) or not v.strip() for v in choices.values()):
            raise ValueError(f"{ident}: choices doit contenir A, B, C, D.")
        if len(set(choices.values())) != 4:
            raise ValueError(f"{ident}: choices doit contenir quatre choix distincts.")
        if q.get("answer") not in ("A", "B", "C", "D"):
            raise ValueError(f"{ident}: answer invalide.")
        distractors = q.get("distractors")
        if not isinstance(distractors, dict) or set(distractors) != set("ABCD") - {q["answer"]} or any(not isinstance(v, str) or not v.strip() for v in distractors.values()):
            raise ValueError(f"{ident}: distractors doit expliquer exactement les trois mauvaises réponses.")
        if not isinstance(q.get("objective"), str) or q["objective"] not in OBJECTIVES[q["domain"]]:
            raise ValueError(f"{ident}: objective invalide.")
        if q.get("difficulty") not in ("basic", "scenario"):
            raise ValueError(f"{ident}: difficulty invalide.")
        ids = q.get("source_ids")
        if not isinstance(ids, list) or not ids or any(type(s) is not int or s not in sources for s in ids):
            raise ValueError(f"{ident}: source inconnue ou invalide.")
        for sid in ids:
            url = sources[sid].get("url", "")
            parsed = urlsplit(url)
            if parsed.scheme not in ("https", "http") or not parsed.netloc:
                raise ValueError(f"source {sid}: URL HTTP(S) requise.")
    for exam in ("A", "B"):
        for domain, objectives in OBJECTIVES.items():
            covered = {q["objective"] for q in bank if q["exam"] == exam and q["domain"] == domain}
            if covered != objectives:
                raise ValueError(f"Examen {exam}, {domain}: objectifs manquants {sorted(objectives - covered)}")


def load_bank(root=None):
    root = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    bank = []
    for domain in DOMAIN_COUNTS:
        path = root / "questions" / f"{domain}.json"
        records = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(records, list):
            raise ValueError(f"{path}: liste de questions attendue.")
        if any(not isinstance(q, dict) or q.get("domain") != domain for q in records):
            raise ValueError(f"{path}: domaine incorrect.")
        bank.extend(records)
    ledger = json.loads((root / "sources/ledger.json").read_text(encoding="utf-8"))
    if not isinstance(ledger, dict) or type(ledger.get("version")) is not int or ledger["version"] != 1:
        raise ValueError("Registre invalide : objet version 1 attendu.")
    entries = ledger.get("sources", [])
    if not isinstance(entries, list) or any(not isinstance(s, dict) or type(s.get("id")) is not int for s in entries):
        raise ValueError("Registre de sources invalide.")
    sources = {s["id"]: s for s in entries}
    if len(sources) != len(entries):
        raise ValueError("Identifiants de sources dupliqués.")
    validate_bank(bank, sources)
    return bank, sources


def select_exam(bank, exam, seed=None):
    if exam not in ("A", "B"):
        raise ValueError("Examen A ou B requis.")
    questions = [q for q in bank if q["exam"] == exam]
    if len(questions) != 50:
        raise ValueError("50 questions requises pour cet examen.")
    if seed is not None:
        random.Random(seed).shuffle(questions)
    return questions


def score(questions, answers):
    domains = {domain: {"correct": 0, "total": 0} for domain in DOMAIN_COUNTS}
    for q in questions:
        domains[q["domain"]]["total"] += 1
        domains[q["domain"]]["correct"] += int(answers.get(q["id"]) == q["answer"])
    correct = sum(d["correct"] for d in domains.values())
    total = len(questions)
    return {"correct": correct, "total": total, "percent": round(100 * correct / total, 1) if total else 0,
            "unanswered": sum(answers.get(q["id"]) not in ("A", "B", "C", "D") for q in questions), "domains": domains}


def correction(q, sources):
    lines = [f"Réponse correcte : {q['answer']}. {q['explanation']}"]
    lines += [f"{letter} — {q['distractors'][letter]}" for letter in "ABCD" if letter != q["answer"]]
    lines += [f"[{sid}] {sources[sid].get('title') or sources[sid]['url']} — {sources[sid]['url']}" for sid in q["source_ids"]]
    return "\n".join(lines)


def export_markdown(questions, sources, target, with_answers=False):
    lines = [f"# Examen d’entraînement {questions[0]['exam']}", "",
             "Questions originales non officielles. Aucun seuil officiel de réussite n’est supposé.",
             "50 questions · 60 minutes · une seule réponse par question.", "", "## Questions", ""]
    for i, q in enumerate(questions, 1):
        lines += [f"### Question {i} — {q['id']}", "", q["question"], ""]
        lines += [f"- {letter}. {q['choices'][letter]}" for letter in "ABCD"]
        lines += [""]
    if with_answers:
        lines += ["---", "", "## Corrigé", "", "Ne consulter qu’après avoir terminé l’ensemble des questions.", ""]
        for i, q in enumerate(questions, 1):
            lines += [f"#### Correction {i} — {q['id']} ({q['domain']}, {q['objective']})", "", correction(q, sources), ""]
    target = Path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def timed_input(prompt, timeout=None):
    """A daemon reader lets the exam end even while stdin is blocked."""
    if timeout is None:
        return input(prompt)
    if timeout <= 0:
        raise TimeoutError
    result = queue.Queue()

    def read():
        try:
            result.put((True, input(prompt)))
        except EOFError:
            result.put((False, None))
    threading.Thread(target=read, daemon=True).start()
    try:
        ok, value = result.get(timeout=timeout)
    except queue.Empty:
        raise TimeoutError from None
    if not ok:
        raise EOFError
    return value


def run_session(questions, sources, mode):
    print("Questions originales non officielles — aucune garantie de réussite.")
    print("A/B/C/D : répondre ; Entrée : passer ; FIN : terminer. Examen : 60 minutes.")
    deadline = time.monotonic() + 3600 if mode == "exam" else None
    answers = {}
    try:
        for i, q in enumerate(questions, 1):
            if deadline is not None and time.monotonic() >= deadline:
                raise TimeoutError
            print(f"\nQuestion {i}/50 — {q['id']}\n{q['question']}")
            for letter in "ABCD":
                print(f"  {letter}. {q['choices'][letter]}")
            while True:
                remaining = deadline - time.monotonic() if deadline is not None else None
                value = timed_input("Votre réponse : ", remaining).strip().upper()
                if deadline is not None and time.monotonic() >= deadline:
                    raise TimeoutError
                if value in ("A", "B", "C", "D", "", "FIN"):
                    break
                print("Choisir A, B, C ou D ; Entrée pour passer ; FIN pour terminer.")
            if value == "FIN":
                break
            if value:
                answers[q["id"]] = value
            if mode == "learn":
                print(correction(q, sources))
    except TimeoutError:
        print("\nTemps écoulé : réponses verrouillées.")
    except (EOFError, KeyboardInterrupt):
        print("\nSession interrompue : résultats partiels.")
    report = score(questions, answers)
    print(f"\nRésultat : {report['correct']}/{report['total']} ({report['percent']} %). Sans réponse : {report['unanswered']}.")
    for domain, counts in report["domains"].items():
        print(f"{domain}: {counts['correct']}/{counts['total']}")
    if mode == "exam":
        print("\nCorrigé après clôture")
        for q in questions:
            print(f"\n{q['id']} — votre réponse : {answers.get(q['id'], 'sans réponse')}")
            print(correction(q, sources))
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description="Quiz indépendant NCA-AIIO hors ligne, interface française.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Racine contenant questions/ et sources/.")
    parser.add_argument("--exam", choices=("A", "B"), default="A")
    parser.add_argument("--mode", choices=("exam", "learn"), default="learn")
    parser.add_argument("--seed", type=int, help="Mélanger les questions de manière reproductible.")
    parser.add_argument("--check", action="store_true", help="Valider sans interaction.")
    parser.add_argument("--export", type=Path, metavar="FICHIER.md", help="Exporter l’examen sélectionné sans corrigé par défaut.")
    parser.add_argument("--with-answers", action="store_true", help="Ajouter un corrigé séparé à --export.")
    parser.add_argument("--export-markdown", type=Path, metavar="DOSSIER", help="Exporter examen-A.md et examen-B.md avec corrigés séparés.")
    args = parser.parse_args(argv)
    try:
        bank, sources = load_bank(args.root)
        if args.check:
            print("Banque valide : 100 questions ; examens A/B de 50 ; pondération 19/20/11 ; objectifs et sources vérifiés.")
        elif args.export_markdown:
            for exam in ("A", "B"):
                target = args.export_markdown / f"examen-{exam}.md"
                export_markdown(select_exam(bank, exam, args.seed), sources, target, True)
                print(f"Export : {target}")
        elif args.export:
            export_markdown(select_exam(bank, args.exam, args.seed), sources, args.export, args.with_answers)
            print(f"Export : {args.export}")
        else:
            run_session(select_exam(bank, args.exam, args.seed), sources, args.mode)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"Erreur : {exc}. Vérifier questions/{{essential,infrastructure,operations}}.json et sources/ledger.json.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
