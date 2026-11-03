# 08 — Orchestration, scheduling et virtualisation accélérée

**Objectifs locaux : O02 — orchestration/job scheduling ; O04 — virtualization considerations.** Liens transversaux : O01 pour l'exploitation de la pile et O03 pour ses métriques. Les identifiants sont pédagogiques, pas des codes NVIDIA. Les exemples décrivent des configurations possibles à vérifier dans leur matrice de support, pas une recette universelle de production.

## Objectifs d'apprentissage

Vous devez pouvoir distinguer une demande de ressources, une décision de placement et l'accès effectif au GPU ; comparer Slurm et Kubernetes sans déclarer l'un universellement supérieur ; expliquer les responsabilités du device plugin, du Container Toolkit et du GPU Operator ; et choisir entre GPU dédié à une VM, vGPU et MIG. Aucune configuration ou commande de ce chapitre n'a été validée sur un cluster GPU réel dans le cadre de ce cours.

## 1. De la demande utilisateur à l'exécution

Un utilisateur veut lancer un travail, mais plusieurs utilisateurs peuvent viser les mêmes accélérateurs. L'**ordonnancement**, ou *scheduling*, décide quelles ressources attribuer et quand, dans les contraintes du système. L'orchestration couvre plus largement la mise en place et la coordination des charges et de leur environnement. Dans un raisonnement d'examen, cherchez d'abord la responsabilité décrite : décider du placement n'est pas installer le pilote, et installer un pilote n'est pas réserver une carte.

La documentation Slurm présente des ressources génériques, **GRES**, pour représenter notamment les GPU et leurs caractéristiques ; les jobs doivent les demander pour qu'elles soient allouées. La documentation Kubernetes décrit, pour sa part, des ressources GPU exposées par des device plugins et consommées par les conteneurs via des demandes adaptées.[43][41]

Représentez la chaîne par quatre questions : le matériel existe-t-il et est-il sain ? Le système annonce-t-il sa capacité réelle ? Le job demande-t-il une ressource compatible ? Enfin, l'environnement peut-il réellement y accéder ? Une erreur à une étape peut ressembler, pour l'utilisateur, au même symptôme : « mon application ne voit aucun GPU ». Le diagnostic consiste à séparer ces étapes, pas à réinstaller toute la pile au hasard.

Il faut aussi préciser l'unité. Demander « un GPU » peut vouloir dire un appareil physique entier, une instance MIG ou une ressource partagée dans une configuration spécialisée. Le nom et la quantité de ressources annoncées doivent être compris avec la politique de partage. Une unité logique n'est pas automatiquement une carte supplémentaire ni une garantie de mémoire ou de débit dédiée.

## 2. Slurm : ressources et jobs de calcul

### 2.1 Déclarer puis demander les GPU

Dans Slurm, l'administrateur décrit les GRES disponibles et leur correspondance avec les nœuds et périphériques. La documentation distingue des demandes par job, par nœud ou par tâche, avec des options et conditions propres à la configuration. Les nœuds dont les ressources détectées ne correspondent pas aux ressources configurées peuvent être placés en état `DRAIN` pour ne plus recevoir de nouveaux travaux selon ces règles.[43]

Pour un entraînement distribué, « quatre GPU par nœud » et « quatre GPU au total » ne sont donc pas des formulations interchangeables. Le candidat doit lire l'échelle de la demande et le nombre de nœuds. L'objectif n'est pas de multiplier des nombres mentalement, mais d'identifier si l'allocation correspond à la topologie et au parallélisme requis par l'application.

Exemple schématique, non soumis à Slurm et à adapter à un cluster possédant la partition et les GRES appropriés :

```bash
#!/bin/bash
#SBATCH --job-name=exemple-entrainement
#SBATCH --nodes=1
#SBATCH --gres=gpu:2
#SBATCH --time=00:30:00
# Lancement illustratif : le programme doit réellement prendre en charge les GPU.
srun python train.py
```

L'option `--gres` exprime ici une demande par nœud, dans le mécanisme décrit par SchedMD. Le simple fait de réserver plusieurs GPU ne rend pas automatiquement un programme mono-GPU distribué.[43]

### 2.2 Allocation, visibilité et contrôle

