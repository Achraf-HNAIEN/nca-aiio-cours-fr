# Couverture du programme NCA-AIIO

Programme de référence : page officielle NVIDIA, consultée le 3 novembre 2026.[1] Les codes ci-dessous sont des **repères pédagogiques locaux**, pas des codes NVIDIA. Les deux séries sont originales et non officielles.

| Objectif local | Compétence reformulée | Chapitre / section | Série A | Série B |
|---|---|---|---|---|
| E01 | Décrire la pile logicielle NVIDIA d'un environnement IA | [03-ecosysteme-nvidia.md](../cours/03-ecosysteme-nvidia.md#e01) | E-013, E-014 | E-031, E-032, E-033 |
| E02 | Comparer les exigences d'architecture de l'entraînement et de l'inférence | [02-calcul-et-cycle-de-vie.md](../cours/02-calcul-et-cycle-de-vie.md#e02) | E-010, E-011, E-012 | E-028, E-029, E-030 |
| E03 | Différencier IA, machine learning et deep learning | [01-fondamentaux-ia.md](../cours/01-fondamentaux-ia.md#e03) | E-001, E-002, E-003 | E-020, E-021 |
| E04 | Expliquer les facteurs d'amélioration et d'adoption de l'IA | [01-fondamentaux-ia.md](../cours/01-fondamentaux-ia.md#e04) | E-004, E-005 | E-022, E-023 |
| E05 | Expliquer les principaux cas d'usage et secteurs | [01-fondamentaux-ia.md](../cours/01-fondamentaux-ia.md#e05) | E-006, E-007 | E-024, E-025 |
| E06 | Expliquer le rôle et les cas d'usage des solutions NVIDIA | [03-ecosysteme-nvidia.md](../cours/03-ecosysteme-nvidia.md#e06) | E-015, E-016, E-017 | E-034, E-035 |
| E07 | Décrire les logiciels du cycle de développement et de déploiement IA | [02-calcul-et-cycle-de-vie.md](../cours/02-calcul-et-cycle-de-vie.md#e07) | E-018, E-019 | E-036, E-037, E-038 |
| E08 | Comparer les architectures CPU et GPU | [02-calcul-et-cycle-de-vie.md](../cours/02-calcul-et-cycle-de-vie.md#e08) | E-008, E-009 | E-026, E-027 |
| I01 | Identifier le matériel adapté à une tâche d'entraînement | [04-serveurs-et-stockage.md](../cours/04-serveurs-et-stockage.md#i01) | I-001, I-011 | I-021, I-031 |
| I02 | Adapter et étendre une infrastructure GPU selon l'usage | [04-serveurs-et-stockage.md](../cours/04-serveurs-et-stockage.md#i02) | I-002, I-012 | I-022, I-032 |
| I03 | Identifier les notions et spécifications générales d'alimentation et de refroidissement | [06-datacenter-et-dimensionnement.md](../cours/06-datacenter-et-dimensionnement.md#i03) | I-003, I-013 | I-023, I-033 |
| I04 | Comparer les avantages et contraintes on-premises et cloud | [06-datacenter-et-dimensionnement.md](../cours/06-datacenter-et-dimensionnement.md#i04) | I-004, I-014 | I-024, I-034 |
| I05 | Identifier les composants et considérations d'un cluster accéléré | [04-serveurs-et-stockage.md](../cours/04-serveurs-et-stockage.md#i05) | I-005, I-015 | I-025, I-035 |
| I06 | Identifier les exigences du site datacenter | [06-datacenter-et-dimensionnement.md](../cours/06-datacenter-et-dimensionnement.md#i06) | I-006, I-016 | I-026, I-036 |
| I07 | Déterminer les exigences réseau d'une charge IA | [05-reseaux-et-dpu.md](../cours/05-reseaux-et-dpu.md#i07) | I-007, I-017 | I-027, I-037 |
| I08 | Identifier et décrire les protocoles et concepts réseau de datacenter | [05-reseaux-et-dpu.md](../cours/05-reseaux-et-dpu.md#i08) | I-008, I-018 | I-028, I-038 |
| I09 | Identifier les réseaux haute vitesse et leurs usages | [05-reseaux-et-dpu.md](../cours/05-reseaux-et-dpu.md#i09) | I-009, I-019 | I-029, I-039 |
| I10 | Expliquer le rôle et les avantages d'un DPU | [05-reseaux-et-dpu.md](../cours/05-reseaux-et-dpu.md#i10) | I-010, I-020 | I-030, I-040 |
| O01 | Décrire les fondamentaux de gestion et de monitoring d'un datacenter IA | [07-exploitation-et-observabilite.md](../cours/07-exploitation-et-observabilite.md#2-bmc-et-administration-hors-bande) | O-001, O-002, O-003 | O-022 |
| O02 | Décrire orchestration de cluster et planification des jobs | [08-orchestration-et-virtualisation.md](../cours/08-orchestration-et-virtualisation.md#1-de-la-demande-utilisateur-à-lexécution) | O-008, O-009 | O-012, O-013, O-014, O-015 |
| O03 | Expliquer les métriques et critères de surveillance des GPU | [07-exploitation-et-observabilite.md](../cours/07-exploitation-et-observabilite.md#4-lire-correctement-les-métriques-gpu) | O-004, O-005, O-006, O-007 | O-016, O-017, O-018 |
| O04 | Identifier les considérations de virtualisation d'une infrastructure accélérée | [08-orchestration-et-virtualisation.md](../cours/08-orchestration-et-virtualisation.md#5-virtualiser--trois-mécanismes-à-distinguer) | O-010, O-011 | O-019, O-020, O-021 |

## Contrôles de structure

- 22 objectifs reliés à des sections explicites.
- Chaque objectif possède au moins une question dans **chacune** des séries.
- Chaque série possède 50 questions : 19 Essential, 20 Infrastructure, 11 Operations.
- La couverture des objectifs ne prouve pas à elle seule l’exactitude technique ; les revues indépendantes et leurs limites sont rapportées séparément.

## Répartition calculée depuis la banque

| Série | Essential | Infrastructure | Operations | Total |
|---|---:|---:|---:|---:|
| A | 19 | 20 | 11 | 50 |
| B | 19 | 20 | 11 | 50 |

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
