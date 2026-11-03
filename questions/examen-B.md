# Examen d’entraînement B

Questions originales non officielles. Aucun seuil officiel de réussite n’est supposé.
50 questions · 60 minutes · une seule réponse par question.

## Questions

### Question 1 — E-020

A retailer has customer behavior records but no predefined customer categories. It wants to discover groups of similar behavior. Which approach best fits?

- A. Unsupervised clustering
- B. Supervised regression to a known continuous target
- C. Supervised classification using customer categories that do not yet exist
- D. Reinforcement learning to choose actions, without a reward or interaction objective

### Question 2 — E-021

A simulated robot tries actions and receives rewards for completing a task safely. Which learning paradigm is most directly illustrated?

- A. Supervised regression from fixed input-output pairs only
- B. Reinforcement learning
- C. Unsupervised clustering of images only
- D. Inference without any learning objective

### Question 3 — E-022

A research group can now use optimized GPU libraries through a high-level framework instead of implementing every kernel itself. How does this support AI adoption?

- A. It proves that the group no longer needs data.
- B. It lowers the effort required to use accelerated computing in applications.
- C. It guarantees that every model will be accurate on every industry.
- D. It makes model-specific testing unnecessary because library kernels are optimized.

### Question 4 — E-023

A manager proposes buying faster GPUs to solve an AI pilot whose training data uses inconsistent labels. What is the best response?

- A. Approve the purchase because hardware speed guarantees correct labels.
- B. Improve data and evaluation quality; faster computation alone does not fix inconsistent targets.
- C. Stop recording labels because all AI is unsupervised.
- D. Increase model size until the inconsistent labels no longer need review.

### Question 5 — E-024

A software company wants an assistant that proposes source code from natural-language requests. Which model category is most directly relevant?

- A. An image classifier trained to recognize software logos
- B. A regression model that predicts software project duration
- C. A large language model capable of code generation
- D. A clustering model that groups existing code files by similarity

### Question 6 — E-025

An industrial team wants to develop a digital twin and simulate robotic activity before physical deployment. Which NVIDIA solution category most directly aligns?

- A. TensorRT used only to optimize an existing classifier
- B. A GPU driver as the complete simulation application
- C. NGC used only as a private artifact registry
- D. Omniverse libraries and microservices for physical AI and simulation

### Question 7 — E-026

Profiling shows that a GPU layer saturates the available device-memory bandwidth while its arithmetic units remain underutilized. No memory-capacity shortage is observed. What is the dominant limitation?

- A. The total memory capacity, even though no capacity shortage is observed
- B. Only the peak arithmetic rate
- C. Memory bandwidth
- D. Only the total persistent storage capacity

### Question 8 — E-027

GPU utilization is low because the host CPU cannot decode and prepare incoming images fast enough. Which action best targets the stated cause?

- A. Profile and improve the input preparation pipeline on the host.
- B. Buy more GPU arithmetic capacity without changing the pipeline.
- C. Remove the CPU because GPU servers never need one.
- D. Increase the inference batch size without checking whether host preparation can supply it.

### Question 9 — E-028

An offline inference job must score a large archive overnight. Individual requests have no interactive deadline, but all results must finish by morning. Which metric is most directly relevant to tuning batching?

- A. Only the fastest isolated response on an empty server
- B. Only the latency of the first result, regardless of when the archive finishes
- C. Only peak GPU arithmetic performance, without measuring completed predictions
- D. Sustained throughput sufficient to complete the workload within the available window

### Question 10 — E-029

A large generative model does not fit the intended inference configuration on one GPU. Which statement is most accurate?

- A. Inference can require multiple GPUs and must be sized for the model and service requirements.
- B. Inference is defined as CPU-only execution.
- C. Only training can ever require more than one GPU.
- D. A model becomes smaller automatically when an API is added.

### Question 11 — E-030

A team quantizes a trained model to reduce inference memory requirements. Which validation is necessary before production deployment?

- A. Recheck task quality and performance on the target hardware and representative inputs.
- B. Assume lower precision guarantees identical outputs and higher speed everywhere.
- C. Measure only the reduced model file size and skip task-quality testing.
- D. Skip compatibility checks because every GPU supports every numeric format.

### Question 12 — E-031

Why do AI frameworks often use optimized libraries such as cuBLAS and cuDNN?

- A. To replace all framework-level model construction and training logic
- B. To reuse accelerated computational building blocks instead of reimplementing every operation
- C. To replace the need for any trained model parameters
- D. To guarantee the business correctness of every prediction

### Question 13 — E-032

A Kubernetes administrator wants to automate installation and management of the supported NVIDIA GPU software stack across GPU nodes. Which component most directly fits?

- A. NVIDIA Triton Inference Server
- B. NGC Private Registry
- C. NVIDIA GPU Operator
- D. NVIDIA TensorRT execution engine

### Question 14 — E-033

A deployment fails before the model runs because the required GPU host driver is missing. At which layer should troubleshooting begin?

- A. The host system and GPU driver layer
- B. The model-serving request queue, before checking host dependencies
- C. The training hyperparameters, before checking host dependencies
- D. The model artifact registry access policy, despite the reported missing driver

### Question 15 — E-034

A speech team wants reproducible training and customization of automatic speech recognition models using pretrained checkpoints. Which NVIDIA framework most directly matches?

- A. A GPU device plugin by itself
- B. NeMo Framework
- C. Triton model instance configuration alone
- D. TensorRT used only to optimize a trained inference model

### Question 16 — E-035

A team needs a catalog of GPU-optimized software and a registry for sharing proprietary AI artifacts. Which NVIDIA service most directly addresses this?

- A. NVIDIA Triton Inference Server
- B. NVIDIA GPU Operator
- C. NVIDIA TensorRT runtime
- D. NGC

### Question 17 — E-036

A newly deployed model violates a required quality criterion. The previous model version and its execution configuration are available and validated. What is the most appropriate immediate release-control action?

- A. Delete the previous version before investigating.
- B. Keep the failing version solely because it is newer.
- C. Change the GPU driver and assume model quality is fixed.
- D. Roll back to the validated version while investigating the regression.

### Question 18 — E-037

A model was evaluated with normalized inputs, but the production API passes raw values with different scales. The hardware is healthy. Which issue should be investigated first?

- A. A guaranteed shortage of GPU cores
- B. The inference batch-size setting as the only possible cause
- C. The assumption that healthy hardware guarantees correct predictions for any input scale
- D. A mismatch between training/evaluation preprocessing and production preprocessing

