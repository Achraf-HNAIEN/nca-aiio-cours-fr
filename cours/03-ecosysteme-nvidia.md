# 03 — Lire la pile logicielle et l’écosystème NVIDIA

**Objectifs locaux couverts : E01, E06 ; consolidation de E07.** Ce chapitre apprend à associer un besoin à un rôle dans la pile NVIDIA : calcul accéléré, développement, optimisation, distribution, serving ou gestion. Ces objectifs correspondent aux thèmes « software stack », « NVIDIA solutions » et cycle de vie publiés pour NCA-AIIO.[1] Les noms commerciaux et les périmètres des offres peuvent évoluer : les fonctions sont le fil conducteur, et la compatibilité exacte doit être vérifiée dans la documentation de la version utilisée.

## Objectifs d’apprentissage

Vous devez pouvoir suivre une requête depuis une application jusqu’au GPU, distinguer un pilote d’un framework, reconnaître le rôle de CUDA, TensorRT, Triton, NIM, NeMo et NGC, et expliquer pourquoi un produit d’infrastructure n’est pas une méthode d’apprentissage. Vous devez aussi savoir repérer ce qu’un outil ne fait pas : un registre ne planifie pas les tâches, un moteur d’inférence ne remplace pas le pilote et un opérateur Kubernetes ne choisit pas les objectifs métier.

<a id="e01"></a>
## E01 — Une pile se comprend du bas vers le haut

### Matériel, système et pilote

Au niveau inférieur se trouvent les processeurs, les mémoires et les chemins d’entrée-sortie. Le système d’exploitation et le **driver**, ou pilote, rendent le matériel utilisable par les autres composants. Dans l’écosystème NVIDIA, le pilote est notamment un composant nécessaire pour permettre l’usage de CUDA ; le GPU Operator peut automatiser sa gestion dans un environnement Kubernetes pris en charge.[40] Le pilote n’est pas le modèle, et il ne possède pas les connaissances apprises dans le jeu d’entraînement.

Une application peut donc échouer avant d’exécuter un seul calcul de modèle : matériel inaccessible, configuration hôte incorrecte ou combinaison de versions non prise en charge. Inversement, voir un GPU dans un inventaire ne prouve pas que l’application l’utilise. Pour raisonner, distinguez la présence du matériel, sa disponibilité pour la charge et l’usage effectif par cette charge. Cette séparation sera approfondie dans le domaine Operations.

### CUDA : plateforme et modèle de programmation

**CUDA** est une plateforme de calcul parallèle et un modèle de programmation NVIDIA permettant d’exploiter le GPU pour des tâches qui ne sont pas limitées au graphisme.[47] Il est possible d’utiliser CUDA directement, mais de nombreux utilisateurs passent par des bibliothèques ou des frameworks qui le mobilisent sous des abstractions de plus haut niveau.[62] Ainsi, « je développe en Python » et « mon application utilise CUDA » ne sont pas des affirmations contradictoires.

Ne réduisez pas CUDA à un mot inscrit sur un GPU. Distinguez le matériel, le pilote, l’environnement de développement et les composants d’exécution utilisés par l’application. Selon la manière dont le logiciel a été distribué, une partie des dépendances peut se trouver dans un conteneur et une autre sur l’hôte. La documentation de GPU Operator montre justement que le support d’une charge GPU implique plusieurs composants logiciels, pas un unique paquet universel.[40]

### Bibliothèques et frameworks

Les **libraries** apportent des routines réutilisables. CUDA cite notamment **cuBLAS** pour des opérations d’algèbre linéaire et **cuDNN** parmi les bibliothèques optimisées employées par les applications et frameworks d’IA.[62] Le candidat n’a pas à réimplémenter une multiplication de matrices ; il doit comprendre qu’une bibliothèque spécialisée fournit des opérations que des couches supérieures peuvent appeler.

Un **framework**, tel que PyTorch, offre une manière plus structurée de définir les modèles et leurs calculs. NeMo Framework, par exemple, est construit sur PyTorch dans la documentation consultée.[52] Le framework n’est pas le pilote, et l’existence d’un framework ne supprime pas les couches inférieures. Une même application peut donc employer un framework, des bibliothèques CUDA et le pilote tout en ne présentant à l’utilisateur qu’une API web.

