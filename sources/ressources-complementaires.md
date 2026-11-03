# Ressources complémentaires — lecture critique, pas collection de dumps

Ce dossier est **indépendant de NVIDIA**. Il accompagne les cours français, pas un programme commercial ni une promesse de certification. Les pages ci-dessous ont réellement été récupérées en HTTP 200 et leur contenu pertinent lu pour ce travail. Les numéros renvoient au registre partagé et à des extraits d’appui vérifiés ; la date de consultation est celle du registre. Les contenus et prix peuvent évoluer après cette consultation.

**Politique de sélection.** Lire en priorité le programme public, puis les documents qui expliquent une notion précise. Une page personnelle peut établir que son auteur **déclare** avoir utilisé une méthode ; elle ne prouve pas que cette durée, ce résultat ou ce sujet seront les tiens. Aucun examen divulgué, dump, compte rendu de question confidentielle, capture de cours payant ou corrigé acheté n’a été copié dans ces supports.

## 1. La hiérarchie à utiliser

| Niveau | Pour quelle question ? | Limite |
|---|---|---|
| NVIDIA — page de certification | Périmètre, pondérations, durée, langue, parcours recommandé | Reconsulter avant inscription ; ne pas compléter une information absente par une rumeur.[1] |
| NVIDIA — documentation technique | Rôle d’un outil, signification de métriques, support d’un produit | Une page `latest` n’est pas la documentation de toutes les versions.[38][39][40] |
| Documentation primaire hors NVIDIA | Fonctionnement de Kubernetes, Docker, Slurm ou Python | Les principes du projet ne garantissent pas une question d’examen sur chaque option.[27][51][53] |
| Guides indépendants | Autre explication, carte mentale, préparation personnelle | Contrôle humain, exactitude et actualité variables.[30][31][32] |
| Témoignage de candidat | Habitudes, erreurs ressenties, organisation | Expérience individuelle, pas statistique de réussite.[35] |

**Recoupement obligatoire.** Une affirmation sur les objectifs se vérifie sur NVIDIA.[1] Une affirmation matérielle chiffrée se vérifie pour le produit concerné, pas dans un tableau communautaire générique.[16][61] Le partage d’un lien par NVIDIA n’est pas une délégation de l’autorité sur les règles d’examen à son auteur.

## 2. Six pages indépendantes réellement examinées

### A. ziash — dépôt GitHub de préparation NCA-AIIO

**Type et accès.** Dépôt communautaire public, page d’accueil lue en HTTP 200. Il organise trois domaines, des notes de terrain et une partie pratique ; il se déclare indépendant et annonce des questions originales sans dumps.[30] Ces déclarations sont celles du dépôt, pas un audit intégral de chaque fichier.

**À en tirer.** Une manière d’organiser ses propres notes par domaine et de relier produits, usages et terrain. Le découpage 38/40/22 de sa page d’accueil concorde avec le programme officiel consulté.[30][1]

**Vigilance.** Le README annonce aussi des captures provenant du cours officiel.[30] Une licence déclarée sur un dépôt ne démontre pas à elle seule les droits de redistribution sur toutes les captures tierces. Ce cours ne reprend ni ces captures ni des extraits de formation payante. Privilégier ses propres schémas et les liens publics.

**Évaluation pédagogique.** Utile comme index secondaire ; ne pas le considérer comme une source normative de compatibilité ou comme une banque d’examen authentique. À ouvrir pour une lacune identifiée, pas pour recopier tout le dépôt.

### B. mgonzalezo — certifications NVIDIA infrastructure

**Type et accès.** Dépôt public avec guides Associate/Professional, cartes Anki et pistes de labs ; page d’accueil lue en HTTP 200.[31] L’auteur déclare avoir réussi NCA-AIIO et NCP-AII et mentionne sa contribution à un simulateur de datacenter.[31] Son identité de candidat et ses résultats ne sont pas authentifiés indépendamment par notre travail.

**À en tirer.** L’idée de réviser brièvement et régulièrement et de conserver des cartes de confusion. Son conseil de travail Anki sur plusieurs semaines est une recommandation personnelle, non une norme NVIDIA.[31]

**Vigilance.** Le dépôt mélange deux niveaux de certification et présente des références de commandes et de dépannage beaucoup plus approfondies côté Professional.[31] Ne pas transformer cette profondeur en liste obligatoire pour l’Associate. Les promesses du type « tout ce qu’il faut pour réussir du premier coup » restent des formulations de l’auteur, pas des garanties. Les pistes cloud ne sont pas exécutées dans notre cours.

