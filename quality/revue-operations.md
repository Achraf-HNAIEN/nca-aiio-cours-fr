# Revue indépendante — Operations

## Verdict

**PASS_WITH_CORRECTIONS — fond technique accepté ; corrections de qualité recommandées avant publication.** Aucun contresens technique bloquant trouvé. Les 22 questions ont chacune une seule réponse défendable parmi leurs quatre choix ; les 66 explications de distracteurs sont cohérentes avec leurs énoncés. Une faiblesse pédagogique moyenne et deux lacunes mineures de citation sont détaillées ci-dessous. Aucune modification des contenus évalués, aucun commit/push.

Revue réalisée le 3 novembre 2026 par un agent distinct de l'auteur. Périmètre intégral : `cours/07-exploitation-et-observabilite.md` (153 lignes), `cours/08-orchestration-et-virtualisation.md` (178 lignes), les 22 entrées de `questions/operations.json`, et les 26 cartes de `revision/flashcards-operations.tsv` (lignes 2–27, sans identifiants propres). Les quatre fichiers ont été lus entièrement. Comparaison avec `research/official-exam.txt`, le registre des sources et les documentations officielles récupérées indépendamment en direct.

## Couverture du référentiel

Les objectifs O01–O04 sont bien annoncés comme des codes pédagogiques locaux. Le référentiel officiel distingue management/monitoring, orchestration/job scheduling, métriques GPU et considérations de virtualisation ; il ne publie pas ces codes locaux.[1]

| Objectif | Enseignement vérifié | Questions | Cartes portant le tag |
|---|---|---|---|
| O01 | Chap. 07 : BMC/OOB, outils, collecte, runbook, conservation des preuves | O-001, O-002, O-003, O-022 : 4 | 5 |
| O02 | Chap. 08 : Slurm/GRES, Kubernetes, placement, plugin, runtime/toolkit, Operator | O-008, O-009, O-012, O-013, O-014, O-015 : 6 | 7 |
| O03 | Chap. 07 : utilisation, mémoire, températures, puissance, ECC/Xid, données absentes | O-004, O-005, O-006, O-007, O-016, O-017, O-018 : 7 | 9 |
| O04 | Chap. 08 : conteneurs/VM, passthrough, vGPU, MIG, compatibilité/licences | O-010, O-011, O-019, O-020, O-021 : 5 | 6 |

Une carte est étiquetée O02 et O03 : les effectifs par tag ne sont donc pas un total de cartes distinctes. Tous les quatre objectifs sont couverts à un niveau fondamental ; cela n'est pas une garantie d'exhaustivité de l'examen. Base Command apparaît dans les lectures conseillées officielles mais son absence de ces deux chapitres n'est pas considérée comme une violation d'un objectif explicitement obligatoire.[1]

## Vérification technique et des appuis documentaires

