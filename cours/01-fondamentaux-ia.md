# 01 — Fondamentaux de l’intelligence artificielle

**Objectifs locaux couverts : E03, E04, E05.** Les identifiants E01–E08 sont des repères pédagogiques de ce cours, pas des codes attribués par NVIDIA. Ce chapitre prépare les notions du domaine *Essential AI Knowledge* ; la page officielle mentionne notamment la distinction AI/ML/DL, les moteurs d’adoption et les cas d’usage.[1]

## Objectifs d’apprentissage

À la fin du chapitre, vous devez pouvoir expliquer en anglais la relation entre **artificial intelligence**, **machine learning** et **deep learning** ; reconnaître un apprentissage supervisé, non supervisé ou par renforcement ; associer un besoin métier à une famille de tâches ; relier les progrès de l’IA aux données, aux algorithmes et au calcul. L’objectif n’est pas de réciter une chronologie de produits. Il est de reconnaître pourquoi une application a besoin de données, de ressources et de contrôles particuliers.

<a id="e03"></a>
## E03 — AI, ML et DL : trois périmètres emboîtés

L’**intelligence artificielle**, ou *artificial intelligence* (**AI**), est le périmètre le plus large. Dans ce cours, elle désigne des systèmes capables d’effectuer des tâches comme la perception, la prédiction ou la prise de décision. Une méthode à règles explicites peut appartenir à l’IA sans apprendre ses règles dans des données. Le **machine learning** (**ML**, apprentissage automatique) est une partie de l’IA dans laquelle un modèle apprend des régularités à partir d’exemples plutôt que de recevoir toutes les règles sous forme de code.[48]

Le **deep learning** (**DL**, apprentissage profond) est à son tour une partie du ML. Il utilise des réseaux de neurones comportant plusieurs couches de transformations. Les paramètres de ces réseaux, notamment les **weights**, sont ajustés pendant l’apprentissage. Une partie de l’extraction des caractéristiques peut ainsi être apprise, au lieu d’être intégralement construite à la main.[48] Retenez la relation : **DL ⊂ ML ⊂ AI**. Tout système DL est donc ML et AI, mais l’inverse n’est pas vrai.

Prenons un filtre de courrier. Un développeur peut coder une règle « si l’expéditeur appartient à une liste bloquée, rejeter le message ». Cette règle n’est pas, à elle seule, un apprentissage automatique. Un autre système reçoit de nombreux courriers classés *spam* ou *not spam* et apprend les associations utiles à cette décision : c’est du ML. Si le classifieur repose sur un réseau profond entraîné sur ces exemples, il relève aussi du DL.[48] Ce scénario est pédagogique : le même besoin métier peut être satisfait par plusieurs techniques.

Le mot **model** ne désigne ni le serveur entier ni l’application complète. Un modèle est une représentation paramétrée qui transforme une entrée en sortie. Une application ajoute autour du modèle l’authentification, l’accès aux données, l’interface et les décisions métier. Un excellent modèle ne suffit donc pas à produire un service fiable. Pour l’examen, distinguez la technique d’apprentissage, le modèle obtenu et le système qui l’utilise. Cette séparation évite de confondre un outil d’infrastructure avec un algorithme.

### Données, caractéristiques et paramètres

Une **feature**, ou caractéristique, est une propriété de l’entrée utilisée pour apprendre ou prédire : montant d’une transaction, heure, nombre d’incidents récents, etc. Un **parameter** est une valeur interne ajustée par l’apprentissage, par exemple un poids. Une **label** est une cible de référence, telle que « fraude confirmée ». Les caractéristiques décrivent l’exemple ; les paramètres décrivent ce que le modèle a appris ; l’étiquette indique le résultat attendu dans une tâche supervisée.[48]

Cette distinction a une conséquence pratique. Corriger le code d’un formulaire ne change pas automatiquement les paramètres du modèle. Ajouter des exemples à un dossier ne réentraîne pas automatiquement celui-ci non plus. Il faut un processus explicite de préparation, d’apprentissage, d’évaluation et de publication. Dans une question anglaise, *trained weights* renvoie au résultat de l’entraînement, tandis que *training dataset* renvoie aux exemples utilisés pour l’obtenir.[48]

### Les principales formes d’apprentissage

