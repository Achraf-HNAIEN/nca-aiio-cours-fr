# Revue indépendante — Infrastructure NCA-AIIO

## Verdict

**Acceptation conditionnelle.** Les trois chapitres, les 40 questions et les 32 flashcards ont été lus intégralement. I01–I10 sont couverts. Aucune erreur factuelle bloquante ni clé techniquement fausse n’a été identifiée ; quatre corrections sont demandées : un motif de réponses exploitable (moyen), une condition mémoire implicite, une ambiguïté bilingue et un titre mal décodé (faibles). Le JSON associé donne les corrections exactes et les positions de réponses proposées.

Contrôle indépendant de l’auteur : aucune modification des chapitres, questions, cartes ou registre partagé. Le rapport auteur a été confronté aux fichiers réels, pas pris comme preuve de conformité.

## Constats prioritaires

### INF-01 — medium — assessment_validity
**Cible :** `questions/infrastructure.json`, I-001 à I-040, champ answer ; les deux examens A/B.

Les 40 clés suivent exactement ABCD répété. L’équilibre des lettres masque un motif exploitable sans connaissance du contenu ; ce n’est pas une erreur de clé technique mais une faiblesse importante de simulation.

**Preuve calculée :** `ABCDABCDABCDABCDABCDABCDABCDABCDABCDABCD` ; 40/40 positions suivent le cycle ABCD. Chaque examen conserve pourtant cinq occurrences de chaque lettre.
**Correction exacte :** Permuter les quatre choix de chaque question pour placer le choix actuellement correct à la lettre indiquée dans recommended_answer_positions ; remapper answer ET les clés de distractors par la même permutation. Garder les textes et les identifiants. Vérifier ensuite unicité de la bonne réponse et cinq A/B/C/D dans chaque examen. Ne pas changer uniquement answer. La table de positions figure dans le JSON.

### INF-02 — low — memory_condition_precision
**Cible :** `questions/infrastructure.json`, I-021.question, ligne 498 ; I-021.explanation, ligne 506.

« the model and each working batch fit » laisse implicites gradients, états optimiseur, activations et buffers temporaires ainsi que leur co-résidence. La réponse A reste le meilleur choix, mais le lecteur pourrait croire que poids + données du lot suffisent à établir la faisabilité de l’entraînement.

**Preuve :** le chapitre 04, ligne 20, décrit déjà poids, états optimiseur, gradients, activations et espaces temporaires ; la documentation PyTorch détaille ces catégories.[79]
**Remplacer le stem par :** A training dataset is much larger than GPU memory, but all tensors required for one training step—including model parameters, optimizer state, gradients, activations, the current batch, and temporary buffers—fit together in usable GPU memory. Which conclusion is justified?
**Explication proposée :** Tout le jeu de données n’a pas à résider en VRAM : l’ensemble des tenseurs requis pour une étape doit y tenir simultanément, et le chemin d’entrée doit fournir les lots à un débit suffisant.

### INF-03 — low — bilingual_semantics
**Cible :** `revision/flashcards-infrastructure.tsv`, ligne 20, Front ; carte 19 hors en-tête.

Le recto anglais demande si le liquide « remove waste heat ». Le refroidissement retire bien la chaleur des composants ; répondre Non ne devient correct que si la question porte sur la suppression du besoin de rejet au site. Le français « élimine » vise cette autre notion.

**Preuve :** le DOE explique que le liquide capture et retire la chaleur des équipements ; il ne fait pas disparaître la nécessité d’évacuer cette chaleur.[72]
**Recto exact :** Does liquid cooling eliminate the need for facility heat rejection? / Le refroidissement liquide supprime-t-il le besoin de rejeter la chaleur hors du site ?
**Verso exact :** Non : il transporte la chaleur des équipements ; le site doit toujours la rejeter. Certaines solutions restent hybrides air-liquide. [72]

### INF-04 — low — source_metadata_encoding
**Cible :** `cours/04-serveurs-et-stockage.md`, Sources [55], ligne 98 ; même titre en 05:104 et 06:100.

Le titre GPUDirect contient un tiret long mal décodé (mojibake). Cela n’invalide pas les faits mais dégrade les références publiées.

