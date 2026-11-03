# Plan adaptable — quatre semaines pour décembre 2026

**Public : Achraf.** Ce programme indépendant propose **36 à 48 heures de travail**, avec une base de 40 heures. Il ne fixe aucune date d’examen : choisir quatre semaines consécutives avant le rendez-vous réellement réservé, en décembre si cela reste ton objectif. Si le diagnostic révèle trop de prérequis manquants, prolonger la préparation plutôt que comprimer les séances. Ce volume est une proposition pédagogique, pas une durée validée par NVIDIA ni une garantie de réussite.

## 1. Le cadre à ne pas inventer

La page officielle décrit un examen Associate en anglais, surveillé à distance, de 50 questions en 60 minutes. Les trois domaines sont Essential AI Knowledge 38 %, AI Infrastructure 40 % et AI Operations 22 %.[1] Ce document reprend ces proportions **pour répartir le temps**, sans affirmer que chaque session réelle contiendra un nombre déterminé de questions par domaine.[1]

NVIDIA mentionne une compréhension de base de l’infrastructure de centre de données ; le diplôme et l’expérience d’entreprise figurent dans les qualifications recommandées, pas comme diplôme obligatoire d’admission.[1] Aucun seuil officiel de réussite n’est établi par les sources officielles consultées ici : ne pas transformer une cible personnelle sur des exercices en note de passage officielle. Reconsulter la page de certification et les politiques liées avant de réserver.[1]

Le parcours recommandé « AI Infrastructure and Operations Fundamentals » est annoncé avec une durée typique de sept heures ; ce n’est ni la durée complète de ce programme de révision ni une obligation de s’arrêter après sept heures.[1] Si tu le suis, impute les passages étudiés au domaine correspondant : n’ajoute pas sept heures invisibles au budget.

## 2. Budget vérifiable : 38 / 40 / 22

Les valeurs ci-dessous sont des **heures décimales**, pas des heures et minutes. Exemple : 15,20 h signifie 15 h 12 min. Les totaux sont calculés sur les pondérations officielles.[1]

| Budget total | Essential — 38 % | Infrastructure — 40 % | Operations — 22 % |
|---|---:|---:|---:|
| 36 h — parcours resserré | 13,68 h | 14,40 h | 7,92 h |
| **40 h — référence** | **15,20 h** | **16,00 h** | **8,80 h** |
| 48 h — consolidation | 18,24 h | 19,20 h | 10,56 h |

**Règle de comptabilité.** Affecter chaque minute à un seul domaine. Une lecture croisée CPU/GPU/réseau peut être divisée en segments, mais pas comptée deux fois. Les exercices blancs mixtes, leur correction et le glossaire sont inclus : répartir leur durée entre domaines selon les erreurs réellement travaillées, puis rééquilibrer les prochaines séances du même domaine. Les temps de pause sont hors budget.

La base hebdomadaire est de 10 h : Essential 3 h 48, Infrastructure 4 h, Operations 2 h 12. Pour 36 h ou 48 h, multiplier les durées des blocs E/I/O par 0,9 ou 1,2 ; conserver les livrables et supprimer ou ajouter de la profondeur, pas un domaine entier. Chaque essai blanc chronométré conserve ses 60 minutes continues ; ajuster le temps de lecture, de consolidation et de correction autour de lui, sans compter deux fois les essais mixtes. Si tu étudies seulement certains jours, déplacer les blocs sans changer leur ordre pédagogique.

## 3. Démarrage — dans les premiers blocs, pas en supplément

Créer un journal personnel avec cinq colonnes : objectif E/I/O, raisonnement initial, erreur, preuve officielle, nouvelle explication sans notes. Marquer **vert** si tu peux expliquer et appliquer, **orange** si tu reconnais seulement les mots, **rouge** si tu confonds deux couches. Ces couleurs sont un diagnostic maison, pas une notation officielle.

Dans le premier bloc Essential, essayer d’expliquer oralement AI/ML/DL, training/inference et CPU/GPU. Dans le premier bloc Infrastructure, dessiner le trajet « stockage → RAM → GPU → réseau → autre nœud ». Dans le premier bloc Operations, expliquer pourquoi une réservation de GPU ne garantit pas un bon débit. Ce sont les thèmes du programme public, organisés ici en activités originales.[1]

Si le vocabulaire anglais ralentit tout, réserver dans chaque bloc cinq à dix minutes au [glossaire](glossaire-en-fr.md), puis revenir immédiatement à un exemple. Ne pas consacrer une semaine entière à apprendre des acronymes sans contexte.

## 4. Les vingt blocs de la base 40 heures

Les blocs E durent chacun **1 h 54**, les blocs I **2 h**, les blocs O **2 h 12**. On peut diviser un bloc en deux séances plus courtes. Les références E01–O04 sont des identifiants pédagogiques locaux du cours, non des codes NVIDIA.

