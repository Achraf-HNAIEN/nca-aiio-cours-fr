# Examen d’entraînement A

Questions originales non officielles. Aucun seuil officiel de réussite n’est supposé.
50 questions · 60 minutes · une seule réponse par question.

## Questions

### Question 1 — E-001

Which relationship between artificial intelligence (AI), machine learning (ML), and deep learning (DL) is correct?

- A. AI is a subset of DL, and DL is a subset of ML.
- B. ML and DL are separate fields that do not overlap.
- C. DL is a subset of ML, and ML is a subset of AI.
- D. Every AI system must use a deep neural network.

### Question 2 — E-002

A utility has historical sensor readings paired with the actual amount of electricity consumed the following day. It wants to predict that amount for tomorrow. Which approach best matches the task?

- A. Unsupervised clustering
- B. Supervised classification
- C. Supervised regression
- D. Reinforcement learning from action rewards

### Question 3 — E-003

A language model is trained to predict text that has been hidden from otherwise unannotated documents. Where does the supervisory signal primarily come from?

- A. A human must manually label every hidden word before training.
- B. The deployed model never needs a training objective.
- C. An action reward from a separate interactive environment supplies each missing-text target.
- D. The original document content provides targets for the prediction task.

### Question 4 — E-004

Which combination best explains major technical enablers of modern AI progress?

- A. Larger models alone, regardless of data or compute availability
- B. Replacing model evaluation with faster processors
- C. More usable data, improved algorithms, and greater accessible computing capability
- D. More compute alone, with no role for changes in data or algorithms

### Question 5 — E-005

A small team wants to adapt an existing text model to its industry vocabulary without repeating its entire original training process. Which strategy best fits?

- A. Train a new foundation model from scratch solely because the vocabulary is specialized.
- B. Fine-tune an appropriate pretrained model and evaluate it on domain-specific examples.
- C. Assume that a pretrained model must already satisfy every industry requirement.
- D. Optimize inference precision without adapting the model to the domain.

### Question 6 — E-006

A manufacturer needs a model to draw a bounding box around each damaged component in a photograph, rather than only reporting whether damage exists. Which task most directly matches?

- A. Whole-image classification only
- B. Image segmentation that returns per-pixel class masks instead of bounding boxes
- C. Object detection
- D. Regression that predicts the total daily number of defective parts

### Question 7 — E-007

An online fraud service uses a fast model, but transaction decisions are delayed while customer profiles are retrieved. What should the team examine first?

- A. Only the number of training epochs
- B. The latency of the data retrieval path used by inference
- C. Only GPU arithmetic throughput, while leaving profile retrieval unchanged
- D. Only the classification threshold, without measuring the retrieval delay

### Question 8 — E-008

Which description best captures the architectural difference between a CPU and a GPU?

- A. A CPU emphasizes fast execution of serial work, while a GPU emphasizes throughput across many parallel threads.
- B. A GPU eliminates the need for host coordination in every application.
- C. A CPU cannot execute any parallel work.
- D. CPU cores and GPU cores are identical units that differ only in count.

### Question 9 — E-009

An application sends a tiny, mostly serial calculation to a GPU and spends more time launching work and transferring data than computing. What is the best conclusion?

- A. Every GPU workload must be faster than a CPU implementation.
- B. Increasing GPU memory capacity must make the serial calculation parallel.
- C. Adding more GPUs must improve this calculation even without dividing its work.
- D. GPU acceleration is not automatically beneficial when parallel work is insufficient relative to overhead.

### Question 10 — E-010

A network fits in GPU memory for inference but runs out of memory during gradient-based training with the same weights. What is the most likely conceptual explanation?

- A. Inference always stores more optimizer state than training.
- B. Training may require additional intermediate values, gradients, and optimizer state beyond the weights.
- C. The training dataset must always fit entirely in GPU memory.
- D. Training and inference necessarily have identical memory requirements whenever weight count matches.

### Question 11 — E-011

A deployed classifier processes new customer requests. No training job or parameter-update process is running. What normally happens to its learned weights during these requests?

- A. The weights remain unchanged while the model computes predictions.
- B. The weights are automatically retrained after every request.
- C. The weights are replaced by the incoming input data.
- D. The batch size alone determines new weight values after each prediction.

### Question 12 — E-012

A team increases batch size for an interactive inference service. Total requests processed per second improves, but some users wait longer for a batch to form. What trade-off is being observed?

- A. Higher throughput guarantees lower latency for every request.
- B. Batching changes inference into supervised training.
- C. Latency and throughput are two names for the same performance metric.
- D. Higher throughput can come with increased request latency.

### Question 13 — E-013

What is CUDA primarily used for in the NVIDIA AI software stack?

- A. Providing a complete model-serving API and request scheduler by itself
- B. Replacing all operating-system and driver components
- C. Providing a parallel computing platform and programming model for GPU-accelerated applications
- D. Acting only as a public catalog of pretrained models

### Question 14 — E-014

A containerized GPU application works on a configured workstation but cannot access the GPU on a new host. Which assumption should be rejected?

- A. The host GPU software configuration can affect the application.
- B. A container image alone guarantees a compatible host GPU driver and device integration.
- C. Container GPU access can depend on runtime integration.
- D. Hardware availability and application access are separate checks.

### Question 15 — E-015

A team has a validated neural network and wants to optimize its inference execution using techniques such as layer fusion and quantization on supported NVIDIA hardware. Which tool family most directly fits?

- A. NVIDIA TensorRT
- B. NGC Private Registry alone
- C. GPU Operator alone
- D. Triton request routing without changing the model execution backend

### Question 16 — E-016

A platform team needs to serve several trained models and configure concurrent model instances and request batching. Which component most directly addresses this requirement?

- A. A GPU driver by itself
- B. NVIDIA TensorRT used only as an inference execution library
- C. NGC used only to store the model artifacts
- D. NVIDIA Triton Inference Server

### Question 17 — E-017

An enterprise manages its own GPU infrastructure and wants a packaged microservice path for deploying a supported pretrained model for inference. Which NVIDIA offering best matches?

- A. NGC used only as an artifact registry
- B. NVIDIA NIM
- C. NeMo used only to train a new model from scratch
- D. TensorRT used only as a low-level execution library that the team must package itself

### Question 18 — E-018

Two experiments have different accuracy results, but the team did not record which dataset version and preprocessing configuration each used. What should be improved first?

