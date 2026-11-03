# Fiches express — comparer, décider, éviter les pièges

**Périmètre : E01–E08, I01–I10, O01–O04.** Les codes sont ceux du cours, pas des codes officiels. Ces fiches condensent le raisonnement ; elles ne remplacent pas les chapitres ni ne prédisent les questions. Le programme officiel pondère Essential 38 %, Infrastructure 40 %, Operations 22 %.[1]

## 1. AI, ML, DL : une inclusion n’est pas une équivalence

| Notion | Critère déterminant | Exemple pédagogique | Erreur de classement |
|---|---|---|---|
| AI | Famille large de systèmes et techniques pour des tâches d’intelligence | Système de décision pouvant inclure des règles | Dire que tout système d’IA utilise nécessairement un réseau profond.[48] |
| ML | Apprentissage de régularités à partir de données | Prédiction d’une consommation à partir d’exemples | Confondre programme à règles fixes et modèle entraîné.[48] |
| DL | Réseaux neuronaux profonds | Modèle de reconnaissance d’images à nombreuses couches | Dire qu’un problème devient DL uniquement parce que le dataset est grand.[48] |

**Raisonnement.** Commencer par « comment la fonction a-t-elle été construite ? » avant « sur quel matériel tourne-t-elle ? ». CPU/GPU décrit une plateforme d’exécution, pas une méthode d’apprentissage.[48][62] Un petit modèle ML peut parfaitement être étudié sur CPU : le premier lab le fait réellement, sans prétendre reproduire un entraînement distribué.

## Adoption et usages — E04/E05