- **BMC/OOB : conforme.** La source IGX décrit console Ethernet, reset, alimentation, contrôle d'accès et capteurs. Le chapitre précise correctement le périmètre produit et la dépendance à l'alimentation/connectivité de gestion ; il ne fait pas du BMC un profiler CUDA.[20]
- **Outils GPU : conforme.** `nvidia-smi` est présenté comme inspection ponctuelle, avec valeurs non supportées `N/A` et sortie non garantie rétrocompatible. DCGM distingue groupes, santé passive et diagnostics actifs exclusifs ; un groupe DCGM n'impose pas l'isolation OS. DCGM Exporter expose les champs pour Prometheus, sans être le scheduler ni le stockage historique ; moteur embarqué ou séparé et combinaisons de versions testées sont explicitement documentés.[39][38][57]
- **Utilisation et mémoire : conforme.** Le cours distingue temps avec kernels actifs, quantité framebuffer occupée et temps d'accès mémoire globale. Il n'assimile aucun de ces indicateurs à la bande passante saturée ou au rendement théorique.[39]
- **Température, puissance, ECC et Xid : conforme.** Pas de seuil thermique universel, pas d'équivalence watts/énergie, ni remplacement automatique sur un Xid. Les compteurs ECC sont contextualisés par type et durée ; les causes Xid peuvent être matérielles, logicielles NVIDIA ou applicatives. Le périmètre MIG des métriques et la distinction absence/zéro sont conservés.[39][37]
- **Kubernetes/Operator/plugin/toolkit : conforme.** Annonce de ressources, placement, intégration runtime et dépendances applicatives restent distincts. Le comportement limits/requests est correctement limité au mécanisme GPU de ressources étendues documenté. GPU Operator automatise plusieurs composants sans devenir le scheduler universel.[41][40][42]
- **Slurm : conforme.** Demande explicite de GRES, `--gres` par nœud, numérotation `CUDA_VISIBLE_DEVICES` et cgroups sont correctement décrits ; aucune réservation ne promet de paralléliser le programme automatiquement.[43]
- **Conteneurs et VM : fond exact, citation à compléter.** Docker explicite le noyau propre d'une VM et le noyau partagé des conteneurs ; l'architecture toolkit citée dans le cours ne suffit pas à elle seule pour cette comparaison : constat OPS-02.[53][42]
- **Passthrough/vGPU/MIG : conforme.** L'assignation entière exclusive est bien limitée au mécanisme décrit ; la supervision depuis l'invité est explicitement documentée. MIG n'est assimilé ni à une VM ni au time slicing, et sa combinaison avec vGPU reste conditionnée au support. Les capacités sont limitées au modèle et aux versions ; la référence vers la liste de GPU doit être ajoutée : OPS-03.[56][44][58]
- **Compatibilité et licences : conforme et correctement circonscrit.** Capacité framebuffer insuffisante pour conclure au support des API ; vérification profil/GPU/hyperviseur/versions requise. Le guide de licensing vise vGPU Software et distingue enforcement logiciel/EULA. Le cours n'étend pas les règles vWS à tout CUDA, passthrough ou MIG bare metal.[58][59]

## Revue individuelle de toutes les questions

Pour chaque ligne : énoncé et quatre choix en anglais lus, clé vérifiée, explication française vérifiée, **les trois distracteurs et leurs explications vérifiés**. « OK » signifie une seule meilleure réponse dans le scénario fourni, pas une validation d'une configuration matérielle réelle.

| ID revu | Objectif | Clé actuelle | Contrôle décisif | Verdict |
|---|---|---|---|---|
| O-001 | O01 | A | Chemin console/alimentation distinct de l'OS indisponible | OK |
| O-002 | O01 | B | Interface DCGM → exposition Prometheus | OK |
| O-003 | O01 | C | Diagnostic explicitement exclusif : intervention approuvée | OK |
| O-004 | O03 | D | Utilisation temporelle, pas efficacité maximale | OK |
| O-005 | O03 | A | Allocations résidentes compatibles avec faible activité | OK |
| O-006 | O03 | B | Indices thermiques : refroidissement/capteurs | OK |
| O-007 | O03 | C | Xid : preuves et contexte avant diagnostic causal | OK |
| O-008 | O02 | D | Demande GPU nécessaire dans le mécanisme GRES donné | OK |
| O-009 | O02 | A | Device plugin chargé d'annoncer la ressource | OK |
| O-010 | O04 | B | VM et GPU entier exclusif : passthrough | OK |
| O-011 | O04 | C | Partition matérielle calcul/chemins mémoire : MIG | OK |
| O-012 | O02 | D | Automatisation de toute la pile : GPU Operator | OK |
| O-013 | O02 | A | Runtime non intégré : Container Toolkit | OK |
| O-014 | O02 | B | Limite GPU utilisée comme demande implicite | OK |
| O-015 | O02 | C | GPU libres ailleurs ne satisfont pas le label requis | OK |
| O-016 | O03 | D | N/A peut signaler un champ non supporté | OK |
| O-017 | O03 | A | ECC : type, périmètre et évolution du compteur | OK |
| O-018 | O03 | B | Consommation observée distincte de la limite | OK |
| O-019 | O04 | C | Certains modes vGPU Software : obligation EULA sans checkout | OK |
| O-020 | O04 | D | Mémoire suffisante ne valide pas toute la combinaison | OK |
| O-021 | O04 | A | MIG et vGPU peuvent être combinés si supportés | OK |
| O-022 | O01 | B | Incident intermittent : séries temporelles et corrélation | OK |

