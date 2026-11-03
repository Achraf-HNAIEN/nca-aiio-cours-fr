# 04 — Serveurs accélérés, mémoire et stockage

**Objectifs locaux : I01, I02, I05.** Ces identifiants sont pédagogiques, et non des codes NVIDIA. À la fin du chapitre, vous devez pouvoir transformer un besoin d'entraînement en contraintes matérielles, reconnaître les composants d'un cluster et proposer une montée en charge qui traite le véritable goulot d'étranglement. Les termes anglais permettent de relier les explications aux formulations de l'examen.

## Partir de la charge, pas du catalogue

Une infrastructure d'IA n'est pas simplement un ensemble de GPU puissants. Elle est un chemin complet entre données persistantes, traitements CPU, mémoire des accélérateurs et échanges entre processus. Les architectures de référence NVIDIA cherchent explicitement à équilibrer les sous-systèmes afin de limiter les goulets d'étranglement ; le stockage et les réseaux font donc partie du dimensionnement initial, pas d'une correction tardive.[68]

La première question utile est : quel résultat doit être obtenu, dans quel délai et avec quelles données ? Pour entraîner un modèle de vision, on précisera la résolution des images, les transformations nécessaires, la taille des lots et la durée acceptable d'une expérience. Pour adapter un modèle de langage, on examinera aussi la longueur des séquences, la méthode d'adaptation et la mémoire réellement consommée. Pour une production d'inférence, on distinguera le débit demandé de la latence tolérée. Ces questions constituent une méthode de conception, pas une liste de spécifications officiellement imposées.

Définissez ensuite une charge représentative et un critère d'acceptation : terminer une époque dans le délai choisi, maintenir le débit sans dépasser la mémoire disponible, ou servir une proportion définie de requêtes sous un seuil de latence. Un essai minuscule peut confirmer que le programme démarre sans démontrer que l'infrastructure supportera les données futures. NVIDIA souligne précisément ce décalage entre une preuve de concept ponctuelle et des besoins de stockage qui évoluent pendant des mois ou des années.[6]

<a id="i01"></a>
## I01 — Relier les composants au travail d'entraînement

Le **GPU** exécute les opérations parallèles du modèle ; sa mémoire contient les tenseurs nécessaires aux calculs. Le **CPU** reste nécessaire pour le système, le pilotage logiciel et les traitements qui lui reviennent. La **RAM système** sert notamment aux processus et aux données préparées côté hôte. Le **stockage persistant** conserve les fichiers lorsque le serveur est arrêté. Enfin, les interfaces réseau et les interconnexions locales déplacent les données entre ces éléments. Un DGX H100/H200 fournit un exemple concret de cette coexistence : GPU, CPU, mémoire système, SSD de démarrage, cache NVMe et cartes réseau sont des composants distincts.[16]

Il faut distinguer la **capacité mémoire**, qui indique combien de données peuvent résider à un instant donné, et la **bande passante mémoire**, qui indique à quelle vitesse les données sont accessibles. Un modèle qui ne tient pas dans la mémoire utilisable pose d'abord un problème de capacité ; un calcul qui attend continuellement ses opérandes peut poser un problème de mouvement des données. Le diagnostic ne se résume donc pas au nombre de GPU. Dans la hiérarchie décrite par NVIDIA, accéder aux données proches du GPU et traverser les couches de stockage n'ont pas les mêmes conséquences sur les performances.[6]

Pour le dimensionnement pédagogique, décomposez l'empreinte d'entraînement en poids, états de l'optimiseur, gradients, activations et espaces temporaires. Cette décomposition est une grille de questions à poser au framework : les valeurs exactes varient avec la précision, le modèle, la taille du lot et la stratégie de calcul. Ne transformez pas une règle approximative en formule universelle. Une estimation doit être suivie d'une mesure sur une configuration représentative.

