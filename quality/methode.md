# Méthode de recherche, de rédaction et de contrôle

## Périmètre

Ce dépôt prépare les connaissances du programme public **NCA-AIIO**, pas une liste de questions réelles. Les identifiants E01–E08, I01–I10 et O01–O04 sont des repères pédagogiques locaux. La page officielle de certification sert à établir le périmètre et les poids ; les documentations techniques servent à expliquer les mécanismes.[1]

La consultation initiale est datée du **3 novembre 2026**. Les sources qui utilisent `/latest/` ou une page produit évolutive peuvent changer après la vérification. Les valeurs propres à un modèle de serveur, une génération de GPU ou une version logicielle ne doivent pas être généralisées à l'ensemble du catalogue.

## Collecte ciblée plutôt qu'aspiration complète

1. Récupérer la page officielle et ses objectifs, puis identifier les lectures recommandées.
2. Lire des documents NVIDIA et les documentations officielles des composants utiles au programme.
3. Examiner des guides indépendants et retours d'expérience, sans leur attribuer l'autorité du programme.
4. Enregistrer les URL dans un registre commun, les dates d'accès et des extraits brefs qui soutiennent les descriptions.
5. Rédiger une synthèse originale en français et citer les sources au fil du texte.

Le moteur d'extraction de pages configuré n'était pas disponible pour cette session. La collecte a donc utilisé des requêtes HTTP publiques et une extraction HTML locale. Une réponse HTTP 200 ne suffit pas : une page de connexion, un interstitiel ou une coquille JavaScript ne constitue pas la lecture d'un document. Le catalogue distingue l'enregistrement d'une URL, la lecture utile et les limitations d'accès.

Les textes intégraux téléchargés pour l'analyse restent dans un répertoire de travail exclu de Git. Ce dépôt redistribue des explications originales et de courts extraits justificatifs, pas une copie des formations ou des sites consultés. Aucun accès payant, compte tiers ou mécanisme de restriction n'a à être contourné.

## Répartition du travail

Les productions sont réparties entre agents aux périmètres distincts :

- Connaissances IA : fondamentaux, architectures, cycle de vie et écosystème.
- Infrastructure : calcul, stockage, réseau, DPU, datacenter et dimensionnement.
- Opérations : observabilité, orchestration, ordonnanceurs et virtualisation.
- Supports d'étude : planning, fiches, glossaire, labs et ressources complémentaires.
- Outils d'entraînement : quiz en terminal, quiz HTML autonome et tests.

Des agents de revue distincts relisent ensuite les productions et leurs sources. Les rapports de revue décrivent le périmètre réellement examiné, leurs constatations et les limites restantes ; ils ne sont pas assimilés à une certification NVIDIA. Le responsable d'intégration applique les corrections, exécute les contrôles et vérifie la publication distante.

## Critères de contrôle

### Couverture

- Les 22 objectifs locaux ont chacun un ou plusieurs chapitres correspondants.
- Chaque série de 50 questions couvre tous les objectifs.
- Chaque série respecte notre répartition pédagogique 19/20/11.
- Les questions et options sont en anglais ; les explications sont en français.

### Sources et technique

- Pas de référence inventée ou de conclusion fondée seulement sur une URL non lue.
- Distinguer CPU/GPU, entraînement/inférence, mémoire/stockage et débit/latence.
- Distinguer NVLink/NVSwitch, réseau inter-nœuds et exceptions propres aux architectures.
- Distinguer Ethernet, RoCE, InfiniBand, GPUDirect RDMA et fonction d'un DPU.
- Distinguer puissance IT, puissance du site, énergie, PUE et contraintes de refroidissement.
- Distinguer métrique observée, hypothèse de diagnostic et test permettant de la vérifier.
- Distinguer conteneur, VM, passthrough, vGPU et MIG, avec leurs conditions de compatibilité.

### Questions et corrigés

- Une réponse correcte non ambiguë par question.
- Des distracteurs plausibles accompagnés d'une explication.
- Pas de copie de questions d'examen protégées ou prétendument divulguées.
- Références techniques associées aux corrigés.
- Les résultats mesurent le travail sur cette banque pédagogique ; ils ne prédisent pas une réussite réelle.

### Outils et publication

- Tests des schémas, comptes, scores, répartitions et erreurs d'entrée.
- Génération du HTML depuis la banque réelle, sans fausses données de démonstration dans le livrable.
- Exécution des labs CPU et indication explicite des commandes GPU non exécutées.
- Contrôle des liens locaux et des références numériques.
- Vérification des fichiers suivis pour exclure secrets, comptes rendus privés de collecte et caches.
- Lecture du dépôt distant et comparaison du commit après push, avant de déclarer la livraison terminée.

Les résultats effectifs et les éventuelles réserves figurent dans [validation.md](validation.md). Cette liste décrit les critères à vérifier, pas une affirmation que chaque contrôle a déjà réussi.

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
