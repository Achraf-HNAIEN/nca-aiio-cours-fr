# Glossaire anglais → français — NCA-AIIO

Les termes anglais sont conservés tels qu’ils apparaissent dans la documentation technique. Les traductions et définitions sont rédigées pour ce cours ; ce n’est pas une traduction officielle NVIDIA. Lire chaque ligne dans les deux sens : reconnaître le terme anglais, puis expliquer en français son rôle et sa limite. Les termes détaillés servent le raisonnement ; cette liste ne prétend pas annoncer les mots exacts d’une question d’examen. Le périmètre général est celui des trois domaines publics.[1]

## A. IA, apprentissage et cycle de vie — E02 à E05, E07

| English term | Français | Définition utile et distinction |
|---|---|---|
| Artificial intelligence (AI) | Intelligence artificielle | Domaine large des systèmes réalisant des tâches associées à l’intelligence ; ne se limite pas à l’apprentissage automatique.[48] |
| Machine learning (ML) | Apprentissage automatique | Sous-ensemble de l’IA où le modèle apprend des régularités dans des données plutôt que recevoir explicitement chaque règle.[48] |
| Deep learning (DL) | Apprentissage profond | Apprentissage utilisant des réseaux neuronaux à plusieurs couches ; sous-ensemble du ML, pas synonyme de toute IA.[48] |
| Neural network | Réseau de neurones | Modèle composé d’unités reliées et de paramètres ajustables ; les couches transforment les entrées en sorties.[48] |
| Supervised learning | Apprentissage supervisé | Apprentissage d’une correspondance à partir d’entrées et de sorties de référence ; classification et régression en sont des exemples.[48] |
| Unsupervised learning | Apprentissage non supervisé | Recherche de structure dans les données sans cible de référence à prédire pour chaque exemple.[48] |
| Reinforcement learning (RL) | Apprentissage par renforcement | Apprentissage de décisions à partir d’interactions avec un environnement et d’un signal de récompense.[48] |
| Classification | Classification | Prédiction d’une catégorie ; une étiquette discrète n’est pas une valeur numérique continue de régression.[48] |
| Regression | Régression | Prédiction d’une quantité, comme une demande estimée ; ne signifie pas ici « régression logicielle ».[48] |
| Clustering | Regroupement | Constitution de groupes selon des similarités sans imposer les catégories de référence du supervisé.[48] |
| Training | Entraînement | Processus qui ajuste les paramètres du modèle à partir de données et d’un objectif ; distinct de l’application du modèle entraîné.[48] |
| Inference | Inférence | Utilisation du modèle pour produire une sortie sur de nouvelles données ; l’opération n’implique pas à elle seule de réentraîner ses paramètres.[48] |
| Training data | Données d’entraînement | Exemples utilisés pour apprendre ; une bonne performance sur ces seuls exemples ne démontre pas la généralisation.[81] |
| Validation data | Données de validation | Données séparées utilisées pendant le développement pour choisir ou régler un modèle, sans les confondre avec l’évaluation finale.[81] |
| Test data | Données de test | Données réservées à l’évaluation du comportement appris ; les utiliser continuellement pour régler le modèle fragilise cette évaluation.[81] |
| Generalization | Généralisation | Capacité à appliquer les régularités apprises à des données nouvelles pertinentes, au-delà de la mémorisation des exemples.[48] |
| Overfitting | Surapprentissage | Ajustement excessif aux données d’entraînement au détriment de la généralisation.[48] |
| Model parameters | Paramètres du modèle | Valeurs apprises, par exemple les poids ; à distinguer des réglages de l’algorithme d’apprentissage.[48] |
| Hyperparameters | Hyperparamètres | Réglages du processus ou de la structure du modèle, choisis et ajustés dans le développement plutôt qu’appris comme les poids.[48] |
| Gradient descent | Descente de gradient | Méthode d’optimisation ajustant les paramètres selon une direction issue du gradient de l’objectif.[48] |
| Loss function | Fonction de perte | Mesure de l’écart que l’entraînement cherche à réduire ; ce n’est pas automatiquement une métrique métier suffisante.[48] |
| Generative AI | IA générative | Famille de systèmes produisant du contenu ; ne représente pas tous les usages de l’IA.[48] |
| Large language model (LLM) | Grand modèle de langage | Modèle de langage de grande taille ; famille de charges de travail ML, pas type de réseau physique.[48] |
| Batch | Lot | Ensemble d’éléments traités ensemble ; en inférence, le regroupement de requêtes peut être assuré par le serveur selon sa configuration.[60] |