**Exemple raisonné.** Une équipe dispose d'un jeu de données très volumineux, mais un lot courant et le modèle tiennent dans la mémoire du GPU. Elle n'a pas nécessairement besoin de charger tout le jeu de données simultanément en VRAM : l'alimentation peut s'effectuer par lots. En revanche, si les tenseurs nécessaires à une étape ne tiennent pas, ajouter des téraoctets de SSD ne rend pas la mémoire locale du GPU plus grande. NVIDIA distingue la mémoire intégrée au GPU, non extensible comme un volume de disques, des couches de stockage et de fabric qui peuvent être agrandies.[6]

Une réponse pertinente peut être un GPU disposant de plus de mémoire, une réduction adaptée du lot ou une distribution explicitement prise en charge. Le bon choix dépend de la contrainte et du logiciel. Ne supposez pas que connecter plusieurs GPU fusionne automatiquement leur mémoire pour tout programme : il faut un mécanisme d'accès et une stratégie d'exécution compatibles. L'existence d'une capacité mémoire agrégée dans une fiche produit ne prouve pas qu'un tenseur arbitraire pourra être alloué comme sur un seul GPU.[6][18]

## Lire un serveur comme un système

Le **nœud de calcul**, ou *compute node*, est le serveur qui exécute les travaux. Il contient aussi des chemins PCIe, des connexions GPU-GPU et des interfaces vers les réseaux externes. La proximité topologique entre GPU et adaptateur peut influencer les transferts directs : le guide GPUDirect RDMA décrit des contraintes liées à la plateforme et au chemin PCI Express. Deux serveurs possédant un nombre identique de GPU ne garantissent donc pas une communication identique.[55]

Les SSD du système d'exploitation, le cache de données local et le stockage partagé ne remplissent pas nécessairement la même fonction. Dans le DGX H100/H200 documenté, les SSD de démarrage sont organisés en RAID 1 et le cache de données en RAID 0. Cette description concerne ce système : elle ne constitue ni une recommandation générale de RAID 0 pour les données importantes, ni une preuve de protection du cache contre une panne de disque.[16]

Un **BMC**, ou *baseboard management controller*, offre un chemin d'administration du matériel distinct de l'application. Le guide du DGX H100/H200 sépare notamment son interface BMC des interfaces destinées au réseau de calcul et au stockage. Cette distinction explique pourquoi un serveur inaccessible par son système d'exploitation peut encore disposer d'un accès matériel d'administration ; elle ne garantit pas que tous ses services de gestion survivent à toute panne électrique.[16]

Pour lire une fiche technique, identifiez toujours la portée de chaque chiffre : par GPU, par port, par serveur, agrégé, bidirectionnel ou dans un sens. Les fiches H100/H200 et les tableaux NVLink contiennent des chiffres de générations et de périmètres différents. Le but de la préparation n'est pas d'apprendre le catalogue le plus récent, mais d'éviter de comparer des quantités qui ne représentent pas le même chemin.[16][18]

## Le stockage : quatre dimensions à séparer

La **capacité**, le **débit**, les **IOPS** et la **latence** répondent à des questions différentes. La capacité représente le volume conservable ; le débit, le volume transféré par unité de temps ; les IOPS, le rythme des opérations ; la latence, le délai d'une opération. À cela s'ajoutent la disponibilité et les performances des métadonnées : ouvrir beaucoup de petits fichiers n'a pas le même profil que lire de gros blocs séquentiels. L'architecture SuperPOD B200 distingue justement un stockage haute performance et un stockage utilisateur dont les profils d'entrées-sorties ne sont pas identiques.[68]

Le **cache local** rapproche des données du calcul et peut réduire des lectures répétées vers le stockage partagé. Il ne remplace pas automatiquement le référentiel durable, la sauvegarde ou la gestion de versions des données. Dans l'exemple DGX H100/H200, le volume local est explicitement présenté comme un cache ; dans l'architecture B200, le stockage partagé fait partie du système complet.[16][68]

Les **checkpoints** enregistrent un état permettant une reprise selon les capacités du logiciel. Pour le dimensionnement, demandez leur taille, leur fréquence et le nombre de travaux qui écrivent simultanément. Un stockage suffisant en lecture peut rester insuffisant lors de pointes d'écriture. L'architecture de référence mentionne les écritures parallèles, les métadonnées et les fonctions de checkpointing dans ses exigences de stockage ; le concepteur doit relier ces propriétés aux usages réels.[68]