### NCCL : communiquer entre GPU

**NCCL**, *NVIDIA Collective Communications Library*, fournit des primitives de communication entre GPU, comme **AllReduce**, ainsi que des échanges point à point.[75] Elle peut servir les communications à l’intérieur d’un nœud et entre plusieurs nœuds ; la documentation cite notamment son usage dans l’entraînement distribué des réseaux.[75] Ce n’est pas un framework complet d’apprentissage et ce n’est pas non plus le câble physique : c’est une bibliothèque qui exploite les chemins disponibles dans une configuration prise en charge.[75]

Scénario pédagogique : plusieurs GPU calculent chacun une contribution à une mise à jour de modèle et doivent combiner leurs résultats. Une primitive collective comme AllReduce est pertinente pour cette combinaison.[75] Retenez trois rôles différents : cuBLAS fournit des opérations de calcul, NCCL des communications entre GPU, et l’interconnexion matérielle transporte les échanges. Une réponse qui confond la bibliothèque et l’interconnexion change de niveau d’abstraction.

### Application, service et orchestration

Le sommet de la pile contient la logique métier et le service proposé à l’utilisateur. Entre le modèle et l’application, un serveur d’inférence peut recevoir les demandes, sélectionner le modèle et organiser leur exécution. Triton propose de la concurrence et plusieurs algorithmes d’ordonnancement ou de regroupement des requêtes.[70] À un autre niveau, Kubernetes et ses composants peuvent organiser la mise à disposition des ressources nécessaires aux charges GPU.[40]

Voici une lecture simplifiée, volontairement non exhaustive : **application → service de modèle → runtime ou framework → bibliothèques → pilote → GPU**. Certaines solutions regroupent plusieurs couches, et les chemins réels ne sont pas tous identiques. Ce schéma sert à poser les bonnes questions : où se produit l’erreur, quel composant remplit le rôle demandé, et quelle dépendance lui manque ? Ce n’est pas une architecture d’installation à copier telle quelle.

<a id="e06"></a>
## E06 — Choisir une solution par son rôle

### TensorRT : optimiser l’inférence

**NVIDIA TensorRT** désigne un écosystème d’outils d’inférence comprenant des compilateurs, des runtimes et des optimisations de modèles. Le SDK peut notamment employer quantification, fusion et choix de kernels pour améliorer l’exécution de réseaux de neurones sur les plateformes compatibles.[3] Une question qui demande de réduire le coût de calcul ou la latence d’un modèle déjà entraîné peut donc orienter vers cette famille.

Cette réponse n’autorise pas à ignorer la qualité ou la compatibilité. Les types numériques pris en charge, les opérateurs et les possibilités de déploiement dépendent des versions et du matériel. TensorRT-LLM vise spécifiquement l’optimisation et l’accélération de l’inférence des grands modèles de langage.[3] Retenez « optimisation d’inférence » plutôt qu’un facteur d’accélération fixe ou une promesse de portabilité universelle d’un artefact compilé.

### Triton : servir et organiser les demandes

**NVIDIA Triton Inference Server** est un logiciel de serving. Sa documentation décrit l’exécution de plusieurs modèles ou instances, sur des systèmes comportant zéro, un ou plusieurs GPU, ainsi que l’exécution sur CPU.[70] Cela permet de séparer la fonction « exposer un service de modèle » du choix « quel processeur exécute le calcul ». Un serveur d’inférence n’est pas défini uniquement par la présence d’un GPU.

Triton peut utiliser différents backends ; TensorRT en fait partie. Les fonctions de serving incluent notamment le **dynamic batching** et l’exécution concurrente selon la configuration.[3][70] Le piège est de répondre TensorRT à toute question contenant le mot *inference*. Si l’énoncé insiste sur la réception de requêtes, plusieurs modèles, leur exécution et leur regroupement, le rôle du serveur est plus directement pertinent que celui d’un optimiseur.

