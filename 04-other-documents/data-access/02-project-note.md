# Two-page project note (single neutral version, FR): for all recipients

**COLDSTART - Prévoir et quantifier les crises sanitaires quand les données locales manquent**

Candidature Ambizione FNS (dépôt : 3 novembre 2026) · Requérant : Dr Erol Orel · Hôte proposé :
Institut de santé globale, Faculté de médecine, UNIGE (programme de recherche indépendant) ·
Durée : 4 ans

## Le problème

Quand une crise sanitaire commence, les données locales nécessaires pour la prévoir n'existent
pas encore. Les modèles les plus performants exigent plusieurs années d'historique ; ils sont
donc les plus faibles exactement là où les décisions - armer des ambulances, ouvrir des lits,
déclencher une escalade - sont les plus coûteuses et les moins réversibles.

Il existe pourtant une information quantitative disponible dès le premier jour : la littérature
publiée sur des événements analogues - associations météo–demande, amplitudes et délais de
surcharge, durées de séjour et occupation, paramètres de transmission. Elle n'est presque
jamais utilisée comme information a priori formelle, parce que personne n'a établi si le faire
aide ou nuit.

## La question

Le projet pose la question de bout en bout : l'évidence publiée peut-elle être extraite de
façon fiable et transportée au contexte local pour prévoir l'état du système de soins quand
les données locales manquent ; peut-on détecter tôt quand elle induit en erreur ; le gain
change-t-il des décisions opérationnelles ; et la chaîne complète peut-elle tourner
automatiquement, vérifiée sur les issues observées, selon des règles pré-enregistrées ?

Le projet s'appuie sur un existant : LiteRev-Evidence, le prototype d'extraction et de
modélisation que j'ai développé ; la cartographie des données constituée pour GESICA ; et
l'étude légionellose genevoise en cours (BASEC 2026-00324), dont je dirige le volet données.

## Ce que je ferai (cinq volets, 48 mois)

1. **Extraction** - mesurer la fiabilité de l'extraction automatique de paramètres
   quantitatifs depuis la littérature, contre un étalon en double extraction humaine, et
   corriger les biais identifiés ; la littérature fournit aussi les variables explicatives,
   les familles de modèles recommandées et les définitions d'issues et de seuils.
2. **Modélisation** - représenter l'état du système de soins comme un processus à régimes
   latents (habituel / tendu / sous tension / critique) plutôt que comme un seuil appliqué à
   une prévision ponctuelle ; les modèles épidémiologiques (type SEIR) n'interviennent que
   pour les crises épidémiologiques, les crises environnementales relevant de structures
   exposition–réponse.
3. **Évaluation** - tester, épisode historique par épisode historique, si les a priori issus
   de la littérature améliorent la prévision en début de crise, en n'utilisant à chaque
   instant que les données et la littérature disponibles à cette date, avec sélection
   automatisée du meilleur modèle selon des règles pré-enregistrées.
4. **Décision** - évaluer non pas la précision statistique mais le bénéfice décisionnel, à
   partir de seuils d'escalade recueillis de façon structurée (protocole SHELF) auprès des
   régulateurs, urgentistes et gestionnaires de capacités.
5. **Automatisation et veille** - données publiques connectées automatiquement ; modèles
   relancés à la cadence de chaque variable ; hypothèses statistiques vérifiées ; veille
   quotidienne de la littérature ; en fin de projet, pour les types d'événements validés et
   sous réserve d'autorisation, un tableau de bord quotidien en mode observation, enregistré
   et évalué prospectivement, jamais décisionnel pendant le projet.

## Comment ce sera testé

Trois archétypes genevois, fixés pour toute la durée du projet : les **épidémies
respiratoires** (SARS-CoV-2, grippe, VRS) portent le test confirmatoire ; la **canicule**
(avec la pollution de l'air comme co-exposition) porte le test de généralisation, conduit
seulement si le premier réussit ; la **légionellose** genevoise est l'extension contrastante
de quatrième année (incidence de cas). Deux bras - avec et sans évidence - passent par la
même sélection automatisée pré-enregistrée ; la machinerie est d'abord validée de bout en
bout sur des **données publiques ouvertes** (benchmark public), puis sur les séries
opérationnelles genevoises.

## Les données

Uniquement des **extraits rétrospectifs agrégés au jour** : aucun identifiant, aucune donnée
individuelle, aucun enregistrement vocal, aucun texte libre. Le périmètre est le canton de
Genève : données de régulation du 144 comme série d'issue principale ; passages aux urgences
et occupation des soins intensifs comme canaux complémentaires ; médecin et pharmacien
cantonaux et SIG pour les volets environnementaux. L'accès opérationnel passerait par la
**voie officielle : une soumission à la CCER, avec moi comme requérant**, précédée des
accords de données institutionnels, préparés avant le mois 1.

## Équipe et calendrier

Programme indépendant hébergé à l'Institut de santé globale, selon les garanties du modèle
FNS (direction scientifique du requérant, supervision de l'équipe, budget, dernier auteur).
Équipe : le requérant, un collaborateur scientifique/technique (50 %) et un extracteur
indépendant contracté ; budget de projet FNS de CHF 250 000 sur 4 ans, salaire du requérant
couvert séparément. **Calendrier** : dépôt 3 novembre 2026 · décision août 2027 · début
entre septembre 2027 et septembre 2028.