### Semaine 1 — construire la carte du système

| Bloc | Durée | Objectifs et activités | Preuve de compréhension à produire |
|---|---:|---|---|
| E1 | 1 h 54 | E03/E08 : diagnostic ; AI, ML, DL ; CPU et GPU ; commencer le glossaire | Expliquer trois inclusions ou différences avec un exemple et un contre-exemple |
| E2 | 1 h 54 | E02/E07 : entraînement, validation, inférence ; exécuter le lab CPU 1 ; examiner le budget mémoire du lab 2 | Montrer quel paramètre change pendant l’entraînement et reste fixe pendant l’inférence |
| I1 | 2 h | I01/I05 : nœud, cluster, RAM, mémoire GPU, stockage ; schéma du chemin des données | Distinguer capacité disponible par GPU et capacité totale du cluster |
| I2 | 2 h | I03/I06 : puissance, alimentation, refroidissement et contraintes de site ; lire une fiche système identifiée | Séparer puissance maximale spécifiée, consommation mesurée et énergie dans le temps |
| O1 | 2 h 12 | O01/O03 : métriques et identité du GPU ; lab CPU 5 ; première page du journal d’erreurs | Expliquer pourquoi « N/A » n’est pas zéro et pourquoi une mesure isolée ne suffit pas |

### Semaine 2 — choisir une architecture plutôt qu’un slogan

| Bloc | Durée | Objectifs et activités | Preuve de compréhension à produire |
|---|---:|---|---|
| E3 | 1 h 54 | E01/E06 : organiser CUDA, bibliothèques, TensorRT, Triton, GPU Operator et DCGM par rôle | Pour chaque outil, nommer un problème qu’il traite et un qu’il ne traite pas |
| E4 | 1 h 54 | E04/E05 : adoption, cas d’usage ; comparer service interactif et traitement nocturne | Écrire une exigence mesurable avant de proposer un produit |
| I3 | 2 h | I02/I07 : scale up/out, communication ; labs CPU 3 et 4 | Identifier le goulet d’étranglement sans supposer un speedup linéaire |
| I4 | 2 h | I08/I09 : Ethernet, InfiniBand, RDMA/RoCE, PCIe/NVLink ; lire les chemins plutôt que mémoriser des débits | Représenter deux trajets distincts : intra-nœud et inter-nœuds |
| O2 | 2 h 12 | O02 : orchestration et ordonnancement ; lab CPU 6 ; corriger les confusions d’allocation | Justifier un job en attente même si le cluster possède de la mémoire libre au total |

### Semaine 3 — intégrer les contraintes

| Bloc | Durée | Objectifs et activités | Preuve de compréhension à produire |
|---|---:|---|---|
| E5 | 1 h 54 | E01/E06/E07 : reprendre le cycle complet données → modèle → déploiement → observation | Carte annotée avec responsabilité de chaque couche et compatibilité à vérifier |
| E6 | 1 h 54 | E02–E05/E08 : mini-cas sans notes ; revoir les erreurs Essential ; rappel espacé | Deux explications de choix, sans réciter seulement la définition |
| I5 | 2 h | I04/I10 : on-prem/cloud, DPU ; coût, données, contrôle et isolation | Comparaison argumentée ; aucune affirmation « cloud toujours moins cher » |
| I6 | 2 h | I01–I09 : scénario de montée en charge ; facility + réseau + stockage + mémoire | Liste des hypothèses, capacité insuffisante possible, mesure qui validerait le choix |
| O3 | 2 h 12 | O04/O01 : conteneur, VM, passthrough, MIG ; plan d’observation non destructif | Distinguer noyau partagé, allocation, partition matérielle et compatibilité |

### Semaine 4 — consolider et décider

| Bloc | Durée | Objectifs et activités | Preuve de compréhension à produire |
|---|---:|---|---|
| E7 | 1 h 54 | Essai blanc mixte, partie du temps imputée à E ; correction des erreurs Essential | Pour chaque erreur, éliminer explicitement trois distracteurs |
| E8 | 1 h 54 | E01–E08 : rappel sans notes, vocabulaire anglais, reprise du domaine faible | Réexpliquer une confusion après un intervalle, pas juste après avoir lu la solution |
| I7 | 2 h | Essai blanc mixte, partie imputée à I ; correction Infrastructure | Raisonner depuis les exigences jusqu’aux composants |
| I8 | 2 h | I01–I10 : fiche express et étude de scénario final ; vérification du programme public | Aucun objectif rouge oublié derrière la mémorisation des noms de produits |
| O4 | 2 h 12 | Essai blanc mixte, partie imputée à O ; O01–O04 ; relire sécurité et métriques | Construire un ordre d’investigation avant toute action intrusive |