**Exemple pédagogique.** Des GPU restent inactifs entre deux lots. Le modèle tient en VRAM, les CPU ne sont pas saturés et la lecture partagée plafonne. La première hypothèse n'est pas un manque de puissance de calcul : il faut examiner le débit du stockage et le chemin qui l'achemine. Si, au contraire, les données arrivent rapidement mais qu'une allocation échoue, on revient au problème de mémoire de travail. Ces deux symptômes ne justifient pas la même dépense.[6]

<a id="i02"></a>
## I02 — Choisir une stratégie de montée en charge

Le **scale-up** renforce un domaine de calcul étroitement connecté ; le **scale-out** ajoute des nœuds et impose de traiter les communications entre eux. Pour un cluster de serveurs accélérés, on distingue souvent les échanges GPU-GPU locaux et le réseau qui relie les nœuds. Ce vocabulaire décrit une intention architecturale, pas une frontière physique immuable : certains domaines NVLink Switch récents s'étendent entre plateaux ou nœuds d'un système à l'échelle du rack.[18][19]

La **data parallelism** répartit des lots entre des répliques du modèle, puis synchronise des résultats nécessaires à l'apprentissage. La **model parallelism** répartit le modèle lui-même et crée d'autres besoins de communication. Au niveau introductif, retenez la conséquence matérielle : ajouter des GPU peut augmenter simultanément les ressources de calcul et la quantité d'échanges. Les bibliothèques comme NCCL fournissent des opérations collectives et des communications permettant différentes formes de parallélisme ; elles ne suppriment pas les contraintes du réseau.[19]

Distinguez un problème de **temps de calcul** d'un problème de **taille de modèle**. Pour accélérer un entraînement déjà compatible avec un GPU, plusieurs répliques peuvent être pertinentes si le logiciel et les communications suivent. Pour un modèle dont l'empreinte dépasse la mémoire d'un GPU, répliquer intégralement ce même modèle ne résout pas cette contrainte. Il faut alors une stratégie qui répartit effectivement l'empreinte, ou une autre adaptation du calcul. C'est un raisonnement de ressources, non une promesse de performance.

La croissance du stockage possède sa propre logique. Ajouter des disques augmente éventuellement la capacité sans augmenter le débit disponible pour tous les clients. NVIDIA insiste sur le besoin de faire évoluer à la fois capacité et performances lorsque la charge d'inférence grandit. Cette notion ne doit pas être confondue avec la mémoire GPU : une extension de stockage ne modifie pas la quantité de VRAM intégrée.[6]

Mesurez donc la montée en charge sur le travail utile : temps jusqu'au résultat, débit traité, contraintes de mémoire et coût total de l'expérience. Une amélioration du nombre de GPU installés n'est pas, à elle seule, une amélioration de l'efficacité. Si les communications ou les lectures partagées deviennent dominantes, le gain supplémentaire peut être faible. Les architectures équilibrées visent précisément à limiter ces changements de goulot lorsque l'on agrandit le système.[68]

<a id="i05"></a>
## I05 — Assembler le cluster, pas seulement les serveurs

Un cluster comprend les nœuds accélérés, mais aussi des nœuds ou services d'administration, le stockage, les fabrics réseau, les logiciels de gestion et les moyens d'exploitation. L'architecture SuperPOD B200 sépare quatre fabrics : calcul, stockage, administration *in-band* et administration *out-of-band*. Ce découpage est un exemple de référence utile, et non la preuve que toute petite installation exige quatre réseaux physiques séparés.[66][68]

L'architecture doit préciser les dépendances : qui fournit les données, qui donne accès aux images logicielles, comment les utilisateurs soumettent les travaux, et comment l'administrateur intervient si le réseau utilisateur est défaillant. Un serveur GPU sans accès aux données ou sans configuration logicielle cohérente n'est pas une capacité immédiatement exploitable. Dans la référence B200, le réseau d'administration relie aussi les services de gestion et les accès à des dépôts et sources de données.[66]

