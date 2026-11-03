# Revue indépendante des supports de révision et des labs

> Note d’intégration : les numéros de références de cette revue ont été alignés sur le registre commun. Les constats décrivent l’état avant correction ; voir [le suivi des corrections](corrections.md).

**Date : 3 novembre 2026. Verdict : utilisables, avec cinq corrections mineures recommandées.** Aucun défaut critique, élevé ou moyen constaté dans ce périmètre. Ce verdict ne certifie ni l’exhaustivité du cours entier ni la réussite à l’examen. Les sept fichiers de support ont été lus ; aucun chapitre, aucune question et aucun outil n’a été modifié.

## 1. Périmètre et preuves

Fichiers audités :

- `revision/plan-decembre.md`
- `revision/glossaire-en-fr.md`
- `revision/fiches-express.md`
- `pratique/labs-sans-gpu.md`
- `pratique/labs-avec-gpu.md`
- `sources/ressources-complementaires.md`
- `tools/labs_cpu.py`

Les résultats reproductibles, commandes, sorties standard/erreur, codes retour, calculs, empreintes des fichiers et réponses HTTP sont conservés dans [`support-audit-evidence.json`](support-audit-evidence.json). Les constats structurés et propositions de correction exactes sont dans [`revue-supports-findings.json`](revue-supports-findings.json). Les extractions web intégrales sont des matériaux de recherche privés sous `research/private/support-audit/`, pas des contenus à redistribuer dans le cours.

**Attention à la numérotation :** les citations de cette revue utilisent un registre d’audit isolé, `quality/revue-supports-sources.json`. Leurs numéros ne sont pas ceux du registre partagé du cours.

## 2. Cohérence avec le programme public

La page officielle a été récupérée indépendamment et son corps effectivement lu. Elle confirme 50 questions, 60 minutes, anglais, télésurveillance, domaines 38/40/22 et respectivement 8, 10 et 4 objectifs publics. La liste locale `quality/objectifs.json` correspond à ces objectifs ; le plan affecte des activités aux trois domaines et identifie correctement ses codes E/I/O comme locaux.[1]

Le plan distingue correctement prérequis de base, qualifications recommandées et obligation d’admission. Il n’invente ni date de rendez-vous, ni seuil officiel de réussite, ni garantie liée à un score d’entraînement. La formation recommandée de sept heures est incluse dans le budget si suivie, pas ajoutée silencieusement au total. La stratégie en deux passes reste explicitement conditionnée aux possibilités de l’interface réelle.[1]

**Réserve pédagogique :** les fiches express annoncent E01–E08 mais ne proposent pas de véritable rappel E04/E05 sur les facteurs d’adoption et les usages sectoriels. Ces thèmes figurent bien au plan et les fiches déclarent ne pas remplacer les chapitres : il s’agit donc d’une lacune du support de révision, pas d’une absence démontrée dans tout le cours. Voir SUP-01.

## 3. Arithmétique et budget — calculs réellement exécutés en Python

| Contrôle | Résultat indépendant |
|---|---|
| 36 h × 38/40/22 % | 13,68 / 14,40 / 7,92 h |
| 40 h × 38/40/22 % | 15,20 / 16,00 / 8,80 h |
| 48 h × 38/40/22 % | 18,24 / 19,20 / 10,56 h |
| Blocs extraits du tableau | 20 : 8 E, 8 I, 4 O |
| Somme E : 8 × 114 min | 912 min = 15 h 12 |
| Somme I : 8 × 120 min | 960 min = 16 h |
| Somme O : 4 × 132 min | 528 min = 8 h 48 |
| Total | 2 400 min = 40 h |
| Moyenne du temps par question | 60 × 60 / 50 = 72 secondes |
| Première/seconde passe personnelle | 45 + 15 = 60 minutes |
| Somme des durées suggérées des six labs | 105 à 135 minutes |

Les valeurs décimales et la base hebdomadaire sont correctes. Les essais mixtes et leurs corrections sont explicitement inclus et non comptés deux fois. Aucun calcul ne démontre toutefois que 36–48 heures suffiront à ce lecteur : le texte présente correctement ce volume comme une proposition pédagogique.

La phrase « multiplier toutes les durées » mérite d’être limitée aux blocs : les essais de format réel doivent conserver 60 minutes même dans les variantes 36/48 h. C’est une ambiguïté éditoriale, pas une erreur de total (SUP-03).