La documentation distingue aussi les modèles sans état entre requêtes et ceux qui maintiennent un état au fil d’une séquence.[70] Au niveau associate, retenez que tous les regroupements de requêtes ne sont pas interchangeables. Dans un exemple pédagogique de conversation ou de traitement séquentiel avec état, mélanger naïvement les demandes ne préserverait pas nécessairement le comportement attendu. Le bon outil doit être correctement configuré pour le modèle, pas seulement installé.

### NIM : simplifier un déploiement de microservice

**NVIDIA NIM** fournit des microservices et des conteneurs pour déployer des modèles d’inférence préentraînés ou personnalisés. NVIDIA le positionne notamment pour des équipes qui gèrent leur infrastructure accélérée mais souhaitent simplifier le logiciel de déploiement.[5] Les moteurs d’inférence intégrés peuvent provenir de NVIDIA ou de la communauté, selon le microservice et sa version.[63]

NIM n’est donc pas synonyme d’un service obligatoirement hébergé hors de l’entreprise. La documentation parle aussi de déploiement autohébergé ; l’infrastructure reste un sujet à gérer.[5] Dans un scénario, l’équipe peut choisir un conditionnement simplifié sans renoncer au contrôle de ses données et de son environnement. Il faut néanmoins vérifier les besoins GPU, la mémoire, les droits d’accès aux artefacts, la licence et les conditions du modèle choisi.

### NeMo : développer et personnaliser

La famille **NVIDIA NeMo** couvre des fonctions liées au cycle de vie des modèles et des applications génératives. La page AI Enterprise décrit notamment la formation de modèles, l’évaluation, les garde-fous et des composants RAG ; la documentation NeMo Framework consultée détaille plus particulièrement les modèles vocaux, leur entraînement et leur personnalisation.[65][52] Il faut donc lire le périmètre de la documentation plutôt que traiter tous les produits portant « NeMo » comme un paquet identique.

Pour une question qui demande d’adapter un modèle au vocabulaire d’un domaine ou de développer une capacité vocale, le rôle de personnalisation est pertinent. Pour une question qui demande seulement de rendre un modèle disponible derrière une API, le rôle d’un serveur ou d’un microservice est plus directement concerné. Une solution de personnalisation peut déboucher sur un déploiement optimisé : les outils se complètent au fil du cycle plutôt que se remplacer tous.

### NGC : trouver, distribuer et partager des artefacts

**NGC** fournit un catalogue de logiciels IA optimisés pour GPU, de SDK et de notebooks, ainsi que des fonctions de registre et de gestion d’organisations dans la documentation consultée.[49] Son nom historique *NVIDIA GPU Cloud* ne signifie pas que tout artefact du catalogue ne s’exécute que dans un cloud public. La documentation mentionne des plateformes incluant stations de travail, instances cloud et serveurs destinés au centre de données ou à l’edge.[49]

Un catalogue ou registre répond à « où obtenir et partager l’artefact ? ». Il ne répond pas à lui seul à « où planifier la tâche ? » ou « quelle qualité de prédiction attendre ? ». Même lorsque des artefacts sont testés ou analysés pour des vulnérabilités, l’entreprise doit contrôler la version effectivement utilisée et ses obligations. Une image disponible dans un registre n’est pas une preuve d’adéquation à tout système ni à tout cas d’usage.

### AI Enterprise et DGX : logiciel pris en charge et plateforme intégrée

**NVIDIA AI Enterprise** est présenté comme une suite logicielle commerciale prise en charge, regroupant microservices, frameworks, bibliothèques et fonctions d’orchestration ou de gestion d’infrastructure.[65] Son rôle est différent de celui d’un GPU physique. Le besoin peut être la stabilité d’un environnement de production, la gestion des vulnérabilités ou l’accès à un support. Les droits et les composants inclus doivent être vérifiés au moment du projet, pas déduits d’un simple nom de marque.

La **plateforme DGX** associe infrastructure, logiciel et expertise pour l’IA d’entreprise. **DGX SuperPOD** relève d’une solution d’infrastructure à grande échelle, tandis que **DGX BasePOD** est présenté comme une architecture de référence avec des partenaires de stockage.[64] Ces noms ne désignent ni des fonctions de perte ni des moteurs de quantification. Dans le domaine Essential, reconnaissez la catégorie et la finalité ; les détails de cluster sont traités dans Infrastructure.