En **supervised learning**, le modèle apprend à rapprocher sa sortie d’une référence. Une **classification** produit une catégorie : transaction légitime ou frauduleuse, type de défaut, catégorie d’un document. Une **regression** prédit une quantité continue : demande électrique, durée d’une panne ou prix. Les deux sont supervisées lorsque les exemples contiennent une cible appropriée.[48] Le critère décisif n’est donc pas « présence de nombres », mais la nature de ce que l’on cherche à prédire.

En **unsupervised learning**, on recherche une structure dans des données sans cible externe de la même nature. Le **clustering** regroupe des exemples similaires, par exemple des profils d’achat. Un cluster n’a pas nécessairement un nom métier donné à l’avance ; c’est ensuite à l’analyste d’interpréter les regroupements. L’absence d’étiquettes ne signifie pas absence de préparation, absence d’hypothèses ou absence d’évaluation.[48]

En **reinforcement learning**, un agent interagit avec un environnement et cherche à maximiser une récompense. Le problème est exprimé par des actions, des états et des conséquences plutôt que par un simple catalogue de bonnes réponses indépendantes. L’exploration peut présenter un risque dans le monde réel ; une simulation ou un environnement contrôlé constitue donc un choix de conception à examiner. La notion à reconnaître est l’apprentissage à partir d’une récompense liée aux actions.[48]

Le **self-supervised learning**, ou apprentissage auto-supervisé, crée un signal d’apprentissage à partir des données elles-mêmes. Prédire une partie masquée d’un texte est un exemple. Il ne nécessite pas qu’un humain annote chaque réponse, mais il existe bien un objectif d’apprentissage. Certaines vulgarisations anciennes parlent globalement d’« apprentissage non supervisé » pour les LLM ; pour raisonner précisément, retenez ici l’idée d’une cible construite depuis les données.[48][9]

### Généraliser plutôt que mémoriser

La finalité du ML est la **generalization** : réussir sur de nouveaux exemples suffisamment représentatifs du problème, pas seulement sur ceux déjà vus.[48] Pour étudier cette différence, imaginez un modèle d’inspection qui reconnaît parfaitement les photographies de formation, mais échoue sur les pièces du prochain lot. Le résultat sur les exemples connus n’établit pas son aptitude à la production. Une séparation entre données de formation et données d’évaluation permet de poser la bonne question : le comportement se transfère-t-il ?

L’**overfitting**, ou surapprentissage, décrit ce piège de l’adaptation excessive aux exemples connus.[48] Le **data leakage**, ou fuite de données, peut rendre une évaluation artificiellement favorable si une information indisponible au moment de la décision se retrouve dans les entrées.[78] Exemple pédagogique : utiliser la confirmation de fraude obtenue après enquête pour prédire une fraude avant autorisation. Ce n’est pas un exploit du GPU ; c’est un défaut de conception de l’évaluation. La priorité est de préserver la validité du test, pas d’accélérer un résultat trompeur.

<a id="e04"></a>
## E04 — Pourquoi l’IA a progressé et s’est diffusée

### Trois moteurs qui se renforcent

Le premier moteur est la disponibilité de **données** numériques : images, textes, transactions, mesures de capteurs et enregistrements. Le deuxième est le progrès des **algorithmes**, notamment des réseaux profonds et des architectures à attention. Le troisième est la disponibilité de **ressources de calcul**, en particulier les GPU capables de traiter de nombreuses opérations parallèles. IBM relie explicitement l’essor du DL à l’importance des grands volumes de données et des GPU ; NVIDIA décrit le rôle du calcul GPU dans l’avancement des applications d’IA.[48][62]

Ces moteurs ne sont pas interchangeables. Beaucoup de données inutilisables ne compensent pas l’absence d’un objectif métier. Un modèle plus grand ne corrige pas automatiquement des données non représentatives. Un GPU plus rapide ne rend pas pertinente une mauvaise évaluation. Pour une question sur les *drivers of AI adoption*, cherchez une combinaison cohérente : données exploitables, méthodes améliorées, calcul accessible et possibilité de déployer la solution, plutôt qu’un composant magique.

### Le logiciel rend le calcul utilisable

