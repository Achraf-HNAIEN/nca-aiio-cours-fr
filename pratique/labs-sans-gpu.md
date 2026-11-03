# Six labs sans GPU — Python standard uniquement

**Objectifs : E02/E07, I01/I02/I05/I07, O02/O03.** Ces activités sont originales, non officielles et sans questions d’examen reproduites. Elles font pratiquer des raisonnements du programme public, pas une simulation fidèle d’un centre de données.[1]

## Contrat de sécurité et de reproductibilité

- Interpréteur **Python 3.9 ou supérieur**, bibliothèque standard uniquement : aucune installation pip, aucun téléchargement ni compte cloud requis.
- Script complet : [`../tools/labs_cpu.py`](../tools/labs_cpu.py). Il ne lance pas de commande système, n’accède à aucun GPU, n’ouvre aucune connexion réseau et n’écrit pas de fichier. La seule sortie normale va sur le terminal.
- Les jeux de données sont des listes minuscules et un CSV synthétique inclus dans le script. Le « milliard de paramètres » du lab 2 est un **nombre utilisé dans un calcul**, pas une allocation de mémoire ni un modèle téléchargé.
- L’entraînement du lab 1 comprend 200 itérations scalaires. Les autres labs calculent sur quelques nombres. Aucun stress test ni balayage de l’hôte n’est réalisé.
- Le nom « GPU » dans les fixtures est fictif. Les labs 2 à 6 sont des modèles, des transformations de données ou des simulations pédagogiques sur CPU, pas des mesures de GPU, de stockage ou de réseau réels.

Depuis la racine du cours, commandes reproductibles **à exécuter par le lecteur** :

```bash
python3 tools/labs_cpu.py --test
python3 tools/labs_cpu.py all
python3 tools/labs_cpu.py 1
```

Le premier appel lance les tests, le second affiche les six résultats en JSON et le troisième affiche le lab 1. Les six choix numériques sont 1 à 6. `--help` décrit cette interface. L’entrée garantie par ce guide est `python3 …` : l’exécution directe par `./…` dépend des permissions du fichier et n’est pas revendiquée comme testée.

## Ce qui a effectivement été exécuté — à distinguer des exemples

Les six fonctions ont été exécutées via `python3 tools/labs_cpu.py --test` : **six tests réussis, `OK`, code de sortie 0**. La validation d’intégration est conservée dans le [journal final](../quality/tests-final.txt). Les résultats ci-dessous sont des **propriétés vérifiées par les assertions réellement passées**, pas une sortie reconstruite pour imiter un terminal.

L’intégration a aussi exercé l’affichage CLI par défaut ; la [revue indépendante](../quality/revue-supports.md) et son [journal d’exécution](../quality/support-audit-evidence.json) documentent les sélecteurs `all` et 1–6. Aucune commande GPU du fichier voisin n’a été exécutée. Lancer le script avec `python3` ; aucune permission d’exécution directe n’est requise.

| Lab | Résultat réellement vérifié | Ce que cela ne prouve pas |
|---|---|---|
| 1 — training | Erreur finale < 10⁻¹⁰ ; prédiction x=4 proche de 8 à cinq décimales ; poids inchangé en inférence | Aucune qualité sur des données réelles ni généralisation statistique |
| 2 — memory_budget | Poids = 2 000 000 000 octets ; conversion en GiB et marge vérifiées ; total < 8 GiB | Aucune réservation ni garantie de tenir sur un vrai GPU |
| 3 — pipeline | Modèle séquentiel = 12,5 lots/s ; recouvrement idéal = 20 lots/s ; limite = stockage | Aucun temps mesuré sur disque, CPU ou GPU |
| 4 — allreduce | Somme [4, 6] ; moyenne [2, 3] ; résultat distribué à deux répliques locales | Aucun paquet réseau ni appel NCCL |
| 5 — telemetry | GPU fictif A : moyenne 40 %, pic 1 200 MiB ; B : donnée absente conservée comme `None` | Aucun vrai GPU présent ou observé |
| 6 — placement | A et D placés au nœud 0, B au nœud 1, C en attente | Aucun job soumis à un ordonnanceur réel |