### Question 19 — E-038

Months after deployment, customer behavior changes and model quality on recent examples declines, although service latency remains stable. What is the best next step?

- A. Assume the model is healthy because infrastructure latency did not change.
- B. Automatically overwrite model weights with every incoming request.
- C. Investigate data and quality changes, then decide whether controlled reevaluation or retraining is needed.
- D. Increase persistent disk capacity and skip all model evaluation.

### Question 20 — I-021

A training dataset is much larger than GPU memory, but all tensors required for one training step—including model parameters, optimizer state, gradients, activations, the current batch, and temporary buffers—fit together in usable GPU memory. Which conclusion is justified?

- A. The dataset can be processed in batches if the input path supplies them at an adequate rate.
- B. The complete dataset must reside in GPU memory at every training step.
- C. Persistent storage capacity is irrelevant once the model fits in GPU memory.
- D. The input path can be ignored because batch memory fits.

### Question 21 — I-022

A model is too large for one GPU. An engineer proposes placing a complete replica on each of four equally sized GPUs. What is the main flaw?

- A. The proposal automatically pools all four GPU memories for each unmodified replica.
- B. Adding persistent storage makes complete replicas fit in the original GPU memory.
- C. Each replica still has the original per-GPU memory requirement.
- D. Replication always reduces model weight size in each replica.

### Question 22 — I-023

A server specification lists multiple power supplies for redundancy. Why is summing their nameplate capacities not a reliable estimate of normal server consumption?

- A. Each supply always delivers its full rated power whenever connected.
- B. Redundant supply capacity and actual system load are different quantities.
- C. Redundant supplies eliminate all system power consumption.
- D. The number of supplies alone determines the annual PUE.

### Question 23 — I-024

A proposal offers the lowest GPU hourly rate but requires large recurring data transfers. What should the buyer do?

- A. Compare GPU hourly rates only because storage is a separate service.
- B. Assume recurring data transfers are free without checking the offer.
- C. Compare only peak GPU FLOPS while ignoring the planned usage period.
- D. Include transfer, storage, compute, and operational costs over the expected usage period.

### Question 24 — I-025

What is a primary purpose of an out-of-band management network in an AI cluster?

- A. Provide shared high-performance storage for all training checkpoints.
- B. Provide the primary application path for all GPU collective traffic.
- C. Provide controlled access to hardware-management interfaces such as BMC ports.
- D. Provide ordinary users unrestricted access to hardware-management ports.

### Question 25 — I-026

Which statement about liquid-cooled AI systems is most accurate?

- A. They eliminate the need for any facility heat rejection.
- B. They still require a validated heat-rejection path, compatible facility interfaces, and maintenance planning.
- C. They can use arbitrary facility fluids without equipment validation.
- D. They always eliminate all air cooling from every server component.

### Question 26 — I-027

A model-serving application runs independent replicas with little GPU-to-GPU communication. Which requirement should guide its network design first?

- A. A requirement for every replica to participate in per-request AllReduce operations.
- B. The actual request, response, data-access, and availability requirements of the service.
- C. Only local GPU peak bandwidth, without request or data-path evaluation.
- D. A full-rack NVLink domain solely because the service performs inference.

### Question 27 — I-028

Which description correctly classifies NCCL in an AI communication stack?

- A. An inter-node physical link standard that replaces InfiniBand and Ethernet.
- B. A GPU-to-GPU switching chip in an NVLink fabric.
- C. A mechanism that automatically pools all GPU memory into one allocation.
- D. A library providing GPU-oriented collective and other communication operations.

### Question 28 — I-029

A design review states, "NVLink can never connect GPUs beyond a single server chassis." Which response is most accurate?

- A. NVLink Switch is simply a conventional Ethernet IP router.
- B. All NVLink generations are restricted to one chassis by definition.
- C. Any GPUs with NVLink can be connected across arbitrary racks without platform validation.
- D. Some supported NVLink Switch scale-up domains span multiple nodes or trays; the exact boundary is architecture-specific.

### Question 29 — I-030

A team proposes moving the main neural-network training computation from GPUs to general-purpose DPU CPU cores to "offload AI." Which evaluation is best?

- A. This confuses application compute with the DPU role of accelerating and isolating suitable infrastructure work.
- B. Any move from a host processor to DPU cores guarantees faster application computation.
- C. DPU offload means the GPU model no longer requires working memory.
- D. A DPU should replace all CPU and GPU functions in an accelerated server.

### Question 30 — I-031

Two candidate servers have the same GPU count. One has a validated GPU-to-network topology for the required direct transfers. Why is GPU count alone insufficient for selection?

- A. The data path, adapter placement, and platform compatibility can affect communication performance.
- B. Only persistent storage capacity can influence direct GPU transfers.
- C. Equal GPU counts guarantee identical communication performance.
- D. A supported direct path removes every software and driver requirement.

### Question 31 — I-032

A project will add compute nodes next year. What is the best infrastructure planning action now?

- A. Plan GPU count alone and defer all supporting capacity until after installation.
- B. Plan expandable compute, storage, network ports, cabling, power, and cooling as a balanced system.
- C. Reserve storage capacity only, treating network and cooling as fixed unlimited resources.
- D. Assume existing shared uplinks scale automatically with node count.

### Question 32 — I-033

A facility report shows improved PUE while useful training throughput has fallen. Which interpretation is valid?

- A. PUE is another name for average GPU utilization.
- B. Lower PUE guarantees a higher number of completed training jobs.
- C. PUE alone does not measure useful AI work or training throughput.
- D. PUE alone establishes that the chosen model is more energy-efficient.

### Question 33 — I-034

A company owns its GPU servers but installs them in a commercial colocation facility. Which statement is correct?

- A. Using a colocation facility necessarily transfers equipment ownership to the facility operator.
- B. Customer-owned colocation hardware is necessarily billed as public-cloud instances.
- C. The equipment can remain customer-owned even though the facility is operated by a colocation provider.
- D. Locating hardware off-site automatically removes workload-management responsibilities.

### Question 34 — I-035

Why does an AI cluster need a coherent software and management layer in addition to GPU servers?

- A. Identical GPU models automatically create a working multi-user cluster.
- B. Nodes, access to data, provisioning, and job execution must be coordinated into an operational service.
- C. Management software replaces the physical compute and storage resources.
- D. An inventory of installed GPUs is sufficient to provision and schedule every workload.

