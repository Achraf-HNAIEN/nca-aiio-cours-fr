# Corrections après les revues indépendantes

Les quatre rapports de revue décrivent **l'état relu avant correction**, avec leurs constatations et limites. Les éventuelles clés et empreintes qu'ils contiennent correspondent à cet état historique, pas nécessairement au fichier final. Ce journal décrit les modifications d'intégration appliquées ensuite.

## Suivi des constats

| Constat | Correction appliquée | Vérification |
|---|---|---|
| RE-01 | E-026 précise maintenant la saturation de bande passante mémoire, sans confondre latence et capacité. | Énoncé et explication comparés à la proposition du relecteur. |
| RE-02 | Référence MLflow [83] ajoutée au suivi des expériences : question E-018, chapitre 02 et flashcard. | Identifiant connu et extrait d'appui présent. |
| RE-03 | Référence de déploiement [84] ajoutée au rollback : question E-036, chapitre 02 et flashcard. | Exemple primaire de mécanisme ; aucun nouvel objectif AWS imposé. |
| INF-01 | Choix des 40 questions infrastructure permutés selon la proposition du relecteur. | Texte correct inchangé ; association entre chaque distracteur et son explication conservée ; cinq A/B/C/D par série. |
| INF-02 | I-021 précise la co-résidence de tous les tenseurs nécessaires à une étape ; référence [79] ajoutée. | Énoncé, explication et source contrôlés. |
| INF-03 | La carte sur le liquide demande si le besoin de rejet thermique disparaît, pas si le liquide retire la chaleur des composants. | Sens anglais/français aligné. |
| INF-04 | Métadonnée GPUDirect [55] corrigée et blocs Sources régénérés. | URL et identifiant inchangés. |
| OPS-01 | Choix des 22 questions opérations permutés, avec clé et explications remappées. | Texte correct et associations des distracteurs conservés ; motif ABCD supprimé. |
| OPS-02 | Référence Docker [53] ajoutée à la comparaison des noyaux conteneur/VM. | Source primaire directe, bloc Sources régénéré. |
| OPS-03 | Référence de la table de GPU supportés [61] ajoutée à la discussion MIG. | Portée par modèle conservée, sans maximum universel. |
| SUP-01 | Rappel E04/E05 ajouté aux fiches, avec liens vers les sections sourcées et exercice de comparaison. | Liens locaux et périmètre contrôlés. |
| SUP-02 | `memory_budget` et `pipeline` refusent les entrées numériques non finies. | Régressions observées en échec avant correction, puis réussies ; sorties par défaut inchangées. |
| SUP-03 | Adaptation des heures limitée aux blocs de travail ; chaque essai chronométré conserve ses 60 minutes. | Règle et planning relus ensemble. |
| SUP-04 | Référence au processus d'agents remplacée par les liens vers les deux séries. | Liens vers les fichiers livrés. |
| SUP-05 | Titre de la documentation Python [54] corrigé sans l'assimiler à la version d'exécution. | Métadonnée et références régénérées. |

## Contrôles d’intégration supplémentaires

Un lien de lab vers le répertoire de recherche privé a été remplacé par le journal publié. Les références de la revue des supports ont été renumérotées depuis son registre local vers le registre commun, sans modifier les constats. Les traces historiques restent distinguées des résultats après correction.

## Contrôles de non-régression

- **54 tests automatisés réussis**, dont les six tests Chromium, dans l'environnement isolé avec les dépendances fonctionnelles.
- **6 tests internes des labs réussis** ; les six exercices restent CPU-only et ne mesurent aucun GPU réel.
- Vérification de la banque : **100 questions, deux examens de 50, répartition 19/20/11 et 22 objectifs dans chaque série**.
- Les permutations ne modifient ni l'énoncé, ni le texte de la bonne réponse, ni l'association texte de distracteur → explication ; seules les lettres et positions changent.
- Les exports Markdown et le HTML autonome sont régénérés depuis les fichiers JSON corrigés.
- Les rapports originaux restent disponibles pour rendre visible la différence entre détection d'un constat et correction de ce constat.

Le [rapport de validation](validation.md) regroupe les résultats. Les revues sont documentaires et pédagogiques : elles ne constituent pas une validation officielle NVIDIA, une preuve exhaustive d'absence d'erreur ou un test de déploiement matériel.