**Évaluation pédagogique.** Utile pour la structure et la répétition ; attention au déplacement du périmètre. Comparer toute priorité aux objectifs officiels NCA-AIIO plutôt qu’aux pondérations d’une autre certification.[1]

### C. Certification Study Library — cterpening

**Type et accès.** Guide indépendant sur GitHub Pages, lu en HTTP 200. Le site indique explicitement une assistance IA et un contrôle humain encore en attente.[32] Il affirme avoir réalisé des vérifications de sources/objectifs et des tests locaux ; notre consultation ne reproduit pas ces tests et ne les compte pas comme les tests de ce cours.

**À en tirer.** Le chemin de raisonnement « besoin → ressources → chemins → exploitation → preuve » et l’insistance sur les commandes non destructives sont utiles pour éviter les réponses par nom de produit.[32]

**Vigilance.** La page contient des détails de versions et des activités proposées : ils vieillissent et ne doivent pas être présentés comme exécutés chez le lecteur. Son avertissement de ne pas lancer stress, reset, firmware ou partitionnement sans validation est pertinent comme discipline, mais la présence d’un exemple de commande ne confère aucun droit d’accès.[32]

**Évaluation pédagogique.** Bon support de couverture et de raisonnement si chaque détail opérationnel est revalidé dans la documentation de la version installée.[38][39][40] Son état de revue est transparent ; il ne faut pas remplacer « revue humaine en attente » par « certifié exact ».

### D. HowToAI — guide et aide-mémoire NCA-AIIO

**Type et accès.** Article indépendant, lu en HTTP 200. Il combine guide gratuit, glossaire, quiz et propositions de préparation supplémentaires.[33] Nous avons évalué le texte public, pas acheté de formation ni reproduit les questions.

**À en tirer.** Sa recommandation de chercher la contrainte d’un scénario et de comprendre le problème résolu par chaque technologie constitue un bon exercice de lecture. Ses tableaux de domaines reprennent les proportions officielles.[33][1]

**Vigilance précise.** Le texte propose un repère de préparation à 80 % ; c’est **une recommandation du site**, pas un seuil de passage officiel.[33] Sa formule raccourcie « jusqu’à sept instances MIG » exige un contexte de produit : la table NVIDIA distingue notamment A30 à quatre et certains H100 à sept.[33][61] Nous ne reprenons pas ses raccourcis comme règles universelles.

**Évaluation pédagogique.** Aide-mémoire secondaire, à utiliser avec une colonne « conditions et exceptions ». Ne pas convertir ses conseils sur le barème, les pourcentages de préparation ou l’interface en règles d’examen sans source officielle.

### E. NicheeLab — panorama NCA-AIIO

**Type et accès.** Article éditorial indépendant, lu en HTTP 200, présentant programme, conseils, technologies et estimations de préparation.[34]

**À en tirer.** Une vue panoramique des familles de ressources et une invitation à raisonner sur le profil initial. Ses fourchettes de durée sont attribuées à des retours communautaires sans que nous disposions ici d’un échantillon contrôlé ; elles ne sont pas reprises comme estimation démontrée pour Achraf.[34]

**Désaccords vérifiés.** La mention limitant MIG à A100/H100 est trop restrictive au regard de la liste officielle consultée, qui comprend notamment A30 et d’autres produits.[34][61] La page donne également des proportions de formats de questions et parle d’une évolution de contenu en 2026 ; nous n’avons pas établi ces annonces dans le programme officiel consulté et ne les utilisons pas pour prédire le contenu.[34][1]

**Évaluation pédagogique.** À parcourir avec prudence, pas à mémoriser. La règle « lire le modèle et la table officiels » prime sur un raccourci éditorial.[61] Les affirmations de valeur salariale ou de renouvellement automatique par une autre certification ne sont pas validées par notre travail et ne fondent aucune décision ici.

### F. Eason Tech Talk — récit de préparation et de réussite

**Type et accès.** Témoignage personnel intitulé « How I Passed NVIDIA NCA-AIIO in 16 Hours », lu en HTTP 200.[35] L’auteur déclare une pratique professionnelle des grands clusters GPU et précise que sa durée ne doit pas être généralisée.[35]