### Omniverse et solutions sectorielles

**Omniverse** est associé au développement d’applications de physical AI, à la simulation robotique et aux jumeaux numériques industriels.[65] La page TensorRT cite également plusieurs solutions spécialisées utilisant des capacités d’inférence, comme Riva pour les usages vocaux ou DeepStream dans l’écosystème d’analyse de flux.[3] Ne transformez pas cette liste en catalogue à mémoriser sans contexte : cherchez d’abord le domaine de la tâche, puis le niveau de la solution.

### RAPIDS, CUDA-X et TAO : agir avant ou autour de l’inférence

L’écosystème **RAPIDS** et les bibliothèques **CUDA-X pour la data science** couvrent l’accélération du traitement de données, de l’analytique et du machine learning.[77] Les exemples comprennent **cuDF** pour des opérations de DataFrame, **cuML** pour des algorithmes ML et **cuGraph** pour des analyses de graphes.[77] Leur rôle rappelle qu’un pipeline d’IA contient aussi du traitement de données et que tout calcul accéléré ne correspond pas à l’inférence d’un réseau profond.

**TAO** fournit des outils de personnalisation de modèles de vision et permet notamment d’adapter des modèles préentraînés à ses propres données.[76] Dans un exemple pédagogique d’inspection industrielle, la personnalisation d’un détecteur peut intervenir avant l’optimisation de son exécution et son déploiement. TAO n’est donc pas un autre nom pour le pilote ; il agit sur la préparation et l’adaptation du modèle, dans le périmètre des architectures et fonctionnalités prises en charge.[76]

## E01 et E07 — Mise à disposition des GPU dans les conteneurs

Le **NVIDIA GPU Operator** automatise, dans Kubernetes, la gestion de composants nécessaires aux GPU : pilote, device plugin, Container Toolkit, étiquetage des nœuds et éléments de supervision DCGM, selon la configuration prise en charge.[40] Il réduit le travail manuel de configuration de cette pile. Il ne remplace ni le matériel, ni Kubernetes, ni un modèle entraîné ; il ne décide pas non plus si les données métier sont correctes.

Le **device plugin** joue un rôle d’intégration des ressources matérielles avec Kubernetes. Le **Container Toolkit** permet l’accès aux capacités GPU depuis l’environnement de conteneur approprié. L’étiquetage et les fonctions de découverte aident à décrire les ressources disponibles.[40] Pour l’examen, comprendre ces responsabilités est plus utile que supposer que le seul mot « container » garantit l’accès à toute la machine.

Scénario pédagogique : une équipe dispose d’un cluster Kubernetes et veut éviter de configurer manuellement chaque nœud GPU. L’objectif renvoie au GPU Operator. Autre scénario : la pile fonctionne déjà, mais il faut publier un modèle derrière un point d’accès d’inférence. L’objectif renvoie plutôt au serving. Dernier scénario : l’application est disponible, mais sa sortie est incorrecte parce que les données ont été mal transformées. Aucun opérateur d’infrastructure ne remplace alors la correction du pipeline.

## Tableau de décision fonctionnel

| Besoin dominant | Rôle à reconnaître | Exemple de solution ou composant |
|---|---|---|
| Programmer ou exploiter le calcul parallèle NVIDIA | Plateforme de calcul | CUDA |
| Réutiliser des primitives de calcul | Bibliothèques optimisées | cuBLAS, cuDNN |
| Optimiser le calcul d’un modèle en inférence | Compilateur/runtime/optimisations | TensorRT, TensorRT-LLM |
| Exposer des modèles et organiser les requêtes | Serving | Triton |
| Simplifier un microservice d’inférence | Conditionnement de déploiement | NIM |
| Développer ou personnaliser des modèles | Workflow et framework de modèle | NeMo |
| Obtenir et partager des artefacts | Catalogue/registre | NGC |
| Automatiser la pile GPU dans Kubernetes | Gestion de composants | GPU Operator |
| Utiliser une suite de production prise en charge | Logiciel commercial et support | AI Enterprise |
| Déployer une plateforme d’infrastructure intégrée | Matériel, logiciel et intégration | DGX |
| Développer une simulation ou un jumeau industriel | Bibliothèques et microservices spécialisés | Omniverse |