**Preuve :** le titre actuel de la documentation porte un tiret long normal.[55]
**Correction exacte :** Remplacer uniquement le titre de la source 55 dans sources/ledger.json par « 1. Overview — GPUDirect RDMA 13.4 documentation », puis régénérer les blocs Sources des trois chapitres. Ne pas modifier URL ni identifiant.

## Vérification technique contradictoire

- **CPU/GPU/mémoire/stockage :** distinctions cohérentes, empreinte complète d’entraînement explicitée, pas de confusion VRAM/SSD ni de fusion mémoire automatique ; RAID 0 décrit comme cache, pas protection durable. Réserves de logiciel et topologie conservées.[6][16][55]
- **NVLink :** le texte évite correctement « toujours intra-node ». La page actuelle décrit explicitement l’extension via NVLink Switch au-delà des nœuds et les domaines rack-scale ; la frontière est liée à la plateforme, pas à tout réseau inter-nœuds.[18]
- **InfiniBand/Ethernet/RoCE :** absence de vainqueur universel, RDMA sur Ethernet reconnu, RoCEv2 IP/UDP vérifié. La référence B200 emploie InfiniBand pour le calcul et offre les deux options pour le stockage ; ce cas ne prouve pas toutes les performances d’une autre architecture.[66][68][80]
- **PFC/ECN :** distinction exacte et périmètre Onyx nommé. Sa table précise PFC sur les ports en lossless, PFC unidirectionnel hôte–ToR en semi-lossless et absence de PFC en lossy. Le texte ne transforme ni lossless en absence absolue de pertes, ni PFC en obligation universelle.[82]
- **GPUDirect/DPU :** chemin mémoire direct distinct d’un processeur d’infrastructure ; les contraintes de pilotes, enregistrement et topologie PCIe subsistent. Le DPU ne devient ni extension VRAM ni remplaçant arbitraire du GPU ; offload/accelerate/isolate est fidèle au corps signé de la source.[12][19][55]
- **Datacenter :** rack, manutention, circuit, PSU, IT/facility, refroidissement et exploitation correctement séparés ; réserves de validation professionnelle appropriées. PUE est un rapport d’énergie et non un score de travail IA ; la variante source est explicitement distinguée du PUE site.[16][67][69]

## Calculs exécutés en Python

Exécution indépendante avec `decimal.Decimal` ; les nombres du chapitre 06:35 et de I-013 sont tous corrects.

| Grandeur | Calcul | Résultat |
|---|---|---|
| IT moyen | 4 × 8 + 3 | 35 kW |
| Facility moyen | 35 × 1,4 | 49 kW |
| Non-IT, pas seulement climatisation | 49 − 35 | 14 kW |
| Énergie IT sur 10 h | 35 × 10 | 350 kWh |
| Énergie facility sur 10 h | 49 × 10 | 490 kWh |
| Énergie non-IT sur 10 h | 14 × 10 | 140 kWh |
| Rapport reconstruit | 490 / 350 | 1,4 |
| Distracteur I-013 D | 35 + 49, double comptage | 84 kW, incorrect |
| Capacité nominale de 6 PSU à 3,3 kW | 6 × 3,3 | 19,8 kW, pas la consommation |

Le chapitre suppose expressément un rapport facility/IT constant : multiplier la puissance moyenne est donc une projection pédagogique recevable, pas une mesure annuelle ni un calibre de circuit. Le DOE donne la définition annuelle et précise les limites du PUE.[72]

## Couverture et verdict par objectif

| Objectif | Questions relues | Verdict |
|---|---|---|
| I01 | I-001, I-011, I-021, I-031 | CPU, GPU, RAM, VRAM, empreinte d’entraînement, stockage et préparation des données : couverts ; préciser I-021. |
| I02 | I-002, I-012, I-022, I-032 | Montée en charge, réplication contre partitionnement, scale-up/scale-out et croissance équilibrée : couverts. |
| I03 | I-003, I-013, I-023, I-033 | Puissance/énergie, IT/facility, TDP/PSU, PUE et calcul : exacts sous hypothèses explicites. |
| I04 | I-004, I-014, I-024, I-034 | Cloud/on-prem/colocation, conformité, responsabilités et TCO : couverts sans promesse économique universelle. |
| I05 | I-005, I-015, I-025, I-035 | Composants du cluster, fabrics, BMC, gestion et dépendances : couverts, quatre fabrics bornés à la référence. |
| I06 | I-006, I-016, I-026, I-036 | Rack, manutention, site, entrées thermiques et refroidissement liquide : couverts ; corriger le recto anglais de la carte 19. |
| I07 | I-007, I-017, I-027, I-037 | Latence, débit utile, simultanéité, topologie, contention et profil applicatif : couverts. |
| I08 | I-008, I-018, I-028, I-038 | Ethernet/IP/TCP, RDMA/RoCEv2, PFC/ECN et bibliothèques : correctement séparés. |
| I09 | I-009, I-019, I-029, I-039 | NVLink/NVSwitch scale-up y compris rack, InfiniBand/Ethernet scale-out et GPUDirect : caveats corrects. |
| I10 | I-010, I-020, I-030, I-040 | DPU offload/accelerate/isolate, distinction NIC/GPUDirect et limites du remplacement CPU/GPU : exacts. |