## 4. Glossaire — 99 entrées examinées

Le parseur indépendant trouve **99 termes et 99 termes uniques**. Les 99 définitions ont été relues conceptuellement, pas simplement comptées. Aucun contresens bloquant relevé. Les distinctions importantes sont préservées :

- AI ⊃ ML ⊃ DL ; training/inference ; paramètres/hyperparamètres ; validation/test. Les notions de ML et de généralisation sont cohérentes avec l’introduction IBM consultée.[48]
- CPU/GPU et parallélisme ; CUDA/bibliothèques ; TensorRT/serveur Triton ; serveur Triton/langage Triton.
- Mémoire locale/agrégée ; capacité/bande passante ; débit/latence ; RDMA/RoCE ; GPUDirect RDMA/Storage ; somme/moyenne d’AllReduce.
- Ordonnanceur/orchestrateur/monitoring ; partition Slurm/MIG ; conteneur/VM ; passthrough/vGPU.
- `memory utilization` ne devient pas `memory used` ; `N/A` ne devient pas zéro ; activité GPU ne devient pas efficacité applicative. Ces formulations correspondent aux définitions `nvidia-smi` relues.[39]

La prudence MIG est justifiée : la table officielle consultée donne A30 à quatre instances maximales, contre sept pour les références H100 indiquées. Les supports ne prétendent pas que tous les GPU supportent MIG ni que sept est une limite universelle.[61]

Cette relecture sémantique ne remplace pas une validation détaillée de toutes les conventions de chaque version de logiciel. Les termes servent le raisonnement et ne sont pas présentés comme les mots garantis de l’examen.

## 5. Sécurité du code et commandes GPU

### Script CPU

Lecture complète et inspection AST : uniquement `argparse`, `csv`, `io`, `json`, `math`, `platform`, `statistics`, `sys`, `unittest`. Aucun appel à `open`, `eval`, `exec`, `os.system` ou `subprocess` dans le script audité ; aucun accès réseau, lancement de commande, allocation GPU ou écriture persistante explicite. Les fixtures sont minuscules ; le milliard de paramètres est un nombre, pas une allocation. Les 200 mises à jour scalaires du lab 1 sont bornées.

**Robustesse limitée :** les garde-fous de `memory_budget` et `pipeline` acceptent `NaN`/`Infinity`. Des sondes réelles ont produit un total mémoire `nan`/`inf` et un pipeline affichant un débit séquentiel `nan` avec un goulet pourtant nommé `storage`. SUP-02 recommande des vérifications `math.isfinite` et trois tests supplémentaires. Les six fixtures accessibles par la CLI documentée ne sont pas affectées. Des sondes supplémentaires sur les autres fonctions sont conservées dans le JSON ; aucune API d’import de données arbitraires n’est promise par le guide.

### Guide GPU

Tous les blocs de commandes ont été examinés : version/aide/inventaire, requêtes de métriques, `nvidia-smi -q -d …`, `nvidia-smi topo -m`, aide et découverte DCGM. Aucun reset, réglage de puissance/fréquence, partitionnement, installation, démarrage de service, `sudo`, conteneur privilégié, soumission de job ou boucle infinie n’est fourni comme exercice exécutable. Les préconditions couvrent autorisation, Linux, pile préinstallée, aide locale, disponibilité des champs et anonymisation.

Les options et les types d’affichage `nvidia-smi` employés correspondent à la documentation récupérée ; le texte demande justement de vérifier leur présence dans la version locale.[39] Le guide ne revendique aucune exécution GPU. **L’audit n’a lui non plus exécuté aucune commande GPU.** La lecture seule n’est pas une dispense d’autorisation ; ce point est explicitement traité.

## 6. Exécution CPU indépendante — résultats observés

Répertoire : `/home/kali/nca-aiio-course`. Interpréteur observé dans la sortie CLI : **Python 3.14.8**.

### Tests internes

Commande réelle : `python3 tools/labs_cpu.py --test` ; **code retour 0**.

