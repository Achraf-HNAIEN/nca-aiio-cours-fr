# 02 — Calcul accéléré et cycle de vie d’un modèle

**Objectifs locaux couverts : E02, E07, E08.** La comparaison CPU/GPU, les différences entre entraînement et inférence et les composants du cycle de développement figurent dans les objectifs publiés pour le domaine Essential AI Knowledge.[1] Les scénarios et les valeurs hypothétiques ci-dessous sont pédagogiques : ce ne sont ni des spécifications matérielles ni des mesures effectuées sur un cluster.

## Objectifs d’apprentissage

Vous devez pouvoir choisir un type de ressource en fonction d’une tâche, distinguer une limite de calcul d’une limite d’accès aux données, comparer les exigences de *training* et d’*inference*, et expliquer le chemin qui mène des données à un service exploitable. Le niveau attendu est conceptuel : comprendre pourquoi on utilise un outil importe davantage que mémoriser une commande d’installation.

<a id="e08"></a>
## E08 — CPU et GPU : complémentarité plutôt que remplacement

Le **CPU**, ou *central processing unit*, est conçu pour exécuter efficacement des séquences d’instructions, avec des mécanismes de contrôle et des caches adaptés à des traitements variés. Le **GPU**, ou *graphics processing unit*, privilégie un très grand nombre de traitements parallèles et le débit total. La documentation CUDA souligne ce compromis entre la performance d’un thread séquentiel et l’exécution de milliers de threads.[62] Évitez donc la formule « le GPU est un CPU plus rapide » : les objectifs de conception diffèrent.

Dans un serveur d’IA, le CPU garde un rôle actif : l’application doit gérer des requêtes, coordonner le travail et préparer des données. Le GPU accélère les portions compatibles avec son organisation. Les frameworks peuvent s’appuyer sur des bibliothèques GPU optimisées sans que chaque utilisateur écrive directement du code CUDA.[62] Le raisonnement correct est celui d’un calcul **hétérogène** : les composants coopèrent au lieu de se substituer intégralement les uns aux autres.

### Pourquoi les réseaux de neurones se prêtent au GPU

De nombreuses couches de réseaux peuvent être formulées comme des produits de matrices ou des collections de produits scalaires. Ces opérations offrent beaucoup de travail parallèle. Les GPU NVIDIA comprennent des **Streaming Multiprocessors** (**SM**), une hiérarchie de caches et une mémoire à haute bande passante ; certains calculs matriciels sont accélérés par des **Tensor Cores**.[71] Le nom « Tensor » renvoie ici à une capacité matérielle spécialisée, pas à un nouveau type de serveur indépendant du GPU.

Tous les calculs ne sont pas exécutés par les Tensor Cores. La documentation de performance distingue les opérations matricielles des opérations élément par élément et précise que les instructions prises en charge dépendent de l’architecture.[71] Au niveau associate, retenez surtout la spécialisation : une comparaison simpliste entre le nombre de « cœurs » CPU et GPU ne permet pas de prédire une performance. Les unités comptées ne sont pas directement équivalentes, et le programme doit pouvoir les alimenter.

### Latence, débit et parallélisme

La **latency** est le temps nécessaire pour obtenir un résultat. Le **throughput** est la quantité de travail terminée pendant une durée. Un système peut traiter beaucoup de demandes par seconde tout en faisant attendre une demande individuelle. Inversement, une seule demande peut être traitée rapidement sans que le service absorbe une forte concurrence. La plateforme d’inférence NVIDIA présente explicitement le compromis entre faible latence et débit total.[5]

Imaginez une file de dossiers. Les grouper peut améliorer l’efficacité du traitement, mais attendre que le groupe se forme ajoute un délai au premier dossier. Le **batching** exploite ce principe en traitant plusieurs exemples ensemble. Il peut augmenter le travail parallèle et la réutilisation des données, mais sa valeur dépend de la contrainte de réponse. Dans une question qui insiste sur une interaction utilisateur, le meilleur débit brut n’est pas automatiquement le bon objectif.[5][71]

### Trois limites à distinguer

Une opération peut être **compute-bound** : le débit de calcul constitue la limite dominante. Elle peut être **memory-bound** : la circulation des données en mémoire limite davantage que les capacités arithmétiques. Elle peut aussi manquer de travail parallèle et être limitée par des latences ou des surcoûts. Le guide NVIDIA organise précisément l’analyse autour du calcul, de la bande passante mémoire et de la latence.[71] Acheter davantage de capacité arithmétique ne résout pas nécessairement les deux autres cas.

