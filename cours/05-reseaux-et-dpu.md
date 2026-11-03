# 05 — Réseaux d'IA, interconnexions GPU et DPU

**Objectifs locaux : I07, I08, I09, I10 ; liens avec I02 et I05.** Vous apprendrez à reconnaître le chemin emprunté par un transfert, à distinguer protocole, matériel et bibliothèque, et à choisir une option réseau selon le profil de la charge. Le vocabulaire est bilingue parce que les questions de préparation et l'examen sont en anglais.

<a id="i07"></a>
## I07 — Pourquoi le réseau devient une ressource de calcul

Dans une application distribuée, plusieurs processus coopèrent pour produire un résultat. Les GPU peuvent être rapides individuellement tout en attendant des données ou une synchronisation. Le réseau influence alors le temps utile de la charge. NVIDIA présente les communications collectives, notamment *AllReduce*, comme un ingrédient important de l'entraînement distribué et décrit des bibliothèques adaptées à la topologie GPU.[19]

La **bande passante**, ou *bandwidth*, représente la quantité de données transportable par unité de temps. La **latence**, ou *latency*, décrit le délai d'une communication. Le **débit utile**, ou *throughput*, est ce que l'application obtient réellement ; il ne se confond pas avec la vitesse nominale d'un lien. Un transfert volumineux bénéficie d'une forte bande passante, tandis que beaucoup de petits échanges synchronisés peuvent rester sensibles à leur délai individuel. La distinction guide le choix du réseau et la manière de le tester.[19]

Les exigences doivent préciser les échanges simultanés. Une paire de serveurs peut communiquer correctement pendant qu'un groupe complet sature les chemins partagés. Il faut donc étudier la topologie et la **bande passante de bissection**, c'est-à-dire la capacité disponible entre grandes parties du système, plutôt que compter uniquement les ports rapides. La référence SuperPOD B200 utilise un fabric de calcul équilibré et non bloquant pour ses objectifs de charge ; ce choix illustre l'importance de la capacité du réseau complet.[68]

Pour une inférence composée de répliques indépendantes, la distribution des requêtes et l'accès aux données peuvent être plus importants qu'une synchronisation permanente entre tous les GPU. Pour un modèle réparti, les communications entre parties du modèle deviennent au contraire centrales. Ne concluez donc pas que toute inférence est légère en réseau ou que tout entraînement exige la même topologie : partez de la manière dont les processus échangent. NVIDIA associe NVLink aussi bien à l'entraînement qu'à l'inférence dans les domaines scale-up compatibles.[18]

## Lire le chemin d'un message

Représentez le chemin : mémoire GPU du processus émetteur, interconnexion locale éventuelle, adaptateur réseau, commutateurs du fabric, adaptateur distant et mémoire cible. Certains trajets passent aussi par des buffers en mémoire CPU. Les bibliothèques de communication choisissent entre plusieurs mécanismes ; un système compatible peut utiliser un chemin direct, tandis qu'une plateforme incompatible ou moins favorable peut utiliser une copie intermédiaire.[19][55]

Cette représentation protège contre une confusion fréquente : une technologie peut améliorer un tronçon sans supprimer les autres. Une meilleure interconnexion locale ne remplace pas les interfaces réseau du cluster ; un réseau plus rapide ne rend pas automatiquement le stockage plus performant ; un accès direct à la mémoire GPU n'en augmente pas la capacité. L'architecture de référence sépare justement les fabrics et leurs rôles.[66]

<a id="i09"></a>
## I09 — NVLink et NVSwitch : le domaine scale-up

**NVLink** est une famille d'interconnexions à forte bande passante entre GPU dans des systèmes pris en charge. **NVSwitch** et les systèmes **NVLink Switch** assurent la commutation de ces liens afin de constituer des domaines de communication plus larges. Il ne faut pas confondre un commutateur NVLink avec un commutateur Ethernet ou InfiniBand de réseau général.[18]

Dans beaucoup de serveurs multi-GPU, le domaine NVLink est local au serveur : on parle alors d'échanges **intra-node**. Mais la phrase « NVLink ne traverse jamais un nœud » serait fausse. La documentation actuelle présente des systèmes NVLink Switch à l'échelle du rack qui relient des GPU sur plusieurs plateaux ou nœuds. La frontière pertinente est le **domaine scale-up compatible**, défini par une architecture et une génération précises, pas systématiquement la boîte métallique d'un serveur.[18]

