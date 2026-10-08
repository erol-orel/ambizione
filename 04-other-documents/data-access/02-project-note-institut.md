# Two-page project note, institutional variant: for Keiser, Ray and Calmy

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
aide ou nuit. C'est la question centrale du projet, posée de façon falsifiable, de
l'extraction jusqu'au système qui tourne et se vérifie.

## D'où vient le projet : LiteRev-Evidence et l'écosystème genevois

- **LiteRev-Evidence**, le prototype que j'ai développé à l'Institut (recherche fédérée dans la
  littérature ouverte, criblage, extraction avec provenance, agrégation en distributions de
  paramètres, ajustement et classement automatisés de modèles candidats), parcourt déjà ce
  pipeline ; le projet le transforme en instrument validé et le met à l'épreuve.
- **GESICA** fournit la cartographie des données (inventaire référencé de 28 sources de
  surveillance) et les relations de travail avec la médecine d'urgence des HUG et la CASU-144 ;
  la revue systématique commune sur l'IA en médecine préhospitalière (soumise en 2026) montre
  que la prévision y est la tâche la plus abordée et que l'incertitude y est rarement traitée.
- **L'étude légionellose genevoise** (BASEC 2026-00324, éthique accordée), dont je dirige le
  volet données, fournit l'archétype contrastant du volet d'extension.

## Ce que le projet fait (cinq volets, 48 mois)

1. **Extraction** - mesurer la fiabilité de l'extraction automatique de paramètres quantitatifs
   depuis la littérature (contre un étalon en double extraction humaine) et corriger les biais ;
   la littérature fournit aussi les variables explicatives, les familles de modèles recommandées
   et les définitions d'issues et de seuils, transposées au contexte local.
2. **Modélisation** - représenter l'état du système de soins comme un **processus à régimes
   latents** (habituel / tendu / sous tension / critique) plutôt que comme un seuil appliqué à
   une prévision ponctuelle ; les modèles épidémiologiques (type SEIR) n'interviennent que pour
   les crises épidémiologiques, les crises environnementales relevant de structures
   exposition–réponse.
3. **Évaluation** - tester, épisode historique par épisode historique, si les a priori issus de
   la littérature améliorent la prévision en début de crise, en n'utilisant à chaque instant que
   les données *et la littérature* disponibles à cette date, avec sélection automatisée du
   meilleur modèle selon des règles pré-enregistrées.
4. **Décision** - évaluer non pas la précision statistique mais **le bénéfice décisionnel**, à
   partir de seuils d'escalade recueillis de façon structurée (protocole SHELF) auprès des
   régulateurs, urgentistes et gestionnaires de capacités.
5. **Automatisation et veille** - données publiques connectées automatiquement ; modèles
   relancés à la cadence de chaque variable ; hypothèses statistiques vérifiées ; veille
   quotidienne de la littérature ; en fin de projet, pour les types d'événements validés et sous
   réserve d'autorisation, un **tableau de bord quotidien en mode observation**, enregistré et
   évalué prospectivement sur les issues observées, jamais décisionnel pendant le projet.

## Les données et la voie réglementaire

Le projet n'utilise que des **extraits rétrospectifs agrégés au jour** (aucun identifiant,
aucune donnée individuelle, aucun texte libre). Le périmètre est le canton de Genève : données
de régulation du 144 comme série d'issue principale, passages aux urgences et occupation des
soins intensifs comme canaux complémentaires, médecin et pharmacien cantonaux et SIG pour les
volets environnementaux. La machinerie est d'abord validée de bout en bout sur des **données
publiques ouvertes** (benchmark public) ; la faisabilité ne dépend donc d'aucun accord unique.
L'accès opérationnel passerait par la **voie officielle : soumission à la CCER avec moi comme
requérant**, précédée des accords de données institutionnels, préparés avant le mois 1.

## L'hébergement à l'ISG

Le programme serait conduit comme un **programme de recherche indépendant aux côtés des groupes
de l'Institut**, selon les garanties du modèle FNS (direction scientifique du requérant, choix
et supervision des collaborateurs, autorité budgétaire, publication en dernier auteur). La
confirmation détaillée est signée par la personne de contact (Prof. Keiser) et la direction de
l'Institut (Prof. Ray). **Aucune implication financière pour l'Institut** : le FNS couvre le
salaire du requérant et un budget de projet (CHF 250 000 sur 4 ans ; doctorants et post-doctorants
exclus par les règles 2026). Restent à l'Institut : les instruments ouverts validés (étalon
d'extraction, benchmark public, bibliothèque évidence-vers-a-priori), le noyau du tableau de
bord, et les publications.

**Calendrier.** Dépôt : 3 novembre 2026 · Décision : août 2027 · Début : entre septembre 2027
et septembre 2028 · Signatures de la confirmation souhaitées d'ici le mardi 14 octobre 2026.
