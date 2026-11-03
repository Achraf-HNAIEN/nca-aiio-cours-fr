# NCA-AIIO — Cours et préparation en français

**Objectif : préparer le NVIDIA-Certified Associate: AI Infrastructure and Operations, passé en anglais.**

Cours indépendant, explications françaises et vocabulaire technique anglais. Parcours conçu pour une préparation en décembre 2026, avec un planning adaptable à ta date exacte. Il couvre les trois domaines du programme publié par NVIDIA : **Essential AI Knowledge (38 %), AI Infrastructure (40 %) et AI Operations (22 %)**.[1]

> **Pas de dumps. Pas de questions volées. Pas de garantie de réussite.** Les QCM sont des créations originales. Ce dépôt n'est ni affilié à NVIDIA ni approuvé par NVIDIA. Les produits, compatibilités et règles d'examen peuvent évoluer : les références sont datées, et la page officielle reste prioritaire.

## Commencer ici

1. Lire le [cadrage de l'examen](cours/00-cadrage-examen.md).
2. Suivre le [plan de préparation de quatre semaines](revision/plan-decembre.md).
3. Étudier les chapitres ci-dessous, en reliant les termes anglais au [glossaire EN–FR](revision/glossaire-en-fr.md).
4. Réaliser les [labs sans GPU](pratique/labs-sans-gpu.md), puis les [labs GPU optionnels](pratique/labs-avec-gpu.md) si tu disposes du matériel compatible.
5. S'entraîner avec les QCM en mode apprentissage, puis réserver une série pour une tentative chronométrée.
6. Utiliser les ressources publiques NVIDIA et revérifier les politiques avant de réserver.[1]

## Le cours

| Partie | Chapitre | À savoir expliquer |
|---|---|---|
| Cadrage | [00 — Examen et méthode](cours/00-cadrage-examen.md) | Programme, portée, méthode et limites des examens blancs |
| Essential AI Knowledge | [01 — Fondamentaux de l'IA](cours/01-fondamentaux-ia.md) | IA, ML, DL, adoption et cas d'usage |
| Essential AI Knowledge | [02 — Calcul et cycle de vie](cours/02-calcul-et-cycle-de-vie.md) | CPU/GPU, entraînement/inférence, étapes et contraintes |
| Essential AI Knowledge | [03 — Écosystème NVIDIA](cours/03-ecosysteme-nvidia.md) | Associer chaque solution à sa fonction, sans confondre les couches |
| AI Infrastructure | [04 — Serveurs et stockage](cours/04-serveurs-et-stockage.md) | Choisir les ressources pour une charge, comprendre les goulots et le scaling |
| AI Infrastructure | [05 — Réseaux et DPU](cours/05-reseaux-et-dpu.md) | Réseaux de calcul/stockage/gestion, protocoles, interconnexions et offload |
| AI Infrastructure | [06 — Datacenter et dimensionnement](cours/06-datacenter-et-dimensionnement.md) | Énergie, refroidissement, site, capacité et on-prem/cloud |
| AI Operations | [07 — Exploitation et observabilité](cours/07-exploitation-et-observabilite.md) | BMC, monitoring, métriques GPU et diagnostic raisonné |
| AI Operations | [08 — Orchestration et virtualisation](cours/08-orchestration-et-virtualisation.md) | Kubernetes/Slurm, conteneurs, passthrough, vGPU et MIG |

La [matrice de couverture](quality/couverture-objectifs.md) relie les **22 objectifs locaux** aux chapitres et aux questions. Les codes E/I/O sont créés pour ce dépôt, pas publiés par NVIDIA.

## Réviser et pratiquer

- [Planning de préparation](revision/plan-decembre.md)
- [Glossaire anglais–français](revision/glossaire-en-fr.md)
- [Fiches express et pièges](revision/fiches-express.md)
- Flashcards TSV importables dans un outil de répétition espacée : [connaissances IA](revision/flashcards-essential.tsv), [infrastructure](revision/flashcards-infrastructure.tsv), [opérations](revision/flashcards-operations.tsv). Première ligne = en-tête ; séparateur = tabulation ; trois colonnes Front, Back, Tags.
- [Examen blanc A — questions et corrigé](questions/examen-A.md)
- [Examen blanc B — questions et corrigé](questions/examen-B.md)
- [Quiz interactif hors ligne](site/quiz.html) : télécharger le fichier et l'ouvrir dans un navigateur. GitHub affiche son code et **ne l'exécute pas** directement.

### Lancer le quiz dans un terminal

Le quiz et le générateur HTML n'utilisent que la bibliothèque standard Python. Depuis la racine du dépôt :

```bash
python3 tools/quiz.py --check
python3 tools/quiz.py --exam A --mode learn
python3 tools/quiz.py --exam B --mode exam
```

Mode apprentissage : corrections au fil des réponses. Mode examen : correction à la fin. Les explications sont en français, les questions et les choix en anglais. Chaque série comporte 50 questions originales : **19 connaissances IA, 20 infrastructure, 11 opérations**. Cette répartition est choisie pour l'entraînement, pas annoncée comme une garantie sur l'examen réel.

Le fichier HTML contient toute la banque : il fonctionne sans serveur et sans requête réseau. Ce n'est pas un environnement d'examen sécurisé ; une personne qui inspecte le code peut lire les réponses.

### Régénérer et tester

```bash
python3 tools/build_site.py
python3 tools/labs_cpu.py
python3 -m pytest -q
```

Les tests de développement nécessitent `pytest` ; il n'est pas requis pour lire le cours, lancer les labs CPU ou utiliser le quiz. Voir [la documentation des outils](tools/README.md) et [le rapport de validation](quality/validation.md) pour les commandes exactes, les résultats et les limites.

## Sources et niveau de confiance

- **Autorité pour l'examen** : page NVIDIA, programme public et politiques en vigueur.[1]
- **Autorité technique** : documentations NVIDIA et documentations officielles des composants concernés, citées dans les chapitres.
- **Compléments** : [guides, retours d'expérience et ressources communautaires évalués](sources/ressources-complementaires.md). Une expérience personnelle ne devient pas une règle officielle.
- [Catalogue des sources consultées et statuts d'accès](sources/catalogue.md) ; [registre machine des références et extraits brefs](sources/ledger.json).
- [Méthode de recherche et de vérification](quality/methode.md), [couverture du programme](quality/couverture-objectifs.md) et [validation](quality/validation.md).

Les pages intégrales récupérées pour la recherche ne sont pas redistribuées. Les explications, scénarios, questions et flashcards sont une synthèse originale ; les citations courtes servent à étayer les affirmations. Les ressources inaccessibles sont signalées, pas présentées comme lues.

## Informations d'examen à revérifier

La page consultée le **3 novembre 2026** indique : **50 questions, 60 minutes, anglais, 125 USD, surveillance à distance et validité de deux ans**.[1] Elle recommande la formation **AI Infrastructure and Operations Fundamentals**, d'une durée typique annoncée de sept heures.[1] Les disponibilités, taxes, conditions de surveillance et règles Certiverse doivent être vérifiées au moment de la réservation. Ce dépôt ne prétend pas connaître un seuil officiel de réussite non indiqué par la source consultée.

## Organisation

```text
cours/       cours progressif en français
revision/    planning, fiches, glossaire, flashcards
pratique/    labs sans GPU et commandes GPU optionnelles
questions/   banque JSON et deux séries lisibles sur GitHub
site/        quiz HTML autonome à télécharger
sources/     références, preuves brèves et ressources complémentaires
quality/     couverture, méthode, revues et validation
tools/       quiz CLI, générateur HTML et labs CPU
tests/       tests automatisés des outils
```

Les sources techniques restent en anglais lorsque c'est leur langue d'origine. L'objectif n'est pas de mémoriser un catalogue de produits, mais de savoir **expliquer le besoin, choisir la bonne couche et justifier une décision**.

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