## Lab 1 — entraîner un petit modèle, puis l’utiliser

**Durée suggérée :** 15 à 25 minutes. **Commande lecteur :** `python3 tools/labs_cpu.py 1`.

**Question.** Quel élément change pendant l’entraînement mais pas pendant l’inférence ? Le modèle est `y = w × x`. Les exemples originaux sont `(1,2)`, `(2,4)`, `(3,6)`. Le poids commence à zéro. Le script calcule une erreur quadratique moyenne et effectue 200 mises à jour par descente de gradient. Il applique ensuite le poids à `x=4` sans mise à jour. La distinction entraînement/inférence suit le sens du ML décrit par IBM ; le calcul précis est notre exemple.[48]

**À observer.** Comparer `initial_mse`, `final_mse`, `prediction_x4`, `parameters_before_inference` et `parameters_after_inference`. Les deux derniers nombres sont égaux : produire une sortie n’est pas continuer l’apprentissage. Le test vérifie aussi que l’erreur a diminué.

**Interprétation.** Le calcul d’entraînement est réel, mais volontairement minuscule et sans biais à apprendre. Il n’est pas un réseau profond. Aucune validation indépendante n’est fournie : le point `x=4` illustre l’application de la règle apprise, pas une preuve suffisante de généralisation. Le sens de la généralisation est justement distinct de la performance sur les données d’entraînement.[48]

**Manipulation personnelle optionnelle.** Dans une copie locale du script, ajouter un exemple contradictoire ; expliquer pourquoi la perte ne tombe plus presque à zéro. Ne pas appeler toute erreur résiduelle un défaut matériel.

**Self-check (English).** *Does generating a prediction necessarily update the model parameters?* **Réponse :** non ; dans cette exécution l’inférence garde le même poids.[48]

## Lab 2 — estimer un budget mémoire sans allouer cette mémoire

**Durée suggérée :** 15 à 20 minutes. **Commande lecteur :** `python3 tools/labs_cpu.py 2`.

**Hypothèses pédagogiques explicites.** Un milliard de paramètres, deux octets chacun, 2 GiB d’état supplémentaire forfaitaire et 20 % de marge. Le script effectue `weight_bytes = parameters × bytes_per_parameter`, convertit en GiB en divisant par `1024**3`, puis calcule `(weight_gib + extra_gib) × (1 + margin)`.

**À observer.** `weight_bytes` vaut deux milliards. Les tests vérifient la conversion, la formule et un total inférieur à 8 GiB. Les dimensions invalides négatives ou nulles prévues par les tests sont refusées. Les hypothèses sont des entrées, pas des caractéristiques d’un modèle NVIDIA.

**Raisonnement.** La capacité mémoire du GPU et la croissance des besoins sont des contraintes distinctes de la seule puissance de calcul.[6] Ce lab montre aussi qu’un budget doit inclure plus que les poids. Il ne prétend pas calculer les activations d’un vrai réseau, l’optimiseur, les buffers, un cache KV, la fragmentation ou les contraintes d’un backend. Le terme `extra_gib` est une provision choisie, pas une formule universelle d’entraînement ou d’inférence.

**Variante à essayer dans une copie.** Doubler `parameters` puis réduire `bytes_per_parameter`. Déterminer ce qui change dans la formule ; ne pas en conclure qu’un vrai modèle conserve automatiquement sa qualité en précision réduite. La quantification est une technique d’optimisation qui doit être appliquée dans une pile appropriée.[3]

**Self-check (English).** *Does total cluster memory imply that one GPU can hold the whole model?* **Réponse :** non ; la mémoire locale et une utilisation multi-GPU supportée sont deux problèmes différents.[6]

## Lab 3 — trouver le goulet d’étranglement d’un pipeline

**Durée suggérée :** 20 minutes. **Commande lecteur :** `python3 tools/labs_cpu.py 3`.