### Question 35 — I-036

During maintenance planning, a technician proposes moving a heavy server without assistance because it fits in a standard rack. What is the best response?

- A. Use qualified personnel and appropriate mechanical or other assistance according to the equipment guidance.
- B. Removing the storage drives always makes any lifting method acceptable.
- C. Handle the server first and check the manufacturer handling guidance afterward.
- D. Standard rack dimensions prove that manual lifting without assistance is safe.

### Question 36 — I-037

Compute synchronization and high-volume storage reads compete on an undersized shared path. Which design change most directly addresses this contention?

- A. Increase per-GPU memory and assume that all storage traffic will disappear.
- B. Increase GPU count without changing the shared path.
- C. Increase storage capacity while leaving the congested path unchanged.
- D. Provision adequate fabric capacity and evaluate separation of compute and storage traffic.

### Question 37 — I-038

A team claims RDMA means that no CPU, driver, or memory setup is involved at any stage. Which correction is best?

- A. RDMA removes the need for compatible drivers once an Ethernet cable is present.
- B. RDMA requires every payload to pass through host application buffers.
- C. RDMA reduces work on the data path, but setup, memory registration, and software support still matter.
- D. RDMA support guarantees identical performance on every hardware topology.

### Question 38 — I-039

An organization already operates Ethernet and is considering a high-speed AI fabric. Which statement best compares Ethernet/RoCE with InfiniBand?

- A. Both can be relevant; compare validated end-to-end performance, congestion handling, integration, and operational capability.
- B. The fastest advertised port alone determines the better end-to-end solution.
- C. Ethernet cannot provide RDMA even with compatible RoCE components.
- D. Existing Ethernet operational experience makes all fabric validation unnecessary.

### Question 39 — I-040

A server supports GPUDirect RDMA with a compatible network adapter. Does this fact alone establish that the server contains a DPU?

- A. Yes; every adapter that accesses GPU memory directly is a programmable DPU.
- B. Yes; GPUDirect RDMA is simply the software name for BlueField hardware.
- C. No; a network adapter cannot participate in direct GPU-memory transfers.
- D. No; a direct GPU-memory data path and a DPU are different capabilities.

### Question 40 — O-012

A platform team wants Kubernetes automation for NVIDIA drivers, the GPU device plugin, container integration, and DCGM-based monitoring. Which product most directly addresses this requirement?

- A. The Kubernetes scheduler by itself
- B. The GPU device plugin by itself
- C. DCGM Exporter by itself
- D. NVIDIA GPU Operator

### Question 41 — O-013

A GPU is usable on the host and allocated to a container workload, but the container runtime has not been integrated with NVIDIA device support. Which component family should the administrator investigate?

- A. The amount of allocated framebuffer only
- B. The device plugin resource count only
- C. NVIDIA Container Toolkit and its runtime integration
- D. The scheduler queue priority only

### Question 42 — O-014

Using the documented Kubernetes extended-resource GPU mechanism, a container specifies a GPU limit but omits a GPU request. How does Kubernetes treat the GPU request?

- A. It uses the GPU limit as the request value
- B. It always defaults to zero, allowing unlimited overcommit
- C. It derives the request from current GPU utilization
- D. It asks DCGM Exporter to choose a request value

### Question 43 — O-015

A Kubernetes Pod requests a GPU and requires a particular accelerator label. It stays Pending although idle GPUs exist only on nodes without that label. Which explanation best fits?

- A. No currently available node satisfies both the resource and placement constraints
- B. DCGM Exporter must allocate one of the idle GPUs
- C. The presence of any idle GPU guarantees placement regardless of labels
- D. The Pod's model weights have necessarily corrupted the GPU driver

### Question 44 — O-016

After enabling MIG, an operator sees N/A for a utilization query in nvidia-smi on the deployed configuration. What is the best interpretation before raising an idle-GPU alarm?

- A. N/A proves that the GPU is consuming zero power
- B. The queried metric may be unsupported at that observation level or in that configuration
- C. MIG has removed all physical memory from the GPU
- D. N/A is equivalent to zero utilization in every NVIDIA tool

### Question 45 — O-017

A reliability review finds that an ECC error counter is nonzero. Which additional context is most useful before deciding how to respond?

- A. Whether errors are corrected or uncorrected, the counter's scope, and how it changes over time
- B. Only whether total GPU utilization is high
- C. Only whether the job received its requested GPU count
- D. Whether a single successful job can justify clearing all error history

### Question 46 — O-018

An operator compares a GPU's measured power draw with its configured power limit. Which statement is correct?

- A. Both values are cumulative job energy measurements
- B. The configured limit guarantees constant application throughput
- C. Power draw is observed consumption, while the limit constrains allowed power behavior
- D. The measured power draw directly reports the number of occupied memory bytes

### Question 47 — O-019

A team argues that no license obligations can apply because its NVIDIA vGPU software deployment does not check out a license from a server. What should the reviewer point out?

- A. Every use of bare-metal MIG automatically requires the same vWS license
- B. All passthrough deployments use identical software and licensing terms
- C. A successful GPU allocation by a scheduler automatically grants software usage rights
- D. Some documented vGPU software licensing modes are enforced through the EULA rather than a server checkout

### Question 48 — O-020

A proposed vGPU profile has enough framebuffer memory for an application. What must still be checked before declaring the deployment compatible?

- A. Only whether the host driver can list the physical GPU
- B. The supported GPU, profile, hypervisor and software versions, and required application features
- C. Only whether a different hypervisor supports a similarly named profile
- D. Only whether the required number of vGPUs can be allocated

### Question 49 — O-021

A design uses MIG-backed vGPUs on a supported platform. A reviewer says MIG and vGPU cannot be combined because they are competing names for the same feature. Which correction is best?

- A. MIG partitions physical GPU resources, while a supported vGPU stack can present those resources to VMs
- B. MIG-backed vGPU support on one hypervisor guarantees support on every hypervisor
- C. vGPU always disables every form of hardware partitioning
- D. MIG and vGPU both require assigning the entire physical GPU exclusively to one VM

### Question 50 — O-022

An intermittent slowdown affects a GPU service. A single local nvidia-smi snapshot taken after recovery looks normal. What is the most useful monitoring improvement?

- A. Conclude that the incident did not occur because the latest snapshot is normal
- B. Use only current BMC sensor values to reconstruct past GPU activity
- C. Collect time-series telemetry and correlate it with workload events and logs
- D. Run an exclusive diagnostic during every production request