- A. Track experiment configuration, data versions, and resulting model artifacts together.
- B. Record only the final accuracy and discard the data and configuration references.
- C. Assume the experiment using more GPU memory is always more accurate.
- D. Skip evaluation and publish whichever artifact was created last.

### Question 19 — E-019

A model meets its task-quality target in a notebook. Before opening a high-traffic inference API, what additional validation is most important?

- A. Measure end-to-end latency, throughput, and errors under representative service load.
- B. Check only the accuracy of a few isolated API calls without measuring load behavior.
- C. Assume that notebook accuracy guarantees API availability.
- D. Use the fastest observed single request as a substitute for a representative load test.

### Question 20 — I-001

A training job fails because its required working tensors exceed available GPU memory. Which change most directly addresses this capacity constraint?

- A. Use a supported configuration with enough usable GPU memory for the working tensors.
- B. Add SSD capacity while keeping GPU memory unchanged.
- C. Increase network bandwidth without changing tensor placement.
- D. Replicate the complete job on another identical GPU without partitioning it.

### Question 21 — I-002

A single-node training run fits in memory. After adding nodes, workers spend much of their time waiting for gradient synchronization. What should be investigated first?

- A. The inter-node communication path and collective-operation performance.
- B. Increase GPU compute capacity before examining synchronization.
- C. Increase archive capacity while leaving active data paths unchanged.
- D. Tune only the single-node training path.

### Question 22 — I-003

Which statement correctly describes Power Usage Effectiveness (PUE)?

- A. It is GPU energy divided by CPU energy.
- B. It is the ratio of total data center energy to IT equipment energy over a consistent measurement boundary and period.
- C. It is cooling energy divided by total facility energy.
- D. It is useful training throughput per kilowatt-hour.

### Question 23 — I-004

A team needs a two-week pilot, has no prepared data center, and is permitted to use a public cloud. Which approach is most reasonable before purchasing a permanent cluster?

- A. Purchase a permanent cluster using only the expected two-week GPU utilization.
- B. Choose the lowest hourly GPU price without checking data and networking.
- C. Evaluate a compatible cloud service, including availability, data movement, and total pilot cost.
- D. Use any available cloud instance without validating GPU memory requirements.

### Question 24 — I-005

Which group best represents the supporting infrastructure of an accelerated compute cluster?

- A. Compute nodes and checkpoint storage, without management or communication fabrics.
- B. GPU servers and local caches, with no shared services or inter-node connectivity.
- C. Compute nodes, storage, communication fabrics, and management services.
- D. Networking and scheduling services without compute or storage resources.

### Question 25 — I-006

A rack has enough empty mounting space for a new GPU server. What must still be validated before installation?

- A. Only the number of GPU slots available in the chassis.
- B. Only the installed GPU driver version.
- C. Mechanical loading, power distribution, cooling, access, and maintenance clearances.
- D. Only the total unused space across all racks.

### Question 26 — I-007

A workload sends many small synchronization messages between workers. Which network property is especially important in addition to bandwidth?

- A. A larger persistent dataset capacity.
- B. Low communication latency.
- C. Higher nominal bandwidth with no latency evaluation.
- D. More storage cache capacity regardless of the communication path.

### Question 27 — I-008

An Ethernet-based AI fabric is intended to provide RDMA. Which technology directly matches that requirement?

- A. TCP/IP over any Ethernet adapter, with no RDMA capability requirement.
- B. NVLink inside each server, without a compatible Ethernet RDMA path.
- C. An isolated BMC network configured for remote console access.
- D. RoCE on compatible adapters and a suitably configured fabric.

### Question 28 — I-009

A design uses NVLink within compatible GPU systems and InfiniBand between systems. What is the best interpretation?

- A. Mixing local GPU links and a different inter-node fabric prevents collective operations.
- B. NVLink provides general IP routing and replaces the InfiniBand fabric.
- C. InfiniBand handles only administration while NVLink carries every inter-system transfer in this design.
- D. The design uses a GPU scale-up interconnect and a separate scale-out network fabric.

### Question 29 — I-010

What is the primary infrastructure role of a DPU?

- A. Serve as an automatic extension of every GPU memory allocation.
- B. Offload, accelerate, and isolate suitable networking, storage, and security functions.
- C. Execute the primary tensor calculations of every training model instead of GPUs.
- D. Provide only a faster physical port, with no programmable infrastructure role.

### Question 30 — I-011

An image-training pipeline has enough GPU memory, but GPUs wait while CPU-side image decoding remains saturated. Which action best matches the observed bottleneck?

- A. Improve the input-preparation path and validate the resulting end-to-end training throughput.
- B. Increase persistent capacity while leaving the decoder unchanged.
- C. Add more GPUs while leaving CPU-side decoding unchanged.
- D. Increase inter-node link speed while retaining the same saturated decoder.

### Question 31 — I-012

A storage expansion doubles usable capacity, but training read throughput does not improve. Which explanation is most appropriate?

- A. Adding persistent capacity necessarily increases per-GPU memory.
- B. Storage scaling can improve capacity but never performance.
- C. Any added disk automatically doubles end-to-end read throughput.
- D. Storage capacity and storage performance are different scaling dimensions.

### Question 32 — I-013

A sizing exercise assumes 35 kW of average IT load and a constant facility-to-IT ratio of 1.4. What estimated average total facility power follows from these assumptions?

- A. 14 kW.
- B. 35 kW.
- C. 49 kW.
- D. 84 kW.

### Question 33 — I-014

An organization has a steady long-term workload and strict data-location requirements. Which comparison best supports an on-premises versus cloud decision?

- A. Compare only the upfront hardware purchase price.
- B. Compare compliant options using utilization, full lifecycle costs, operational responsibilities, and data constraints.
- C. Compare only the lowest advertised hourly GPU rate.
- D. Assume a fixed utilization rate is irrelevant to the economics.

### Question 34 — I-015

Why might a reference AI cluster separate compute, storage, and management traffic?

- A. To make all traffic use identical security and performance settings.
- B. To let ordinary cluster users directly administer every BMC.
- C. To match distinct traffic requirements and reduce interference or exposure between functions.
- D. To guarantee that no shared infrastructure component can ever fail.

### Question 35 — I-016

A dense rack has adequate room-level cooling capacity, but upper server inlets exceed their supported temperature. What should be investigated?