Chaque objectif possède quatre questions au total, deux par examen. Les 32 cartes couvrent I01–I10 ; toutes les lignes 2–33 ont été relues (seule la ligne 20 fait l’objet d’un constat). Les codes I01–I10 sont bien locaux ; leur correspondance a été comparée aux dix thèmes Infrastructure du blueprint fourni.

## Relecture de toutes les questions

Les stems et quatre choix sont anglais ; les explications et trois réfutations sont français. Chaque clé a été réévaluée sans se contenter du champ `answer`. « Conforme » signifie une seule meilleure réponse parmi les choix, avec justification et distracteurs recevables ; toutes les questions subissent en plus le défaut transversal INF-01. Une attente de synchronisation (I-002) motive un premier contrôle réseau/collectives mais ne démontre pas à elle seule une cause racine.

| ID | Objectif | Clé réévaluée | Verdict et motif |
|---|---|---|---|
| I-001 | I01 | A | Conforme — VRAM suffisante ou partitionnement réel ; SSD, réseau seul et réplication intégrale ne corrigent pas la capacité. |
| I-002 | I02 | B | Conforme — Le chemin inter-nœuds et les collectives sont le meilleur premier examen parmi les choix ; attente ne prouve pas à elle seule la cause racine. |
| I-003 | I03 | C | Conforme — PUE = énergie totale / énergie IT ; limites et période cohérentes. |
| I-004 | I04 | D | Conforme — Pilote court : évaluer un cloud compatible et son coût complet, sans garantie économique. |
| I-005 | I05 | A | Conforme — Calcul, stockage, fabrics et gestion forment le système complet. |
| I-006 | I06 | B | Conforme — Les U libres ne valident pas mécanique, alimentation et thermique. |
| I-007 | I07 | C | Conforme — Petits messages synchronisés : latence pertinente en plus de la bande passante. |
| I-008 | I08 | D | Conforme — RoCE compatible satisfait la demande RDMA sur Ethernet ; les autres choix ne le font pas. |
| I-009 | I09 | A | Conforme — NVLink scale-up et InfiniBand scale-out dans CE scénario ; pas de règle NVLink strictement intra-châssis. |
| I-010 | I10 | B | Conforme — DPU : fonctions réseau, stockage et sécurité adaptées ; pas extension VRAM ou remplacement du GPU. |
| I-011 | I01 | C | Conforme — Saturation du décodage CPU : traiter la préparation des données puis mesurer le débit complet. |
| I-012 | I02 | D | Conforme — Capacité de stockage et performances sont distinctes ; ajout de disques ne garantit pas le débit. |
| I-013 | I03 | A | Conforme — 35 × 1,4 = 49 kW ; 14 est le non-IT, 84 double-compte la charge IT. |
| I-014 | I04 | B | Conforme — Comparer options conformes, utilisation et coûts de cycle de vie ; pas un prix isolé. |
| I-015 | I05 | C | Conforme — Séparer des besoins de trafic et des expositions, sans garantie absolue de résilience. |
| I-016 | I06 | D | Conforme — Températures aux entrées hors limites : étudier la recirculation et le chemin local. |
| I-017 | I07 | A | Conforme — All-to-all simultané : capacité partagée, topologie, congestion et sursouscription. |
| I-018 | I08 | B | Conforme — PFC et ECN sont distincts ; pas de nécessité universelle de PFC sur tous les liens. |
| I-019 | I09 | C | Conforme — Adaptateur vers mémoire GPU sans staging hôte : GPUDirect RDMA ; pas DPU obligatoire. |
| I-020 | I10 | D | Conforme — Isolation des fonctions de contrôle/sécurité opérateur hors OS locataire. |
| I-021 | I01 | A | À préciser (INF-02) — Clé A attendue et unique meilleure réponse ; préciser que TOUS les tenseurs de travail tiennent ensemble (INF-02). |
| I-022 | I02 | B | Conforme — Une réplication intégrale conserve le besoin mémoire par copie. |
| I-023 | I03 | C | Conforme — Capacité nominale des PSU redondantes distincte de la consommation réelle. |
| I-024 | I04 | D | Conforme — Coûts de transfert, stockage, calcul et exploitation sur la durée pertinente. |
| I-025 | I05 | A | Conforme — OOB : accès matériel contrôlé aux BMC ; pas fabric applicatif ni accès public. |
| I-026 | I06 | B | Conforme — Liquide : rejet de chaleur, interfaces compatibles et maintenance restent requis. |
| I-027 | I07 | C | Conforme — Répliques indépendantes : besoin réseau dicté par requêtes, réponses, données et disponibilité. |
| I-028 | I08 | D | Conforme — NCCL est une bibliothèque GPU de collectives et autres communications. |
| I-029 | I09 | A | Conforme — Certains domaines NVLink Switch dépassent un châssis ; architecture et génération obligatoires. |
| I-030 | I10 | B | Conforme — DPU généraliste ne remplace pas arbitrairement le calcul tensoriel GPU. |
| I-031 | I01 | C | Conforme — Nombre identique de GPU ne décrit pas chemin PCIe, placement adaptateur et compatibilité. |
| I-032 | I02 | D | Conforme — Croissance cohérente du calcul, stockage, ports, câbles, alimentation et refroidissement. |
| I-033 | I03 | A | Conforme — PUE seul ne mesure ni débit utile ni efficacité du modèle. |
| I-034 | I04 | B | Conforme — Colocation et propriété du matériel sont deux dimensions distinctes. |
| I-035 | I05 | C | Conforme — Provisionnement, données et exécution nécessitent des couches coordonnées. |
| I-036 | I06 | D | Conforme — Personnel qualifié et assistance appropriée conformément aux consignes du système. |
| I-037 | I07 | A | Conforme — Capacité suffisante et séparation de flux à évaluer pour traiter la contention. |
| I-038 | I08 | B | Conforme — RDMA réduit le travail du chemin de données sans supprimer préparation, enregistrement et pilotes. |
| I-039 | I09 | C | Conforme — InfiniBand ou Ethernet/RoCE : choisir sur validation bout-en-bout et capacité opérationnelle. |
| I-040 | I10 | D | Conforme — Le chemin GPUDirect RDMA ne prouve pas la présence d’un processeur DPU. |