**Organisation des essais mixtes.** Réserver une heure continue à l’intérieur de ces blocs pour chaque essai chronométré, puis répartir cette heure et la correction entre E/I/O dans le journal. Deux essais ne doivent pas être des relectures immédiates de la même banque. Ils sont des entraînements originaux, jamais présentés comme des questions réellement vues à l’examen. Utiliser les deux banques originales [examen A](../questions/examen-A.md) et [examen B](../questions/examen-B.md), sans consulter leur correction avant l’essai.

## 5. Ajuster 36 h et 48 h sans déformer les pondérations

**36 h :** commencer par les notions rouges, raccourcir les deuxièmes lectures et les fiches décoratives. Conserver les six petits labs CPU, les comparaisons, une correction raisonnée et les objectifs de chaque domaine. Les ressources tierces servent seulement à débloquer une confusion précise ; ne pas ouvrir six guides concurrents en parallèle.

**48 h :** ajouter de la profondeur dans chaque domaine à hauteur de son budget : nouveaux scénarios Essential, seconde architecture Infrastructure et investigation Operations à partir de données fictives. Le matériel GPU n’est pas obligatoire pour ce parcours : les commandes optionnelles sont dans [labs-avec-gpu.md](../pratique/labs-avec-gpu.md), sans droit implicite d’agir sur une machine partagée.

**Si une semaine est perdue :** décaler le rendez-vous si possible, ou revenir au budget 36 h si les prérequis sont déjà solides ; ne pas présenter 27 h comme le même programme. **Si un domaine est beaucoup plus faible :** augmenter le budget total ou réduire une activité redondante dans ce même domaine. La répartition 38/40/22 est le cadre demandé ici, pas une preuve scientifique d’allocation optimale individuelle.

## 6. Exam strategy — English only

These are study recommendations, not undisclosed NVIDIA testing rules. The official baseline is 50 questions in 60 minutes, in English.[1] That is an average of **72 seconds per question**, calculated from the published totals, not a required per-question timer.

1. **Read the actual instruction.** Identify the required number of answers and words such as *primary*, *best*, *most appropriate*, *NOT* and *EXCEPT*. Do not infer the format from a community article.
2. **Extract the constraint.** Is the scenario about capacity, throughput, latency, isolation, availability, power or operations? Select the option that solves the stated problem rather than the newest product name.
3. **Name the layer.** A scheduler allocates resources; an inference optimizer transforms supported models; a monitoring tool provides signals. A plausible tool at the wrong layer is still the wrong answer.[3][27][38]
4. **Use two passes only if the actual interface allows review.** A personal practice budget is 45 minutes for the first pass and 15 minutes for unresolved items and instruction checks. This is not an official timing requirement or an assertion about the exam interface.
5. **Avoid universal claims.** More GPUs do not remove every data-path constraint. Hardware partitions, virtual machines and containers address different boundaries.[6][44][53]
6. **Review explanations, not letters.** State why the selected option satisfies the constraint and why each alternative fails it. Do not memorize an answer key or buy alleged real-exam dumps.
7. **Treat practice results as diagnostics.** Consistency, explanation quality and objective coverage matter. No local percentage in this course is an official pass score or a passing guarantee.

## 7. Feu vert personnel — décision, pas certification anticipée

Avant de conserver ton rendez-vous, pouvoir : expliquer les huit objectifs Essential, discuter les dix objectifs Infrastructure et raisonner sur les quatre objectifs Operations ; exécuter et commenter les labs CPU ; distinguer mémoire occupée et activité GPU ; justifier le choix d’un outil ; comprendre les consignes d’un scénario en anglais.[1] La grille personnelle compte aussi les erreurs de confiance : une mauvaise réponse très sûre révèle une confusion à corriger.

Pour chaque point encore rouge, écrire une question précise et retrouver une source primaire. Les récits de préparation rapide sont des témoignages dépendant du profil : Eason précise lui-même que son approche accélérée suppose une expérience des clusters GPU.[35] Ils ne remplacent donc ni ton diagnostic ni le programme officiel.

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
[3] https://developer.nvidia.com/tensorrt — NVIDIA TensorRT
[6] https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing — NVIDIA: Scaling Storage for AI Training and Inferencing
[27] https://slurm.schedmd.com/overview.html — Slurm Workload Manager - Overview
[35] https://easontechtalk.com/nvidia-nca-aiio-exam — How I Passed NVIDIA NCA-AIIO in 16 Hours: Study Plan and 7 Exam Topics | Eason Tech Talk
[38] https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html — NVIDIA DCGM Feature Overview
[44] https://docs.nvidia.com/datacenter/tesla/mig-user-guide/introduction.html — NVIDIA MIG User Guide Introduction
[53] https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container — What is a container? | Docker Docs