- A. Local airflow, recirculation, containment, and inlet conditions.
- B. Use only the room wall sensor as proof of safe server inlet conditions.
- C. Treat average rack temperature as sufficient even when individual inlets are out of range.
- D. Increase total room cooling capacity without examining inlet airflow.

### Question 36 — I-017

A network meets a point-to-point bandwidth target, but simultaneous all-to-all traffic performs poorly. What additional aspect most directly needs evaluation?

- A. Only the latency of an otherwise idle pair of nodes.
- B. Only the nominal speed of one adapter port.
- C. Only the aggregate storage capacity.
- D. Shared fabric capacity, topology, congestion, and oversubscription under the real traffic pattern.

### Question 37 — I-018

An engineer says that PFC and ECN are interchangeable names for the same RoCE function. Which correction is most accurate?

- A. PFC is priority-based flow control, whereas ECN signals congestion; their use depends on the validated fabric design.
- B. PFC provides IP routing, while ECN increases GPU memory capacity.
- C. Both mechanisms guarantee that congestion never occurs.
- D. ECN eliminates the need to validate the fabric configuration.

### Question 38 — I-019

A supported network adapter transfers data directly to GPU memory rather than staging it through host memory. Which capability is being described?

- A. A transfer that always stages payloads through host application buffers.
- B. A DPU-only feature that requires moving the training model onto DPU CPU cores.
- C. NVLink-only communication with no network adapter involvement.
- D. GPUDirect RDMA.

### Question 39 — I-020

A cloud operator wants infrastructure security functions to remain separate from the tenant-controlled host operating system. Which DPU benefit is most directly relevant?

- A. Combining tenant and operator security functions inside the same tenant-controlled process.
- B. Isolation of suitable infrastructure control and security functions.
- C. Moving all tenant tensor calculations to the DPU CPU cores.
- D. Replacing access policies because hardware isolation is sufficient by itself.

### Question 40 — O-001

A GPU server no longer responds through its operating system network interface. The operator needs a separate management path to inspect the console and power state. Which component is most appropriate?

- A. The server's BMC on the management network
- B. nvidia-smi invoked over the unavailable host SSH connection
- C. DCGM Exporter's GPU telemetry endpoint
- D. A GPU device plugin running in the unavailable host OS

### Question 41 — O-002

A team already uses Prometheus and wants GPU telemetry fields from DCGM to be available for scraping. Which component directly provides this interface?

- A. Slurm's GPU resource allocation
- B. DCGM Exporter
- C. The BMC platform telemetry interface
- D. A local NVML query without an exporter

### Question 42 — O-003

Production jobs are running on a node. An operator proposes running an invasive DCGM diagnostic that requires exclusive GPU access. What is the best next action?

- A. Run it immediately because every DCGM operation is passive
- B. Arrange an approved maintenance opportunity and exclusive access before the test
- C. Disable job logging so that the test completes faster
- D. Treat a previous utilization reading as proof that the hardware is fully validated

### Question 43 — O-004

A dashboard shows high GPU utilization from nvidia-smi, but application throughput remains poor. Which interpretation is justified by the utilization metric alone?

- A. The application has reached the GPU's theoretical compute throughput
- B. GPU memory capacity must be exhausted
- C. At least one kernel was executing during much of the sampling interval
- D. The network is certainly the bottleneck

### Question 44 — O-005

An inference model remains loaded in GPU memory while few requests arrive. Memory used is high and GPU utilization is low. What is the best interpretation?

- A. The GPU must be replaced because these readings cannot coexist
- B. High memory used proves that memory bandwidth is saturated
- C. Low utilization proves that the GPU has no allocated memory
- D. Resident allocations and kernel activity measure different aspects of the workload

### Question 45 — O-006

Training throughput falls while GPU clocks decline and thermal limiting is reported. Which investigation is the best first match to this evidence?

- A. Assume that the model checkpoint format is incompatible
- B. Check cooling conditions, relevant temperature limits, and platform telemetry
- C. Increase the power limit without checking platform constraints
- D. Add GPU memory solely because clock frequency decreased

### Question 46 — O-007

A job fails and an Xid message appears in the kernel log. What is the most defensible initial response?

- A. Replace the GPU because every Xid proves a hardware defect
- B. Ignore the event because Xid messages concern only graphics applications
- C. Delete the log and rerun until the message disappears
- D. Preserve the message and workload context, then investigate the documented possible causes

### Question 47 — O-008

A Slurm cluster manages GPUs as GRES. A submitted job requests CPU resources but does not request any GPU GRES. What should the user change to obtain a GPU allocation?

- A. Set an arbitrary GPU index in the application and bypass the scheduler
- B. Include an appropriate GPU resource request in the job submission
- C. Run a DCGM health check instead of requesting resources
- D. Increase only the job's CPU memory request

### Question 48 — O-009

GPU drivers work on Kubernetes nodes, but the cluster does not expose the vendor GPU resource to Pods. Which component is responsible for advertising these specialized devices through the standard device-plugin mechanism?

- A. Slurm's GRES configuration
- B. NVIDIA Container Toolkit runtime integration
- C. The DCGM host engine
- D. The GPU vendor's device plugin

### Question 49 — O-010

An application in a supported VM must have exclusive access to an entire physical GPU, without sharing that GPU among VMs. Which mechanism directly matches this requirement?

- A. GPU passthrough
- B. A time-sliced vGPU profile shared with other VMs
- C. A MIG instance assigned to a bare-metal process
- D. A container GPU visibility environment variable

### Question 50 — O-011

On a GPU model that supports it, which feature partitions compute resources and memory-system paths into separate GPU instances?

- A. GPU time slicing without hardware partitioning
- B. A device plugin advertising whole physical GPUs
- C. Multi-Instance GPU (MIG)
- D. GPU passthrough of an entire card

---

## Corrigé

Ne consulter qu’après avoir terminé l’ensemble des questions.

#### Correction 1 — E-001 (essential, E03)

Réponse correcte : C. Le deep learning est une famille de méthodes de machine learning ; le ML est lui-même un sous-ensemble de l’intelligence artificielle.
A — L’ordre des ensembles est inversé : AI est le périmètre le plus large.
B — Les méthodes DL font partie du ML ; ces catégories ne sont pas disjointes.
D — Une méthode à règles peut relever de l’IA sans utiliser de réseau profond.
[48] IBM: What is machine learning? — https://www.ibm.com/think/topics/machine-learning