## B. Calcul accéléré et logiciels — E01, E06 à E08

| English term | Français | Définition utile et distinction |
|---|---|---|
| Central processing unit (CPU) | Processeur central | Processeur généraliste orienté notamment vers le contrôle et l’exécution rapide de séquences ; reste indispensable dans un système accéléré.[62] |
| Graphics processing unit (GPU) | Processeur graphique | Processeur adapté au débit de nombreux calculs parallèles ; le GPU n’accélère pas automatiquement tout programme séquentiel.[62] |
| Parallel computing | Calcul parallèle | Répartition de travaux pouvant s’exécuter simultanément ; utile seulement si le calcul et le mouvement des données le permettent.[62] |
| Thread | Fil d’exécution | Séquence d’opérations ; l’exécution de nombreux threads est centrale dans le modèle de calcul GPU.[62] |
| CUDA | CUDA | Plateforme et modèle de programmation de NVIDIA pour exploiter les GPU au-delà des API graphiques.[62] |
| CUDA programming model | Modèle de programmation CUDA | Abstraction définissant comment organiser et exécuter le travail sur la plateforme CUDA ; ne se réduit pas à un modèle particulier de carte GPU.[47] |
| cuBLAS | cuBLAS | Bibliothèque NVIDIA accélérée pour l’algèbre linéaire de base, citée parmi les bibliothèques CUDA.[62] |
| cuDNN | cuDNN | Bibliothèque NVIDIA de primitives pour réseaux neuronaux, utilisée par des logiciels d’apprentissage profond.[62] |
| NCCL | Bibliothèque de communications collectives NVIDIA | Bibliothèque spécialisée dans les communications collectives GPU et adaptée à la topologie ; pas un câble ni un commutateur.[19] |
| TensorRT | TensorRT | Écosystème d’optimisation et d’exécution d’inférence ; n’est pas un ordonnanceur de cluster.[3] |
| Quantization | Quantification | Représentation numérique à précision réduite pour optimiser un modèle, à valider avec ses exigences de qualité et sa compatibilité.[3] |
| NVIDIA Triton Inference Server | Serveur d’inférence NVIDIA Triton | Logiciel de service de modèles, avec plusieurs backends, protocoles et politiques de regroupement ; distinct du langage de programmation Triton.[60][62] |
| Dynamic batching | Regroupement dynamique de requêtes | Assemblage par le serveur de requêtes d’inférence compatibles en lots, selon la configuration du modèle.[60] |
| Model repository | Dépôt de modèles | Emplacement organisé contenant les modèles que Triton doit rendre disponibles pour l’inférence.[60] |
| Backend | Moteur d’exécution spécialisé | Composant auquel Triton transmet les entrées pour exécuter le type de modèle correspondant.[60] |
| NVIDIA AI Enterprise | NVIDIA AI Enterprise | Plateforme logicielle d’entreprise incluant des logiciels de production et une offre de support ; ce n’est pas le nom d’une carte GPU.[60] |
| NVIDIA GPU Operator | Opérateur GPU NVIDIA | Opérateur Kubernetes automatisant la gestion de composants logiciels nécessaires aux GPU : pilotes, device plugin, toolkit et surveillance notamment.[40] |
| NVIDIA Container Toolkit | NVIDIA Container Toolkit | Composant de la pile permettant l’usage des GPU NVIDIA depuis des conteneurs ; ne rend pas le pilote de l’hôte inutile.[40] |
| Device plugin | Module d’exposition des périphériques | Mécanisme Kubernetes utilisé pour rendre des ressources matérielles spécialisées accessibles à l’orchestration.[40] |
| Driver | Pilote | Logiciel de la pile système permettant l’accès au matériel ; sa compatibilité est distincte de la seule présence d’une image de conteneur.[40] |