**Données fictives.** Trois temps de service par lot : stockage 50 ms, préparation 20 ms, calcul 10 ms. Le modèle séquentiel utilise la somme ; le modèle en régime établi avec recouvrement parfait utilise le maximum. Il ignore amorçage, vidange, files, variance et conflits de ressources.

**Résultats vérifiés.** Le modèle strictement séquentiel donne 12,5 lots/s. Le recouvrement idéal donne 20 lots/s et le nom `storage` comme limite. Le test couvre aussi un cas où les trois temps sont égaux et un temps nul refusé. **Ce sont des résultats de calcul sur des entrées choisies, pas des mesures chronométrées de matériel.**

**Raisonnement.** Une extension du stockage doit traiter sa performance aussi bien que sa capacité ; l’article NVIDIA le souligne pour les charges IA.[6] Dans notre exemple seulement, le temps de calcul n’est pas l’étape la plus lente : accélérer cette étape seule ne supprime pas la limite des autres. Cela motive la mesure du chemin complet avant un achat.

**Variante pédagogique.** Donner 5 ms au calcul en gardant les autres valeurs : expliquer, avant de modifier une copie, pourquoi la limite du modèle recouvert reste le stockage. Donner ensuite 10 ms au stockage et identifier la nouvelle limite. Ne pas présenter ces valeurs comme des spécifications CPU/GPU.

**Self-check (English).** *Is the ideal overlapped throughput a measured performance guarantee?* **Réponse :** non ; il est conditionnel à des hypothèses volontairement idéales.

## Lab 4 — comprendre une réduction collective

**Durée suggérée :** 15 à 20 minutes. **Commande lecteur :** `python3 tools/labs_cpu.py 4`.

**Entrées locales.** Deux listes `(1,2)` et `(3,4)` représentent deux contributions de même poids. Le script additionne chaque position, divise par le nombre de contributions et crée deux copies du résultat. NCCL fournit de vraies communications collectives sur GPU ; ce lab en illustre seulement l’idée mathématique avec des listes.[19]

**Résultat vérifié.** La somme est `[4,6]`, la moyenne `[2,3]`, les deux répliques reçoivent `[2,3]`. Les listes vides et les tailles incompatibles sont refusées. Il n’y a ni workers réseau, ni processus distribués, ni synchronisation réelle.

**Pourquoi somme puis division ?** Une opération collective de somme et une moyenne ne sont pas la même opération. Nous choisissons des contributions égales ; un cas où chaque worker représente un nombre différent d’exemples nécessiterait une pondération appropriée. Le lab ne suppose aucune convention universelle de réduction de gradients dans les frameworks.

**Variante.** Ajouter une troisième contribution et vérifier que la longueur des vecteurs reste identique. Puis imaginer un participant manquant : noter ce que le modèle local ne représente pas, par exemple les délais et pannes de communication.

**Self-check (English).** *Did this lab benchmark NCCL or an InfiniBand fabric?* **Réponse :** non ; il démontre un calcul collectif fictif, pas son coût de communication.

## Lab 5 — traiter des métriques sans inventer des valeurs

**Durée suggérée :** 20 à 25 minutes. **Commande lecteur :** `python3 tools/labs_cpu.py 5`.

**Entrée incluse, explicitement synthétique :**

```csv
uuid,util_pct,used_mib
gpu-A,30,1000
gpu-A,50,1200
gpu-B,N/A,500
```

Ce schéma simplifié est conçu pour le lab ; il n’est pas présenté comme la sortie exacte d’une version de `nvidia-smi`. La documentation officielle distingue les champs, les formats CSV et les valeurs `N/A` non supportées.[39]

**Résultats vérifiés.** Pour A : moyenne d’activité de 40 % et pic de mémoire utilisée de 1 200 MiB. Pour B : `mean_util_pct = None`, un échantillon manquant, mémoire disponible dans la fixture. `None` se sérialise comme `null` dans le JSON. Les tests rejettent `NaN` et une utilisation supérieure à 100 ; un CSV avec en-tête seulement produit un résultat vide.

