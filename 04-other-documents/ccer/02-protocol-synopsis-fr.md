# Synopsis de protocole (français, prêt pour BASEC): v0.1

> Rédigé sur le modèle du protocole légionellose v1.4 (BASEC 2026-00324). Les `[[…]]` sont les
> éléments que seul le requérant ou les détenteurs de données peuvent fournir.

**Titre :** COLDSTART - Valeur des connaissances publiées pour la prévision de la demande
d'urgence en début de crise sanitaire : réutilisation d'extraits agrégés des données
opérationnelles genevoises (2015–2026)

**Requérant (investigateur principal) :** Dr Erol Orel, Institut de santé globale, Faculté de
médecine, Université de Genève. **Promoteur :** `[[UNIGE / ISG - à confirmer]]`

**Catégorie :** Réutilisation de données personnelles liées à la santé, sans consentement
(art. 34 LRH) `[[ou : demande de clarification de compétence si agrégation à la source - voir
01-route-strategy.md]]`. Risque : catégorie A (données uniquement, aucune intervention).

## 1. Contexte et justification

Au début d'une crise sanitaire, les données locales nécessaires à la prévision de la demande
d'urgence n'existent pas encore. Le projet détermine si l'évidence quantitative publiée,
extraite et agrégée automatiquement, améliore la prévision probabiliste dans cette fenêtre - et
quand elle induit en erreur. L'évaluation repose sur la reconstruction rétrospective de crises
passées (épidémies respiratoires ; canicules), en n'utilisant à chaque origine de prévision que
l'information disponible à cette date.

## 2. Objectif nécessitant les données

Constituer les séries d'issue et d'observation : (i) **demande d'urgence quotidienne par motif
de recours et degré d'urgence** dérivée des données de régulation de la CASU-144 (critère
principal : motifs respiratoires ; critère du volet canicule : motifs sensibles à la chaleur -
déshydratation, rénal, psychiatrique) ; (ii) passages aux urgences par catégorie (canal
complémentaire) ; (iii) occupation des soins intensifs (canal complémentaire).

## 3. Données demandées

Voir la spécification jointe (`03-data-specification.md`). En résumé : **comptes quotidiens
agrégés**, période `[[2015]]`–2026, par motif/catégorie, degré d'urgence et classe d'âge large ;
**aucun identifiant direct, aucune donnée individuelle nominative, aucun texte libre, aucun
enregistrement vocal**. `[[Sous-échantillon de validation du codage : à décrire si la voie C est
retenue - taille, variables, pseudonymisation.]]`

## 4. Justification de l'absence de consentement (si art. 34 LRH)

Environ dix années d'appels (~165'000/an toutes catégories) ; recueillir un consentement
individuel est impossible en pratique (volume, absence de canal de contact, biais de sélection
qui invaliderait la série). Les données demandées sont agrégées, l'intérêt de la recherche est
prépondérant et aucun intérêt des personnes concernées n'est menacé : aucune décision individuelle,
aucun recontact, aucune ré-identification possible au niveau des comptes journaliers.
`[[Vérifier les seuils de petits effectifs : les comptes rares (p.ex. motif × âge × jour < 5)
seront regroupés selon la règle convenue avec les détenteurs.]]`

## 5. Traitement, sécurité et conservation

Traitement dans l'environnement sécurisé de l'UNIGE `[[Baobab/Yggdrasil sécurisé - préciser]]` ;
accès limité au requérant et au collaborateur du projet ; pas de transfert hors de Suisse ;
conservation `[[10 ans]]` puis destruction/archivage selon les règles UNIGE ; code
d'analyse versionné et publié, données protégées, équivalents synthétiques publiés lorsque
possible.

## 6. Bénéfices et risques

Aucun risque pour les personnes (données agrégées, rétrospectives). Bénéfice : évaluation
documentée de la valeur - et des limites - de l'évidence publiée pour l'anticipation des crises,
restituée aux services d'urgence partenaires.

## 7. Calendrier

Demande de clarification / soumission : `[[T4 2026 – T1 2027]]`. Début du traitement des données :
après autorisation et convention avec les HUG (projet Ambizione : démarrage entre le 01.09.2027
et le 01.09.2028).