La **memory capacity** répond à « les données nécessaires peuvent-elles tenir ? ». La **memory bandwidth** répond à « à quelle vitesse peut-on les lire et les écrire ? ». Ces deux propriétés ne sont pas synonymes. Une carte peut avoir assez de mémoire mais alimenter trop lentement une opération donnée ; elle peut aussi offrir un débit élevé et manquer de capacité pour la configuration choisie. NVIDIA distingue la mémoire GPU, les chemins de transfert et les supports de stockage dans sa hiérarchie des données.[6][71]

Scénario pédagogique : un GPU reste souvent en attente pendant que le CPU décode des images et lit de petits fichiers. Avant de remplacer le GPU, examinez la préparation et l’alimentation des données. Autre scénario : le GPU est occupé mais le modèle ne tient plus dans sa mémoire avec la configuration demandée. L’enjeu devient la capacité et l’organisation de l’exécution. Les deux problèmes impliquent le même serveur mais appellent des réponses différentes.

<a id="e02"></a>
## E02 — Training et inference : même modèle, autres priorités

### Entraîner : apprendre les paramètres

Le **training** ajuste les paramètres pour réduire une erreur ou améliorer un objectif. Dans un réseau entraîné par gradient, une étape conceptuelle comprend une **forward pass**, le calcul d’une **loss**, une **backward pass** pour obtenir les gradients, puis une mise à jour par l’**optimizer**. Le rôle de la rétropropagation et de la descente de gradient est expliqué dans la présentation IBM du deep learning.[48] Un *gradient* indique comment faire varier un paramètre pour agir sur la fonction optimisée ; ce n’est pas la prédiction donnée à l’utilisateur.

Cette différence explique une partie des besoins de mémoire. En plus des poids, l’entraînement peut conserver des résultats intermédiaires nécessaires au calcul des gradients et des états liés à l’optimisation.[79] La consommation ne se résume donc pas au fichier contenant les paramètres. Pour ce cours, utilisez une liste de postes à vérifier plutôt qu’un multiplicateur fixe : poids, valeurs intermédiaires, gradients, états de l’optimiseur et espace de travail.[79] Le détail varie avec la méthode et l’implémentation ; un chiffre universel serait trompeur.

La priorité d’un long entraînement est souvent le **time to train** ou **time to solution** : obtenir un modèle répondant à l’objectif dans un temps acceptable. Il faut alimenter le calcul, préserver les résultats intermédiaires utiles et pouvoir reprendre après incident. Un **checkpoint** sauvegarde un état permettant une reprise ou une réutilisation ; les frameworks de personnalisation NVIDIA utilisent notamment des checkpoints préentraînés.[52] La fréquence de sauvegarde doit être raisonnée avec son coût d’écriture et la quantité de travail que l’on accepte de perdre.

### Inférer : appliquer les paramètres

L’**inference** utilise un modèle pour calculer une sortie sur de nouvelles entrées. Elle ne réalise pas, par défaut, une mise à jour des paramètres à chaque requête ; la généralisation apprise pendant le training est appliquée à de nouveaux exemples.[48] Un service en ligne n’est donc pas « en entraînement permanent » simplement parce que des utilisateurs lui posent des questions. Un éventuel apprentissage ultérieur constitue une étape distincte à concevoir et à contrôler.

Les priorités d’inférence incluent la latence, le débit et l’efficacité du service. Un détecteur exécuté sur un flux, un assistant conversationnel et une analyse de fichiers pendant la nuit n’ont pas la même tolérance au délai. L’inférence peut fonctionner sur CPU ou GPU selon le modèle et la contrainte ; Triton peut exécuter des modèles sur les deux types de processeur.[70] « Inference » n’implique donc ni « petit modèle » ni « absence de GPU ».

Une inférence de grand modèle peut demander plusieurs GPU et une organisation distribuée. La page NVIDIA dédiée décrit notamment des outils de serving pour des environnements distribués et de grandes flottes.[5] Inversement, un petit entraînement ou une expérimentation limitée ne nécessite pas obligatoirement un grand cluster. Dans l’énoncé anglais, basez votre réponse sur la taille et le comportement de la charge, pas uniquement sur le mot *training* ou *inference*.

### Comparaison raisonnée

| Dimension | Entraînement | Inférence |
|---|---|---|
| Finalité | Ajuster des paramètres | Calculer des sorties avec un modèle |
| Calcul conceptuel | Propagation, objectif, gradients, mise à jour | Exécution du modèle pour la prédiction |
| Mémoire à examiner | Poids et états nécessaires à l’apprentissage | Poids, données et états nécessaires à la requête |
| Indicateur fréquent | Temps pour atteindre la qualité recherchée | Latence et débit au niveau de service attendu |
| Données persistantes | Jeux d’apprentissage, versions, checkpoints | Modèles déployés, entrées et références nécessaires |
| Exigence opérationnelle | Reprise et efficacité de longues tâches | Disponibilité et comportement sous charge |

