# Two-page project note: attach to the Desmettre and Larribau emails

**COLDSTART - Prévoir les crises sanitaires quand les données locales manquent**

Candidature Ambizione FNS (dépôt : 3 novembre 2026) · Requérant : Dr Erol Orel · Hôte :
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
aide ou nuit. C'est la question centrale du projet, posée de façon falsifiable.

## D'où vient le projet : la continuité avec GESICA

Le projet dérive en partie de notre travail commun dans GESICA, tout en s'en distinguant.

- **La revue systématique que nous avons co-signée** (intelligence artificielle en médecine
  préhospitalière pour les catastrophes et urgences sanitaires, soumise en 2026) montre que la prévision est la tâche la plus abordée et que l'incertitude, la transparence
  et l'explicabilité y sont rarement traitées. COLDSTART attaque précisément ces
  manques.
- **L'inventaire GESICA des sources de données** (28 sources, infectieuses et non
  infectieuses, sur GE–VD–NE) fournit la cartographie sur laquelle le protocole de données du
  projet est construit.
- **La relation de travail est établie** : l'accès aux données de la centrale 144 existe déjà
  dans le cadre de GESICA. COLDSTART est un projet distinct, avec sa propre question, son
  propre requérant et sa propre base éthique ; il ne réutilise pas l'accès GESICA.

## Ce que le projet fait (cinq volets, 48 mois)

1. **Extraction** - mesurer la fiabilité de l'extraction automatique de paramètres
   quantitatifs depuis la littérature (contre un étalon en double extraction humaine), et
   corriger les biais identifiés. Le projet s'appuie sur LiteRev-Evidence, le prototype que
   j'ai développé (recherche fédérée dans la littérature ouverte, criblage,
   extraction avec provenance), que le projet transforme en instrument validé. La littérature
   fournit aussi les variables pertinentes, les familles de modèles recommandées et les
   définitions d'issues et de seuils, transposées au contexte local.
2. **Modélisation** - représenter l'état du système de soins comme un **processus à régimes
   latents** (habituel / tendu / sous tension / critique) plutôt que comme un seuil appliqué à
   une prévision ponctuelle, avec une modélisation explicite de la queue de distribution pour
   l'état critique. Les ancrages provisoires des états sont des percentiles de la demande
   saisonnière et des indicateurs de capacité ; leur interprétation décisionnelle est précisée avec les équipes de terrain. Les
   modèles épidémiologiques (type SEIR) n'interviennent que pour les crises épidémiologiques ; les crises environnementales relèvent de structures exposition–réponse.
3. **Évaluation** - tester, épisode historique par épisode historique, si les a priori issus
   de la littérature améliorent la prévision en début de crise, en n'utilisant à chaque
   instant que les données *et la littérature* disponibles à cette date, contre des
   références établies, avec sélection automatisée du meilleur modèle selon des règles
   pré-enregistrées.
4. **Décision** - évaluer non pas la précision statistique mais **le bénéfice décisionnel**,
   à partir de seuils d'escalade recueillis de façon structurée (protocole SHELF) auprès de
   celles et ceux qui agissent dessus : régulateurs, urgentistes, gestion des capacités.
5. **Automatisation et veille** - données publiques connectées automatiquement ; modèles
   relancés à la cadence de chaque variable ; hypothèses statistiques vérifiées ; algorithmes
   comparés sur des métriques établies ; veille quotidienne de la littérature signalant toute
   évidence qui modifierait un paramètre, une variable, un seuil ou le modèle recommandé
   (mises à jour selon des règles pré-enregistrées seulement).

## Les données : ce qui serait demandé, et par quelle voie

**Ce qui serait demandé.** Un **extrait rétrospectif agrégé au jour** : date, effectifs par
motif de recours et degré d'urgence (144), ou par catégorie de passage (urgences),
idéalement par classe d'âge large. **Aucun identifiant direct, aucune donnée
individuelle, aucun enregistrement vocal, aucun texte libre.** Les données de régulation du
144 constituent la **série d'issue principale** ; le critère principal est la demande à motif
respiratoire, celui du volet canicule la demande à motifs sensibles à la chaleur
(déshydratation, rénal, psychiatrique) - d'où l'importance de catégories de motifs couvrant
les deux. Les passages aux urgences et l'occupation des soins intensifs sont des canaux complémentaires. Le périmètre est le canton de Genève au jour : un choix délibéré, appuyé sur l'écosystème
de données genevois (144, urgences, soins intensifs, médecin et pharmacien cantonaux).

**Par quelle voie.** Rien n'est demandé aujourd'hui en matière de données. Si le projet est
financé, l'accès passerait par la **voie officielle : une soumission à la CCER, avec moi comme
requérant**, précédée des accords de données institutionnels nécessaires. Ce que j'espère de
votre part à ce stade est double : une **lettre de collaboration** pour le dossier FNS
(confirmant la collaboration et sa contribution concrète - le FNS écarte les lettres de
recommandation), et un **accord de principe** sur cette voie officielle le moment venu.
Le dispositif est d'abord validé de bout en bout sur des **données publiques ouvertes** ;
la faisabilité ne repose donc pas sur un seul accord, et ce sont vos séries qui transforment
un résultat méthodologique en résultat opérationnel.

## Ce que vous y gagnez

- Une évaluation indépendante et pré-enregistrée de la valeur réelle des prévisions précoces.
- Des seuils d'escalade explicités et documentés, construits avec vos équipes.
- Pour les types d'événements dont les modèles auront été validés, un **tableau de bord
  quotidien en mode observation** pour vos équipes (régulation 144, urgences, soins
  intensifs) : états et prévisions rafraîchis automatiquement, enregistrés, jamais décisionnels
  pendant le projet ; le noyau d'une future plateforme de surveillance.
- Publications communes, dans la continuité de GESICA.

**Calendrier.** Dépôt : 3 novembre 2026 · Décision : août 2027 · Début : entre septembre
2027 et septembre 2028. Lettre de collaboration souhaitée d'ici la mi-octobre 2026.