---

## Corrigé

Ne consulter qu’après avoir terminé l’ensemble des questions.

#### Correction 1 — E-020 (essential, E03)

Réponse correcte : A. La recherche de groupes sans catégories de référence préexistantes correspond au clustering non supervisé.
B — Le scénario ne fournit pas de quantité cible connue à prédire.
C — La classification supervisée exige une cible ; le scénario cherche justement à découvrir les groupes.
D — Le problème décrit une découverte de groupes, pas des actions évaluées par récompense.
[48] IBM: What is machine learning? — https://www.ibm.com/think/topics/machine-learning

#### Correction 2 — E-021 (essential, E03)

Réponse correcte : B. L’agent apprend en fonction des conséquences de ses actions et d’une récompense ; c’est le cadre du renforcement.
A — Le scénario insiste sur les actions et récompenses, pas uniquement sur des paires d’exemples statiques.
C — Aucun regroupement d’images n’est décrit ; il faut apprendre un comportement.
D — Le robot apprend à améliorer une récompense ; il existe donc un objectif d’apprentissage.
[48] IBM: What is machine learning? — https://www.ibm.com/think/topics/machine-learning

#### Correction 3 — E-022 (essential, E04)

Réponse correcte : B. Les bibliothèques et frameworks rendent les capacités GPU plus accessibles et évitent de réimplémenter des opérations déjà optimisées.
A — Un meilleur accès logiciel au calcul ne remplace pas les données du problème.
C — Les abstractions logicielles ne garantissent pas la généralisation ou l’adéquation métier.
D — Une implémentation accélérée n’établit pas la validité des prédictions pour le modèle et le cas d’usage.
[62] 1.1. Introduction — CUDA Programming Guide — https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/introduction.html

#### Correction 4 — E-023 (essential, E04)

Réponse correcte : B. Des cibles incohérentes affectent ce qui est appris et mesuré ; accélérer les calculs ne corrige pas ce défaut de données.
A — Le matériel exécute les calculs ; il ne rend pas les annotations cohérentes.
C — L’IA n’est pas entièrement non supervisée ; la tâche peut nécessiter des cibles de référence.
D — Un modèle plus grand ne garantit pas de corriger la cohérence des cibles ; les données doivent être examinées.
[48] IBM: What is machine learning? — https://www.ibm.com/think/topics/machine-learning
[62] 1.1. Introduction — CUDA Programming Guide — https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/introduction.html

#### Correction 5 — E-024 (essential, E05)

Réponse correcte : C. NVIDIA cite la génération de code parmi les applications des LLM ; ce besoin porte sur la génération d’un contenu structuré à partir du langage.
A — Reconnaître des logos ne produit pas du code à partir de requêtes en langage naturel.
B — Une prévision de durée ne génère pas le code demandé.
D — Regrouper des fichiers similaires ne suffit pas à générer du code à partir d’une demande.
[9] NVIDIA: What Are Large Language Models Used For? — https://blogs.nvidia.com/blog/what-are-large-language-models-used-for

#### Correction 6 — E-025 (essential, E05)

Réponse correcte : D. Omniverse est associé aux jumeaux numériques industriels et à la simulation robotique ; le besoin est celui d’un environnement de simulation.
A — Optimiser l’exécution d’un classifieur n’apporte pas à lui seul les fonctions de jumeau numérique et de simulation.
B — Le pilote permet l’accès au matériel mais ne constitue pas à lui seul l’application de jumeau numérique.
C — Le registre peut distribuer des ressources, mais n’est pas l’outil qui fournit les fonctions de simulation demandées.
[65] NVIDIA AI Enterprise software platform — https://www.nvidia.com/en-us/data-center/products/ai-enterprise

#### Correction 7 — E-026 (essential, E08)

Réponse correcte : C. Le profil confirme une saturation de la bande passante de la mémoire du GPU ; l’opération est donc memory-bandwidth-bound, et non simplement limitée par la capacité mémoire ou le débit arithmétique.
A — Capacité et bande passante sont distinctes ; le profil indique un débit de mouvement des données limitant.
B — Le profil indique précisément que les transferts, et non les calculs, dominent.
D — La capacité du stockage ne doit pas être confondue avec la bande passante de la mémoire du GPU.
[71] NVIDIA GPU performance background for deep learning — https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html

#### Correction 8 — E-027 (essential, E08)

Réponse correcte : A. Le GPU attend les entrées : le premier levier vise la préparation qui l’alimente, plutôt que son débit arithmétique.
B — Davantage de calcul GPU ne corrige pas à lui seul la préparation insuffisante des entrées.
C — CPU et GPU sont complémentaires ; retirer la coordination ne résout pas ce chemin de données.
D — Cela ne corrige pas directement le décodage trop lent et ne garantit pas une meilleure alimentation du GPU.
[62] 1.1. Introduction — CUDA Programming Guide — https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/introduction.html
[71] NVIDIA GPU performance background for deep learning — https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html

#### Correction 9 — E-028 (essential, E02)

Réponse correcte : D. Le besoin concerne la quantité de travail achevée dans une fenêtre donnée ; le débit soutenu est donc prioritaire, sans ignorer qualité et fiabilité.
A — Une requête isolée rapide ne garantit pas l’achèvement de toute l’archive sous charge.
B — Le premier résultat rapide ne garantit pas que tout le travail soit terminé dans la fenêtre disponible.
C — Un pic théorique ne mesure pas le débit soutenu de la charge réelle ni son achèvement.
[5] NVIDIA: AI inference — https://developer.nvidia.com/topics/ai/ai-inference
[70] Triton Inference Server model execution — https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_execution.html

#### Correction 10 — E-029 (essential, E02)

Réponse correcte : A. L’inférence n’est pas nécessairement petite ; les grands modèles peuvent nécessiter des ressources distribuées selon leur configuration et le service attendu.
B — L’inférence peut utiliser des GPU ; elle est définie par l’application du modèle, pas par le processeur.
C — Des systèmes d’inférence distribuée existent également pour les charges importantes.
D — L’interface API ne réduit pas par elle-même les exigences du modèle.
[5] NVIDIA: AI inference — https://developer.nvidia.com/topics/ai/ai-inference

#### Correction 11 — E-030 (essential, E02)