Cette table est une grille de comparaison, pas une règle de dimensionnement. La séparation entre apprentissage et application du modèle est fondamentale ; les choix de stockage et les objectifs de performance restent dépendants du cas d’usage.[48][6][5]

### Optimiser sans ignorer la qualité

La **quantization** emploie des représentations de précision réduite pour certaines valeurs. Elle peut réduire des besoins de mémoire et de transfert, mais son effet doit être évalué sur le matériel, le modèle et les données ciblés. TensorRT comprend des outils de quantification et d’autres optimisations d’inférence comme la fusion et l’ajustement des kernels.[3] Une précision plus faible n’est ni une garantie de vitesse sur tout matériel ni une garantie d’absence de dégradation.

Ne confondez pas optimiser une représentation et apprendre une nouvelle capacité métier. Une optimisation peut accélérer un modèle déjà valide ; elle n’établit pas que ses prédictions sont correctes. La bonne séquence pédagogique est : fixer les critères de qualité, mesurer une référence, appliquer une optimisation, réévaluer la qualité et la performance dans des conditions comparables. Les accélérations marketing associées à des configurations particulières ne sont pas des constantes à appliquer à tous les serveurs.

<a id="e07"></a>
## E07 — Le cycle de vie : des données à un service maintenable

### Définir le besoin et préparer les données

Commencez par le résultat attendu : quelle entrée, quelle sortie et quelle décision ? Définissez ensuite la qualité minimale et les contraintes de fonctionnement. Ce cadrage permet de choisir une tâche ML adaptée, de savoir si un modèle existant suffit et de construire une évaluation représentative. L’étape de préparation transforme les données brutes en entrées adaptées ; IBM décrit la représentation numérique des caractéristiques et le rôle du *feature engineering*.[48]

Un **data pipeline** collecte, nettoie et transforme les données. Il peut comporter de la validation de format, de l’annotation, de la normalisation et de la séparation des ensembles.[48] Le logiciel qui prépare les entrées en production doit rester cohérent avec celui utilisé pendant l’évaluation.[78] Dans un scénario pédagogique, changer le codage d’une catégorie ou l’ordre des caractéristiques sans revoir le modèle peut rendre ses sorties inutilisables, même si le serveur ne signale aucune erreur matérielle.

### Développer, apprendre et suivre les expériences

Un **framework** offre des abstractions pour construire et exécuter les modèles. Il se situe au-dessus de bibliothèques et de runtimes qui exploitent l’accélérateur ; la documentation CUDA explique que les frameworks peuvent utiliser ces bibliothèques.[62] Un outil de suivi d’expériences conserve le lien entre configuration, version des données, résultats et artefacts.[83] Dans ce cours, ces fonctions sont décrites sans imposer un produit particulier : leur utilité est la comparaison et la reproductibilité.

L’**artifact** publié peut inclure les poids, une configuration, un tokenizer ou d’autres éléments indispensables à l’exécution. Il doit être identifiable. Si deux équipes disent seulement « nous utilisons le modèle final », elles ne disposent pas d’une traçabilité suffisante. Une version de modèle doit être associée à une version de traitement des entrées et à des critères d’acceptation. NGC fournit des mécanismes de distribution et de partage d’artefacts logiciels et de ressources pour les workflows IA.[49]

### Évaluer, conditionner, déployer

L’évaluation pose deux questions distinctes : « la sortie est-elle suffisamment bonne ? » et « le service fonctionne-t-il dans ses contraintes ? ». Le premier volet examine les performances de la tâche ; le second les temps de réponse, la capacité, les erreurs et le comportement sous charge. Le compromis latence/débit est central pour l’inférence.[5] Une validation uniquement sur quelques requêtes sans concurrence n’est donc pas un test représentatif d’un service fortement sollicité.

Le **packaging** réunit les éléments nécessaires à l’exécution. Un conteneur facilite la distribution d’un environnement applicatif, mais l’accès au GPU exige aussi une pile hôte compatible. La documentation GPU Operator identifie explicitement les pilotes, le Container Toolkit et le device plugin comme composants nécessaires à la mise à disposition des GPU dans Kubernetes.[40] Ne concluez jamais qu’une image de conteneur contient à elle seule toute l’infrastructure requise.

Le **serving** reçoit les requêtes et fait exécuter les modèles. TensorRT optimise l’exécution d’inférence ; Triton fournit des fonctions de service, de concurrence et de batching ; NIM simplifie la distribution de microservices d’inférence.[3][70][5] Ces rôles peuvent se compléter. Un ordonnanceur de cluster place les charges sur des ressources, tandis qu’un ordonnanceur interne au serveur d’inférence gère les requêtes de modèle : ils n’agissent pas au même niveau.