**Limites assumées.** Deux échantillons valides ne suffisent pas à caractériser un service ; la moyenne est ici non pondérée et il n’y a pas d’horodatage. Le parseur attend exactement les colonnes du lab ; ce n’est pas un importeur universel de logs. Mémoire utilisée et activité GPU restent deux signaux différents ; `N/A` ne doit pas devenir zéro dans la moyenne.[39] La fonction `statistics.mean` calcule la moyenne arithmétique des valeurs retenues.[54]

**Variante.** Remplacer le `N/A` par une valeur valide dans une copie ; vérifier la différence entre « donnée absente » et « activité réellement nulle ». Ne pas conclure que le GPU B est en panne à partir de son nom ou d’un seul champ.

**Self-check (English).** *Why should an unsupported utilization value not be replaced by zero?* **Réponse :** zéro affirmerait une activité mesurée nulle, ce que l’absence de donnée ne démontre pas.[39]

## Lab 6 — placement et fragmentation des ressources

**Durée suggérée :** 20 à 25 minutes. **Commande lecteur :** `python3 tools/labs_cpu.py 6`.

**Modèle original.** Deux nœuds fictifs, chacun avec deux slots et 8 GiB. Les jobs demandent respectivement A `(1 slot,6 GiB)`, B `(1,6)`, C `(1,4)`, D `(1,2)`. Un parcours first-fit essaie chaque job sur le premier nœud où il tient ; un job non placé reste en attente et le parcours continue. Les « slots » sont une ressource abstraite : ce n’est ni une déclaration CUDA ni un périphérique réellement réservé.

**Résultats vérifiés.** A est placé sur 0 ; B sur 1 ; C ne tient sur aucun nœud au moment de son examen ; D est placé sur 0. Il reste zéro slot et zéro GiB sur 0, un slot et 2 GiB sur 1. Le test couvre également la liste vide, une demande invalide et des noms de jobs dupliqués.

**Raisonnement.** Après A et B, les ressources restantes sont fragmentées entre nœuds : une somme globale de mémoire ne satisfait pas une demande qui doit tenir sur un nœud. Slurm alloue et arbitre de véritables ressources ; Kubernetes place également selon des demandes et des ressources disponibles, mais ni l’un ni l’autre n’est implémenté par notre algorithme.[27][51]

**Ce qui manque volontairement.** Pas de durée, de libération de ressources, de priorité, de quotas, de gang scheduling, de réseau, de topologie GPU, de multi-utilisateur ni de tolérance aux pannes. Le fait de continuer vers D ne représente pas une politique complète de backfill ni une garantie d’équité d’un vrai système.

**Variante.** Modifier l’ordre des jobs dans une copie et expliquer le changement éventuel de placement. Écrire ensuite une règle de priorité en français avant de la programmer : distinguer politique et mécanisme.

**Self-check (English).** *Does a pending job prove that its requested GPUs are defective?* **Réponse :** non ; la file et les contraintes de ressources doivent être examinées avant une conclusion matérielle.[27]

## Bilan de séance

Conserver la commande exécutée, le code retour et une phrase sur ce que l’activité démontre **et ne démontre pas**. Dans le cours, le fichier de preuves contient les résultats CPU réellement observés. Aucune sortie hypothétique de GPU n’y est mélangée. Pour la suite, lire les [commandes optionnelles en lecture seule](labs-avec-gpu.md), sans les exécuter sur un environnement partagé sans autorisation.

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
[3] https://developer.nvidia.com/tensorrt — NVIDIA TensorRT
[6] https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing — NVIDIA: Scaling Storage for AI Training and Inferencing
[19] https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io — Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog
[27] https://slurm.schedmd.com/overview.html — Slurm Workload Manager - Overview
[39] https://docs.nvidia.com/deploy/nvidia-smi/index.html — NVIDIA System Management Interface
[48] https://www.ibm.com/think/topics/machine-learning — IBM: What is machine learning?
[51] https://kubernetes.io/docs/concepts/overview — Overview | Kubernetes
[54] https://docs.python.org/3/library/statistics.html — statistics — Mathematical statistics functions — Python documentation