Réponse correcte : A. La quantification est une optimisation à valider : compatibilité, qualité et performances dépendent du modèle, du matériel et des données.
B — Aucune garantie universelle de qualité identique ou d’accélération ne découle du seul changement de précision.
C — Une taille réduite ne démontre pas que la précision des sorties ni la performance du service restent acceptables.
D — Les capacités dépendent des architectures et des versions ; les formats ne sont pas universels.
[3] NVIDIA TensorRT — https://developer.nvidia.com/tensorrt
[71] NVIDIA GPU performance background for deep learning — https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html

#### Correction 12 — E-031 (essential, E01)

Réponse correcte : B. Ces bibliothèques fournissent des opérations optimisées que les frameworks peuvent exploiter, ce qui facilite productivité et performance.
A — Les bibliothèques fournissent des primitives ; elles ne remplacent pas toute la logique du framework et du modèle.
C — Une bibliothèque d’opérations ne fournit pas automatiquement les poids propres à la tâche.
D — La bonne implémentation du calcul ne garantit pas l’adéquation métier du modèle.
[62] 1.1. Introduction — CUDA Programming Guide — https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/introduction.html

#### Correction 13 — E-032 (essential, E01)

Réponse correcte : C. L’opérateur automatise les composants GPU de Kubernetes, notamment pilotes, intégration des conteneurs et device plugin selon la configuration.
A — Triton fournit le serving des modèles ; il ne remplace pas la gestion de la pile GPU sur les nœuds Kubernetes.
B — Le registre stocke et distribue les artefacts ; il n’automatise pas la configuration des composants GPU des nœuds.
D — Le moteur exécute l’inférence optimisée ; ce n’est pas un gestionnaire de pilotes et de runtimes de cluster.
[40] NVIDIA GPU Operator Overview — https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html

#### Correction 14 — E-033 (essential, E01)

Réponse correcte : A. Le défaut décrit concerne une dépendance d’accès au matériel, en dessous du modèle et de sa logique métier.
B — Le modèle ne démarre pas faute de pilote ; régler la file de requêtes ne résout pas cette dépendance.
C — Une modification d’apprentissage ne rend pas le GPU accessible sans la pile hôte requise.
D — Un problème d’autorisation de téléchargement serait d’une autre nature ; le défaut indiqué est le pilote hôte.
[40] NVIDIA GPU Operator Overview — https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html

#### Correction 15 — E-034 (essential, E06)

Réponse correcte : B. La documentation NeMo Framework décrit les checkpoints préentraînés, l’entraînement et la personnalisation des modèles vocaux.
A — Le plugin expose des ressources GPU ; il ne fournit pas le workflow d’entraînement vocal demandé.
C — Cette configuration concerne le serving, pas le développement et l’apprentissage de la capacité vocale.
D — L’optimisation d’inférence d’un modèle existant n’est pas le framework d’entraînement et de personnalisation vocale demandé.
[52] NVIDIA NeMo Framework overview — https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html

#### Correction 16 — E-035 (essential, E06)

Réponse correcte : D. NGC couvre un catalogue de ressources GPU et des fonctions de registre privé et de partage d’artefacts.
A — Triton sert les modèles ; il ne remplit pas le rôle de catalogue et de registre privé demandé.
B — L’opérateur gère la pile GPU dans Kubernetes, pas la distribution d’artefacts au moyen d’un catalogue et registre.
C — Le runtime exécute le modèle optimisé ; il ne fournit pas le service de catalogue et partage recherché.
[49] NVIDIA NGC overview — https://docs.nvidia.com/ngc/gpu-cloud/ngc-overview/index.html

#### Correction 17 — E-036 (essential, E07)

Réponse correcte : D. Le retour arrière contrôlé rétablit une version dont les critères sont connus ; l’investigation de la régression peut ensuite guider une correction.
A — Cela retire l’option de retour arrière alors qu’elle est disponible et validée.
B — La nouveauté ne remplace pas le respect d’un critère de qualité requis.
C — Le scénario ne désigne pas le pilote comme cause ; son changement ne prouve pas la correction des sorties.
[84] Amazon SageMaker AI deployment guardrails — https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html

#### Correction 18 — E-037 (essential, E07)

Réponse correcte : D. Le modèle reçoit une représentation différente de celle validée ; il faut vérifier le pipeline et la cohérence des caractéristiques avant d’accuser le matériel.
A — Le scénario décrit un écart de préparation et ne démontre aucun manque de calcul.
B — Le scénario désigne un changement de représentation des entrées ; il faut vérifier cette transformation avant un réglage de débit.
C — Un matériel sain peut exécuter un modèle sur des entrées mal préparées ; cela ne garantit pas la qualité des sorties.
[78] scikit-learn common pitfalls: preprocessing and data leakage — https://scikit-learn.org/stable/common_pitfalls.html

#### Correction 19 — E-038 (essential, E07)

Réponse correcte : C. Une latence stable ne prouve pas une qualité stable. Il faut étudier l’évolution des données et réévaluer avant de décider d’une mise à jour contrôlée.
A — L’état du service et la pertinence des prédictions sont deux dimensions différentes.
B — L’inférence standard n’est pas une mise à jour des paramètres ; cette action n’est ni une évaluation ni une politique contrôlée.
D — La capacité disque ne démontre ni ne corrige la cause de la dégradation de qualité.
[48] IBM: What is machine learning? — https://www.ibm.com/think/topics/machine-learning
[52] NVIDIA NeMo Framework overview — https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html

#### Correction 20 — I-021 (infrastructure, I01)

Réponse correcte : A. Tout le jeu de données n’a pas à résider en VRAM : l’ensemble des tenseurs requis pour une étape doit y tenir simultanément, et le chemin d’entrée doit fournir les lots à un débit suffisant.
B — Cette exigence n’est pas nécessaire pour un traitement par lots compatible.
C — Les données doivent rester stockées et fournies à un débit suffisant.
D — Le débit d’alimentation peut encore limiter la charge.
[6] NVIDIA: Scaling Storage for AI Training and Inferencing — https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing
[79] PyTorch training memory usage and optimizer state — https://docs.pytorch.org/tutorials/intermediate/optimizer_step_in_backward_tutorial.html

#### Correction 21 — I-022 (infrastructure, I02)

Réponse correcte : C. La réplication intégrale ne réduit pas l’empreinte d’une copie. Il faut une stratégie qui répartit effectivement le modèle ou réduit ses besoins.
A — La mémoire agrégée n’est pas une allocation unique automatique.
B — Les disques n’augmentent pas la capacité locale du GPU.
D — Une copie complète conserve les mêmes poids.
[6] NVIDIA: Scaling Storage for AI Training and Inferencing — https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing
[19] Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog — https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io