À l'extérieur de ce domaine, un cluster peut utiliser un réseau **scale-out**, notamment InfiniBand ou Ethernet. Dans l'architecture SuperPOD B200 étudiée, les connexions NVLink/NVSwitch du serveur et le fabric InfiniBand entre systèmes ont des rôles distincts. Le fait qu'un système possède NVLink ne signifie donc pas que ses liens de réseau inter-nœuds deviennent inutiles.[68]

Les chiffres de génération ne sont pas universels. La page NVLink compare plusieurs générations et signale aussi des spécifications préliminaires pour certaines plateformes. Lors d'une lecture de fiche, identifiez la génération, le périmètre, le sens du débit et le nombre de GPU du domaine. Pour l'examen introductif, privilégiez la distinction fonctionnelle : communication GPU étroitement couplée dans un domaine compatible, puis communication à l'échelle du cluster.[18]

<a id="i08"></a>
## I08 et I09 — InfiniBand, Ethernet et RoCE

**InfiniBand** est une technologie de fabric conçue pour des communications à faible latence et haut débit, avec prise en charge de RDMA. Les adaptateurs sont souvent appelés **HCA**, pour *host channel adapter*. Les générations et les configurations diffèrent ; un débit donné dans une référence d'architecture n'est pas un plafond éternel d'InfiniBand. La référence B200 documente, par exemple, une conception de calcul reposant sur NDR InfiniBand.[68]

**Ethernet** est une famille de technologies réseau également utilisée dans les datacenters. Une infrastructure Ethernet peut transporter des communications TCP/IP classiques et, avec les composants et la configuration adaptés, des communications RDMA via **RoCE**, *RDMA over Converged Ethernet*. Dire « Ethernet n'offre jamais RDMA » serait donc incorrect ; dire « tout Ethernet donne automatiquement les performances RDMA voulues » le serait aussi.[19][82]

**RDMA**, *remote direct memory access*, permet des transferts entre régions mémoire avec un chemin de données qui réduit les copies et l'intervention CPU par rapport à des chemins traditionnels. Cela ne signifie pas que les CPU, pilotes, bibliothèques et opérations de préparation disparaissent : le guide GPUDirect décrit notamment l'enregistrement et la gestion des régions mémoire. Retenez « moins de travail et de copies sur le chemin de données », pas « aucun logiciel nécessaire ».[19][55]

**TCP/IP** et **RoCE** ne sont pas deux noms pour le même mécanisme. Dans le vocabulaire réseau, Ethernet correspond notamment au transport local de trames, IP à l'adressage et au routage de paquets, TCP à un transport fiable en flux. RoCE transporte des opérations RDMA sur une infrastructure Ethernet compatible ; la variante RoCEv2 utilise une encapsulation IP/UDP.[80] Ne déduisez pas de la présence d'UDP que l'application bénéficie des mêmes mécanismes qu'une application UDP ordinaire : il s'agit d'une pile RDMA avec ses propres exigences.[19][82]

Le contrôle de congestion est important parce que beaucoup d'émetteurs peuvent viser une même destination. **ECN**, *Explicit Congestion Notification*, signale la congestion ; dans la documentation Onyx étudiée, des notifications conduisent la source à limiter son rythme d'injection. **PFC**, *Priority Flow Control*, intervient sur le contrôle de flux par priorité dans les configurations qui l'utilisent. Ces mécanismes ne sont pas synonymes et ne doivent pas être activés à l'aveugle.[82]

Attention à une simplification répandue : « RoCE impose toujours PFC partout ». La documentation Onyx 3.10.4606 LTS décrit des modes *lossless*, *semi-lossless* et *lossy*, avec des usages différents de PFC. Cela montre qu'il faut préciser la solution validée, la version et la politique de congestion. Une question d'introduction peut associer RoCE aux exigences de configuration du fabric, sans en faire une règle absolue valable pour toutes les architectures.[82]

## Topologie, sursouscription et séparation des flux

Un **commutateur leaf** raccorde les terminaux ; une couche **spine** relie les leafs pour fournir plusieurs chemins. Une topologie *fat-tree* cherche à fournir une capacité adaptée aux échanges entre branches. La **sursouscription**, ou *oversubscription*, apparaît lorsque les débits proposés par les ports d'accès dépassent la capacité des liaisons communes. Elle n'est pas automatiquement un défaut : sa pertinence dépend de la simultanéité et du budget de performance.[66]