## C. Infrastructure et chemins des données — I01 à I10

| English term | Français | Définition utile et distinction |
|---|---|---|
| Compute node | Nœud de calcul | Serveur fournissant des ressources de calcul au cluster ; le job peut demander plusieurs nœuds.[27] |
| Cluster | Grappe de machines | Ensemble de nœuds gérés comme un environnement de travail ; les ressources ne deviennent pas pour autant une mémoire unique sans contraintes.[27][6] |
| GPU memory | Mémoire du GPU | Mémoire directement associée au GPU qui contient les données et états du calcul ; capacité et débit sont deux caractéristiques différentes.[6] |
| System memory | Mémoire système | RAM du serveur, distincte de la mémoire GPU ; les fiches système présentent séparément ces capacités.[16] |
| Memory bandwidth | Bande passante mémoire | Quantité de données que le chemin mémoire peut transporter par unité de temps ; ne décrit pas sa capacité de stockage.[62] |
| PCIe | PCI Express | Interconnexion utilisée dans le trajet des périphériques du serveur ; un chemin PCIe n’est pas automatiquement un chemin NVLink.[19][39] |
| NVLink | NVLink | Interconnexion NVIDIA de communication rapide entre composants compatibles, notamment GPU ; lire la topologie réelle plutôt que supposer un accès uniforme.[19][39] |
| NVSwitch | NVSwitch | Technologie de commutation utilisée pour interconnecter des GPU via NVLink dans des systèmes compatibles, par exemple DGX H100/H200.[16] |
| Network interface card (NIC) | Carte réseau | Adaptateur reliant le système au réseau ; dans le contexte de la source, NIC désigne notamment l’adaptateur Ethernet.[19] |
| Host channel adapter (HCA) | Adaptateur de canal hôte | Adaptateur hôte utilisé notamment pour InfiniBand ; ne pas le confondre avec le commutateur du fabric.[19] |
| Ethernet | Ethernet | Famille de technologies réseau de centre de données et au-delà ; peut transporter du RDMA avec une pile RoCE compatible.[19] |
| InfiniBand | InfiniBand | Technologie d’interconnexion de calcul offrant notamment RDMA ; une option de fabric inter-nœuds, pas une désignation de mémoire GPU.[19] |
| Remote direct memory access (RDMA) | Accès direct à la mémoire distante | Mécanisme de transfert entre mémoires de nœuds supportés avec réduction de l’implication CPU ; exige une pile compatible de bout en bout.[19] |
| RDMA over Converged Ethernet (RoCE) | RDMA sur Ethernet convergé | Mise en œuvre de RDMA sur Ethernet ; ni « tout Ethernet est RDMA » ni « RDMA exige toujours InfiniBand ».[19] |
| GPUDirect RDMA | GPUDirect RDMA | Chemin supporté entre mémoire GPU et périphérique tiers compatible, notamment un adaptateur réseau ; à distinguer de l’accès GPU au stockage.[19] |
| GPUDirect Storage | GPUDirect Storage | Technologie permettant un chemin de données direct supporté entre stockage et mémoire GPU ; ne supprime pas les besoins de stockage.[6] |
| AllReduce | Réduction collective avec redistribution | Opération qui combine des contributions puis rend le résultat disponible aux participants ; la moyenne demande une normalisation si l’opération de base est une somme.[19] |
| Topology | Topologie | Organisation des connexions et proximités ; un même nombre de GPU peut donner des chemins de communication différents.[19][39] |
| Latency | Latence | Délai d’une opération ou requête ; ne se confond pas avec le nombre de requêtes traitées par seconde.[60] |
| Throughput | Débit de traitement | Quantité de travail utile effectuée par unité de temps ; un débit élevé ne garantit pas une faible latence de chaque requête.[60] |
| Scale up | Extension verticale | Accroissement des capacités d’un système existant ; distinguer capacité supplémentaire et performance effective.[6] |
| Scale out | Extension horizontale | Ajout de systèmes ou ressources distribuées ; vérifier que la performance et le chemin des données suivent la croissance.[6] |
| Data processing unit (DPU) | Unité de traitement des données | Processeur spécialisé dans la décharge, l’accélération et l’isolation de fonctions d’infrastructure ; ne remplace pas le GPU pour entraîner un modèle.[12] |
| BlueField | BlueField | Famille de DPU NVIDIA ; nom de solution d’infrastructure, pas modèle de réseau neuronal.[12] |
| Data plane | Plan de données | Partie qui traite et déplace le trafic effectif, susceptible d’être déchargée vers du matériel spécialisé.[12] |
| Control plane | Plan de contrôle | Partie qui pilote les décisions et politiques ; peut être isolée de l’application, notamment dans des architectures DPU.[12] |
| Baseboard management controller (BMC) | Contrôleur de gestion de carte mère | Contrôleur dédié aux fonctions d’administration du système ; la fiche DGX H100/H200 distingue son interface hors bande.[16] |
| Out-of-band management | Gestion hors bande | Gestion par un chemin dédié distinct de la gestion dans le système principal ; ce n’est pas une connectivité universellement accessible sans autorisation.[16] |
| Power supply unit (PSU) | Bloc d’alimentation | Composant fournissant l’alimentation du serveur ; somme des puissances nominales et consommation du système sont des notions distinctes.[16] |
| Redundancy | Redondance | Présence de composants ou capacités permettant de tolérer certaines pannes ; les conditions doivent être lues dans la spécification précise.[16] |

