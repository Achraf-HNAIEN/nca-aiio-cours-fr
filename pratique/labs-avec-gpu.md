# Avec GPU — observations optionnelles, en lecture seule

**Objectifs : E08, I05/I07/I09, O01/O03/O04.** Ce fichier est un guide d’observation. **Aucune des commandes GPU ci-dessous n’a été exécutée pour produire le cours ; aucune sortie matérielle n’est revendiquée.** Les seules exécutions réalisées concernent les fonctions CPU testées dans [labs-sans-gpu.md](labs-sans-gpu.md).

## 1. Prérequis, périmètre et arrêt sûr

Utiliser uniquement une machine NVIDIA que tu es autorisé à consulter. Pour le parcours proposé : hôte **Linux**, pilote NVIDIA fonctionnel et `nvidia-smi` déjà installé et visible dans `PATH`. Aucun environnement Windows, WSL, VM, conteneur ou GPU loué n’est supposé équivalent. Depuis un conteneur, la visibilité peut être limitée ; demander à l’administrateur quel périmètre est réellement exposé plutôt que lancer un conteneur privilégié.

Pour DCGM : logiciel et service déjà installés, version supportée par la combinaison GPU/pilote/OS du site, et autorisation de lecture. Ne pas installer DCGM, démarrer son service ou modifier un groupe pour suivre ce guide. Les capacités de DCGM varient selon les produits et fonctions ; une interface disponible ne garantit pas tous les champs.[38]

**Versionnement.** Les références consultées sont les documentations publiques en ligne récupérées pour ce cours ; ce ne sont pas des garanties pour toutes les versions installées. Relever la version de l’outil avant de choisir les commandes, utiliser l’aide locale, puis ouvrir la documentation de **cette version** si une option diffère. La documentation `nvidia-smi` dit explicitement que certains appareils/environnements ne supportent pas toutes les informations et emploient `N/A`.[39] Les tables MIG indiquent les GPU et limites par produit ; elles ne dispensent pas de vérifier les profils et la configuration du site.[61]

**Ne pas continuer** si le matériel n’est pas visible, si les droits manquent ou si un outil annonce une incompatibilité. Ne pas résoudre cela par `sudo`, un téléchargement de pilote ou une configuration du cluster. Noter le message et demander au responsable. La lecture peut révéler des identifiants d’infrastructure : anonymiser UUID, nom d’hôte et numéros de série dans un compte rendu public.

## 2. Inventorier l’outil et les périphériques visibles

**Portée :** `nvidia-smi` installé, options présentes dans son aide locale. **Effet attendu :** affichage sur le terminal seulement.[39]

```bash
nvidia-smi --version
nvidia-smi -L
nvidia-smi --help-query-gpu
```

- `--version` permet de relever la version de l’outil ; conserver ce résultat dans les notes personnelles.
- `-L` inventorie les GPU exposés avec leurs identifiants ; l’index n’est pas une identité stable à supposer entre redémarrages.[39]
- `--help-query-gpu` permet de vérifier les champs de requête **réellement acceptés** avant de recopier la commande suivante.[39]

**Livrable personnel.** Tableau outil/version, GPU/modèle, UUID anonymisé et contexte d’exécution (hôte ou environnement restreint). Si aucune ligne n’apparaît, ne pas inventer un modèle ni un nombre de GPU. L’inventaire ne mesure pas un débit applicatif.

## 3. Lire un instantané de métriques

**Précondition supplémentaire :** chaque champ suivant figure dans l’aide de la version installée. Retirer un champ seulement après avoir compris qu’il est absent de cette version ; documenter cette adaptation. Conserver d’abord les unités et l’en-tête.[39]

```bash
nvidia-smi --query-gpu=uuid,name,memory.total,memory.used,utilization.gpu,temperature.gpu,power.draw --format=csv
```

Les options `csv`, `noheader` et `nounits` sont documentées, mais ici on conserve en-tête et unités pour éviter de confondre quantité de mémoire, pourcentage, température et puissance.[39] Un champ peut être `N/A` même si la requête elle-même réussit. Ce n’est ni zéro ni la preuve d’une panne.[39]

**Questions à résoudre.** Quel périphérique et quelle période sont observés ? Quelle unité est affichée ? Quelle proportion des champs est disponible ? Une mémoire occupée importante démontre-t-elle une activité de calcul élevée ? Non : ce sont des métriques distinctes.[39]

**Échantillonnage prudent.** Sur une machine autorisée et sans modification de la charge, répéter manuellement cet instantané à quelques moments connus. Ce fichier ne propose aucune boucle infinie ni collecte sur un parc entier. Ne pas transformer les observations d’une charge de production en fichier public contenant des identifiants sensibles.

## 4. Distinguer activité et mémoire utilisée

**Portée :** types d’affichage `-d` disponibles dans la version de `nvidia-smi`, GPU supporté. **Effet :** interrogation seulement.[39]

```bash
nvidia-smi -q -d MEMORY,UTILIZATION
```

Dans la documentation consultée, l’utilisation GPU est la part de la fenêtre d’échantillonnage durant laquelle un ou plusieurs kernels s’exécutent. L’utilisation mémoire rapporte l’activité de lecture/écriture pendant une fenêtre, pas simplement la part de capacité allouée.[39] Interpréter ces indicateurs avec le travail réellement lancé et sa phase, sans utiliser un pourcentage élevé comme preuve de performance idéale.