## Sources effectivement lues et limites d’accès

**Sept sources primaires récupérées en direct**, toutes HTTP 200, via requests/BeautifulSoup et pdftotext ; lecture de passages de fond, pas seulement des titres :

| Source | Lecture indépendante |
|---|---|
| [12] | Corps signé, mission, accélération et isolation ; résumé IA non utilisé. Extraction : `research/private/infrastructure-review/source-12.txt` |
| [16] | Composants, RAID, interfaces BMC et spécifications électriques/redondance. Extraction : `research/private/infrastructure-review/source-16.txt` |
| [18] | Scale-up rack, extension multi-nœuds et réserve de spécifications préliminaires. Extraction : `research/private/infrastructure-review/source-18.txt` |
| [55] | Overview, enregistrement mémoire, Supported Systems et contraintes PCIe. Extraction : `research/private/infrastructure-review/source-55.txt` |
| [72] | Sections 5.6 refroidissement et 8.1 PUE, plus passages ciblés air/UPS. Extraction : `research/private/infrastructure-review/source-72.txt` |
| [82] | Congestion ECN/CNP et trois modes lossless/semi-lossless/lossy. Extraction : `research/private/infrastructure-review/source-82.txt` |
| [80] | RoCEv1/v2, IP/UDP et routage ; PDF relu après conversion pdftotext. Extraction : `research/private/infrastructure-review/source-80.txt` |

Les autres références ont été lues dans les extractions privées auteur : stockage, Network IO, fabrics et composants B200, sécurité, EPA historique et guide IT. Le document PyTorch a été lu pour la condition mémoire ; le blueprint est `research/official-exam.txt`. Ces lectures d’extractions ne sont pas présentées comme de nouveaux accès live.[6][19][79]