**Exemple pédagogique.** Deux groupes de travaux lisent leurs données pendant qu'un entraînement distribué synchronise ses résultats. Si tous partagent une capacité limitée, le stockage peut perturber le calcul. Séparer les flux critiques, physiquement ou logiquement selon la conception, peut rendre les performances plus prévisibles. Dans la référence SuperPOD B200, le fabric de stockage est indépendant du fabric de calcul, tandis que l'administration possède ses chemins dédiés.[66][68]

La séparation **in-band/out-of-band** concerne aussi la résilience et la sécurité. *In-band* désigne ici des services de gestion et d'accès qui utilisent le réseau de fonctionnement du cluster. *Out-of-band*, ou **OOB**, concerne notamment les ports d'administration matérielle : BMC, commutateurs et PDU. L'objectif est de conserver un accès contrôlé aux équipements sans exposer ces interfaces aux utilisateurs ordinaires. Il faut ensuite vérifier les dépendances réelles : séparation logique ne signifie pas absence de tout composant commun.[66]

## GPUDirect : accélérer le chemin, pas ajouter un processeur

**GPUDirect RDMA** permet à un équipement compatible, par exemple une interface réseau, d'accéder à la mémoire GPU par un chemin direct pris en charge. Il peut éviter le passage des données par un buffer intermédiaire en mémoire hôte. **GPUDirect P2P** concerne les échanges entre pairs GPU, et **GPUDirect Storage** les chemins de données entre stockage compatible et mémoire GPU. Ces fonctions appartiennent à une famille ; elles ne sont pas interchangeables.[19][6][55]

GPUDirect n'est ni une carte DPU, ni un protocole de routage, ni un mécanisme qui agrandit la VRAM. Sa disponibilité et son intérêt dépendent du matériel, du logiciel et de la topologie. Le guide GPUDirect RDMA et l'article Network IO exposent explicitement des contraintes de plateforme et des cas où des chemins intermédiaires restent employés. Une fiche annonçant un GPU et une carte rapide ne suffit donc pas à garantir le meilleur chemin direct.[55][19]

**NCCL**, la bibliothèque NVIDIA de communications collectives, est encore une autre couche. Elle propose des opérations adaptées aux GPU et exploite les transports disponibles. **MPI** décrit un modèle et des interfaces de communication utilisés en calcul distribué ; **UCX** fournit une couche de communication utilisant différents transports. Ces noms sont des éléments logiciels, pas des types de câbles. À l'examen, commencez par classer la réponse proposée : matériel, transport, mécanisme d'accès mémoire ou bibliothèque.[19]

<a id="i10"></a>
## I10 — Le DPU : offload, accelerate, isolate

Un **DPU**, ou *data processing unit*, est un processeur d'infrastructure associant des capacités de traitement et d'accélération adaptées aux flux de données. NVIDIA résume sa mission en trois verbes : **décharger**, **accélérer** et **isoler** les fonctions d'infrastructure. BlueField constitue une famille NVIDIA de DPU ; toutes les capacités détaillées dépendent du modèle et de la pile déployée.[12]

**Offload** signifie transférer une tâche d'infrastructure depuis le CPU hôte, afin que ce dernier conserve davantage de ressources pour les applications. **Accelerate** signifie utiliser des moteurs adaptés au traitement visé, plutôt que déplacer simplement le même travail sur d'autres cœurs généralistes. **Isolate** signifie exécuter certaines fonctions de contrôle et de sécurité dans un domaine distinct de celui de l'application et du système hôte.[12]

Les cas d'usage comprennent des traitements de réseau, de stockage, de sécurité et de contrôle d'infrastructure. Un opérateur de cloud peut vouloir conserver ses fonctions de protection et de télémétrie séparées du système administré par un client. Le DPU ne remplace pas pour autant les règles d'accès, les mises à jour ou la conception de sécurité : c'est une possibilité d'architecture, pas une immunité automatique aux compromissions.[12]

Un **NIC** est une interface réseau ; certaines cartes disposent déjà de fonctions d'accélération. Un DPU ne se réduit cependant pas à « un NIC plus rapide » : l'intérêt étudié inclut la programmabilité et l'isolation de fonctions d'infrastructure. Inversement, GPUDirect RDMA ne nécessite pas conceptuellement un DPU : des adaptateurs compatibles peuvent participer à ces transferts. DPU et GPUDirect répondent à des questions différentes et peuvent être complémentaires.[19][55]