#### Correction 2 — E-002 (essential, E03)

Réponse correcte : C. La cible est une quantité continue connue pour les exemples historiques : il s’agit d’une régression supervisée.
A — Le clustering cherche des groupes et ne correspond pas ici à la prédiction d’une quantité de référence.
B — La classification prédit une catégorie ; la consommation demandée est une quantité continue.
D — Le scénario décrit des exemples et des cibles, pas un agent choisissant des actions pour une récompense.
[48] IBM: What is machine learning? — https://www.ibm.com/think/topics/machine-learning

#### Correction 3 — E-003 (essential, E03)

Réponse correcte : D. En auto-supervision, une cible est construite depuis les données elles-mêmes ; il n’est pas nécessaire qu’un humain annote chaque cible.
A — Ce serait une annotation humaine systématique ; le signal peut être extrait du document original.
B — L’auto-supervision possède un objectif, par exemple prédire le contenu masqué.
C — Le scénario utilise le texte original comme cible ; il ne décrit pas une récompense issue d’actions dans un environnement.
[48] IBM: What is machine learning? — https://www.ibm.com/think/topics/machine-learning

#### Correction 4 — E-004 (essential, E04)

Réponse correcte : C. Les données, les progrès des modèles et la disponibilité du calcul se renforcent mutuellement ; aucun composant isolé n’explique tout.
A — La taille des modèles ne suffit pas ; données exploitables et ressources de calcul contribuent aussi aux progrès.
B — Le calcul ne remplace pas la validation de la qualité.
D — Le calcul est un moteur important, mais pas l’unique cause des progrès de l’IA.
[48] IBM: What is machine learning? — https://www.ibm.com/think/topics/machine-learning
[62] 1.1. Introduction — CUDA Programming Guide — https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/introduction.html

#### Correction 5 — E-005 (essential, E04)

Réponse correcte : B. La réutilisation d’un modèle préentraîné avec fine-tuning permet une adaptation ; l’évaluation locale reste nécessaire.
A — Le scénario demande précisément d’éviter de répéter tout l’apprentissage initial ; le préentraînement peut être réutilisé.
C — Préentraîné ne signifie pas validé pour le domaine ou la tâche locale.
D — L’optimisation d’inférence peut modifier les performances d’exécution, mais ne constitue pas à elle seule une adaptation au vocabulaire métier.
[48] IBM: What is machine learning? — https://www.ibm.com/think/topics/machine-learning
[9] NVIDIA: What Are Large Language Models Used For? — https://blogs.nvidia.com/blog/what-are-large-language-models-used-for

#### Correction 6 — E-006 (essential, E05)

Réponse correcte : C. La localisation d’objets ou de composants dans une image correspond à la détection ; une simple classification ne fournit pas cette localisation.
A — Une classe globale peut indiquer la présence d’un défaut sans localiser chaque composant.
B — Des masques par pixel ne sont pas le format de boîtes englobantes explicitement demandé.
D — Prédire un total ne localise pas chaque composant endommagé dans une photographie.
[48] IBM: What is machine learning? — https://www.ibm.com/think/topics/machine-learning

#### Correction 7 — E-007 (essential, E05)

Réponse correcte : B. La latence du service comprend l’obtention des données ; accélérer uniquement le modèle ne corrige pas une attente dominante du profil client.
A — Les epochs concernent l’apprentissage et ne ciblent pas l’attente décrite en production.
C — Le calcul du modèle est déjà rapide ; laisser le chemin de récupération inchangé ne cible pas la cause décrite.
D — Changer le seuil de décision ne réduit pas la latence de récupération du profil.
[6] NVIDIA: Scaling Storage for AI Training and Inferencing — https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing

#### Correction 8 — E-008 (essential, E08)

Réponse correcte : A. CPU et GPU ont des objectifs de conception complémentaires : contrôle et performance séquentielle d’un côté, parallélisme massif et débit de l’autre.
B — La présence du GPU ne supprime pas la coordination et les autres tâches de l’application.
C — Le CPU peut effectuer du travail parallèle ; la différence porte sur l’organisation et l’échelle privilégiées.
D — Ces unités ne sont pas directement équivalentes ; les architectures et les compromis diffèrent.
[62] 1.1. Introduction — CUDA Programming Guide — https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/introduction.html

#### Correction 9 — E-009 (essential, E08)

Réponse correcte : D. Le GPU doit recevoir assez de travail parallélisable pour amortir les coûts ; son utilisation n’est pas une garantie de gain sur une petite tâche séquentielle.
A — L’accélération dépend du parallélisme et des coûts, pas de la seule présence du GPU.
B — Davantage de capacité mémoire ne crée pas le parallélisme absent dans le calcul.
C — Multiplier les accélérateurs sans répartir un travail parallélisable ne garantit pas un gain.
[62] 1.1. Introduction — CUDA Programming Guide — https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/introduction.html
[71] NVIDIA GPU performance background for deep learning — https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html

#### Correction 10 — E-010 (essential, E02)

Réponse correcte : B. L’apprentissage ne stocke pas seulement les poids ; les états nécessaires aux gradients et aux mises à jour peuvent augmenter la consommation mémoire.
A — L’inférence standard n’effectue pas les mises à jour par l’optimiseur décrites dans l’apprentissage.
C — Le jeu complet peut être traité par portions ; ce n’est pas une obligation universelle.
D — Les mêmes poids n’impliquent pas les mêmes états temporaires, gradients ou états d’optimiseur.
[79] PyTorch training memory usage and optimizer state — https://docs.pytorch.org/tutorials/intermediate/optimizer_step_in_backward_tutorial.html

#### Correction 11 — E-011 (essential, E02)

Réponse correcte : A. L’inférence applique les paramètres appris. Le simple fait de recevoir de nouvelles entrées ne constitue pas un entraînement.
B — Une mise à jour nécessite un processus d’apprentissage ; elle n’est pas implicite dans chaque prédiction.
C — Entrées et paramètres ont des rôles distincts ; les données de requête ne remplacent pas les poids.
D — Le regroupement de requêtes ne déclenche pas une mise à jour des paramètres ; il faut un mécanisme d’apprentissage.
[48] IBM: What is machine learning? — https://www.ibm.com/think/topics/machine-learning

#### Correction 12 — E-012 (essential, E02)