```text
test_allreduce (__main__.LabTests.test_allreduce) ... ok
test_memory_budget (__main__.LabTests.test_memory_budget) ... ok
test_pipeline (__main__.LabTests.test_pipeline) ... ok
test_placement (__main__.LabTests.test_placement) ... ok
test_telemetry (__main__.LabTests.test_telemetry) ... ok
test_training (__main__.LabTests.test_training) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

### Les six résultats effectivement affichés

Commande réelle : `python3 tools/labs_cpu.py all` ; **code retour 0**. Sortie conservée telle qu’observée :

```text
Python 3.14.8 | CPU-only stdlib | synthetic fixtures
LAB 1 training
{"final_mse": 0.0, "initial_mse": 18.666666666666668, "parameters_after_inference": 2.0, "parameters_before_inference": 2.0, "prediction_x4": 8.0}
LAB 2 memory_budget
{"margin_fraction": 0.2, "total_gib": 4.635174179077148, "weight_bytes": 2000000000, "weight_gib": 1.862645149230957, "workspace_gib": 2}
LAB 3 pipeline
{"bottleneck": "storage", "overlap_ideal_batches_s": 20.0, "serial_batches_s": 12.5, "stage_ms": [50, 20, 10]}
LAB 4 allreduce
{"mean": [2.0, 3.0], "replicas": [[2.0, 3.0], [2.0, 3.0]], "sum": [4.0, 6.0]}
LAB 5 telemetry
{"gpu-A": {"mean_util_pct": 40.0, "missing_util_samples": 0, "peak_used_mib": 1200.0}, "gpu-B": {"mean_util_pct": null, "missing_util_samples": 1, "peak_used_mib": 500.0}}
LAB 6 placement
{"assigned": {"A": 0, "B": 1, "D": 0}, "pending": ["C"], "remaining": [{"memory_gib": 0, "slots": 0}, {"memory_gib": 2, "slots": 1}]}
```

Chaque commande `python3 tools/labs_cpu.py 1` à `… 6` a aussi été exécutée séparément : six codes retour 0 ; chaque objet JSON est égal au résultat correspondant de `all`. L’appel sans argument a été exécuté et sa sortie comparée à `all` : identique. `--help` réussit, code 0 ; le choix invalide `7` est refusé, code 2. Ce sont onze invocations distinctes consignées dans le JSON, pas une inférence tirée des seuls tests internes.

Les résultats décrits dans le guide sont conformes : poids 2, prédiction 8, paramètres inchangés en inférence ; budget 4,635174179077148 GiB ; 12,5/20 lots/s ; somme [4,6] et moyenne [2,3] ; moyenne A 40 %, mémoire maximale 1 200 MiB, B absent et non nul ; A/D sur 0, B sur 1, C en attente. Les valeurs d’infrastructure sont correctement étiquetées synthétiques et ne sont pas transformées en benchmark matériel.

Le blocage historique d’approbation décrit dans le guide n’est pas un échec de cette exécution indépendante. L’auteur distingue honnêtement ses six fonctions testées de ses branches CLI alors non exercées. La présente revue apporte désormais une preuve supplémentaire ; elle ne réécrit pas ce récit historique ni ne prouve rétrospectivement toute la séquence TDD annoncée dans `research/labs-results.txt`.

## 7. Liens, citations et attribution communautaire

Contrôle structurel : **aucune référence numérique non définie**, aucune discordance entre URL de source et registre partagé, **huit occurrences de liens locaux existantes**. Contrôle HTTP indépendant de **26 URL distinctes citées : 26 réponses 200**, avec URL finale et corps sauvegardés. La redirection du lien historique CUDA vers le nouveau guide est fonctionnelle. Les corps ont un contenu pertinent, pas seulement un écran de connexion. La disponibilité HTTP ne suffit pas à garantir toutes les affirmations : les recoupements de contenu suivants ont été réalisés.

| Source substantiellement recoupée | Constat |
|---|---|
| Page officielle NVIDIA | Format et objectifs/pondérations concordants.[1] |
| Eason Tech Talk | L’auteur dit explicitement que son approche accélérée suppose une expérience pratique ; le support attribue correctement les 16 heures à son cas personnel.[35] |
| cterpening | Mention réelle « AI-assisted » et « HUMAN REVIEW PENDING » ; le support ne transforme pas ses tests déclarés en tests de notre cours.[32] |
| ziash | Déclarations de questions originales, absence de dumps et absence d’affiliation présentes ; le support les rapporte comme déclarations et réserve les droits sur les captures.[30] |
| mgonzalezo | Déclarations de réussite aux deux niveaux et mélange Associate/Professional présents ; le support ne prétend pas authentifier ces résultats.[31] |
| HowToAI | Le repère « 80%+ » est bien un conseil du site, pas une note de passage officielle.[33] |
| NicheeLab et table officielle MIG | Le raccourci « A100/H100 only » existe réellement et le contre-exemple A30 est établi par NVIDIA ; la réserve du support est fondée.[34][61] |
| `nvidia-smi` | Les distinctions d’activité GPU, activité mémoire et mémoire occupée sont conformes.[39] |

Aucun témoignage n’est utilisé pour garantir une durée de préparation, une réussite ou un contenu précis d’examen. L’audit n’authentifie pas davantage les identités ni les certifications déclarées par les auteurs externes. Une petite corruption d’encodage dans le titre de la référence Python subsiste : SUP-05.

## 8. Corrections transmises au parent

| ID | Sévérité | Cible | Correction demandée |
|---|---|---|---|
| SUP-01 | Faible | Fiches express, périmètre E04/E05 | Ajouter un bref rappel ou des renvois explicites et exploitables vers le chapitre correspondant. |
| SUP-02 | Faible | `labs_cpu.py`, validation numérique | Refuser NaN/Infinity dans les deux fonctions et compléter les tests ; fixtures normales inchangées. |
| SUP-03 | Faible | Plan, adaptation 36/48 h | Limiter la mise à l’échelle aux blocs, préserver les essais de 60 minutes. |
| SUP-04 | Faible | Plan, organisation des essais | Remplacer « les autres agents du cours » par les liens vers les banques finales. |
| SUP-05 | Faible | Deux listes de sources | Corriger le titre Python mal décodé sans modifier l’URL. |

Le JSON fournit pour chacun sévérité, fichier, emplacement, problème, preuve et correction exacte. **Aucune correction n’a été appliquée aux livrables audités.**

## 9. Limites à conserver dans la livraison

- Tests exécutés sur Python 3.14.8 uniquement. La syntaxe est acceptée par `ast.parse(feature_version=(3,9))`, mais cela ne constitue pas une exécution sur Python 3.9.
- Aucun GPU, pilote, service DCGM, ordonnanceur réel, conteneur ou cloud n’a été exercé.
- Pas de test d’exécution directe `./tools/labs_cpu.py`, non requis par le guide ; aucune permission modifiée.
- Recoupements précis de sources et lecture du glossaire, pas expertise exhaustive de toutes les pages, versions, fichiers de dépôts et formations externes.
- Les commandes actuelles corroborent la réussite des six tests et vérifient les sorties CLI ; elles ne prouvent pas tous les événements historiques de développement.
- Recontrôler les informations d’examen avant réservation. Les constats valent pour les fichiers dont les empreintes figurent dans la preuve d’audit.

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
[30] https://github.com/ziash/nvidia-nca-aiio-study-guide — GitHub - ziash/nvidia-nca-aiio-study-guide: Comprehensive NCA-AIIO exam prep: study notes, diagrams, screenshots, and field experience for the NVIDIA Certified Associate: AI Infrastructure and Operations certification. · GitHub
[31] https://github.com/mgonzalezo/nvidia-ai-infra-certs — GitHub - mgonzalezo/nvidia-ai-infra-certs: Everything you need to pass the NVIDIA NCP-AII and NCA-AII certifications: study guides, exam tips, practice questions, and real-world troubleshooting scenarios for GPU clusters, NVLink, DCGM, and AI infrastructure at scale. · GitHub
[32] https://cterpening.github.io/certification-study-library/guides/NCA-AIIO-nvidia-ai-infrastructure-operations-associate — NVIDIA-Certified Associate: AI Infrastructure and Operations (NCA-AIIO) Study Guide - Certification Study Library
[33] https://howtoai.com/nca-aiio-study-guide — NCA-AIIO Study Guide 2026: Domains, Cheat Sheet, Free Prep
[34] https://nicheelab.com/en/articles/nvidia/aiio-overview — NVIDIA-Certified Associate: AI Infrastructure & Operations (NCA-AIIO) Guide (2026)
[35] https://easontechtalk.com/nvidia-nca-aiio-exam — How I Passed NVIDIA NCA-AIIO in 16 Hours: Study Plan and 7 Exam Topics | Eason Tech Talk
[39] https://docs.nvidia.com/deploy/nvidia-smi/index.html — NVIDIA System Management Interface
[48] https://www.ibm.com/think/topics/machine-learning — IBM: What is machine learning?
[61] https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-gpus.html — Supported GPUs — NVIDIA Multi-Instance GPU User Guide
