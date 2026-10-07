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
aide ou nuit. C'est la question centrale du projet, posée de façon falsifiable : si les a
priori issus de la littérature n'améliorent pas la prévision, ou si leurs effets nuisibles ne
peuvent pas être détectés à temps, le projet l'établira aussi - et ce résultat-là serait
également utile.

## D'où vient le projet : la continuité avec GESICA

Le projet dérive en partie de notre travail commun dans GESICA, tout en s'en distinguant.

- **La revue systématique que nous avons co-signée** (intelligence artificielle en médecine
  préhospitalière pour les catastrophes et urgences sanitaires, soumise en 2026) montre que la
  prévision est la tâche la plus fréquemment abordée, et que l'incertitude, la transparence et
  l'explicabilité y sont rarement traitées explicitement. COLDSTART attaque précisément ces
  manques : incertitude propagée de bout en bout, règles d'évaluation pré-enregistrées,
  bénéfice décisionnel comme critère final.
- **L'inventaire GESICA des sources de données** (28 sources, infectieuses et non
  infectieuses, sur GE–VD–NE) fournit la cartographie sur laquelle le protocole de données du
  projet est construit.
- **La relation de travail est établie** : l'accès aux données de la centrale 144 existe déjà
  dans le cadre de GESICA. COLDSTART est un projet distinct, avec sa propre question, son
  propre requérant et sa propre base éthique ; il ne réutilise pas l'accès GESICA.

## Ce que le projet fait (quatre volets, 48 mois)

1. **Extraction** - mesurer la fiabilité de l'extraction automatique de paramètres
   quantitatifs depuis la littérature (contre un étalon en double extraction humaine), et
   corriger les biais identifiés. Le projet s'appuie sur LiteRev-Evidence, le prototype que
   j'ai développé (recherche fédérée en direct dans la littérature ouverte, criblage,
   extraction avec provenance), que le projet transforme en instrument validé.
2. **Modélisation** - représenter l'état du système de soins comme un **processus à régimes
   latents** (habituel / tendu / sous tension / critique) plutôt que comme un seuil appliqué à
   une prévision ponctuelle, avec une modélisation explicite de la queue de distribution pour
   l'état critique. Les ancrages provisoires des états sont des percentiles de la demande
   saisonnière et des indicateurs de capacité (occupation des soins intensifs, attente aux
   urgences) ; ils sont affinés avec les équipes de terrain, pas imposés. Ces outils viennent
   de l'économétrie financière, où j'ai travaillé quinze ans.
3. **Évaluation** - tester, épisode historique par épisode historique, si les a priori issus
   de la littérature améliorent la prévision en début de crise, en n'utilisant à chaque
   instant que les données *et la littérature* disponibles à cette date (reconstruction
   stricte de l'information), contre des références établies (modèles saisonniers,
   algorithmes de surveillance, nowcasting bayésien).
4. **Décision** - évaluer non pas la précision statistique mais **le bénéfice décisionnel**,
   à partir de seuils d'escalade recueillis de façon structurée (protocole SHELF) auprès de
   celles et ceux qui agissent dessus : régulateurs, urgentistes, gestion des capacités.

## Les données : ce qui serait demandé, et par quelle voie

**Ce qui serait demandé.** Un **extrait rétrospectif agrégé au jour** : date, effectifs par
motif de recours / catégorie large et degré d'urgence (144), ou par catégorie de passage
(urgences), idéalement par classe d'âge large. **Aucun identifiant direct, aucune donnée
individuelle, aucun enregistrement vocal, aucun texte libre.** Les données de régulation du
144 constituent la **série d'issue principale** ; le critère principal est la demande à motif
respiratoire, celui du volet canicule la demande à motifs sensibles à la chaleur
(déshydratation, rénal, psychiatrique) - d'où l'importance de catégories de motifs couvrant
les deux. Les passages aux urgences et l'occupation des soins intensifs sont des canaux
d'observation complémentaires. Le périmètre est le canton de Genève au jour ; une validation
externe pré-spécifiée est prévue sur GE–VD–NE.

**Par quelle voie.** Rien n'est demandé aujourd'hui en matière de données. Si le projet est
financé, l'accès passerait par la **voie officielle : une soumission à la CCER, avec moi comme
requérant**, précédée des accords de données institutionnels nécessaires. Ce que j'espère de
votre part à ce stade est double : une **lettre de collaboration** pour le dossier FNS
(confirmant la collaboration et sa contribution concrète - le FNS écarte les lettres de
recommandation), et un **accord de principe** sur cette voie officielle le moment venu.

## Ce que vous y gagnez

- Une évaluation indépendante et pré-enregistrée de ce que valent réellement les prévisions
  précoces pour la planification des ressources - y compris un résultat négatif, s'il est
  négatif.
- Des seuils d'escalade explicités et documentés, construits avec vos équipes.
- Un déploiement en **mode observation** en fin de projet : les prévisions sont enregistrées,
  non utilisées pour décider - aucun impact clinique, aucune charge opérationnelle.
- Publications communes, dans la continuité de la revue systématique GESICA.

## Calendrier

Dépôt : 3 novembre 2026 · Phase 1 : avril 2027 · Entretien (sciences de la vie) : 3–4 juin
2027 · Décision : août 2027 · Début : entre le 1er septembre 2027 et le 1er septembre 2028.
Pour le dossier : lettre de collaboration souhaitée d'ici la mi-octobre 2026.