#### Correction 22 — I-023 (infrastructure, I03)

Réponse correcte : B. La capacité disponible inclut des marges et de la redondance ; il faut les spécifications système et le scénario de charge, pas seulement la somme des PSU.
A — La charge réelle ne correspond pas nécessairement à la capacité nominale.
C — Elles assurent des chemins alternatifs, pas une consommation nulle.
D — Le PUE dépend des énergies mesurées du site et de l’IT.
[16] Introduction to NVIDIA DGX H100/H200 Systems — NVIDIA DGX H100/H200 User Guide — https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html

#### Correction 23 — I-024 (infrastructure, I04)

Réponse correcte : D. Le coût complet sur la durée peut être différent du tarif GPU isolé ; les transferts et le stockage font partie de l’évaluation.
A — Le fait de facturer séparément ne rend pas le coût négligeable.
B — Les conditions réelles de transfert doivent être examinées.
C — La vitesse crête ne décrit pas le coût complet sur la durée.
[74] NVIDIA Evolving Your Infrastructure for AI: Considerations for IT Leaders — https://images.nvidia.com/aem-dam/Solutions/documents/bus-leader-industry-brief-evolving-for-ai-3150350.pdf

#### Correction 24 — I-025 (infrastructure, I05)

Réponse correcte : C. L’OOB vise notamment les interfaces de gestion matérielle et permet de les séparer des accès ordinaires des utilisateurs.
A — Le stockage partagé possède un autre rôle et son propre chemin.
B — Le réseau OOB vise la gestion matérielle, pas le fabric applicatif principal.
D — L’OOB sert un accès contrôlé, pas une exposition générale.
[66] Network Fabrics — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/network-fabrics.html
[16] Introduction to NVIDIA DGX H100/H200 Systems — NVIDIA DGX H100/H200 User Guide — https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html

#### Correction 25 — I-026 (infrastructure, I06)

Réponse correcte : B. Le liquide transporte la chaleur ; il faut toujours l’évacuer et respecter les exigences de conception et d’exploitation.
A — Le fluide déplace la chaleur ; il faut toujours la rejeter.
C — La compatibilité du fluide et des interfaces doit être vérifiée.
D — Des solutions hybrides conservent des besoins d’air.
[72] DOE Best Practices Guide for Energy-Efficient Data Center Design (2024) — https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design.pdf

#### Correction 26 — I-027 (infrastructure, I07)

Réponse correcte : B. La topologie doit suivre les échanges réels. L’absence de communication étroite entre répliques ne justifie pas automatiquement un grand domaine scale-up.
A — Le scénario ne décrit pas une telle coopération entre répliques.
C — Le service dépend aussi des requêtes et des données.
D — Le mot inférence ne suffit pas à justifier une communication GPU étroite.
[18] NVLink & NVLink Switch: Fastest HPC Data Center Platform | NVIDIA — https://www.nvidia.com/en-us/data-center/nvlink
[6] NVIDIA: Scaling Storage for AI Training and Inferencing — https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing

#### Correction 27 — I-028 (infrastructure, I08)

Réponse correcte : D. NCCL est une couche logicielle exploitant les transports compatibles ; ce n’est ni une famille de câbles ni un protocole de facility.
A — NCCL est une bibliothèque qui exploite des transports.
B — Cela décrit une fonction matérielle, pas NCCL.
C — La communication ne garantit pas une allocation mémoire unifiée.
[19] Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog — https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io

#### Correction 28 — I-029 (infrastructure, I09)

Réponse correcte : D. La frontière du domaine NVLink dépend de la plateforme. Certaines architectures à l’échelle du rack dépassent un seul serveur ; on ne doit pas généraliser un ancien périmètre.
A — La commutation NVLink n’est pas un routeur Ethernet général.
B — Cette règle ignore les domaines NVLink Switch étendus compatibles.
C — L’extension dépend d’une architecture compatible.
[18] NVLink & NVLink Switch: Fastest HPC Data Center Platform | NVIDIA — https://www.nvidia.com/en-us/data-center/nvlink

#### Correction 29 — I-030 (infrastructure, I10)

Réponse correcte : A. Le DPU vise les fonctions d’infrastructure adaptées. Déplacer arbitrairement le calcul GPU sur ses cœurs généralistes n’apporte pas le bénéfice annoncé.
B — Sans accélération adaptée, déplacer le calcul peut réduire les performances.
C — Le choix d’un processeur ne supprime pas les besoins mémoire du modèle.
D — La répartition des rôles reste spécialisée.
[12] Offloading and Isolating Data Center Workloads with NVIDIA Bluefield DPU | NVIDIA Technical Blog — https://developer.nvidia.com/blog/offloading-and-isolating-data-center-workloads-with-bluefield-dpu

#### Correction 30 — I-031 (infrastructure, I01)

Réponse correcte : A. Le nombre de GPU ne décrit pas la topologie ni la compatibilité GPUDirect ; il faut examiner le chemin réel.
B — Le chemin PCIe, les équipements et les logiciels interviennent aussi.
C — Le nombre de GPU ne décrit pas la topologie ni l’adaptateur.
D — La compatibilité et la préparation logicielle restent nécessaires.
[55] 1. Overview — GPUDirect RDMA 13.4 documentation — https://docs.nvidia.com/cuda/gpudirect-rdma/index.html
[19] Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog — https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io

#### Correction 31 — I-032 (infrastructure, I02)

Réponse correcte : B. La croissance du calcul doit être accompagnée des chemins de données et de la facility ; sinon un autre composant peut empêcher le gain attendu.
A — Cette démarche risque de rendre les GPU inutilisables ou sous-alimentés.
C — Ces ressources ont aussi des limites qui doivent être anticipées.
D — La capacité des liaisons communes reste bornée.
[66] Network Fabrics — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/network-fabrics.html
[68] Key Components of the DGX SuperPOD — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html
[72] DOE Best Practices Guide for Energy-Efficient Data Center Design (2024) — https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design.pdf

#### Correction 32 — I-033 (infrastructure, I03)

