# Validation du cours

## État d'intégration

La banque réelle est intégrée : **100 questions originales**, deux séries de 50 avec répartition 19/20/11, les 22 objectifs présents dans chaque série. Le registre et les liens des chapitres sont contrôlés séparément de la vérification technique des explications.

**Quatre revues indépendantes terminées** : [connaissances IA](revue-essential.md), [infrastructure](revue-infrastructure.md), [opérations](revue-operations.md) et [supports](revue-supports.md). Les rapports énumèrent les 100 questions relues. Les 15 constats (3 moyens, 12 faibles) ont été traités dans le [journal des corrections](corrections.md). Les rapports originaux conservent leur état pré-correction ; les tests finaux portent sur les fichiers corrigés. Aucune erreur technique bloquante n’a été identifiée par ces revues, sans que cela constitue une garantie d’absence d’erreur.

## Résultats réellement exécutés

| Contrôle | Résultat observé | Preuve |
|---|---|---|
| Quiz et générateur, tests Python et Chromium | 54 tests réussis, aucun ignoré dans l’environnement isolé | [Journal final](tests-final.txt) |
| Labs CPU, tests internes | 6 tests réussis | [Journal](tests-labs.txt) |
| Chargement de la banque réelle | 100 questions, schémas/références/pondérations/objectifs valides | `python3 tools/quiz.py --check` |
| Exports Markdown et HTML autonome | Générés depuis les trois fichiers JSON réels | `python3 tools/quiz.py --export-markdown questions` puis `python3 tools/build_site.py` |
| Session navigateur sur A | 50 réponses correctes injectées → 50/50 ; 50 corrigés | [Résultats UI](tests-ui.json) |
| Session navigateur sur B | 50 réponses incorrectes injectées → 0/50 ; 50 corrigés | [Résultats UI](tests-ui.json) |
| Modes et remise à zéro | Pas de correction avant clôture en examen ; correction et verrouillage en apprentissage ; remise à zéro effective ; aucune erreur JS observée | [Résultats UI](tests-ui.json) |
| Citations des documents d'étude | 18 documents vérifiés, zéro erreur ; toutes les sources citées disposent d'au moins un extrait d'appui | Vérificateur de citations exécuté avec `--evidence` |

Les scores 50/50 et 0/50 ci-dessus testent le **calcul du logiciel avec des réponses connues**, pas les connaissances d'un candidat. Ils ne valident pas à eux seuls les réponses techniques.

## Reproduire les contrôles

Depuis la racine du dépôt :

```bash
python3 tools/quiz.py --check
python3 tools/quiz.py --export-markdown questions
python3 tools/build_site.py
python3 tools/labs_cpu.py
python3 tools/labs_cpu.py --test
python3 -m pytest -q
```

La dernière commande nécessite pytest. Les six tests navigateur nécessitent également le paquet Python Playwright et Chromium. Dans un environnement sans ces dépendances fonctionnelles, ils sont explicitement ignorés : **un résultat avec tests ignorés n'est pas une validation navigateur complète**. Les programmes livrés restent exécutables avec la bibliothèque standard Python ; Playwright n'est pas une dépendance du quiz ou des labs.

Les tests de cette session ont été exécutés avec un environnement Python isolé comprenant les dépendances navigateur fonctionnelles. Les tests de minuterie avancent l'horloge du navigateur : ils ne prétendent pas avoir attendu réellement une heure. Les fixtures synthétiques des tests ne sont pas utilisées comme banque de questions du livrable.

## Contrôle de publication

- 90 liens Markdown locaux vérifiés contre les fichiers destinés au dépôt, avec contrôle des ancres.
- Aucun fichier de recherche privée, cache Python ou secret détecté par le contrôle de motifs avant publication. Ce contrôle automatique ne constitue pas un audit de sécurité exhaustif.
- Les textes intégraux récupérés restent exclus de Git ; les sources citées possèdent des extraits brefs et le registre ne contient aucun chemin privé absolu.

## Limites

- Aucun GPU, cluster, hyperviseur ou réseau InfiniBand n'a été installé ou administré pour valider les exemples du cours.
- Les commandes GPU sont des exemples optionnels, à confronter au matériel, aux versions et aux autorisations du site.
- Les labs CPU démontrent des notions sur des jeux de données originaux et fictifs ; ils ne constituent pas des benchmarks NVIDIA.
- Les retours communautaires sont attribués à leurs auteurs, pas présentés comme des règles officielles.
- Le registre fournit des références et des extraits brefs, pas des copies intégrales des pages. Les extraits redondants ou trop longs ont été réduits avant publication.
- Une revue par agents ne remplace ni la documentation du produit installé ni une validation officielle NVIDIA.