Réponse correcte : D. Le regroupement peut accroître l’efficacité globale tout en ajoutant une attente par requête ; débit et latence ne sont pas synonymes.
A — Le délai d’attente de formation du batch peut augmenter malgré le débit supérieur.
B — Regrouper des requêtes ne signifie pas calculer une loss et mettre les paramètres à jour.
C — La latence mesure un délai, tandis que le débit mesure une quantité traitée par unité de temps.
[5] NVIDIA: AI inference — https://developer.nvidia.com/topics/ai/ai-inference
[70] Triton Inference Server model execution — https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_execution.html

#### Correction 13 — E-013 (essential, E01)

Réponse correcte : C. CUDA permet d’exploiter le calcul parallèle des GPU NVIDIA ; son rôle est plus général que l’affichage graphique ou un registre de modèles.
A — CUDA est une plateforme de calcul ; une API de serving et l’organisation des requêtes relèvent d’autres composants.
B — La plateforme s’appuie sur une pile système ; elle ne supprime pas ces couches.
D — Ce rôle correspond davantage à un catalogue d’artefacts comme NGC, pas à la définition de CUDA.
[47] CUDA C++ Programming Guide — https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html
[62] 1.1. Introduction — CUDA Programming Guide — https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/introduction.html

#### Correction 14 — E-014 (essential, E01)

Réponse correcte : B. Le conteneur ne suffit pas à garantir la pile hôte ; pilotes et intégration de l’accès GPU doivent être compatibles et présents.
A — Cette affirmation est correcte : la configuration hôte est précisément une dépendance à vérifier.
C — Cette dépendance est réelle ; le Container Toolkit fait partie de la pile décrite par NVIDIA.
D — Il est utile de distinguer matériel présent et accès depuis la charge ; cette affirmation ne doit pas être rejetée.
[40] NVIDIA GPU Operator Overview — https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html

#### Correction 15 — E-015 (essential, E06)

Réponse correcte : A. TensorRT cible l’optimisation de l’inférence, notamment par fusion et quantification, sous réserve de qualité et de compatibilité.
B — Un registre stocke et partage des artefacts ; il n’effectue pas à lui seul cette optimisation du calcul.
C — L’opérateur gère la pile GPU Kubernetes ; ce n’est pas le compilateur d’optimisation de réseaux demandé.
D — Le routage de serving seul n’effectue pas les optimisations de fusion et de quantification du modèle demandées.
[3] NVIDIA TensorRT — https://developer.nvidia.com/tensorrt

#### Correction 16 — E-016 (essential, E06)

Réponse correcte : D. Triton fournit des fonctions de serving, de concurrence et de regroupement ; ce sont les responsabilités décrites par le scénario.
A — Le pilote permet l’accès au matériel mais n’expose pas à lui seul le service multimodèle demandé.
B — Le runtime optimise le calcul ; les fonctions de service multimodèle et d’organisation des requêtes demandent le serveur approprié.
C — Le registre distribue les artefacts, mais n’exécute pas à lui seul le service concurrent décrit.
[70] Triton Inference Server model execution — https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_execution.html
[3] NVIDIA TensorRT — https://developer.nvidia.com/tensorrt

#### Correction 17 — E-017 (essential, E06)

Réponse correcte : B. NIM propose des microservices et des conteneurs d’inférence, notamment pour simplifier un déploiement sur une infrastructure gérée par l’équipe.
A — Un registre fournit les artefacts ; il ne constitue pas le microservice d’inférence conditionné recherché.
C — Le scénario cherche un déploiement d’inférence de modèle existant, pas un nouvel entraînement.
D — Cette option peut contribuer à l’exécution, mais ne fournit pas directement la voie de déploiement en microservice conditionné décrite pour NIM.
[5] NVIDIA: AI inference — https://developer.nvidia.com/topics/ai/ai-inference
[63] NVIDIA AI platform — https://www.nvidia.com/en-us/ai

#### Correction 18 — E-018 (essential, E07)

Réponse correcte : A. La traçabilité permet de comparer et reproduire les expériences ; sans connaître les entrées et la configuration, la différence de score est difficile à interpréter.
B — Le score isolé ne permet pas de relier le résultat aux données et à la configuration nécessaires à sa reproduction.
C — La consommation de mémoire n’établit pas la qualité ni la cause de l’écart.
D — La date de création ne remplace ni l’évaluation ni la comparaison contrôlée.
[83] MLflow ML Experiment Tracking — https://mlflow.org/docs/latest/ml/tracking

#### Correction 19 — E-019 (essential, E07)

Réponse correcte : A. Un score de qualité ne démontre pas les propriétés du service sous charge ; il faut tester le comportement opérationnel représentatif.
B — Quelques appels isolés ne valident pas le comportement d’un service fortement sollicité.
C — La qualité des prédictions et la disponibilité d’un service sont des dimensions différentes.
D — La meilleure requête isolée ne décrit ni les files d’attente ni les erreurs et débits sous charge.
[5] NVIDIA: AI inference — https://developer.nvidia.com/topics/ai/ai-inference
[48] IBM: What is machine learning? — https://www.ibm.com/think/topics/machine-learning

#### Correction 20 — I-001 (infrastructure, I01)

Réponse correcte : A. La contrainte porte sur la mémoire de travail du GPU ; il faut une capacité utilisable suffisante ou une stratégie logicielle qui réduit ou répartit cette empreinte.
B — Les SSD n’augmentent pas la mémoire locale utilisable pour les tenseurs.
C — Un lien plus rapide ne résout pas directement un manque de capacité mémoire.
D — Une copie complète garde la même empreinte par GPU.
[6] NVIDIA: Scaling Storage for AI Training and Inferencing — https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing
[16] Introduction to NVIDIA DGX H100/H200 Systems — NVIDIA DGX H100/H200 User Guide — https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html

#### Correction 21 — I-002 (infrastructure, I02)

Réponse correcte : A. Le symptôme apparaît pendant la synchronisation distribuée ; le fabric et les opérations collectives sont donc les premières hypothèses à examiner.
B — Le temps d’attente décrit un problème de communication, pas d’abord de calcul local.
C — La capacité d’archive ne modifie pas le chemin des gradients.
D — Le symptôme apparaît précisément avec les échanges entre nœuds.
[19] Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog — https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io
[68] Key Components of the DGX SuperPOD — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html

#### Correction 22 — I-003 (infrastructure, I03)