Réponse correcte : C. Le rapport facility/IT peut s’améliorer sans prouver une hausse du travail utile ; il faut d’autres mesures pour évaluer l’IA.
A — Le PUE porte sur les énergies facility et IT.
B — Le nombre de travaux n’entre pas dans sa définition.
D — Il ne mesure pas le travail utile du modèle par énergie.
[72] DOE Best Practices Guide for Energy-Efficient Data Center Design (2024) — https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design.pdf

#### Correction 33 — I-034 (infrastructure, I04)

Réponse correcte : C. La référence SuperPOD distingue la propriété du matériel et son hébergement : une colocation peut accueillir des systèmes appartenant au client.
A — La propriété dépend du contrat ; le scénario conserve la propriété cliente.
B — Hébergement et modèle de service ne sont pas synonymes.
D — Les responsabilités applicatives doivent être précisées ; elles ne disparaissent pas.
[68] Key Components of the DGX SuperPOD — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html

#### Correction 34 — I-035 (infrastructure, I05)

Réponse correcte : B. Les ressources physiques ne suffisent pas à fournir un service exploitable ; la référence associe matériel, gestion et orchestration.
A — L’accès aux données, la configuration et les services restent nécessaires.
C — Le logiciel coordonne les ressources, il ne les crée pas.
D — Un inventaire seul ne fournit pas le service complet.
[68] Key Components of the DGX SuperPOD — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html
[66] Network Fabrics — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/network-fabrics.html

#### Correction 35 — I-036 (infrastructure, I06)

Réponse correcte : A. Le format rack ne rend pas une charge lourde sûre à manipuler ; les consignes de manutention et les moyens adaptés s’appliquent.
B — Une réduction de poids supposée ne remplace pas les consignes validées.
C — Les précautions doivent être vérifiées avant la manutention.
D — Le format rack ne supprime pas les risques de manutention.
[67] Safety — NVIDIA DGX H100/H200 User Guide — https://docs.nvidia.com/dgx/dgxh100-user-guide/safety.html

#### Correction 36 — I-037 (infrastructure, I07)

Réponse correcte : D. Le problème est la capacité partagée entre deux flux critiques ; dimensionner et séparer leurs chemins peut réduire l’interférence.
A — Davantage de mémoire ne garantit pas la suppression des accès aux données.
B — Cela risque d’augmenter encore le trafic sur le goulot.
C — Le volume stockable ne corrige pas sa capacité de transport.
[66] Network Fabrics — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/network-fabrics.html
[68] Key Components of the DGX SuperPOD — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html

#### Correction 37 — I-038 (infrastructure, I08)

Réponse correcte : C. Le chemin de données peut éviter des copies et une partie du traitement CPU ; les étapes de préparation et la pile logicielle restent nécessaires.
A — Le matériel et la pile logicielle doivent prendre en charge RDMA.
B — L’objectif est justement d’éviter certains passages et copies.
D — La topologie et les contraintes de plateforme restent importantes.
[55] 1. Overview — GPUDirect RDMA 13.4 documentation — https://docs.nvidia.com/cuda/gpudirect-rdma/index.html
[19] Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog — https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io

#### Correction 38 — I-039 (infrastructure, I09)

Réponse correcte : A. La pertinence dépend du fabric complet et de l’usage, pas du seul nom de technologie. Les options de stockage B200 illustrent les deux familles.
B — La topologie, la congestion et l’intégration comptent également.
C — RoCE fournit précisément cette possibilité.
D — Les compétences aident, mais la solution RDMA doit être validée.
[19] Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog — https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io
[66] Network Fabrics — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/network-fabrics.html
[82] NVIDIA Onyx 3.10.4606 LTS — RoCE (direct documentation URL) — https://networking-docs.nvidia.com/onyxum/3104606lts/rdma-over-converged-ethernet-roce

#### Correction 39 — I-040 (infrastructure, I10)

Réponse correcte : D. GPUDirect RDMA décrit un chemin d’accès mémoire ; un DPU est un processeur d’infrastructure. Une carte compatible peut fournir le chemin direct sans que cette seule information prouve la présence d’un DPU.
A — Le chemin mémoire ne prouve pas la présence d’un DPU.
B — La technologie GPUDirect n’est pas un synonyme de la famille BlueField.
C — Cette réponse nie une capacité décrite par GPUDirect RDMA.
[55] 1. Overview — GPUDirect RDMA 13.4 documentation — https://docs.nvidia.com/cuda/gpudirect-rdma/index.html
[19] Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog — https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io
[12] Offloading and Isolating Data Center Workloads with NVIDIA Bluefield DPU | NVIDIA Technical Blog — https://developer.nvidia.com/blog/offloading-and-isolating-data-center-workloads-with-bluefield-dpu

#### Correction 40 — O-012 (operations, O02)

Réponse correcte : D. GPU Operator automatise la gestion de plusieurs composants NVIDIA de la pile Kubernetes, dont pilotes, plugin GPU, Container Toolkit et monitoring DCGM.
A — Le scheduler place les Pods ; il ne gère pas à lui seul le déploiement de cette pile NVIDIA.
B — Le plugin annonce les ressources GPU ; il ne remplace pas l'automatisation de tous les composants cités.
C — L'exporter publie la télémétrie ; il ne déploie pas à lui seul pilotes, plugin et toolkit.
[40] NVIDIA GPU Operator Overview — https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html

#### Correction 41 — O-013 (operations, O02)

Réponse correcte : C. Le Container Toolkit fournit des composants d'intégration permettant aux runtimes de configurer l'accès NVIDIA des conteneurs. La disponibilité sur l'hôte et l'allocation ne garantissent pas cette intégration.
A — Une quantité de mémoire ne vérifie pas l'intégration du runtime et l'exposition des appareils.
B — Le compte de ressources publié ne configure pas les périphériques dans le runtime ; l'allocation a déjà eu lieu dans ce scénario.
D — La priorité de file ne configure pas l'accès GPU dans un conteneur déjà alloué.
[42] NVIDIA Container Toolkit Architecture Overview — https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/arch-overview.html

#### Correction 42 — O-014 (operations, O02)

Réponse correcte : A. Pour le mécanisme GPU documenté, Kubernetes utilise la limite comme demande si la demande est omise. Si les deux sont précisées, elles doivent être égales.
B — Ce mécanisme ne décrit pas une demande GPU nulle avec surallocation illimitée.
C — La demande déclarative ne se calcule pas à partir de l'utilisation observée.
D — L'exporter publie des métriques ; il ne choisit pas la demande de ressources du Pod.
[41] Kubernetes Schedule GPUs — https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus
[57] NVIDIA Install DCGM Exporter — https://docs.nvidia.com/datacenter/dcgm/latest/installation/install-dcgm-exporter.html

