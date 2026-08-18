# One-page project note — attach to the request

**COLDSTART — Prévoir les crises sanitaires quand les données locales manquent**
Candidature Ambizione FNS · Requérant : Dr Erol Orel · Hôte : DS4DH, Département de radiologie et
informatique médicale, Faculté de médecine, UNIGE · Durée : 4 ans

## Le problème

Quand une crise sanitaire commence, les données locales nécessaires pour la prévoir n'existent pas
encore. Les modèles les plus performants exigent plusieurs années d'historique ; ils sont donc les
plus faibles exactement là où les décisions sont les plus coûteuses et les moins réversibles.

Il existe pourtant une information disponible dès le premier jour : la littérature publiée sur des
événements analogues — associations météo–demande, amplitudes de surcharge, paramètres de
transmission. Elle n'est pas utilisée quantitativement, parce que personne n'a établi si le faire
aide ou nuit.

## Ce que le projet fait

1. **Extraction** — mesurer la fiabilité de l'extraction automatique de paramètres quantitatifs
   depuis la littérature, et corriger le biais identifié. Le projet s'appuie sur LiteRev-Evidence,
   plateforme que j'ai développée (>80 000 publications indexées).
2. **Modélisation** — représenter l'état du système de soins comme un **processus à régimes
   latents** (habituel / tendu / sous tension / critique) plutôt que comme un seuil appliqué à une
   prévision ponctuelle, avec une modélisation de la queue de distribution pour l'état critique.
   Ces outils viennent de l'économétrie financière, où j'ai travaillé quinze ans.
3. **Évaluation** — tester si les a priori issus de la littérature améliorent la prévision en
   début de crise, en n'utilisant à chaque instant que les données *et la littérature* disponibles
   à cette date.
4. **Décision** — évaluer non pas la précision statistique mais **le bénéfice décisionnel**, à
   partir de seuils d'escalade recueillis auprès de celles et ceux qui agissent dessus.

## Ce que je demanderais aux HUG / à la CASU 144

Un **extrait rétrospectif agrégé au jour** : date, effectifs, catégorie large. Aucun identifiant
direct, aucun texte libre. L'accès se ferait sous approbation CCER.

## Ce que vous y gagnez

- Une évaluation indépendante de ce que valent réellement les prévisions précoces pour la
  planification des ressources — y compris un résultat négatif, s'il est négatif.
- Des seuils d'escalade explicités et documentés, construits avec vos équipes.
- Un déploiement en **mode observation** en fin de projet : les prévisions sont enregistrées, non
  utilisées pour décider — aucun impact clinique, aucune charge opérationnelle.
- Publications communes, dans la continuité de la revue systématique GESICA.

## Calendrier

Dépôt : 3 novembre 2026. Décision : `[[~mi-2027]]`. Début : `[[fin 2027]]`.