**À en tirer.** Transformer les mauvaises réponses en notes de confusion, puis vérifier les réponses générées par IA sur des documents officiels ; sa page distingue explicitement expérience personnelle et durée typique d’un parcours.[35] Ce sont des habitudes proposées, pas des résultats mesurés pour tous les candidats.

**Vigilance.** Ne pas recopier sa liste de « sujets faciles à confondre » comme une liste de questions rencontrées ou promises. Ses mentions de formation et de pratique tierces n’impliquent ni accès gratuit vérifié pour nous ni obligation d’achat. Sa discussion de MIG doit rester rattachée aux produits/profils officiels.[35][61]

**Évaluation pédagogique.** Témoignage utile pour l’organisation d’un candidat expérimenté, **pas** justification d’un plan de 16 heures pour un débutant. Le présent cours retient 36–48 h comme budget adaptable et non comme promesse.[35]

## 3. Documents primaires hors NVIDIA — quatre apports concrets

Ces projets ne sont pas des sources officielles de politique d’examen NVIDIA. Ils sont en revanche les éditeurs de leurs propres documentations techniques.

| Ressource récupérée | Pourquoi la lire | Apport vérifié | Limite d’utilisation |
|---|---|---|---|
| Kubernetes — Overview | Comprendre état désiré, contrôleurs, placement et services | Plateforme de gestion déclarative de charges conteneurisées ; demandes CPU/RAM et état désiré explicités.[51] | Ne prouve pas qu’un GPU est utilisable sans pile et plugins appropriés.[40] |
| Docker — What is a container? | Comparer conteneur et VM | Conteneurs comme processus isolés et partage du noyau ; VM avec son noyau.[53] | Les slogans de portabilité ne doivent pas effacer les dépendances GPU de l’hôte.[40] |
| SchedMD — Slurm Overview | Lire allocation, file et jobs sans apprendre des commandes destructives | Trois fonctions : attribuer les ressources, exécuter/suivre et arbitrer la file.[27] | Ne prédit pas la politique d’un site ni ses quotas, plugins ou priorités. |
| Python — statistics | Vérifier ce que calcule une moyenne | Définition de la moyenne arithmétique et fonctions associées.[54] | Une moyenne correcte ne répare pas des valeurs absentes transformées à tort en zéros.[39] |

IBM fournit en complément une introduction substantielle aux concepts ML, à la distinction apprentissage/généralisation, aux paradigmes et à l’optimisation ; elle sert aux définitions de base, pas à déterminer les questions de l’examen.[48]

## 4. Recoupements techniques retenus sur NVIDIA

| Sujet rencontré chez des tiers | Source primaire retenue | Conséquence pour les supports |
|---|---|---|
| « Combien d’instances MIG ? » | Introduction MIG et table des GPU supportés.[44][61] | Nombre et support toujours rattachés au modèle ; ne pas généraliser sept. |
| « GPU Operator fait tout » | Documentation GPU Operator et principes Kubernetes.[40][51] | Distinguer gestion de pile GPU, orchestration et scaling applicatif. |
| « Mémoire pleine = GPU bien utilisé » | Définitions `nvidia-smi`.[39] | Distinguer activité GPU, activité mémoire et quantité mémoire occupée. |
| « DCGM = gestionnaire de file » | DCGM Feature Overview.[38] | Replacer télémétrie/santé/diagnostic dans leur couche ; ordonnanceur séparé. |
| « Ajouter du calcul résout le stockage » | Article NVIDIA sur l’extension du stockage.[6] | Examiner capacité **et** performance du chemin des données. |
| « TensorRT et Triton sont le même outil » | TensorRT et documentation Triton.[3][60] | Distinguer optimisation/exécution d’un modèle et couche de service. |
| « Un DPU est juste un CPU/GPU de plus » | Analyse NVIDIA BlueField.[12] | Identifier la fonction d’infrastructure déchargée, accélérée ou isolée. |

Les articles techniques historiques expliquent des principes dans leur contexte de publication ; leurs débits ou exemples matériels ne sont pas transformés en caractéristiques actuelles universelles.[6][12][19] Les résumés générés par IA présents en haut de certains blogs NVIDIA n’ont pas servi de substitut à la lecture du corps de l’article.

## 5. Méthode de consommation des ressources