#### Correction 43 — O-015 (operations, O02)

Réponse correcte : A. La capacité libre globale ne suffit pas : le nœud doit aussi satisfaire les contraintes de sélection ou d'affinité. Kubernetes documente ces mécanismes pour les clusters comportant plusieurs types de GPU.
B — DCGM Exporter est une interface de télémétrie et non le décideur de placement.
C — Les labels et contraintes restent applicables même si une carte est libre ailleurs.
D — Un état Pending lié aux contraintes ne démontre pas une corruption du pilote par le modèle.
[41] Kubernetes Schedule GPUs — https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus
[57] NVIDIA Install DCGM Exporter — https://docs.nvidia.com/datacenter/dcgm/latest/installation/install-dcgm-exporter.html

#### Correction 44 — O-016 (operations, O03)

Réponse correcte : B. NVIDIA documente des restrictions de métriques avec MIG et l'usage de N/A pour des informations non supportées. Une valeur absente ne doit pas devenir artificiellement un zéro.
A — Une information indisponible sur l'utilisation ne renseigne pas une puissance nulle.
C — MIG partitionne des ressources ; cette lecture n'indique pas leur disparition.
D — N/A signifie indisponibilité, pas valeur numérique nulle universelle.
[39] NVIDIA System Management Interface — https://docs.nvidia.com/deploy/nvidia-smi/index.html
[44] NVIDIA MIG User Guide Introduction — https://docs.nvidia.com/datacenter/tesla/mig-user-guide/introduction.html

#### Correction 45 — O-017 (operations, O03)

Réponse correcte : A. Les compteurs ECC distinguent plusieurs types d'erreurs et périmètres de comptage. La nature des erreurs et leur évolution sont plus utiles qu'une valeur historique isolée pour orienter l'analyse.
B — Une forte activité ne précise ni le type ni le périmètre ni la récence des erreurs ECC.
C — Une allocation correcte ne caractérise pas les erreurs mémoire observées.
D — Un job réussi ne suffit pas à effacer ou caractériser l'historique de fiabilité ; cela supprimerait du contexte.
[39] NVIDIA System Management Interface — https://docs.nvidia.com/deploy/nvidia-smi/index.html

#### Correction 46 — O-018 (operations, O03)

Réponse correcte : C. La puissance observée et la limite de puissance sont des informations différentes. Le GPU peut ajuster son état de performance pour respecter une enveloppe ; une puissance en watts ne constitue pas une énergie cumulée de job.
A — Des valeurs de puissance ne sont pas des quantités cumulées d'énergie.
B — Une contrainte de puissance ne garantit pas un débit constant pour toutes les charges.
D — La puissance ne mesure pas la capacité mémoire occupée.
[39] NVIDIA System Management Interface — https://docs.nvidia.com/deploy/nvidia-smi/index.html

#### Correction 47 — O-019 (operations, O04)

Réponse correcte : D. Le guide vGPU décrit un enforcement contractuel EULA sans checkout dans certains cas. Il faut identifier l'offre et le mode de déploiement exacts ; cela ne permet pas d'étendre ces règles à tout CUDA ou MIG.
A — MIG est un mécanisme matériel ; le besoin de licence dépend de la pile et de l'offre, pas du seul mot MIG.
B — L'assignation technique ne détermine pas à elle seule une règle de licence identique pour tous les logiciels.
C — Une allocation de ressources ne remplace pas des droits contractuels d'utilisation du logiciel.
[59] Introduction to NVIDIA vGPU Software Licensing — https://docs.nvidia.com/vgpu/latest/grid-licensing-user-guide/intro-to-grid-licensing.html
[44] NVIDIA MIG User Guide Introduction — https://docs.nvidia.com/datacenter/tesla/mig-user-guide/introduction.html

#### Correction 48 — O-020 (operations, O04)

Réponse correcte : B. La capacité mémoire seule ne valide pas les API ni la combinaison de support. NVIDIA précise que le support CUDA dépend des types vGPU et GPU, et que les capacités doivent être vérifiées par hyperviseur et versions.
A — Détecter la carte sur l'hôte ne valide pas le profil invité et les fonctions applicatives.
C — Le support sur un autre hyperviseur ne valide pas automatiquement celui qui sera déployé.
D — Une allocation possible ne garantit pas le support des API et fonctions nécessaires.
[58] Introduction to NVIDIA vGPU Software — https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/grid-vgpu-introduction.html

#### Correction 49 — O-021 (operations, O04)

Réponse correcte : A. MIG et vGPU sont des mécanismes distincts pouvant être combinés dans les configurations prises en charge. MIG partitionne les ressources ; vGPU ajoute la présentation et la gestion dans un environnement VM.
B — Les combinaisons GPU, versions et hyperviseur doivent être vérifiées ; le support n'est pas universel.
C — Le guide documente précisément des configurations de vGPU fondées sur MIG.
D — Le passthrough correspond à cette assignation entière ; MIG partitionne et vGPU peut partager les ressources.
[44] NVIDIA MIG User Guide Introduction — https://docs.nvidia.com/datacenter/tesla/mig-user-guide/introduction.html
[58] Introduction to NVIDIA vGPU Software — https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/grid-vgpu-introduction.html

#### Correction 50 — O-022 (operations, O01)

Réponse correcte : C. Un instantané après récupération ne décrit pas l'incident. Une collecte suivie, par exemple via DCGM Exporter et Prometheus, aide à rapprocher mesures, travaux et événements ; les journaux restent nécessaires pour le contexte d'erreur.
A — Une mesure hors de la fenêtre d'incident ne réfute pas un problème intermittent.
B — Des lectures actuelles de plateforme ne reconstituent pas l'historique d'activité GPU pendant l'incident.
D — Les diagnostics exclusifs sont invasifs et ne doivent pas être imposés à chaque requête de production.
[57] NVIDIA Install DCGM Exporter — https://docs.nvidia.com/datacenter/dcgm/latest/installation/install-dcgm-exporter.html
[37] NVIDIA Xid Errors Introduction — https://docs.nvidia.com/deploy/xid-errors/introduction.html
[38] NVIDIA DCGM Feature Overview — https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html
[20] NVIDIA IGX BMC Introduction — https://docs.nvidia.com/igx-orin/bmc/latest/introduction.html