Les 22 identifiants sont uniques, avec 11 questions d'examen A et 11 d'examen B. Chaque objet possède quatre choix A–D, une clé existante, exactement trois explications de distracteurs couvrant les autres lettres, et des identifiants de sources existants. Les sources de la bonne réponse sont adéquates pour chaque question ; certaines sources complémentaires des distracteurs ne sont pas individuellement répétées dans `source_ids`, sans conséquence sur la correction technique.

## Revue de toutes les flashcards

**26/26 cartes acceptées techniquement.** Lecture de chaque front/back et de ses références : lignes 2–6 (BMC, OOB, outils, exporter, diagnostics), 7–14 (Xid, utilisation, mémoire, raisonnement, thermique, puissance, ECC, N/A), 15–21 (GRES, visibilité, plugin, requests, toolkit, Operator, allocation/productivité), 22–27 (passthrough, supervision invité, partage, MIG/vGPU, compatibilité, licences). Chaque ligne a exactement trois colonnes TSV `Front`, `Back`, `Tags`. Aucun raccourci n'a transformé une restriction produit/licence en règle universelle.

## Constats et corrections exactes recommandées

### OPS-01 — Moyenne — Clés systématiquement cycliques

- **Fichier/localisation :** `questions/operations.json`, O-001 à O-022, champ `answer` et ordre des choix.
- **Problème :** la clé suit exactement A,B,C,D en boucle dans l'ordre du fichier : `ABCDABCDABCDABCDABCDAB`. Cela donne un indice positionnel sans rapport avec le contenu si les questions sont présentées dans cet ordre ; ce n'est pas une erreur de bonne réponse. Un moteur qui mélange effectivement les choix peut neutraliser cette faiblesse, mais ce comportement n'a pas été vérifié ici.
- **Preuve :** test Python `all(q['answer'] == 'ABCD'[i % 4] for i, q in enumerate(questions))` → `True` ; répartition A=6, B=6, C=5, D=5.
- **Correction exacte proposée :** conserver intégralement textes et explications ; pour chaque question échanger l'option actuellement correcte avec l'option de la lettre cible suivante, déplacer l'explication du distracteur échangé sur l'ancienne lettre correcte, puis mettre à jour `answer` : `O-001:A, O-002:B, O-003:B, O-004:C, O-005:D, O-006:B, O-007:D, O-008:B, O-009:D, O-010:A, O-011:C, O-012:D, O-013:C, O-014:A, O-015:A, O-016:B, O-017:A, O-018:C, O-019:D, O-020:B, O-021:A, O-022:C`. Les cibles identiques à la clé actuelle ne nécessitent aucun échange. Cette permutation conserve A=6/B=6/C=5/D=5 ; revérifier les 22 associations choix/explications après modification. Autre résolution recevable : vérifier et documenter un mélange des choix à chaque présentation, sans perdre l'association des explications.

### OPS-02 — Faible — Comparaison noyau conteneur/VM insuffisamment sourcée localement

- **Fichier/localisation :** `cours/08-orchestration-et-virtualisation.md`, ligne 79, §3.2.
- **Problème :** l'affirmation est exacte mais seule la référence toolkit [42] est donnée au paragraphe ; elle ne formule pas explicitement la différence des noyaux VM/conteneur.
- **Preuve :** Docker indique « a VM is an entire operating system with its own kernel » et « If you run multiple containers, they all share the same kernel ».[53]
- **Correction exacte :** remplacer la première phrase par `Un conteneur Linux n'est pas une VM complète : les conteneurs partagent le noyau de leur hôte, tandis qu'une VM dispose de son propre noyau.[53]` ; conserver le reste du paragraphe et [42] pour l'intégration runtime. Ajouter aux Sources : `[53] https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container — What is a container? | Docker Docs`.

### OPS-03 — Faible — Référence MIG trop générale pour les caractéristiques par produit