1. **Partir d’une difficulté.** Par exemple : « je confonds ordonnanceur et outil de monitoring », pas « je dois lire tous les guides ».
2. **Lire une explication secondaire courte**, puis reformuler sans copier son paragraphe.
3. **Ouvrir la source primaire** et noter les conditions : version, produit, environnement, champ ou unité.
4. **Écrire un contre-exemple.** Par exemple une inférence par lots, un GPU compatible MIG ayant un autre maximum, ou un job en attente malgré une capacité totale non nulle.[60][61][27]
5. **Produire sa propre preuve.** Schéma, comparaison, réponse originale ou résultat CPU réellement exécuté ; ne pas ajouter un journal GPU inventé.
6. **Limiter le temps.** Un retour de candidat ou guide tiers aide à organiser ; il ne doit pas absorber tout le budget du domaine faible.

## 6. Limites explicites de cette évaluation

- Le contrôle porte sur les pages publiques décrites et leurs passages pertinents, pas sur un audit exhaustif de chaque dépôt, cours, archive ou quiz externe.
- Aucune réussite déclarée par un auteur n’a été authentifiée ; aucune durée de préparation communautaire n’est une garantie.
- Aucun contenu payant n’a été acheté, extrait ou recopié. Aucun quiz externe n’est présenté comme une banque officielle ou comme des questions réelles.
- Aucune inscription, vérification d’identité, installation de navigateur sécurisé ou réservation n’a été effectuée.
- Les informations du programme doivent être recontrôlées auprès de NVIDIA avant décembre ; ce dossier ne crée ni date d’examen ni note minimale officielle.[1]

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
[3] https://developer.nvidia.com/tensorrt — NVIDIA TensorRT
[6] https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing — NVIDIA: Scaling Storage for AI Training and Inferencing
[12] https://developer.nvidia.com/blog/offloading-and-isolating-data-center-workloads-with-bluefield-dpu — Offloading and Isolating Data Center Workloads with NVIDIA Bluefield DPU | NVIDIA Technical Blog
[16] https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html — Introduction to NVIDIA DGX H100/H200 Systems — NVIDIA DGX H100/H200 User Guide
[19] https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io — Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog
[27] https://slurm.schedmd.com/overview.html — Slurm Workload Manager - Overview
[30] https://github.com/ziash/nvidia-nca-aiio-study-guide — GitHub - ziash/nvidia-nca-aiio-study-guide: Comprehensive NCA-AIIO exam prep: study notes, diagrams, screenshots, and field experience for the NVIDIA Certified Associate: AI Infrastructure and Operations certification. · GitHub
[31] https://github.com/mgonzalezo/nvidia-ai-infra-certs — GitHub - mgonzalezo/nvidia-ai-infra-certs: Everything you need to pass the NVIDIA NCP-AII and NCA-AII certifications: study guides, exam tips, practice questions, and real-world troubleshooting scenarios for GPU clusters, NVLink, DCGM, and AI infrastructure at scale. · GitHub
[32] https://cterpening.github.io/certification-study-library/guides/NCA-AIIO-nvidia-ai-infrastructure-operations-associate — NVIDIA-Certified Associate: AI Infrastructure and Operations (NCA-AIIO) Study Guide - Certification Study Library
[33] https://howtoai.com/nca-aiio-study-guide — NCA-AIIO Study Guide 2026: Domains, Cheat Sheet, Free Prep
[34] https://nicheelab.com/en/articles/nvidia/aiio-overview — NVIDIA-Certified Associate: AI Infrastructure & Operations (NCA-AIIO) Guide (2026)
[35] https://easontechtalk.com/nvidia-nca-aiio-exam — How I Passed NVIDIA NCA-AIIO in 16 Hours: Study Plan and 7 Exam Topics | Eason Tech Talk
[38] https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html — NVIDIA DCGM Feature Overview
[39] https://docs.nvidia.com/deploy/nvidia-smi/index.html — NVIDIA System Management Interface
[40] https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html — NVIDIA GPU Operator Overview
[44] https://docs.nvidia.com/datacenter/tesla/mig-user-guide/introduction.html — NVIDIA MIG User Guide Introduction
[48] https://www.ibm.com/think/topics/machine-learning — IBM: What is machine learning?
[51] https://kubernetes.io/docs/concepts/overview — Overview | Kubernetes
[53] https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container — What is a container? | Docker Docs
[54] https://docs.python.org/3/library/statistics.html — statistics — Mathematical statistics functions — Python documentation
[60] https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html — NVIDIA Triton Inference Server — NVIDIA Triton Inference Server
[61] https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-gpus.html — Supported GPUs — NVIDIA Multi-Instance GPU User Guide