## D. Exploitation, observabilité et partage — O01 à O04

| English term | Français | Définition utile et distinction |
|---|---|---|
| Kubernetes | Kubernetes | Plateforme déclarative de gestion de charges conteneurisées ; ses contrôleurs rapprochent l’état observé de l’état désiré.[51] |
| Container | Conteneur | Processus isolé et ses fichiers ; plusieurs conteneurs d’un même hôte partagent le noyau, contrairement à des VM complètes.[53] |
| Virtual machine (VM) | Machine virtuelle | Machine logicielle avec son propre système et noyau sur du matériel virtualisé ; peut elle-même héberger des conteneurs.[53] |
| Slurm Workload Manager | Gestionnaire de charges Slurm | Système de gestion de ressources et de jobs : allocation, lancement/suivi et arbitrage d’une file de travail.[27] |
| Job scheduling | Ordonnancement des travaux | Décision de quand et où allouer les ressources demandées aux jobs, selon contraintes et politiques.[27] |
| Resource allocation | Allocation de ressources | Attribution de ressources pour une durée ou une charge ; ne mesure pas leur utilisation effective.[27] |
| Partition | Partition Slurm | Groupe logique de nœuds assorti de règles de file ; sans rapport automatique avec une partition matérielle MIG.[27] |
| Job | Travail soumis | Allocation de ressources attribuée à un utilisateur pour une durée ; peut contenir plusieurs étapes d’exécution.[27] |
| Job step | Étape de travail | Ensemble de tâches exécutées dans une allocation Slurm existante.[27] |
| Pending | En attente | État d’un travail qui attend une allocation ; pas la preuve que le GPU est défaillant.[27] |
| Preemption | Préemption | Possibilité, selon les politiques de l’ordonnanceur, qu’un travail cède les ressources à un autre prioritaire.[27] |
| Rollback | Retour à un état antérieur | Rétablissement d’un déploiement précédent ; Kubernetes propose des mécanismes de rollouts et rollbacks.[51] |
| NVIDIA System Management Interface (nvidia-smi) | Interface d’administration système NVIDIA | Outil d’interrogation et de gestion des GPU ; seules les commandes explicitement en lecture sont retenues dans les labs optionnels.[39] |
| GPU UUID | Identifiant unique de GPU | Identifiant utilisé pour suivre un périphérique ; plus approprié que supposer que l’index reste identique après chaque redémarrage.[39] |
| GPU utilization | Utilisation du GPU | Indicateur d’activité sur une fenêtre d’échantillonnage ; ne signifie pas pourcentage de la performance théorique obtenue.[39] |
| Memory utilization | Activité mémoire | Métrique d’activité du sous-système mémoire ; distincte du volume de mémoire allouée ou occupée.[39] |
| Frame buffer memory | Mémoire locale du GPU | Mémoire dont nvidia-smi rapporte notamment le total et l’utilisation ; ne pas assimiler « used » à « calcul utile ».[39] |
| Error correcting code (ECC) | Code correcteur d’erreurs | Mécanisme de protection mémoire dont des compteurs d’erreurs sont observables sur les GPU compatibles.[38][39] |
| Xid | Code d’événement d’erreur NVIDIA | Indication de problème ou événement GPU à interpréter avec son contexte ; la valeur du code n’est pas un nombre d’incidents.[38][39] |
| Thermal slowdown | Ralentissement thermique | Réduction de fonctionnement liée à une contrainte thermique ; à corréler avec température, charge et limites plutôt qu’une seule mesure.[38] |
| NVIDIA Data Center GPU Manager (DCGM) | Gestionnaire de GPU de centre de données NVIDIA | Outils/API de télémétrie, santé, statistiques et diagnostic GPU ; ne remplace pas l’ordonnanceur.[38] |
| Health check | Contrôle de santé | Vérification d’indicateurs ou sous-systèmes ; ne garantit pas à elle seule la qualité applicative ni l’absence future de panne.[38] |
| Multi-Instance GPU (MIG) | GPU multi-instances | Partitionnement matériel de ressources d’un GPU compatible avec isolation ; les profils et maxima dépendent du modèle.[44][61] |
| GPU pass-through | Attribution directe de GPU à une VM | Mode de virtualisation exposant directement le GPU à un invité compatible ; ce n’est pas automatiquement le partage du même GPU entre de nombreuses VM.[44] |
| vGPU | GPU virtualisé | Technologie de GPU virtuel en environnement hyperviseur ; MIG et vGPU peuvent être combinés dans des configurations supportées.[44] |