La croissance par unités cohérentes permet de prévoir ports, câbles et chemins de communication. La référence B200 utilise des *scalable units* ; elle demande même d'anticiper le fabric d'une unité complète quand tous les nœuds ne sont pas installés immédiatement. Il faut en retenir le principe de planification, pas une taille d'unité supposée valable pour toutes les générations de SuperPOD.[66][68]

## Atelier de décision : deux projets, deux infrastructures

**Projet A : laboratoire de vision.** Le modèle tient sur un GPU ; les expériences sont indépendantes ; le budget est limité. Commencez par mesurer une expérience représentative, puis examinez si plusieurs GPU peuvent exécuter des expériences distinctes. Un réseau de calcul distribué complexe ne doit pas être acheté uniquement parce que le mot « IA » apparaît dans le projet. Le stockage reste à dimensionner, car plusieurs expériences simultanées peuvent multiplier les lectures.[6]

**Projet B : grand entraînement distribué.** Les processus doivent fréquemment échanger des données et écrire des checkpoints communs. La conception doit coordonner mémoire, interconnexion GPU, réseau inter-nœuds et stockage partagé. Une architecture de référence constitue alors un guide de cohérence : son intérêt est l'équilibre du système complet, pas seulement l'identité des GPU.[68]

Dans les deux cas, rédigez une justification courte : contrainte principale, composant concerné, modification proposée et mesure qui confirmerait l'amélioration. Cette méthode évite les réponses automatiques du type « ajouter des GPU » ou « prendre le réseau le plus rapide ». Elle vous entraîne aussi à éliminer les distracteurs anglais qui changent une ressource sans traiter le symptôme décrit.

## Pièges fréquents et synthèse

- **« Plus de stockage corrige une erreur de VRAM. »** Non : espace persistant et mémoire de travail ne sont pas interchangeables.[6]
- **« La mémoire agrégée est une allocation unique automatique. »** Non : les possibilités dépendent du système et du logiciel.[6][18]
- **« Le débit d'un port décrit le cluster complet. »** Non : topologie, chemins et partage des ressources comptent aussi.[66]
- **« Un serveur GPU suffit à définir un cluster. »** Non : stockage, réseaux et gestion complètent l'infrastructure.[68]

**À retenir :** partez du travail, séparez les ressources, mesurez les goulets, puis faites évoluer ensemble les composants qui déterminent le résultat.

## Auto-évaluation corrigée

1. **Un jeu de données dépasse la VRAM, mais un lot et les états du modèle tiennent. Faut-il obligatoirement changer de GPU ?** Non. Le traitement par lots peut convenir ; il faut vérifier que les données arrivent assez vite.[6]
2. **Pourquoi un volume partagé plus grand peut-il ne pas accélérer l'entraînement ?** Parce que capacité, débit et profil d'opérations sont des dimensions distinctes.[6][68]
3. **Quel est l'intérêt d'un accès BMC séparé ?** Administrer le matériel par un chemin distinct des services applicatifs, dans les limites de la disponibilité matérielle.[16]
4. **Pourquoi tester plusieurs nœuds avant d'acheter un grand cluster ?** Pour vérifier que les communications et le stockage restent équilibrés avec le calcul.[19][68]

## Sources

[6] https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing — NVIDIA: Scaling Storage for AI Training and Inferencing
[16] https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html — Introduction to NVIDIA DGX H100/H200 Systems — NVIDIA DGX H100/H200 User Guide
[18] https://www.nvidia.com/en-us/data-center/nvlink — NVLink & NVLink Switch: Fastest HPC Data Center Platform | NVIDIA
[19] https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io — Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog
[55] https://docs.nvidia.com/cuda/gpudirect-rdma/index.html — 1. Overview — GPUDirect RDMA 13.4 documentation
[66] https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/network-fabrics.html — Network Fabrics — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200
[68] https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html — Key Components of the DGX SuperPOD — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200