Réponse correcte : B. Le PUE compare les énergies facility et IT sur un périmètre cohérent ; il ne mesure ni la vitesse des GPU ni la qualité des modèles.
A — Le périmètre du PUE couvre le site et l’ensemble IT, pas ce rapport de composants.
C — Le refroidissement contribue aux charges non IT, mais ce rapport n’est pas le PUE.
D — Le travail utile par énergie est une autre mesure.
[72] DOE Best Practices Guide for Energy-Efficient Data Center Design (2024) — https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design.pdf

#### Correction 23 — I-004 (infrastructure, I04)

Réponse correcte : C. Un pilote court sans site prêt peut justifier une offre cloud ; il faut néanmoins vérifier disponibilité, données et coût complet au lieu de promettre un avantage automatique.
A — Cette décision ignore l’absence de site préparé et le coût d’un investissement durable.
B — Le tarif isolé ne garantit pas le service nécessaire.
D — La compatibilité et la mémoire restent des contraintes même dans le cloud.
[74] NVIDIA Evolving Your Infrastructure for AI: Considerations for IT Leaders — https://images.nvidia.com/aem-dam/Solutions/documents/bus-leader-industry-brief-evolving-for-ai-3150350.pdf

#### Correction 24 — I-005 (infrastructure, I05)

Réponse correcte : C. Le cluster est un système complet : calcul, stockage, réseau et gestion doivent fonctionner ensemble.
A — Le stockage ne remplace ni les communications ni l’administration.
B — Ce sous-ensemble omet des dépendances nécessaires au cluster distribué.
D — Les services logiciels et réseaux ne fournissent pas à eux seuls le calcul et les données.
[68] Key Components of the DGX SuperPOD — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html

#### Correction 25 — I-006 (infrastructure, I06)

Réponse correcte : C. L’espace disponible ne prouve ni la sécurité mécanique ni l’aptitude électrique et thermique du rack.
A — La capacité d’extension interne ne valide pas le site.
B — Le pilote ne démontre pas l’aptitude électrique, mécanique et thermique.
D — Une place globale ne prouve pas qu’un rack précis peut accueillir la charge.
[67] Safety — NVIDIA DGX H100/H200 User Guide — https://docs.nvidia.com/dgx/dgxh100-user-guide/safety.html
[72] DOE Best Practices Guide for Energy-Efficient Data Center Design (2024) — https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design.pdf

#### Correction 26 — I-007 (infrastructure, I07)

Réponse correcte : B. De nombreux petits échanges dépendants peuvent rendre le délai de communication déterminant, même lorsque les liens ont un débit élevé.
A — La capacité stockable n’est pas le délai d’un message.
C — Un débit élevé seul ne garantit pas de faibles délais pour de petits messages.
D — Le cache de stockage ne corrige pas nécessairement la latence de synchronisation.
[19] Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog — https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io

#### Correction 27 — I-008 (infrastructure, I08)

Réponse correcte : D. RoCE signifie RDMA over Converged Ethernet ; il exige une pile et une infrastructure compatibles.
A — Ethernet/TCP ne garantit pas un chemin RDMA ; RoCE exige une prise en charge adaptée.
B — Le domaine NVLink ne remplace pas le transport RDMA sur Ethernet demandé.
C — L’OOB n’est pas le chemin RDMA de la charge.
[19] Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog — https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io
[82] NVIDIA Onyx 3.10.4606 LTS — RoCE (direct documentation URL) — https://networking-docs.nvidia.com/onyxum/3104606lts/rdma-over-converged-ethernet-roce

#### Correction 28 — I-009 (infrastructure, I09)

Réponse correcte : D. La conception distingue les échanges dans le domaine GPU étroitement couplé et les communications entre systèmes. Certaines architectures étendent le domaine NVLink, mais cela ne change pas le sens de ce scénario.
A — Les bibliothèques compatibles peuvent exploiter plusieurs mécanismes.
B — NVLink n’est pas le routage IP général du cluster.
C — L’énoncé attribue explicitement les communications entre systèmes à InfiniBand.
[18] NVLink & NVLink Switch: Fastest HPC Data Center Platform | NVIDIA — https://www.nvidia.com/en-us/data-center/nvlink
[19] Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog — https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io
[68] Key Components of the DGX SuperPOD — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html

#### Correction 29 — I-010 (infrastructure, I10)

Réponse correcte : B. Le DPU traite des fonctions d’infrastructure et peut les isoler du domaine applicatif hôte ; ce n’est pas un remplaçant universel du CPU ou GPU.
A — Le DPU ne crée pas une VRAM unifiée universelle.
C — Le calcul principal du modèle n’est pas sa mission générale.
D — Cette description ignore les fonctions de traitement et d’isolation étudiées.
[12] Offloading and Isolating Data Center Workloads with NVIDIA Bluefield DPU | NVIDIA Technical Blog — https://developer.nvidia.com/blog/offloading-and-isolating-data-center-workloads-with-bluefield-dpu

#### Correction 30 — I-011 (infrastructure, I01)

Réponse correcte : A. Les symptômes désignent la préparation des données ; il faut traiter ce chemin et mesurer le résultat avant d’ajouter du calcul GPU.
B — Le problème indiqué n’est pas le volume stockable.
C — Des GPU supplémentaires augmentent la demande sur le chemin déjà saturé.
D — Le goulot décrit est local à la préparation CPU, pas au fabric de calcul.
[16] Introduction to NVIDIA DGX H100/H200 Systems — NVIDIA DGX H100/H200 User Guide — https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html
[74] NVIDIA Evolving Your Infrastructure for AI: Considerations for IT Leaders — https://images.nvidia.com/aem-dam/Solutions/documents/bus-leader-industry-brief-evolving-for-ai-3150350.pdf

#### Correction 31 — I-012 (infrastructure, I02)

Réponse correcte : D. Augmenter le volume stockable ne garantit pas davantage de débit ; le chemin et les ressources de service restent à dimensionner.
A — La mémoire GPU intégrée reste distincte.
B — Certaines architectures font évoluer les deux ; il faut les dimensionner.
C — Les contrôleurs, le réseau et le profil d’accès peuvent rester limitants.
[6] NVIDIA: Scaling Storage for AI Training and Inferencing — https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing

#### Correction 32 — I-013 (infrastructure, I03)