Pour les facteurs d’amélioration et d’adoption, reprendre les [sections E04](../cours/01-fondamentaux-ia.md#e04) et [E05](../cours/01-fondamentaux-ia.md#e05) du chapitre 01, avec leurs références : expliquer plusieurs facteurs complémentaires plutôt que d’attribuer tout progrès à un seul GPU.

**Exercice de comparaison original.** Examiner trois situations : détection de défauts en industrie, prévision de demande et assistant documentaire. Pour chacune, nommer la tâche, les données à collecter, une mesure de réussite et une contrainte d’exploitation. Comparer ensuite ses réponses au chapitre : ce sont des exercices de raisonnement, pas une liste de questions annoncées à l’examen.

## 2. Training et inference : comparer la fonction, puis le service

| Dimension | Training | Inference | Pourquoi la distinction compte |
|---|---|---|---|
| Paramètres | Ajustés par apprentissage | Utilisés pour produire une sortie | Le lab 1 observe cette différence avec un poids appris.[48] |
| Données | Exemples et objectif d’apprentissage | Entrées à traiter par un modèle entraîné | Avoir de nouvelles entrées ne signifie pas réentraîner.[48] |
| Logiciels | Cadres et bibliothèques d’apprentissage | Optimisation et service, par exemple TensorRT et Triton | TensorRT n’est pas un système de gestion des files de jobs.[3][60] |
| Service attendu | À préciser : quantité de travail, délai de fin, reprise | À préciser : délai de réponse, concurrence, débit | L’inférence peut être interactive **ou** par lots ; Triton prend en charge plusieurs types de requêtes.[60] |
| Dimensionnement | État et mouvements nécessaires au travail | État et mouvements nécessaires au service | Le stockage et la mémoire restent des contraintes dans les deux cas.[6] |

**Piège :** « training = toujours throughput, inference = toujours latency ». Ce sont des priorités possibles, pas des définitions universelles. Une inférence nocturne peut privilégier le débit ; un service interactif doit vérifier ses délais. La documentation Triton distingue justement des requêtes en temps réel, par lots et en streaming.[60]

**Mini-cas original.** Deux projets utilisent le même modèle : analyse nocturne d’un stock d’images et interaction utilisateur. Ne pas proposer la même politique de regroupement par réflexe : demander d’abord le délai admissible et le débit attendu. Comparer ensuite, dans un essai autorisé, les réglages de batching et les résultats.[60]

## 3. CPU et GPU : complémentarité avant opposition

| Question | CPU | GPU | Conclusion à retenir |
|---|---|---|---|
| Travail visé | Séquences, contrôle et polyvalence | Nombreux travaux parallèles et débit agrégé | Le GPU ne remplace pas toutes les fonctions CPU.[62] |
| Valeur d’un grand nombre d’unités | Dépend de l’algorithme | Dépend du parallélisme exploitable | « Plus de cœurs » sans profil de charge n’est pas un dimensionnement.[62] |
| Accès aux données | Mémoire système, orchestration du travail | Mémoire et trajets du GPU | Un accélérateur rapide peut attendre ses données.[6] |
| Mesure à demander | Temps par étape et ressources consommées | Temps par étape, activité, mémoire et chemins | Observer le système, pas seulement le nom de la puce.[39] |

**Test oral.** « Pourquoi ne suffit-il pas d’acheter le GPU le plus récent ? » Réponse attendue : le programme doit exploiter son parallélisme, disposer de mémoire suffisante et recevoir ses données assez vite ; la topologie et le reste de la pile comptent.[6][19][62]

## 4. Un outil, une couche, un problème

| Élément | Rôle principal | N’en déduis pas que… |
|---|---|---|
| CUDA | Plateforme et modèle de calcul GPU | Un programme Python quelconque utilise automatiquement le GPU.[47] |
| cuDNN / cuBLAS | Primitives spécialisées pour des opérations fréquentes | Une bibliothèque remplace le cycle de déploiement.[62] |
| NCCL | Communications collectives adaptées aux GPU/topologies | NCCL est le fabric physique ou le scheduler.[19] |
| TensorRT | Optimisation et exécution d’inférence | TensorRT est un ordonnanceur de cluster ou un outil général d’entraînement.[3] |
| Triton Inference Server | Service de modèles, backends, batching, API et métriques | Le serveur exige exclusivement des GPU pour tous ses backends : la documentation mentionne aussi CPU.[60] |
| GPU Operator | Gestion de composants logiciels GPU dans Kubernetes | Il est à lui seul le moteur d’autoscaling des requêtes applicatives.[40][51] |
| Slurm | Allocation et ordonnanceur de jobs | Une allocation garantie implique un débit applicatif optimal.[27] |
| DCGM | Télémétrie, santé, statistiques et diagnostics | Une fonctionnalité de diagnostic est toujours sans effet sur la charge ; ici on ne lance aucun diagnostic actif.[38] |
| BMC | Gestion hors bande du système | Il optimise les graphes d’inférence ou apprend les poids.[16] |

**Piège des noms proches.** NVIDIA Triton Inference Server est le logiciel de service décrit dans sa documentation ; le langage Triton cité dans le guide CUDA est une autre technologie. Déterminer lequel le scénario désigne.[60][62]

## 5. Capacité, bande passante, débit, latence

| Grandeur | Question correcte | Mauvaise substitution |
|---|---|---|
| Capacité mémoire | L’état nécessaire tient-il sur les ressources utilisées ? | Répondre uniquement avec la puissance de calcul.[6] |
| Bande passante mémoire ou lien | Combien de données peut-on transférer par unité de temps ? | En déduire la capacité mémoire disponible.[6][62] |
| Débit applicatif | Combien de travail utile est terminé par unité de temps ? | Assimiler le pourcentage d’activité GPU à ce débit.[39][60] |
| Latence | Quel délai pour une requête ou opération ? | Répondre avec le débit moyen sans vérifier le délai.[60] |
| Disponibilité | Le service peut-il continuer pendant les opérations nécessaires ? | Supposer que plus de capacité élimine une interruption de maintenance.[6] |

**Chaîne de diagnostic.** Dans le modèle pédagogique du lab 3, stockage 50 ms, préparation 20 ms et calcul 10 ms ne sont pas des mesures d’un vrai GPU. Le modèle distingue traitement strictement séquentiel et recouvrement idéal ; il fait raisonner sur la limite avant de parler d’accélération. Le résultat n’est pas un benchmark.

## 6. Interconnexions : identifier les deux extrémités

| Besoin | Technologie ou concept pertinent | Condition / piège |
|---|---|---|
| Relier des périphériques au serveur | PCIe | Ne pas appeler tout chemin local « NVLink ».[39] |
| Communications GPU locales compatibles | NVLink, parfois NVSwitch dans un système équipé | La topologie réelle prime sur l’addition des débits théoriques.[16][19] |
| Fabric réseau de calcul | InfiniBand ou réseau Ethernet adapté aux exigences | Les options ne sont pas interchangeables sans conception du réseau.[19] |
| RDMA sur Ethernet | RoCE | Tout trafic Ethernet n’est pas du RDMA.[19] |
| Réseau / périphérique compatible ↔ mémoire GPU | GPUDirect RDMA | Compatibilité de la pile et du chemin indispensable.[19] |
| Stockage ↔ mémoire GPU | GPUDirect Storage | Ne pas le confondre avec n’importe quelle communication GPU↔GPU.[6] |
| Combinaison de contributions des participants | AllReduce / NCCL | Opération logicielle collective, pas marque de câble.[19] |

**Piège :** « le cluster a assez de mémoire au total, donc le modèle tient sur une carte ». La capacité locale et la capacité agrégée ne sont pas une même chose ; le recours à plusieurs GPU exige une prise en charge et des trajets adaptés, pas seulement leur présence.[6][19]

**DPU — trois verbes.** Décharger certaines fonctions d’infrastructure, les accélérer avec des mécanismes spécialisés, isoler les domaines. Le déplacer de calcul sans accélération adaptée n’est pas une promesse de gain ; l’article BlueField explique explicitement pourquoi déplacer arbitrairement du travail applicatif vers des cœurs DPU ne suffit pas.[12]

## 7. Site et déploiement : grille de décision, pas réponse universelle

La comparaison on-premises/cloud, les besoins de site et la puissance/refroidissement font partie des objectifs publics.[1] Utiliser cette grille de questions pour produire son propre dossier, sans inventer une économie chiffrée :

| Axe | À vérifier pour une proposition locale | À vérifier pour une proposition cloud |
|---|---|---|
| Capacité | Matériel réellement disponible, temps d’installation, marge | Instance, région, quotas et capacité effectivement disponibles |
| Données | Localisation, droits, stockage et accès | Autorisation de transfert, localisation, coût de mouvement à confirmer |
| Exploitation | Responsabilité des changements, inventaire et support | Partage contractuel des responsabilités et limites du service |
| Coût | Hypothèses d’utilisation, durée, site et personnel | Prix réellement proposés, durée, stockage et transferts |
| Réversibilité | Mise à niveau et remplacement | Portabilité, export des données et dépendances |

Ces lignes sont des **questions d’analyse**, pas des affirmations de prix ou de fonctionnalités d’un fournisseur. La bonne réponse dépend des contraintes données. « Cloud toujours moins cher » et « on-prem toujours plus rapide » ne découlent pas de la seule catégorie d’hébergement.

Pour le site, lire la spécification du **modèle précis**. La documentation DGX H100/H200 distingue composants, poids, blocs d’alimentation, puissance et redondance.[16] Ne pas multiplier simplement le nombre de PSU par leur puissance pour affirmer la consommation réelle du système. Ne pas transposer la même installation à tous les DGX. Une fiche de révision ne remplace pas l’étude électrique et thermique d’une installation.

## 8. Scheduler, orchestrateur, monitoring : trois responsabilités

| Situation | Responsabilité à examiner | Pourquoi |
|---|---|---|
| Un job attend des ressources | Ordonnanceur, contraintes et file | Slurm arbitre des demandes concurrentes et alloue des ressources.[27] |
| Un service doit conserver un état désiré | Contrôleurs Kubernetes | Les boucles de contrôle rapprochent l’état réel de l’état déclaré.[51] |
| Le GPU apparaît mais sa pile logicielle doit être gérée | GPU Operator dans une configuration supportée | Il automatise plusieurs composants matériels/logiciels de la pile GPU.[40] |
| Une charge est lente ou présente une erreur GPU | Signaux DCGM/nvidia-smi + contexte du travail | Télémétrie et santé éclairent l’investigation ; elles ne remplacent pas une politique d’allocation.[38][39] |

**Mini-cas du lab 6.** Deux nœuds fictifs ont chacun de la mémoire libre, mais aucun ne peut satisfaire une demande indivisible à cet instant. La somme du cluster ne suffit pas. Notre algorithme first-fit parcourt ensuite un plus petit job ; il n’émule pas une politique complète de Slurm ou Kubernetes et ne démontre aucune garantie d’équité.

## 9. VM, conteneur, MIG et vGPU : ne pas mélanger les frontières

| Mécanisme | Ce qui est organisé ou isolé | Vérification nécessaire |
|---|---|---|
| VM | Machine et système invité avec son noyau | Hyperviseur, pilote invité et chemin GPU supportés.[53][44] |
| Conteneur | Processus et fichiers, avec noyau partagé sur l’hôte | Runtime et accès GPU ; le conteneur ne fournit pas à lui seul un noyau indépendant.[53][40] |
| GPU pass-through | Exposition directe à un invité compatible | Topologie et support ; ne pas en déduire une mutualisation arbitraire.[44] |
| MIG | Ressources matérielles partitionnées avec chemins mémoire isolés sur GPU compatibles | Modèle, profils, version et configuration ; pas « tous les GPU ».[44][61] |
| vGPU | GPU virtuel en environnement hyperviseur | Matrice et droits de la solution retenue ; peut être combiné avec MIG dans des configurations supportées.[44] |

**Piège chiffré à éviter.** La table officielle indique par exemple quatre instances maximales sur A30 et sept sur certains H100 ; elle contient aussi des produits ultérieurs.[61] « MIG = A100/H100 uniquement » et « MIG = sept partout » sont donc de mauvaises règles. Le nombre exact n’est utile qu’avec le modèle et les profils concernés.

## 10. Métriques : ce que le nombre dit réellement

| Observation | Interprétation prudente | Conclusion non démontrée |
|---|---|---|
| GPU utilization élevé | Des kernels sont actifs pendant une grande partie de la fenêtre | Tout le calcul est efficace ou la performance maximale est atteinte.[39] |
| Mémoire occupée élevée | De la mémoire est allouée/occupée | Le GPU calcule activement tout le temps.[39] |
| Memory utilization élevé | Activité de lectures/écritures mémoire pendant la fenêtre | Même chose que pourcentage de capacité occupée.[39] |
| N/A | Information non supportée ou indisponible dans ce contexte | Valeur zéro ou absence de panne.[39] |
| Température ou consommation inhabituelle | Signal à corréler avec limites, charge et ralentissements | Remplacement matériel immédiat obligatoire.[38][39] |
| Code Xid observé | Code à interpréter avec événements et contexte | La valeur numérique est un compteur d’incidents.[38][39] |

**Ordre d’investigation pédagogique.** Décrire l’impact → identifier nœud/GPU/job et période → vérifier changements récents → inspecter ressources et télémétrie → comparer aux exigences et à une référence pertinente → faire valider une action. Dans ce parcours, aucun reset, partitionnement, stress test, changement de pilote ni modification de cluster n’est autorisé implicitement. La présence d’une commande dans une documentation ne constitue pas une autorisation de l’exécuter.

## Exam traps — English practice checklist

- **Purpose before product:** What constraint must the selected option satisfy?
- **Capacity is not throughput:** Are the units and the scope consistent?
- **Allocated is not utilized:** A scheduled GPU can still wait for data.[27][6]
- **Busy is not efficient:** GPU activity is not useful application throughput.[39][60]
- **Local is not distributed:** Identify both communication endpoints.[19]
- **Supported is not universal:** Check the GPU model, profile and software configuration.[44][61]
- **Typical is not always:** Real-time and batched inference both exist.[60]
- **Monitoring is not remediation:** Reading a signal does not justify a disruptive change.[38][39]
- **One source is not an exam guarantee:** Community study time and practice scores are not official passing criteria.[1][35]

## Auto-contrôle — réponses originales

**1. Un modèle produit une prédiction sans modifier ses poids : training ou inference ?** Inférence ; la fonction de l’opération, et non le GPU utilisé, fait la distinction.[48]

**2. Le service doit exposer plusieurs modèles avec API et batching : TensorRT ou Triton pour la couche serveur ?** Triton correspond au service ; TensorRT peut être une technologie utilisée pour certains modèles derrière ce serveur.[3][60]

**3. Un nombre « N/A » doit-il entrer dans une moyenne comme zéro ?** Non ; conserver le statut indisponible, documenter le nombre d’échantillons valides, et ne pas fabriquer une activité nulle.[39]

**4. Une VM contenant des conteneurs est-elle contradictoire ?** Non ; les conteneurs peuvent fonctionner dans une VM et partager son noyau invité.[53]

**5. Une moyenne de gradients est-elle toujours la somme brute ?** Non ; dans notre lab à deux contributions de poids égal, on divise la somme par deux. Le lab illustre une réduction et redistribution ; ce n’est ni une mesure NCCL ni une règle universelle sur les conventions de tous les frameworks.[19]

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
[3] https://developer.nvidia.com/tensorrt — NVIDIA TensorRT
[6] https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing — NVIDIA: Scaling Storage for AI Training and Inferencing
[12] https://developer.nvidia.com/blog/offloading-and-isolating-data-center-workloads-with-bluefield-dpu — Offloading and Isolating Data Center Workloads with NVIDIA Bluefield DPU | NVIDIA Technical Blog
[16] https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html — Introduction to NVIDIA DGX H100/H200 Systems — NVIDIA DGX H100/H200 User Guide
[19] https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io — Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog
[27] https://slurm.schedmd.com/overview.html — Slurm Workload Manager - Overview
[35] https://easontechtalk.com/nvidia-nca-aiio-exam — How I Passed NVIDIA NCA-AIIO in 16 Hours: Study Plan and 7 Exam Topics | Eason Tech Talk
[38] https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html — NVIDIA DCGM Feature Overview
[39] https://docs.nvidia.com/deploy/nvidia-smi/index.html — NVIDIA System Management Interface
[40] https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html — NVIDIA GPU Operator Overview
[44] https://docs.nvidia.com/datacenter/tesla/mig-user-guide/introduction.html — NVIDIA MIG User Guide Introduction
[47] https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html — CUDA C++ Programming Guide
[48] https://www.ibm.com/think/topics/machine-learning — IBM: What is machine learning?
[51] https://kubernetes.io/docs/concepts/overview — Overview | Kubernetes
[53] https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container — What is a container? | Docker Docs
[60] https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html — NVIDIA Triton Inference Server — NVIDIA Triton Inference Server
[61] https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-gpus.html — Supported GPUs — NVIDIA Multi-Instance GPU User Guide
[62] https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/introduction.html — 1.1. Introduction — CUDA Programming Guide