Le plugin GRES GPU de Slurm définit `CUDA_VISIBLE_DEVICES` pour les étapes des jobs afin de présenter les appareils alloués. La documentation explique que les identifiants visibles dans le job peuvent différer de ceux des programmes Prolog/Epilog, notamment quand les cgroups contraignent les périphériques. Une différence de numérotation n'est donc pas nécessairement une mauvaise allocation.[43]

Cependant, la visibilité fournie par une variable ne doit pas être confondue avec une frontière de sécurité suffisante à elle seule. Dans une procédure d'exploitation, on vérifie aussi les mécanismes de contrainte configurés par l'administrateur, l'accès aux périphériques et la comptabilisation. Un script utilisateur ne doit pas contourner l'allocation en choisissant arbitrairement des appareils du voisin.

### 2.3 Pourquoi un job attend-il ?

Dans un scénario pédagogique, un job multi-nœuds reste en attente alors que des GPU sont inoccupés. La capacité libre totale ne prouve pas qu'une allocation compatible soit possible : les appareils peuvent être répartis sur les mauvais nœuds, manquer de mémoire disponible côté hôte, ou appartenir à des ressources dont le type demandé diffère. L'état de la file et la demande exacte doivent être examinés avant de conclure à une panne matérielle.

Pour les workloads batch de calcul scientifique et d'entraînement, Slurm constitue une option naturelle lorsque l'organisation veut raisonner en allocations et étapes de jobs. Cela reste un choix d'architecture et d'exploitation, pas une règle interdisant les services sur Slurm ou les entraînements sur Kubernetes. Le mécanisme GRES est le point technique à reconnaître ici.[43]

## 3. Kubernetes : du Pod au GPU accessible

### 3.1 Ce que fait le device plugin

Le **device plugin** fait connaître au système les ressources matérielles spécialisées du fournisseur. Pour le mécanisme GPU décrit par Kubernetes, l'administrateur installe les pilotes du fournisseur et le plugin correspondant ; le cluster peut ensuite exposer une ressource telle que `nvidia.com/gpu`.[41]

Cette annonce donne au scheduler une information exploitable pour placer les Pods. Elle n'installe pas magiquement toutes les dépendances de calcul dans l'image applicative, et ne transforme pas une image CPU en programme CUDA. Une application doit être conçue pour utiliser le GPU et disposer des bibliothèques nécessaires à sa propre exécution.

Avec le mécanisme de ressources étendues GPU décrit dans cette documentation, une limite GPU sans demande explicite devient aussi la demande ; si `requests` et `limits` sont tous deux fournis pour ce GPU, leurs valeurs doivent être égales. Il ne faut pas transposer sans contrôle les habitudes de surallocation CPU à cette ressource GPU entière.[41]

Fragment illustratif d'un conteneur dans un manifeste, pas un fichier complet à appliquer :

```yaml
resources:
  limits:
    nvidia.com/gpu: 1
```

Cette syntaxe demande une unité de la ressource exposée sous ce nom. Sa signification réelle dépend de la configuration du plugin et du partage ; dans un enseignement de base sans partage configuré, on raisonne sur un GPU entier. Pour des types de GPU différents, labels et sélecteurs ou affinités permettent de cibler des nœuds adaptés, comme l'explique Kubernetes.[41]

### 3.2 Runtime et NVIDIA Container Toolkit

Le **container runtime** crée et exécute les conteneurs ; l'accès aux GPU nécessite une intégration appropriée avec l'hôte. Le **NVIDIA Container Toolkit** fournit des composants qui permettent de configurer l'accès NVIDIA des conteneurs, notamment via des bibliothèques, outils et intégrations runtime. La documentation décrit plusieurs chemins, dont des mécanismes OCI et la génération de spécifications **CDI**, Container Device Interface.[42]

Retenez le partage des responsabilités : le driver rend le matériel utilisable au niveau du système ; le plugin l'annonce dans Kubernetes ; le toolkit participe à son exposition dans les conteneurs ; l'image contient le programme et ses dépendances applicatives. L'absence de GPU dans un conteneur peut donc relever d'une configuration runtime même quand le driver fonctionne sur l'hôte.[40][41][42]