Réponse correcte : C. Le calcul pédagogique est 35 × 1,4 = 49 kW. Il ne constitue pas une mesure annuelle du PUE ni une validation électrique des circuits.
A — Cette valeur est l’écart non IT, pas le total.
B — Cette réponse omet les charges non IT du modèle.
D — Cette valeur additionne à tort la charge IT à un total qui l’inclut déjà.
[72] DOE Best Practices Guide for Energy-Efficient Data Center Design (2024) — https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design.pdf

#### Correction 33 — I-014 (infrastructure, I04)

Réponse correcte : B. La décision dépend du besoin durable, des contraintes de données et du coût complet ; aucune localisation n’est toujours la meilleure.
A — L’exploitation sur la durée et la conformité restent à examiner.
C — Le tarif isolé omet données, durée, réseau et responsabilités.
D — L’utilisation influence la comparaison du coût complet.
[74] NVIDIA Evolving Your Infrastructure for AI: Considerations for IT Leaders — https://images.nvidia.com/aem-dam/Solutions/documents/bus-leader-industry-brief-evolving-for-ai-3150350.pdf

#### Correction 34 — I-015 (infrastructure, I05)

Réponse correcte : C. Les fonctions ont des besoins différents ; la séparation peut préserver les performances et contrôler l’accès d’administration.
A — La séparation vise au contraire des besoins distincts.
B — L’accès de gestion doit être restreint et contrôlé.
D — La séparation ne prouve pas l’absence de toutes dépendances communes.
[66] Network Fabrics — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/network-fabrics.html
[68] Key Components of the DGX SuperPOD — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html

#### Correction 35 — I-016 (infrastructure, I06)

Réponse correcte : A. La capacité globale ne prouve pas que chaque entrée reçoit un air adapté ; le chemin local doit être examiné.
B — Une sonde de salle ne décrit pas nécessairement chaque entrée.
C — Les conditions locales hors spécification doivent être corrigées.
D — Ce changement peut manquer une recirculation ou un défaut local.
[72] DOE Best Practices Guide for Energy-Efficient Data Center Design (2024) — https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design.pdf
[67] Safety — NVIDIA DGX H100/H200 User Guide — https://docs.nvidia.com/dgx/dgxh100-user-guide/safety.html

#### Correction 36 — I-017 (infrastructure, I07)

Réponse correcte : D. Une liaison isolée ne représente pas tous les chemins partagés ; il faut tester le fabric sous des échanges simultanés.
A — Un test sans contention ne suffit pas pour le trafic simultané.
B — La vitesse d’un port isolé ne représente pas les chemins simultanés.
C — Le volume stockable ne décrit pas le fabric all-to-all.
[66] Network Fabrics — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/network-fabrics.html
[68] Key Components of the DGX SuperPOD — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200 — https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html

#### Correction 37 — I-018 (infrastructure, I08)

Réponse correcte : A. Les deux mécanismes traitent des aspects différents. La documentation Onyx présente des modes qui n’utilisent pas tous PFC de la même manière.
B — Ni le routage général ni l’ajout de VRAM ne définit ces fonctions.
C — Ils gèrent des aspects du trafic ; ils ne rendent pas toute congestion impossible.
D — Le signalement de congestion doit faire partie d’une conception validée.
[82] NVIDIA Onyx 3.10.4606 LTS — RoCE (direct documentation URL) — https://networking-docs.nvidia.com/onyxum/3104606lts/rdma-over-converged-ethernet-roce

#### Correction 38 — I-019 (infrastructure, I09)

Réponse correcte : D. GPUDirect RDMA vise ce chemin direct entre un équipement pair et la mémoire GPU, sous contraintes de compatibilité et de topologie.
A — Le scénario indique précisément l’évitement d’un buffer hôte intermédiaire.
B — Le chemin GPUDirect ne suppose ni DPU obligatoire ni migration du modèle.
C — L’énoncé décrit l’intervention directe d’un adaptateur réseau.
[55] 1. Overview — GPUDirect RDMA 13.4 documentation — https://docs.nvidia.com/cuda/gpudirect-rdma/index.html
[19] Accelerating IO in the Modern Data Center: Network IO | NVIDIA Technical Blog — https://developer.nvidia.com/blog/accelerating-io-in-the-modern-data-center-network-io

#### Correction 39 — I-020 (infrastructure, I10)

Réponse correcte : B. Un domaine DPU séparé peut héberger des fonctions de contrôle et de sécurité indépendantes du système applicatif hôte.
A — Cela ne fournit pas le domaine séparé demandé.
C — Le besoin porte sur l’isolation de l’infrastructure, pas sur le calcul du modèle.
D — L’isolation ne dispense pas de politiques et de maintenance.
[12] Offloading and Isolating Data Center Workloads with NVIDIA Bluefield DPU | NVIDIA Technical Blog — https://developer.nvidia.com/blog/offloading-and-isolating-data-center-workloads-with-bluefield-dpu

#### Correction 40 — O-001 (operations, O01)

Réponse correcte : A. Le BMC fournit des fonctions de gestion de plateforme, notamment console, alimentation et récupération. Un chemin OOB évite de dépendre uniquement de l'accès à l'OS hôte, sous réserve que le BMC et son réseau soient disponibles.
B — Une commande via la connexion SSH indisponible ne fournit pas un chemin de récupération distinct de l'OS hôte.
C — L'exporter expose de la télémétrie GPU ; il ne fournit pas les fonctions de console et d'alimentation de plateforme.
D — Le plugin annonce des ressources au cluster mais reste dépendant de l'environnement hôte ; ce n'est pas le contrôleur OOB.
[20] NVIDIA IGX BMC Introduction — https://docs.nvidia.com/igx-orin/bmc/latest/introduction.html
[41] Kubernetes Schedule GPUs — https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus

#### Correction 41 — O-002 (operations, O01)

Réponse correcte : B. DCGM Exporter convertit les champs DCGM sélectionnés au format d'exposition Prometheus. La collecte et la conservation des séries sont des responsabilités distinctes.
A — Une allocation de scheduler décide quelles ressources un job reçoit ; elle n'expose pas directement cette interface de télémétrie.
C — Les mesures de plateforme du BMC ne sont pas la conversion directe des champs DCGM au format Prometheus.
D — Une interrogation locale NVML ne fournit pas à elle seule l'interface d'exposition Prometheus demandée.
[57] NVIDIA Install DCGM Exporter — https://docs.nvidia.com/datacenter/dcgm/latest/installation/install-dcgm-exporter.html
[43] Slurm Generic Resource Scheduling — https://slurm.schedmd.com/gres.html
[20] NVIDIA IGX BMC Introduction — https://docs.nvidia.com/igx-orin/bmc/latest/introduction.html