Ce tableau synthétise les rôles décrits dans les documentations, sans garantir la compatibilité de toutes les combinaisons.[62][3][65] Une question peut présenter plusieurs produits liés entre eux ; choisissez celui dont la responsabilité répond le plus directement au besoin formulé.

## Deux parcours commentés

**Parcours 1 : modèle visuel déjà validé.** L’équipe obtient ses artefacts et identifie leurs versions, prépare un environnement compatible, mesure l’exécution de référence, teste une optimisation, puis met le modèle derrière un serveur d’inférence. NGC peut participer à la distribution, TensorRT à l’optimisation et Triton au serving.[49][3] Aucun de ces noms, isolément, ne garantit la qualité du modèle ou le respect du délai de bout en bout. Le parcours doit inclure des tests d’application et un responsable du service.

**Parcours 2 : assistant d’entreprise à déployer localement.** L’équipe définit son cas d’usage, choisit un modèle et un mode d’accès aux documents, puis décide si une personnalisation est nécessaire. Un microservice NIM peut simplifier l’inférence, tandis que des composants NeMo ou RAG couvrent d’autres parties du workflow.[5][65] L’infrastructure locale conserve ses contraintes de ressources, de confidentialité et d’exploitation. L’expression « déploiement simplifié » signifie réduction d’un effort logiciel, pas disparition des exigences de production.

## Pièges et auto-évaluation corrigée

1. **Does installing a container eliminate the need for a host GPU driver?** Non. La pile GPU comporte aussi des composants hôtes ; le GPU Operator gère notamment les pilotes et l’intégration des conteneurs.[40]
2. **Which role fits reducing inference execution cost for a trained network?** L’optimisation d’inférence, par exemple TensorRT, à vérifier contre les contraintes de qualité et de compatibilité.[3]
3. **Which role fits serving several models with configurable request scheduling?** Un serveur d’inférence tel que Triton.[70]
4. **Does NGC mean public-cloud-only execution?** Non. La documentation décrit aussi des logiciels destinés aux stations de travail et aux serveurs de centre de données.[49]
5. **Is AI Enterprise the same thing as a DGX GPU server?** Non. Le premier est une suite logicielle commerciale ; DGX désigne une plateforme d’infrastructure intégrée.[65][64]
6. **Does GPU Operator train a model or choose its architecture?** Non. Il automatise la gestion des composants de la pile GPU dans Kubernetes.[40]

## Récapitulatif

Retenez un verbe par niveau : le matériel **calcule**, le pilote **permet l’accès**, CUDA et les bibliothèques **accélèrent**, le framework **structure**, l’optimiseur **transforme l’exécution**, le serveur **sert**, le registre **distribue** et l’opérateur **automatise la pile**. Les offres intégrées assemblent plusieurs de ces rôles. Comprendre leur articulation permet de répondre à des scénarios nouveaux, même lorsque la formulation anglaise ne ressemble pas exactement à une fiche de révision.

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
[3] https://developer.nvidia.com/tensorrt — NVIDIA TensorRT
[5] https://developer.nvidia.com/topics/ai/ai-inference — NVIDIA: AI inference
[40] https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html — NVIDIA GPU Operator Overview
[47] https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html — CUDA C++ Programming Guide
[49] https://docs.nvidia.com/ngc/gpu-cloud/ngc-overview/index.html — NVIDIA NGC overview
[52] https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html — NVIDIA NeMo Framework overview
[62] https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/introduction.html — 1.1. Introduction — CUDA Programming Guide
[63] https://www.nvidia.com/en-us/ai — NVIDIA AI platform
[64] https://www.nvidia.com/en-us/data-center/dgx-platform — NVIDIA DGX platform
[65] https://www.nvidia.com/en-us/data-center/products/ai-enterprise — NVIDIA AI Enterprise software platform
[70] https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_execution.html — Triton Inference Server model execution
[75] https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html — NVIDIA NCCL overview
[76] https://developer.nvidia.com/tao-toolkit — NVIDIA TAO Toolkit
[77] https://developer.nvidia.com/rapids — NVIDIA RAPIDS accelerated data science