**Scénario raisonné.** Le CPU d'un serveur est fortement occupé par des fonctions réseau et de sécurité, alors que l'on veut préserver ses ressources applicatives et isoler le contrôle d'infrastructure. Un DPU compatible est un candidat cohérent. Si la difficulté est au contraire une empreinte de modèle trop importante pour le GPU, le DPU ne constitue pas une extension de VRAM. Et s'il s'agit d'accélérer le calcul principal d'un réseau neuronal, transférer ce calcul vers les cœurs généralistes du DPU n'est pas sa mission.[12]

## Atelier : choisir sans slogan

Pour un entraînement étroitement couplé, comparez des fabrics InfiniBand et Ethernet/RoCE en examinant la latence, le débit utile simultané, la maîtrise de la congestion, l'intégration logicielle et les compétences disponibles. Il n'existe pas de vainqueur universel indépendant de l'architecture. Une référence InfiniBand peut fournir un ensemble validé ; une solution Ethernet peut convenir avec les fonctions et la validation appropriées. La référence B200 elle-même prévoit des options InfiniBand ou Ethernet/RoCE pour le stockage.[68][66]

Pour un petit service de classification indépendant, commencez par le trafic réel de requêtes et de données. Acheter un domaine NVLink étendu n'est pas justifié si la charge n'échange presque rien entre GPU. Pour un modèle réparti entre GPU qui communiquent fortement, la même interconnexion peut être déterminante. Dans votre justification, associez toujours une technologie à un chemin précis et à une contrainte mesurable.

## Synthèse et pièges de vocabulaire

- **NVLink/NVSwitch** : domaine GPU scale-up compatible, parfois au-delà d'un seul serveur ; ne pas généraliser une génération.[18]
- **InfiniBand ou Ethernet/RoCE** : options de fabric de communication à l'échelle du cluster, selon conception.[19]
- **RDMA/GPUDirect** : mécanismes qui optimisent l'accès aux données et réduisent certaines copies ; pas une capacité mémoire supplémentaire.[55]
- **NCCL/UCX/MPI** : couches et interfaces logicielles de communication ; pas du matériel.[19]
- **DPU** : décharge, accélération et isolation de tâches d'infrastructure ; pas un remplaçant universel du CPU ou du GPU.[12]

## Auto-évaluation corrigée

1. **Un port Ethernet rapide assure-t-il automatiquement RDMA ?** Non : il faut les composants, la pile et la configuration compatibles, par exemple RoCE.[19][82]
2. **Pourquoi « NVLink est toujours intra-serveur » est-il un piège ?** Certains systèmes NVLink Switch étendent un domaine scale-up à plusieurs nœuds du rack.[18]
3. **Pourquoi GPUDirect et DPU ne sont-ils pas synonymes ?** L'un concerne des chemins d'accès directs aux données ; l'autre est un processeur d'infrastructure avec des objectifs d'offload et d'isolation.[55][12]
4. **PFC et ECN réalisent-ils la même opération ?** Non : contrôle de flux par priorité et signalement de congestion sont distincts ; leur emploi dépend du fabric validé.[82]

## Sources

[6] https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing — NVIDIA: Scaling Storage for AI Training and Inferencing
[12] https://developer.nvidia.com/blog/offloading-and-isolating-data-center-workloads-with-bluefield-dpu — Offloading and Isolating Data Center Workloads with NVIDIA Bluefield DPU | NVIDIA Technical Blog
[18] https://www.nvidia.com/en-us/data-center/nvlink — NVLink & NVLink Switch: Fastest HPC Data Center Platform | NVIDIA
[19] https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io — Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog
[55] https://docs.nvidia.com/cuda/gpudirect-rdma/index.html — 1. Overview — GPUDirect RDMA 13.4 documentation
[66] https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/network-fabrics.html — Network Fabrics — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200
[68] https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html — Key Components of the DGX SuperPOD — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200
[80] https://docs.nvidia.com/networking/display/mlnxenv23102131201lts/rdma-over-converged-ethernet-roce.pdf — NVIDIA MLNX_EN 23.10 LTS — RoCE and RoCEv2
[82] https://networking-docs.nvidia.com/onyxum/3104606lts/rdma-over-converged-ethernet-roce — NVIDIA Onyx 3.10.4606 LTS — RoCE (direct documentation URL)