**Livrable personnel.** Trois colonnes : métrique, unité, ce qu’elle ne prouve pas. Si tu connais seulement une sortie unique, écris « instantané » ; ne l’appelle pas « moyenne sur une heure ».

## 5. Observer température, puissance et erreurs exposées

**Portée :** champs et types supportés ; certaines cartes/environnements ne présentent pas les mêmes compteurs. **Effet :** interrogation ; pas de diagnostic actif, pas de réglage.[39]

```bash
nvidia-smi -q -d TEMPERATURE,POWER,ECC
```

L’objectif est d’identifier les informations présentes, leur unité et leur portée temporelle, pas d’inventer un seuil universel. Les limites et explications d’un produit ne sont pas forcément celles d’un autre.[39] Pour les métriques DCGM, les catégories de surveillance, santé, statistiques et ralentissements sont détaillées dans sa documentation.[38]

**Pièges.** Un nombre d’erreurs corrigées n’est pas le même signal qu’une erreur non corrigée ; un code d’événement n’est pas un décompte d’incidents. Une température unique sans modèle, charge, référence et limites ne prouve pas une défaillance.[38][39] Documenter et faire valider l’investigation plutôt que modifier les fréquences ou la limite de puissance.

## 6. Lire une topologie, sans changer le fabric

**Portée :** commande de topologie présente, visibilité des périphériques suffisante. Certaines informations dépendent de l’accès au système et de l’environnement.[39]

```bash
nvidia-smi topo -m
```

La documentation donne une matrice des chemins et affinités avec des codes comme `SYS`, `PHB`, `PIX` et `NV#` ; lire **la légende de la sortie et de la version installée**, pas une valeur de benchmark.[39] Un chemin NVLink, un passage par PCIe et un chemin traversant des domaines NUMA ne sont pas une simple étiquette « tous les GPU sont connectés pareil ».[39]

**Livrable personnel.** Choisir une paire de périphériques visible et décrire le trajet indiqué. Expliquer ensuite pourquoi cette carte ne démontre ni le débit réseau inter-nœuds ni le temps d’un AllReduce. Les bibliothèques et réseaux de communication sont des couches complémentaires de l’interconnexion physique.[19]

## 7. Découvrir DCGM, uniquement s’il est déjà en service

**Prérequis renforcés :** `dcgmi` et le service associé sont déjà disponibles dans l’environnement autorisé ; vérifier l’aide locale et la documentation correspondante. Ne pas créer de groupe et ne pas démarrer de service pour contourner une erreur.

```bash
dcgmi --help
dcgmi discovery -l
```

La documentation consultée utilise `dcgmi discovery -l` pour lister les GPU supportés visibles ; elle précise que l’énumération par défaut porte sur les GPU actifs.[38] Comparer le périmètre à l’inventaire `nvidia-smi` sans supposer qu’une différence signifie automatiquement une panne. Une absence peut exiger une vérification de visibilité, version ou état par l’administrateur.

**Pas de diagnostic actif ici.** DCGM propose aussi configuration, politiques et diagnostics ; l’existence de ces fonctionnalités ne rend pas leur lancement non intrusif.[38] Ce guide s’arrête à la découverte et à la lecture.

## 8. Observer MIG sans partitionner

Aucune commande d’activation ni de création d’instance n’est fournie. Si le GPU est déjà partitionné et que l’inventaire expose des instances, noter leur présence et ouvrir la documentation du produit avec l’administrateur. MIG organise des ressources et chemins mémoire isolés sur des GPU compatibles ; les maxima dépendent du produit.[44][61]

**Exemple documentaire, non exécuté :** la table officielle donne quatre instances maximales sur A30 et sept sur certains H100.[61] Cela ne prouve pas qu’une instance particulière est disponible sur la machine observée, ni que l’on peut modifier sa configuration sans interrompre des travaux. Ne pas déduire le profil à partir de la seule quantité de mémoire agrégée.

## 9. Ce que ce guide exclut explicitement

Aucune installation, mise à jour de pilote/firmware, commande de reset, modification de fréquences ou puissance, changement de mode MIG, suppression/création d’instance, stress test ou soumission de job. Aucun `kubectl apply`, lancement de conteneur, `sudo` ou achat cloud. Aucun export automatique de télémétrie de production. Ces actions ne sont pas des lectures et sortent de l’autorisation de ce parcours.

La réussite de la préparation n’exige pas de posséder un GPU. Les [six labs CPU](labs-sans-gpu.md) sont la voie réellement exécutée pour le cours ; les présentes commandes restent des exemples documentés, optionnels et non vérifiés sur ton matériel.

## Sources

[19] https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io — Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog
[38] https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html — NVIDIA DCGM Feature Overview
[39] https://docs.nvidia.com/deploy/nvidia-smi/index.html — NVIDIA System Management Interface
[44] https://docs.nvidia.com/datacenter/tesla/mig-user-guide/introduction.html — NVIDIA MIG User Guide Introduction
[61] https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-gpus.html — Supported GPUs — NVIDIA Multi-Instance GPU User Guide