Un conteneur Linux n'est pas une VM complète : les conteneurs partagent le noyau de leur hôte, tandis qu'une VM dispose de son propre noyau.[53] Dans le raisonnement pratique, empaqueter l'application améliore la reproductibilité mais ne supprime pas la dépendance à une combinaison compatible de pilote, runtime et bibliothèques. L'architecture documentée du toolkit s'appuie précisément sur l'intégration au système et au runtime.[42]

### 3.3 Ce qu'automatise GPU Operator

Le **NVIDIA GPU Operator** utilise le modèle Operator de Kubernetes pour automatiser la gestion des composants NVIDIA nécessaires aux GPU : pilotes, device plugin, Container Toolkit, découverte/étiquetage et monitoring fondé sur DCGM figurent parmi les éléments documentés.[40]

Il ne faut pas l'assimiler au scheduler de tous les jobs, à l'application d'entraînement ou à une permission automatique de partager un GPU entre tous les utilisateurs. Il réduit le travail de mise en place et de maintien de la pile concernée. Le fonctionnement exact dépend de la plateforme et des options retenues ; les matrices de support restent à vérifier.[40]

**Cas guidé :** après l'ajout de nœuds, les Pods GPU restent en attente et aucune capacité GPU n'est annoncée. Une approche raisonnable consiste à vérifier le pilote, l'état du plugin, la configuration opérateur et les ressources publiées. Augmenter le nombre de réplicas du service ne crée pas les ressources manquantes. Si les Pods sont placés mais que l'application ne voit pas l'appareil, l'analyse descend vers le runtime et l'environnement conteneur.[40][41][42]

## 4. Choisir une stratégie d'orchestration

Pour comparer Slurm et Kubernetes, partez de la charge et des pratiques de l'équipe. Un environnement centré sur des allocations batch, des étapes de calcul et des utilisateurs HPC se reconnaît dans les concepts Slurm. Un environnement centré sur des applications conteneurisées et la gestion déclarative de services se reconnaît dans les objets Kubernetes. Les deux peuvent exposer des ressources GPU ; ni l'un ni l'autre n'élimine les besoins de driver, de réseau, de stockage ou d'observabilité.[43][41]

Proposition d'analyse avant déploiement : préciser les durées des charges, le besoin de service continu ou batch, les contraintes de placement collectif, le nombre de locataires, les politiques de priorité et les compétences de l'exploitation. Un orchestrateur adapté à la culture de l'équipe mais mal configuré ne devient pas fiable par son seul nom. Un orchestrateur différent n'est pas automatiquement la réponse à une alimentation en données insuffisante.

**Piège fréquent :** confondre GPU alloué et GPU productif. Un job peut réserver des appareils et passer du temps en préparation CPU ou en synchronisation. Les informations de scheduling expliquent qui possède la ressource ; les métriques et la progression expliquent ce que cette ressource produit. Les deux vues doivent être rapprochées, comme le permettent les concepts de groupes et de statistiques de jobs DCGM.[38]

## 5. Virtualiser : trois mécanismes à distinguer

### 5.1 GPU passthrough : assigner un appareil entier

Le **GPU passthrough**, ou assignation directe, affecte un GPU physique entier à une VM. Le pilote de la VM l'utilise exclusivement ; l'appareil n'est pas partagé entre plusieurs VM par ce mécanisme. Dans le périmètre documenté NVIDIA, le mode passthrough contourne le Virtual GPU Manager.[56]

Ce choix répond à un besoin d'accès dédié à l'appareil, mais limite la mutualisation de ce GPU entre VM. Il faut vérifier les fonctions de virtualisation d'E/S de la plateforme, les restrictions de l'hyperviseur, l'OS invité et les pilotes. La documentation citée décrit des prérequis BIOS et des restrictions spécifiques ; on ne les généralise pas à toutes les combinaisons matérielles imaginables.[56]

La supervision est aussi affectée. Pour le passthrough décrit dans ce guide, la performance du GPU doit être observée depuis la VM ; les outils passant par l'hyperviseur ne disposent pas de la même visibilité. Prévoir la collecte dans l'invité évite de prendre l'absence de télémétrie hôte pour une disparition de la carte.[56]

### 5.2 vGPU : présenter des ressources GPU à plusieurs VM