## Utilisation active

- Choisir cinq termes puis former une chaîne causale : par exemple *training → GPU memory → AllReduce → topology → throughput*. Expliquer ce que chaque lien impose à l’infrastructure.
- Comparer les homonymes : *Partition* Slurm n’est pas *MIG*.[27][44] Distinguer *memory utilization* et *memory used*.[39] NVIDIA Triton Inference Server n’est pas le langage Triton.[60][62]
- Relier les termes aux [fiches comparatives](fiches-express.md) puis vérifier avec une source primaire. Ne pas apprendre « sept instances MIG sur tous les GPU » : la liste officielle distingue notamment A30 et H100.[61]

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
[3] https://developer.nvidia.com/tensorrt — NVIDIA TensorRT
[6] https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing — NVIDIA: Scaling Storage for AI Training and Inferencing
[12] https://developer.nvidia.com/blog/offloading-and-isolating-data-center-workloads-with-bluefield-dpu — Offloading and Isolating Data Center Workloads with NVIDIA Bluefield DPU | NVIDIA Technical Blog
[16] https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html — Introduction to NVIDIA DGX H100/H200 Systems — NVIDIA DGX H100/H200 User Guide
[19] https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io — Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog
[27] https://slurm.schedmd.com/overview.html — Slurm Workload Manager - Overview
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
[81] https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets — Datasets: Dividing the original dataset  |  Machine Learning  |  Google for Developers