L’accélérateur matériel devient plus utile lorsque les équipes peuvent l’exploiter sans réécrire chaque opération. Des bibliothèques et des frameworks exposent des primitives optimisées ; la documentation CUDA cite notamment cuBLAS et cuDNN comme moyens d’éviter de réimplémenter des algorithmes déjà disponibles.[62] Des modèles préentraînés, des conteneurs et des ressources de développement raccourcissent également le chemin entre expérimentation et application ; NGC fournit un catalogue de logiciels optimisés pour GPU.[49]

Il faut distinguer **amélioration technique** et **adoption organisationnelle**. La première peut augmenter la qualité d’un modèle ou diminuer son temps de calcul. La seconde suppose une intégration dans un processus, des compétences disponibles, une exploitation acceptable et un coût soutenable. Une application peut fonctionner en démonstration et rester peu intéressante si elle nécessite une révision humaine plus coûteuse que le travail initial. Dans ce cours, ce raisonnement économique est une grille d’analyse, pas une statistique de marché.

### Réutiliser sans supposer que tout est acquis

Un **pretrained model** a déjà appris sur un jeu de données. Le **fine-tuning** adapte ses paramètres à une tâche ou à un domaine ; il n’est pas synonyme d’entraîner un modèle depuis zéro.[48][9] Cette réutilisation permet de démarrer sans reproduire toute la phase initiale. Elle ne dispense pas de vérifier les droits d’usage, les performances sur les données locales et les risques propres à l’application. La disponibilité d’un téléchargement ne prouve ni sa conformité ni sa pertinence.

Dans le cas pédagogique d’un service documentaire interne, on peut d’abord tester un modèle existant, lui fournir des documents pertinents au moment de la requête, puis déterminer si une personnalisation des paramètres est nécessaire. La *retrieval-augmented generation* (**RAG**) connecte une application générative à des données d’entreprise ; les workflows NVIDIA AI Enterprise comprennent ce type d’intégration.[65] L’intuition utile est simple : apporter des documents au contexte d’une requête n’est pas identique à modifier les poids du modèle.

<a id="e05"></a>
## E05 — Relier les cas d’usage aux contraintes

### Vision : voir, localiser, segmenter

La **computer vision** traite notamment des images et des vidéos. Une classification attribue une catégorie à une image. Une **object detection** repère et localise des objets. Une **segmentation** attribue des classes à des régions ou à des pixels. Ces tâches sont utilisées dans des secteurs comme la santé, le transport et l’inspection.[48] Pour l’examen, la différence entre « dire s’il existe un défaut » et « indiquer où se trouve le défaut » permet souvent de choisir la bonne famille.

Scénario pédagogique : une usine souhaite trier les pièces à la sortie d’une ligne. Les entrées sont les images des pièces ; les sorties peuvent être une classe et une localisation ; la contrainte opérationnelle est de décider avant que la pièce n’atteigne le mécanisme de tri. Une erreur de faux négatif laisse passer un défaut, tandis qu’un faux positif peut faire rejeter une pièce saine. La qualité et la latence doivent donc être évaluées ensemble, pas dans deux projets séparés.

### Langage et génération

Le **natural language processing** (**NLP**) couvre le traitement du langage : classification de texte, traduction, résumé, reconnaissance de la parole et génération. Les **large language models** (**LLM**) relèvent du DL et peuvent être employés pour produire ou transformer du contenu ; un assistant conversationnel n’est qu’un cas d’usage parmi d’autres.[48][9] La génération de code, l’aide à la recherche documentaire et certaines applications en sciences du vivant figurent aussi parmi les usages décrits par NVIDIA.[9]

Scénario pédagogique : un service juridique veut résumer des dossiers. Le besoin est un résumé traçable, pas simplement un texte fluide. On demandera donc des références aux documents, un contrôle des droits d’accès, une évaluation sur des dossiers représentatifs et une procédure de validation humaine. Une réponse bien rédigée n’est pas une preuve de vérité. Les risques à examiner comprennent l’invention d’informations, l’exposition de données et l’usage d’un résultat en dehors du périmètre validé.

### Prédiction, recommandation et anomalies