**NVIDIA vGPU** permet à plusieurs VM d'accéder à un GPU physique via la pile de virtualisation prise en charge. Ce n'est pas simplement le fait de placer une application CUDA dans un conteneur. La documentation distingue notamment des configurations de vGPU avec partage temporel et des configurations fondées sur MIG, selon les GPU et logiciels compatibles.[58]

Dans un partage temporel (*time slicing*), les travaux se partagent le temps d'exécution de ressources physiques. Il ne faut donc pas conclure que chaque vGPU possède, par définition, tous les moteurs de calcul physiquement dédiés. Les profils, la mémoire disponible et les règles de scheduling déterminent ce qui est présenté aux invités ; ces choix doivent correspondre à la charge et aux objectifs de performance.[58]

Toutes les fonctions CUDA ne sont pas garanties dans chaque profil vGPU. NVIDIA précise que le support CUDA et OpenCL dépend d'un sous-ensemble de types vGPU et de GPU pris en charge. Choisir un profil parce qu'il affiche suffisamment de mémoire ne dispense donc pas de vérifier les API et fonctions utilisées par l'application.[58]

### 5.3 MIG : partitionner le matériel compatible

**Multi-Instance GPU**, MIG, partitionne les ressources d'un GPU pris en charge en instances disposant de ressources de calcul et de chemins mémoire séparés. La documentation décrit notamment l'affectation de parties du cache L2, des contrôleurs et de la mémoire aux instances, pour un comportement plus prévisible entre charges.[44]

MIG n'est ni une VM, ni un simple nouveau nom pour le partage temporel. Il peut être utilisé en bare metal, avec des conteneurs et dans des configurations virtualisées prises en charge. Les deux notions MIG et vGPU ne sont donc pas mutuellement exclusives : une offre vGPU peut s'appuyer sur une instance MIG.[44][58]

Le nombre d'instances, leurs profils et les fonctionnalités disponibles dépendent du GPU et de la version. La liste « Supported GPUs » donne notamment les modèles pris en charge et leur nombre maximal d'instances ; il ne faut pas transformer la valeur d'un produit en constante valable pour tout GPU NVIDIA. Un GPU d'une architecture récente ne prouve pas à lui seul le support de MIG : vérifier le modèle exact et les configurations supportées.[44][61]

### 5.4 Comparaison raisonnée

| Mécanisme | Unité et logique principales | Question à vérifier avant de choisir |
|---|---|---|
| Passthrough | Un GPU physique assigné à une VM | Dédié nécessaire, support invité et visibilité ? |
| vGPU | Ressource GPU présentée à une VM | Profil, mode de partage, fonctions et licence ? |
| MIG | Partition matérielle d'un GPU compatible | Taille de l'instance, isolation requise et support ? |
| Conteneur avec GPU | Application empaquetée utilisant un accès GPU | Driver/runtime et ressources réellement allouées ? |

Les trois mécanismes de virtualisation et partitionnement doivent être distingués.[44][56][58]
L’accès GPU d’un conteneur exige pour sa part une intégration au runtime.[42] La table n’est pas une promesse de support pour une combinaison non consultée.

## 6. Compatibilité, licence et exploitation

La **compatibilité** n'est pas un simple oui/non attaché au mot GPU. Il faut vérifier une combinaison : modèle physique, serveur et firmware, hyperviseur, OS invité, version du logiciel vGPU et des pilotes, profil demandé et fonctions applicatives. Le guide vGPU renvoie aux notes de version par hyperviseur pour le support des instances ; il ne suffit pas qu'un autre hyperviseur supporte une fonction similaire.[58]

La **licence** est une question distincte de la capacité matérielle. Le guide de licensing consulté concerne les produits NVIDIA vGPU Software, notamment vWS, vPC et vApps, avec des droits et modes de déploiement différents. Certaines configurations décrites utilisent une vérification logicielle de licence ; d'autres relèvent d'une obligation contractuelle EULA même sans checkout de licence. Une absence de dialogue visible avec un serveur de licences ne prouve donc pas l'absence d'obligation.[59]

Précaution essentielle : les règles de ce guide ne doivent pas être étendues à toute utilisation CUDA, à tout passthrough ou à tout MIG. Une assignation PCIe est un mécanisme technique ; les droits applicables dépendent du logiciel utilisé et de son offre. De même, un MIG bare metal ne prouve pas qu'une pile vGPU commerciale est installée. Pour un projet réel, valider les droits exacts de l'offre retenue, ses conditions et son support plutôt que réciter une règle « toujours gratuit » ou « toujours licence vWS ».[44][59]