- **Fichier/localisation :** `cours/08-orchestration-et-virtualisation.md`, ligne 121, §5.3.
- **Problème :** [44] mène à l'introduction, pas à la table des modèles/profils invoquée. Le conseil de vérifier le modèle exact est bon mais le lecteur doit recevoir le lien de support pertinent.
- **Preuve :** l'introduction explique le partitionnement ; la page « Supported GPUs » donne les produits et leur nombre maximum d'instances, par exemple A30=4 et H100-SXM5 80GB=7.[44][61]
- **Correction exacte :** remplacer le paragraphe par `Le nombre d'instances, leurs profils et les fonctionnalités disponibles dépendent du GPU et de la version. La liste « Supported GPUs » donne notamment les modèles pris en charge et leur nombre maximal d'instances ; il ne faut pas transformer la valeur d'un produit en constante valable pour tout GPU NVIDIA. Un GPU d'une architecture récente ne prouve pas à lui seul le support de MIG : vérifier le modèle exact et les configurations supportées.[44][61]` Ajouter aux Sources : `[61] https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-gpus.html — Supported GPUs — NVIDIA Multi-Instance GPU User Guide`.

## Preuves indépendantes et limites

**16 pages officielles récupérées en direct**, HTTP 200 avec contenu documentaire substantiel : sources 1, 20, 37–44, 53, 56–59 et 61. Les corps et URLs après redirection sont conservés dans `research/private/operations-review/`, avec `fetch-manifest.json`. Les sections pertinentes ont été lues, pas seulement les titres ou extraits de recherche. Les pages courtes 20/37/40/41/42/44/58/59/61 ont été lues entièrement ; pour les longs manuels 38/39/43/56/57, seules les sections nécessaires aux affirmations de ces contenus ont été lues. Le référentiel live et la section Docker pertinente ont également été lus.

Extraits courts de contrôle :

- DCGM : « This form of health check is invasive, requiring exclusive access to the target GPUs. »[38]
- `nvidia-smi` : « Percent of time over the past sample period during which one or more kernels was executing on the GPU. » ; mémoire : « Percent of time over the past sample period during which global (device) memory was being read or written. »[39]
- Xid : « The messages can be indicative of a hardware problem, an NVIDIA software problem, or a user application problem. »[37]
- Kubernetes : « Kubernetes will use the limit as the request value by default. »[41]
- Licensing : « When licensing is enforced only through the EULA, no licenses are checked out from the license server. »[59]

**Limites :** revue documentaire et structurelle, sans GPU/cluster/hyperviseur réel, sans exécution des exemples Slurm/GPU, sans audit juridique des contrats ni validation exhaustive de toutes les matrices versions/produits. Les liens `latest` sont mouvants : le verdict concerne les contenus récupérés à la date de revue. Pas de preuve exhaustive d'originalité/plagiat des questions, ni d'accès à une banque officielle non publique ; aucun contenu d'examen confidentiel utilisé. Le rendu final du moteur de quiz et son éventuel mélange des choix n'ont pas été testés. Les empreintes SHA-256 des quatre fichiers évalués sont conservées dans `reviewed-content-sha256.json` afin de délimiter ce verdict. Aucun fichier de cours, questions ou révision n'a été corrigé par cette revue.

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
[20] https://docs.nvidia.com/igx-orin/bmc/latest/introduction.html — NVIDIA IGX BMC Introduction
[37] https://docs.nvidia.com/deploy/xid-errors/introduction.html — NVIDIA Xid Errors Introduction
[38] https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html — NVIDIA DCGM Feature Overview
[39] https://docs.nvidia.com/deploy/nvidia-smi/index.html — NVIDIA System Management Interface
[40] https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html — NVIDIA GPU Operator Overview
[41] https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus — Kubernetes Schedule GPUs
[42] https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/arch-overview.html — NVIDIA Container Toolkit Architecture Overview
[43] https://slurm.schedmd.com/gres.html — Slurm Generic Resource Scheduling
[44] https://docs.nvidia.com/datacenter/tesla/mig-user-guide/introduction.html — NVIDIA MIG User Guide Introduction
[53] https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container — What is a container? | Docker Docs
[56] https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/using-gpu-pass-through.html — NVIDIA Using GPU Pass-Through
[57] https://docs.nvidia.com/datacenter/dcgm/latest/installation/install-dcgm-exporter.html — NVIDIA Install DCGM Exporter
[58] https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/grid-vgpu-introduction.html — Introduction to NVIDIA vGPU Software
[59] https://docs.nvidia.com/vgpu/latest/grid-licensing-user-guide/intro-to-grid-licensing.html — Introduction to NVIDIA vGPU Software Licensing
[61] https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-gpus.html — Supported GPUs — NVIDIA Multi-Instance GPU User Guide
