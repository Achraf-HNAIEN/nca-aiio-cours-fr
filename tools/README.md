# Quiz hors ligne NCA-AIIO

Questions originales et **non officielles**, sans dumps ni garantie de réussite. Énoncés et quatre choix en anglais ; interface, explications et analyse des distracteurs en français. Aucun seuil officiel de réussite n’est inventé.

## Dépendances

- Exécution et génération : **Python 3.10+**, bibliothèque standard uniquement.
- Quiz HTML : navigateur moderne avec JavaScript ; ni serveur, ni Node.js, ni installation JavaScript nécessaire.
- Tests Python : `pytest`.
- Tests navigateur facultatifs : paquet Python `playwright` et Chromium installé (`chromium` ou `chromium-browser` dans le PATH). Les six tests concernés sont ignorés explicitement si ces dépendances sont absentes/incomplètes. Le paquet Playwright distribué par pip inclut son pilote Node ; l’application elle-même n’en dépend pas.

Depuis la racine du dépôt :

```sh
python3 tools/quiz.py --check
python3 tools/quiz.py --exam A --mode learn
python3 tools/quiz.py --exam B --mode exam
python3 tools/build_site.py
```

Les scripts trouvent la racine à partir de leur propre emplacement : les commandes ne dépendent pas du répertoire de lancement. `--root CHEMIN` permet de travailler sur une autre banque (utile pour les tests).

**Prérequis de contenu :** `questions/essential.json`, `questions/infrastructure.json`, `questions/operations.json` et `sources/ledger.json` doivent exister et être complets. Une banque absente ou invalide produit un message d’erreur et un code de sortie 2, jamais des questions de remplacement. Le registre est lu uniquement ; aucun script ne le modifie.

## CLI

```sh
# Ordre reproductible, sans changer les choix ni l’appartenance à A/B
python3 tools/quiz.py --exam A --mode learn --seed 2026

# Un seul examen exporté, sans réponses par défaut
python3 tools/quiz.py --exam A --export revision/examen-sans-corrige.md

# Même export avec corrigé dans une section séparée en fin de document
python3 tools/quiz.py --exam B --export revision/examen-corrige.md --with-answers

# Deux examens pour lecture directe sur GitHub (questions puis corrigés séparés)
python3 tools/quiz.py --export-markdown questions
# Écrit questions/examen-A.md et questions/examen-B.md ; ne touche pas aux JSON.
```

`--export` prend un **chemin de fichier Markdown**, `--export-markdown` un **dossier**. Les dossiers sont créés si nécessaire ; un export existant au même emplacement est remplacé. `--seed ENTIER` mélange seulement l’ordre des questions dans chaque examen ; sans cette option, l’ordre de la banque est conservé. `--check` valide la banque complète sans demander de réponse.

Pendant une session : `A`, `B`, `C`, `D` puis Entrée ; une ligne vide passe la question ; `FIN` termine. Une réponse invalide est redemandée. En apprentissage, le corrigé apparaît après chaque réponse/passage. En examen, le corrigé attend la fin : limite de 60 minutes, clôture même si la saisie bloque, aucune réponse tardive acceptée. Le CLI avance sans retour arrière. EOF ou Ctrl-C clôturent avec un résultat partiel. Sans réponse = zéro point, sans pénalité supplémentaire. Le score final détaille chaque domaine et les questions sans réponse.

## Quiz HTML autonome

`python3 tools/build_site.py` génère `site/quiz.html` avec les **100 vrais enregistrements validés au moment de la génération**. Ouvrir le fichier directement (`file://`) ; copier ce seul fichier suffit. Après modification de la banque ou du registre, relancer la génération. Autre destination :

```sh
python3 tools/build_site.py --output revision/quiz-autonome.html
```

- Choix A/B et examen/apprentissage ; 50 questions par session.
- Sélectionner puis **Valider ma réponse** pour l’enregistrer. Une sélection non validée ne compte pas. Précédente/Suivante permettent de passer une question. En examen, modifier puis valider remplace la réponse enregistrée.
- Apprentissage : correction immédiate après validation et verrouillage de la question.
- Examen : aucun corrigé dans l’interface avant Terminer ou expiration ; compte à rebours de 60 minutes, contrôle de l’échéance à chaque action et lors du retour à l’onglet ; score par domaine et corrigé complet après clôture. Les réponses sont alors verrouillées.
- Recommencer efface réponses, corrigés, score et minuterie ; il faut choisir puis démarrer une nouvelle session. Recharger perd la session ; aucune persistance, requête réseau, police distante ou télémétrie.
- Navigation clavier native, labels, légende des réponses, focus visible, indications de statut et présentation adaptée au mobile. Les liens sources nécessitent une connexion et s’ouvrent séparément.

**Limite assumée :** un fichier hors ligne doit contenir les solutions pour se corriger. Elles ne sont jamais affichées avant validation/clôture selon le mode, mais restent consultables dans le code source ou les outils de développement. Il s’agit d’un outil d’autoévaluation, pas d’un dispositif anti-triche. La minuterie utilise l’horloge locale ; elle n’est pas inviolable.

## Validation

La validation impose : 100 identifiants uniques au format E/I/O-000 ; A/B seulement ; 50 questions par examen, exactement 19 Essential, 20 Infrastructure, 11 Operations ; couverture de chaque objectif local dans **chaque** examen ; quatre choix distincts et non vides ; réponse A–D ; explication non vide ; exactement les trois distracteurs incorrects ; difficulté basic/scenario ; références entières non vides et connues dans le registre ; URL des sources HTTP(S). Les enregistrements doivent être placés dans le bon fichier de domaine. Le rendu public n’embarque que id/titre/URL des sources utilisées, jamais les preuves ou chemins privés du registre.

Cette validation structurelle ne prouve ni l’exactitude technique, ni l’unicité sémantique, ni la langue du contenu : ces points nécessitent la revue humaine/indépendante de la banque.

## Tests

```sh
python3 -m pytest tests/test_quiz.py tests/test_build_site.py -q
```

Les fixtures synthétiques sont créées exclusivement dans le dossier temporaire de pytest ; elles ne sont **jamais** ajoutées à `questions/`. Couverture : schéma, identifiants, réponses/distracteurs, références, répartition et objectifs, scoring/dénominateurs par domaine, graine, CLI réelle en sous-processus, exports et corrigés différés, JSON embarqué, échappement des balises et absence de chemins privés.

Pour exercer aussi le vrai navigateur dans un environnement isolé (Chromium système nécessaire) :

```sh
python3 -m venv /chemin/vers/venv-quiz
/chemin/vers/venv-quiz/bin/pip install pytest playwright
/chemin/vers/venv-quiz/bin/python -m pytest tests/test_quiz.py tests/test_build_site.py -q
```

Les tests navigateur ouvrent réellement le fichier HTML en mode réseau hors ligne, vérifient A/B, correction différée/immédiate, score/domaines, sources, verrouillage à expiration, remise à zéro et largeur mobile. Ils avancent l’horloge du vrai Chromium via Playwright pour tester les 60 minutes sans attente réelle. Un résultat avec `skipped` n’est pas une validation navigateur complète.