Prévoir aussi l'exploitation : collecte hôte et invité, identification stable des instances, procédure de modification des profils, sauvegarde des configurations et retour arrière. Une opération de reconfiguration doit être évaluée pour son impact sur les charges ; l'existence d'un mécanisme de partition ne donne pas une permission de le modifier pendant un entraînement. Le cours recommande de planifier ces changements et d'en vérifier le résultat applicatif.

## 7. Trois décisions commentées

**Scénario A — Une grosse VM d'entraînement veut toute la carte.** Si l'objectif est l'accès exclusif à un GPU entier dans une VM compatible, le passthrough répond au mécanisme demandé. On vérifie ensuite le pilote invité, le support hyperviseur et la supervision depuis la VM. Répondre MIG sans besoin de partitionnement ne traite pas le besoin principal.[56]

**Scénario B — Plusieurs petites charges doivent être isolées sur une carte compatible.** MIG est un candidat quand chacune tient dans un profil disponible et que l'on recherche la séparation des ressources décrite par le matériel. Si les charges doivent être hébergées dans des VM, évaluer une configuration MIG/vGPU supportée, au lieu de supposer que MIG crée ces VM.[44][58]

**Scénario C — Une VM vGPU est lente après un changement d'environnement.** Ne pas diagnostiquer uniquement une saturation GPU. Vérifier d'abord profil, versions, fonction CUDA utilisée et état de licence dans le périmètre logiciel choisi. Le guide décrit des dégradations de capacité en cas d'échec d'obtention de licence avec certains modes d'enforcement. Ce diagnostic est propre à ce logiciel, pas une explication universelle de toute lenteur de VM.[58][59]

## 8. Récapitulatif et autoévaluation

Le scheduler attribue des ressources ; le plugin les annonce ; le toolkit intègre l'accès GPU des conteneurs.[41][42][43]
GPU Operator automatise la gestion de composants NVIDIA.[40] Garder ces responsabilités séparées rend le dépannage plus précis.

**Question 1.** Un programme utilise-t-il automatiquement les GPU réservés par Slurm ? **Réponse :** non ; la réservation fournit des ressources, mais l'application et son lancement doivent réellement les exploiter.[43]

**Question 2.** Le device plugin remplace-t-il le GPU Operator ? **Réponse :** non ; le plugin est un composant spécialisé, alors que l'Operator gère plusieurs composants de la pile.[40][41]

**Question 3.** MIG et vGPU sont-ils incompatibles par définition ? **Réponse :** non ; des déploiements vGPU reposent sur MIG dans des combinaisons prises en charge.[44][58]

**Question 4.** Passthrough signifie-t-il partage de la carte entre plusieurs VM ? **Réponse :** non ; il assigne directement l'appareil physique entier à une VM dans le mécanisme décrit.[56]

**Question 5.** Peut-on décider de la licence à partir du seul nom MIG ? **Réponse :** non ; il faut identifier la pile logicielle et l'offre réellement déployées, puis appliquer leurs conditions.[44][59]

## Sources

[38] https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html — NVIDIA DCGM Feature Overview
[40] https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html — NVIDIA GPU Operator Overview
[41] https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus — Kubernetes Schedule GPUs
[42] https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/arch-overview.html — NVIDIA Container Toolkit Architecture Overview
[43] https://slurm.schedmd.com/gres.html — Slurm Generic Resource Scheduling
[44] https://docs.nvidia.com/datacenter/tesla/mig-user-guide/introduction.html — NVIDIA MIG User Guide Introduction
[53] https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container — What is a container? | Docker Docs
[56] https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/using-gpu-pass-through.html — NVIDIA Using GPU Pass-Through
[58] https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/grid-vgpu-introduction.html — Introduction to NVIDIA vGPU Software
[59] https://docs.nvidia.com/vgpu/latest/grid-licensing-user-guide/intro-to-grid-licensing.html — Introduction to NVIDIA vGPU Software Licensing
[61] https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-gpus.html — Supported GPUs — NVIDIA Multi-Instance GPU User Guide