**Limites explicites :**

- web_extract indisponible : requêtes HTTP requests + BeautifulSoup ; PDF via pdftotext. Sept sources primaires indépendamment récupérées HTTP 200 et passages de fond effectivement lus.
- Les autres références sont vérifiées sur les extractions privées fournies et le registre partagé, pas toutes re-téléchargées. Le blueprint officiel est lu dans research/official-exam.txt, non revalidé en direct.
- Le fichier auteur roce v2 (rocev2.txt) est déclaré binaire à cause d’octets NUL ; la source 80 a été re-téléchargée et convertie indépendamment, ce qui lève ce blocage de lecture. pue.txt est un ancien 404 : pue-authority.txt est la source 69 correcte effectivement lue.
- NVLink : page produit vivante avec chiffres préliminaires ; aucun chiffre préliminaire n’est présenté ici comme norme ni mesure vérifiée. Onyx : version 3.10.4606 LTS, pas garantie universelle des configurations RoCE.
- DOE PDF : texte des formules graphiques imparfait dans pdftotext ; définition PUE en prose lisible et calcul recomposé avec Decimal.
- Pas d’accès au cours payant, à un examen réel, à du matériel GPU/réseau ni à un site électrique ; aucun benchmark ni validation de conception opérationnelle.
- Single-best-answer évalué par lecture contradictoire des quatre choix et des trois réfutations françaises ; pas preuve psychométrique ou garantie d’alignement à toute future version d’examen.

## Traçabilité de la livraison

- `quality/revue-infrastructure.json` : constats structurés, correction exacte, 40 verdicts individuels, 10 verdicts objectifs, calculs et empreintes SHA-256 des cinq fichiers relus.
- `research/private/infrastructure-review/` : extractions indépendantes, manifeste HTTP, contrôles Python et script de génération ; documents sources conservés en privé, pas redistribués dans le cours.
- Le rapport auteur annonçait bien 40 questions, 32 cartes, 32 étiquettes scénario et cinq lettres de chaque sorte par examen. Ces comptes sont reproduits ; ils ne détectaient pas le motif ABCD.
- Aucun chapitre/question/carte corrigé par le reviewer ; corrections à intégrer par le parent, puis revalidation du remappage des clés et distracteurs.

## Sources

[6] https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing — NVIDIA: Scaling Storage for AI Training and Inferencing
[12] https://developer.nvidia.com/blog/offloading-and-isolating-data-center-workloads-with-bluefield-dpu — Offloading and Isolating Data Center Workloads with NVIDIA Bluefield DPU | NVIDIA Technical Blog
[16] https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html — Introduction to NVIDIA DGX H100/H200 Systems — NVIDIA DGX H100/H200 User Guide
[18] https://www.nvidia.com/en-us/data-center/nvlink — NVLink & NVLink Switch: Fastest HPC Data Center Platform | NVIDIA
[19] https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io — Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog
[55] https://docs.nvidia.com/cuda/gpudirect-rdma/index.html — 1. Overview — GPUDirect RDMA 13.4 documentation
[66] https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/network-fabrics.html — Network Fabrics — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200
[67] https://docs.nvidia.com/dgx/dgxh100-user-guide/safety.html — Safety — NVIDIA DGX H100/H200 User Guide
[68] https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html — Key Components of the DGX SuperPOD — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200
[69] https://www.energystar.gov/ia/partners/prod_development/downloads/DataCenterRating_General.pdf — ENERGY STAR for Data Centers — PUE metric
[72] https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design.pdf — DOE Best Practices Guide for Energy-Efficient Data Center Design (2024)
[79] https://docs.pytorch.org/tutorials/intermediate/optimizer_step_in_backward_tutorial.html — PyTorch training memory usage and optimizer state
[80] https://docs.nvidia.com/networking/display/mlnxenv23102131201lts/rdma-over-converged-ethernet-roce.pdf — NVIDIA MLNX_EN 23.10 LTS — RoCE and RoCEv2
[82] https://networking-docs.nvidia.com/onyxum/3104606lts/rdma-over-converged-ethernet-roce — NVIDIA Onyx 3.10.4606 LTS — RoCE (direct documentation URL)