#### Correction 42 — O-003 (operations, O01)

Réponse correcte : B. DCGM distingue les contrôles passifs de santé et les diagnostics actifs invasifs. Un test nécessitant l'exclusivité doit être coordonné avec l'exploitation et les travaux.
A — Le fait que DCGM serve à surveiller ne rend pas tous ses diagnostics non invasifs.
C — Supprimer les journaux ne donne pas l'exclusivité et détruit des éléments utiles au diagnostic.
D — Une lecture d'utilisation ne remplace ni un diagnostic ni une validation matérielle appropriée.
[38] NVIDIA DCGM Feature Overview — https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html

#### Correction 43 — O-004 (operations, O03)

Réponse correcte : C. L'utilisation GPU de nvidia-smi représente le temps de l'intervalle pendant lequel au moins un kernel s'exécute. Elle ne prouve ni l'efficacité des kernels ni la cause d'un faible débit applicatif.
A — L'activité temporelle n'est pas une mesure directe du rendement maximal du calcul.
B — L'utilisation GPU ne mesure pas la capacité mémoire occupée.
D — Une conclusion certaine sur le réseau exige d'autres observations ; cette métrique seule ne l'établit pas.
[39] NVIDIA System Management Interface — https://docs.nvidia.com/deploy/nvidia-smi/index.html

#### Correction 44 — O-005 (operations, O03)

Réponse correcte : D. Un modèle résident peut occuper la mémoire tout en exécutant rarement des kernels. Il faut distinguer quantité de mémoire occupée, temps d'activité mémoire et activité de calcul.
A — Ces mesures sont compatibles avec un service peu sollicité ; elles ne prouvent pas une panne.
B — Une quantité occupée élevée ne mesure pas la saturation de la bande passante mémoire.
C — L'absence relative de kernels n'implique pas l'absence d'allocations.
[39] NVIDIA System Management Interface — https://docs.nvidia.com/deploy/nvidia-smi/index.html

#### Correction 45 — O-006 (operations, O03)

Réponse correcte : B. La corrélation entre limitation thermique, baisse de fréquence et baisse de débit justifie d'examiner le refroidissement et les limites du produit. Le BMC peut compléter l'observation des capteurs de plateforme.
A — Le format des checkpoints ne correspond pas aux indices thermiques observés.
C — Modifier la puissance sans comprendre les contraintes peut aggraver le risque ; ce n'est pas l'investigation demandée.
D — Une fréquence réduite n'établit pas un manque de capacité mémoire.
[39] NVIDIA System Management Interface — https://docs.nvidia.com/deploy/nvidia-smi/index.html
[20] NVIDIA IGX BMC Introduction — https://docs.nvidia.com/igx-orin/bmc/latest/introduction.html

#### Correction 46 — O-007 (operations, O03)

Réponse correcte : D. Un Xid est un rapport d'erreur du pilote ; ses causes peuvent être matérielles, logicielles ou applicatives. Le message complet et son contexte sont nécessaires pour guider l'enquête.
A — Le code Xid seul ne prouve pas une cause matérielle unique.
B — Les Xid sont des rapports d'erreurs GPU et ne se limitent pas aux applications graphiques.
C — Effacer les preuves ne corrige pas la cause et empêche de comparer les incidents.
[37] NVIDIA Xid Errors Introduction — https://docs.nvidia.com/deploy/xid-errors/introduction.html

#### Correction 47 — O-008 (operations, O02)

Réponse correcte : B. Dans le mécanisme GRES, les ressources génériques ne sont pas attribuées au job sans demande appropriée. La réservation doit précéder l'utilisation du GPU par l'application.
A — Choisir arbitrairement une carte contourne l'allocation et peut entrer en conflit avec d'autres jobs.
C — Un contrôle de santé ne réserve pas une ressource au job.
D — Demander plus de RAM CPU ne constitue pas une demande GRES GPU.
[43] Slurm Generic Resource Scheduling — https://slurm.schedmd.com/gres.html
[38] NVIDIA DCGM Feature Overview — https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html

#### Correction 48 — O-009 (operations, O02)

Réponse correcte : D. Le device plugin du fournisseur expose les appareils spécialisés comme ressources consommables par les Pods. Un pilote hôte fonctionnel ne suffit pas à lui seul à publier cette ressource dans Kubernetes.
A — GRES relève de Slurm et ne publie pas à lui seul des ressources dans Kubernetes.
B — Le toolkit intègre l'accès des conteneurs au GPU ; le plugin est responsable de l'annonce comme ressource Kubernetes.
C — Le moteur DCGM assure des fonctions de gestion et télémétrie ; il n'est pas le device plugin Kubernetes.
[41] Kubernetes Schedule GPUs — https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus

#### Correction 49 — O-010 (operations, O04)

Réponse correcte : A. Le passthrough assigne directement le GPU physique entier à une VM. Dans le mécanisme décrit, le pilote invité utilise cet appareil exclusivement.
B — Un profil partagé temporellement ne correspond pas à l'exclusivité de la carte entière demandée.
C — Une instance matérielle plus petite utilisée en bare metal ne donne pas la carte entière à la VM demandée.
D — Une variable de visibilité conteneur ne réalise pas l'assignation directe de la carte entière à une VM.
[56] NVIDIA Using GPU Pass-Through — https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/using-gpu-pass-through.html
[58] Introduction to NVIDIA vGPU Software — https://docs.nvidia.com/vgpu/latest/grid-vgpu-user-guide/grid-vgpu-introduction.html

#### Correction 50 — O-011 (operations, O04)

Réponse correcte : C. MIG partitionne les ressources d'un GPU compatible en instances séparées, notamment avec des ressources de calcul et des chemins mémoire dédiés décrits par NVIDIA.
A — Le partage temporel sans partitionnement matériel alterne l'accès ; il ne crée pas les ressources matérielles séparées demandées.
B — L'annonce de GPU entiers ne réalise pas leur partitionnement matériel.
D — Le passthrough d'une carte entière assigne cet appareil ; il ne le divise pas en instances.
[44] NVIDIA MIG User Guide Introduction — https://docs.nvidia.com/datacenter/tesla/mig-user-guide/introduction.html
