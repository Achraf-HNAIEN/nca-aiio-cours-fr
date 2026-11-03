# 00 — Se préparer au NCA-AIIO sans apprendre des réponses par cœur

> Cours indépendant en français pour un examen en anglais. Les questions de ce dépôt sont des créations pédagogiques : elles ne proviennent pas de l'examen et ne constituent pas un produit NVIDIA.

## 1. Ce que l'examen cherche à vérifier

Le **NVIDIA-Certified Associate: AI Infrastructure and Operations (NCA-AIIO)** évalue les notions fondamentales nécessaires pour comprendre une infrastructure IA et son exploitation. La page NVIDIA décrit un examen de niveau Associate, en ligne avec surveillance à distance, composé de **50 questions en 60 minutes**, proposé en anglais, au prix affiché de **125 USD**. La certification est annoncée valable deux ans. Ces informations ont été consultées le **3 novembre 2026** ; les conditions applicables au moment de ton inscription doivent être revérifiées sur le site officiel.[1]

Le prérequis indiqué dans les détails de l'examen est une compréhension élémentaire de l'infrastructure d'un datacenter. Le diplôme universitaire et l'expérience en datacenter apparaissent dans les **qualifications recommandées** : il ne faut pas transformer ces recommandations en obligations d'admission.[1]

Ce parcours n'est donc ni un cours complet d'entraînement de réseaux neuronaux en Python, ni une préparation avancée d'administrateur InfiniBand. Son fil conducteur est : **quel besoin métier, quel calcul, quelle infrastructure, quel fonctionnement opérationnel ?** La profondeur proposée dans certains labs sert à comprendre les mécanismes, pas à prédire le niveau exact d'une question.

## 2. Les trois domaines : apprendre à relier les couches

| Domaine officiel | Poids publié | Question de raisonnement à se poser |
|---|---:|---|
| Essential AI Knowledge | 38 % | Que fait la charge IA et quel rôle joue chaque composant logiciel ou matériel ? |
| AI Infrastructure | 40 % | Quelles ressources et quelles interconnexions permettent de l'exécuter correctement ? |
| AI Operations | 22 % | Comment la déployer, la partager, l'observer et diagnostiquer ses limites ? |

Les poids proviennent du programme publié par NVIDIA.[1] Dans nos examens blancs, nous choisissons **19, 20 et 11 questions**, respectivement, pour représenter ces proportions sur 50 questions. C'est une construction pédagogique ; la page officielle ne promet pas cette répartition exacte pour chaque session réelle.

Les identifiants **E01–E08, I01–I10 et O01–O04** sont nos repères locaux. Ils servent à relier chaque objectif, chapitre et question dans la [matrice de couverture](../quality/couverture-objectifs.md). Ce ne sont pas des codes publiés par NVIDIA.

### Une même situation traverse les trois domaines

Exercice mental : une équipe veut mettre en production un service de génération de texte. Commence par identifier ce qui relève de chaque couche, sans chercher immédiatement un nom de produit :

1. **Besoin** : faut-il entraîner un modèle, l'adapter, ou seulement servir un modèle existant ?
2. **Critères d'acceptation** : quelle qualité de réponse, quelle latence, quel débit, quel budget ?
3. **Données** : où résident-elles, qui peut les utiliser, quelles contraintes de confidentialité ?
4. **Calcul** : quelle mémoire et quelle capacité de calcul sont nécessaires ?
5. **Transport** : les échanges limitants sont-ils entre CPU et GPU, entre GPU, vers le stockage ou vers les utilisateurs ?
6. **Exploitation** : comment réserver les ressources, détecter un ralentissement et réagir à une panne ?

Ce questionnaire est une méthode d'analyse proposée par ce cours. À la fin du parcours, tu dois pouvoir y répondre sans confondre les fonctions des différentes briques.

## 3. Utiliser le cours en trois passages

### Passage 1 — Comprendre et expliquer

Lis les huit chapitres dans l'ordre. Pour chaque section, ferme la page et reformule en français, puis prononce les termes importants en anglais. Si tu n'arrives qu'à réciter une définition, cherche un exemple : quelle décision cette définition te permet-elle de prendre ?

Objectif personnel : expliquer pourquoi une réponse serait adaptée à une situation et pourquoi les alternatives ne le seraient pas. La mémorisation d'un nom de solution n'est utile que si tu sais le relier à sa fonction.

### Passage 2 — Comparer et pratiquer

Utilise les tableaux des [fiches express](../revision/fiches-express.md), puis réalise les [labs sans GPU](../pratique/labs-sans-gpu.md). Les exercices CPU illustrent des raisonnements : ils ne mesurent pas les performances d'un cluster NVIDIA. Les [labs avec GPU](../pratique/labs-avec-gpu.md) sont optionnels et exigent un environnement compatible ; une commande présentée dans le cours n'est pas la preuve de son exécution sur ta machine.

Constitue ton journal d'erreurs avec cinq colonnes :

| Question ou notion | Mon raisonnement initial | Erreur précise | Règle corrigée | Quand retester |
|---|---|---|---|---|
| Exemple personnel | Ce que j'avais supposé | Confusion de fonction, de métrique ou de périmètre | Une phrase explicative | Dans deux jours |