Les données structurées et les séries temporelles alimentent des tâches de prévision et de détection d’anomalies.[48] Un distributeur peut prévoir la demande, une équipe de maintenance rechercher des comportements inhabituels de capteurs, et un commerce classer des produits à recommander. La recommandation ne signifie pas nécessairement génération de texte ; son résultat peut être une liste ordonnée. De même, « anomalie » ne signifie pas automatiquement « fraude prouvée » : un signal doit être interprété dans son processus métier.

Scénario pédagogique : une banque évalue une transaction au moment du paiement. Le système doit obtenir les informations nécessaires et rendre une décision rapidement. NVIDIA utilise précisément la détection de fraude pour illustrer l’importance de la latence des accès aux données en inférence.[6] Accélérer uniquement les opérations du modèle ne suffit pas si la récupération du profil client domine le temps total. Le besoin métier se propage donc jusqu’aux exigences de stockage et de réseau.

### Simulation et industrie

Les **digital twins**, ou jumeaux numériques, représentent des environnements ou des systèmes pour les simuler et les analyser. NVIDIA présente Omniverse comme un ensemble de bibliothèques et de microservices pour les applications de physical AI, notamment les jumeaux industriels et la simulation robotique.[65] Ce rôle est différent de celui d’un moteur générique d’optimisation d’inférence. Identifier le type de problème précède le choix du nom de produit.

## Méthode de raisonnement pour une question anglaise

Lisez d’abord le verbe : **differentiate** demande une distinction ; **identify** demande de reconnaître une catégorie ; **compare** exige de conserver les deux côtés. Repérez ensuite l’entrée, la sortie et la contrainte dominante. Enfin, éliminez une réponse qui confond les niveaux : un GPU n’est pas un algorithme, un LLM n’est pas toute l’IA, et un cluster n’est pas une stratégie d’apprentissage.

**Pièges fréquents :** croire que tout ML est DL ; considérer qu’un modèle apprend automatiquement pendant chaque requête ; confondre classification et régression ; supposer que plus de données signifie toujours meilleure qualité ; assimiler toute IA à un chatbot ; choisir un produit avant d’avoir défini le résultat attendu. Ces erreurs sont conceptuelles : les corriger facilite ensuite les questions d’infrastructure.

## Auto-évaluation corrigée

1. **A spam filter learns from labeled emails. Which learning category fits?** Réponse : *supervised learning*, car une référence accompagne les exemples ; la présence d’un réseau profond n’est pas précisée.[48]
2. **A company groups customers without predefined categories. Is this regression?** Non : le besoin décrit un *clustering*, pas la prédiction d’une quantité continue.[48]
3. **Does a successful training score prove production readiness?** Non. Il faut étudier la généralisation sur des exemples adaptés au futur usage, puis les exigences du service.[48]
4. **Why do GPUs alone not explain AI adoption?** Parce que les algorithmes, les données et la disponibilité d’outils logiciels interviennent également ; l’utilité métier doit ensuite être démontrée.[48][62]
5. **Is a document retrieved for a prompt necessarily a weight update?** Non : une donnée fournie à une requête n’équivaut pas à un apprentissage des paramètres. Distinguez le contexte de l’adaptation du modèle.[48][65]

## Récapitulatif

Gardez trois cartes mentales : les ensembles emboîtés **AI → ML → DL** ; la chaîne **données → apprentissage → modèle → inférence** ; et la grille **entrée → sortie → qualité → contraintes métier**. Si vous pouvez expliquer pourquoi un filtre appris, un détecteur visuel et un assistant documentaire n’ont pas les mêmes besoins, vous maîtrisez mieux le domaine que par une simple liste d’acronymes.

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
[6] https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing — NVIDIA: Scaling Storage for AI Training and Inferencing
[9] https://blogs.nvidia.com/blog/what-are-large-language-models-used-for — NVIDIA: What Are Large Language Models Used For?
[48] https://www.ibm.com/think/topics/machine-learning — IBM: What is machine learning?
[49] https://docs.nvidia.com/ngc/gpu-cloud/ngc-overview/index.html — NVIDIA NGC overview
[62] https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/introduction.html — 1.1. Introduction — CUDA Programming Guide
[65] https://www.nvidia.com/en-us/data-center/products/ai-enterprise — NVIDIA AI Enterprise software platform
[78] https://scikit-learn.org/stable/common_pitfalls.html — scikit-learn common pitfalls: preprocessing and data leakage