### Observer, décider et revenir en arrière

Après déploiement, l’équipe doit surveiller le système et les résultats.[48] Une application peut rester disponible tout en devenant moins utile si les entrées évoluent. On parle de **drift** pour étudier ces changements ; il faut ensuite décider s’ils justifient une réévaluation ou un réentraînement.[48] La logique est une boucle contrôlée, pas une modification aveugle des poids au moindre signal. Les workflows de développement et de déploiement sont itératifs ; NVIDIA décrit plusieurs cycles de personnalisation, d’évaluation et de préparation à l’inférence pour les modèles vocaux NeMo.[52]

Un **rollback** consiste à revenir à une version validée lorsqu’un déploiement pose problème.[84] Il faut donc garder la version précédente et les éléments nécessaires pour l’exécuter. Scénario pédagogique : un modèle améliore une moyenne de qualité, mais augmente les faux rejets dans une région. La réponse n’est pas forcément de réserver davantage de GPU. Il faut examiner les résultats par population, les données et le changement de version, puis appliquer la politique de retour arrière si les critères ne sont plus respectés.

## Scénario complet : du laboratoire à l’API

Une équipe entraîne un classifieur d’images, obtient une qualité acceptable, puis ouvre un service interne. Au laboratoire, les images étaient locales et les appels isolés. En production, les utilisateurs téléchargent des images de tailles variables et arrivent par vagues. Le temps total inclut désormais transfert, décodage, préparation, attente, exécution et réponse. Ce découpage est une méthode de diagnostic : mesurer chaque étape avant d’accuser le GPU.

L’équipe compare ensuite un batching limité à une exécution sans regroupement. Elle conserve la configuration qui respecte la contrainte de réponse tout en utilisant efficacement les ressources. Elle teste enfin une optimisation de précision et refuse de la publier si la qualité n’est plus acceptable. Ce scénario applique les compromis de serving et d’optimisation documentés par NVIDIA, sans promettre un gain numérique particulier.[5][3]

## Pièges et auto-évaluation corrigée

- **Does more GPU compute always fix a memory-bound layer?** Non : la limite concerne surtout l’accès aux données, pas seulement le débit arithmétique.[71]
- **Does inference update weights by default?** Non : elle applique un modèle appris à de nouvelles entrées ; l’actualisation des paramètres relève d’un processus d’apprentissage.[48]
- **Why keep checkpoints?** Pour conserver un état réutilisable ou reprendre un travail plutôt que dépendre uniquement de l’exécution en cours.[52]
- **Can a GPU server have a CPU bottleneck?** Oui : l’accélération GPU ne supprime pas les étapes séquentielles ou de préparation ; CPU et GPU ont des rôles complémentaires.[62]
- **Are TensorRT and a model-serving server interchangeable?** Non : l’optimisation du calcul du modèle et l’organisation du service de requêtes sont des rôles distincts, même si le serveur utilise TensorRT comme backend.[3]

## Récapitulatif

Pour chaque question, demandez-vous **quelle étape travaille**, **quelle ressource la limite** et **quel critère doit être respecté**. Le CPU coordonne et traite des tâches générales ; le GPU exploite un parallélisme important. Le training apprend ; l’inference applique. Le cycle de vie ne s’arrête pas à un bon score : il inclut conditionnement, publication, observation et maintien d’une version fiable.

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
[3] https://developer.nvidia.com/tensorrt — NVIDIA TensorRT
[5] https://developer.nvidia.com/topics/ai/ai-inference — NVIDIA: AI inference
[6] https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing — NVIDIA: Scaling Storage for AI Training and Inferencing
[40] https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html — NVIDIA GPU Operator Overview
[48] https://www.ibm.com/think/topics/machine-learning — IBM: What is machine learning?
[49] https://docs.nvidia.com/ngc/gpu-cloud/ngc-overview/index.html — NVIDIA NGC overview
[52] https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html — NVIDIA NeMo Framework overview
[62] https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/introduction.html — 1.1. Introduction — CUDA Programming Guide
[70] https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_execution.html — Triton Inference Server model execution
[71] https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html — NVIDIA GPU performance background for deep learning
[78] https://scikit-learn.org/stable/common_pitfalls.html — scikit-learn common pitfalls: preprocessing and data leakage
[79] https://docs.pytorch.org/tutorials/intermediate/optimizer_step_in_backward_tutorial.html — PyTorch training memory usage and optimizer state
[83] https://mlflow.org/docs/latest/ml/tracking — MLflow ML Experiment Tracking
[84] https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html — Amazon SageMaker AI deployment guardrails