Ne note pas seulement une lettre correcte. Une lettre ne te prépare pas à un scénario reformulé.

### Passage 3 — Répondre en anglais sous contrainte

Utilise le mode apprentissage pour obtenir une correction après chaque réponse. Réserve au moins une des deux séries de 50 questions pour une première tentative chronométrée, sans consulter les explications. Si tu recommences une série connue, considère le résultat comme un exercice de consolidation, pas comme une nouvelle mesure indépendante de préparation.

Conseil de travail, **pas seuil officiel** : vise deux tentatives solides sur des questions réellement comprises, sans faiblesse persistante dans un domaine. Ce dépôt ne présente aucun pourcentage comme un seuil NVIDIA de réussite et ne peut pas garantir l'obtention de la certification.

## 4. Lire les questions anglaises sans se faire piéger

Les exemples ci-dessous sont des conseils de lecture, pas une description garantie du format des questions réelles.

- **Most appropriate / best** : chercher la meilleure solution pour les contraintes données, et non une solution simplement possible.
- **Primary purpose** : identifier le rôle principal, sans attribuer à une brique toutes les fonctions du système.
- **Compared with** : préciser ce qui est comparé ; débit, latence, isolation, coût, capacité mémoire et simplicité d'exploitation ne sont pas synonymes.
- **Training / inference** : identifier l'étape de travail avant de choisir l'architecture.
- **Within a server / across nodes** : localiser le trajet des données avant de choisir une interconnexion.
- **Observed / likely / next step** : distinguer une mesure, une hypothèse et l'action permettant de la vérifier.
- **Always / only / guarantees** : examiner si la proposition oublie une condition de compatibilité, une version ou une limitation matérielle. Une formulation absolue n'est pas automatiquement fausse, mais elle mérite d'être justifiée.

Méthode proposée : reformuler la contrainte essentielle en une phrase, éliminer les réponses qui ne remplissent pas la fonction demandée, puis comparer les réponses restantes sur la contrainte précise. Ne remplace pas une lecture du scénario par une association automatique « mot-clé → produit ».

## 5. Ce qui vient de NVIDIA et ce qui vient du cours

| Élément | Statut |
|---|---|
| Intitulé, format annoncé, domaines, poids et liste d'objectifs | Informations de la page officielle, datées et sourcées.[1] |
| Formation AI Infrastructure and Operations Fundamentals | Formation recommandée par NVIDIA, annoncée d'une durée typique de sept heures sur la page de certification.[1] |
| Explications françaises, exemples et calculs | Synthèse pédagogique indépendante, avec sources techniques lorsqu'elle décrit des fonctions de produits. |
| Examens blancs, flashcards et conseils de préparation | Créations originales ; ni questions officielles, ni prédiction de la session réelle. |
| Témoignages et guides communautaires | Ressources complémentaires évaluées séparément ; pas autorité sur le programme ou les règles. |

La formation officielle et les questions publiques accessibles dans la rubrique **Practice Questions** constituent des ressources distinctes à consulter depuis [la page NVIDIA](https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate/).[1] Ce dépôt ne contourne pas une connexion, ne reproduit pas une formation payante et ne prétend pas fournir tous ses contenus.

## 6. Checklist avant décembre

- [ ] Lire le [plan de révision adaptable](../revision/plan-decembre.md) et placer les séances selon la date réelle de l'examen.
- [ ] Pouvoir expliquer les 22 objectifs locaux sans notes.
- [ ] Reconnaître les termes du [glossaire anglais–français](../revision/glossaire-en-fr.md).
- [ ] Réaliser les labs CPU et expliquer leurs limites.
- [ ] Passer les deux séries originales, analyser les erreurs et revisiter les chapitres concernés.
- [ ] Consulter les questions d'entraînement publiques de NVIDIA et les ressources officielles indiquées.
- [ ] Revérifier les [FAQ et politiques NVIDIA](https://www.nvidia.com/en-us/learn/certification/#faq), les conditions Certiverse, l'identité requise, la compatibilité du poste, l'environnement de surveillance, le fuseau horaire, les délais de report et le tarif applicable.

Ne présume pas qu'une règle de report ou de surveillance est identique à celle d'une autre certification. Ce cours renvoie aux politiques en vigueur plutôt que d'inventer un résumé contractuel.

## 7. Auto-évaluation de départ

Réponds sans ouvrir les chapitres. Il ne s'agit pas d'un test noté :

1. Comment distinguer entraînement et inférence dans une demande métier ?
2. Pourquoi « davantage de GPU » n'est-il pas à lui seul un plan de dimensionnement ?
3. Quelles couches faut-il examiner lorsqu'une application est lente ?
4. Quelle différence fais-tu entre une capacité mémoire, un débit et une latence ?
5. Sais-tu séparer une observation de monitoring de l'explication de sa cause ?

Garde tes réponses et réécris-les après les chapitres 03, 06 et 08. La progression attendue est un raisonnement plus précis, pas seulement un vocabulaire plus long.

## Sources

[1] https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate — AI Infrastructure and Operations (AIIO) Certification for Professionals | NVIDIA
