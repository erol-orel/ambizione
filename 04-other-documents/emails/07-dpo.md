# To the data protection officer: the CCER route question

> À : `[[DPO UNIGE - vérifier l'adresse sur unige.ch (Bureau de la protection des données);
> mettre en copie le DPO des HUG une fois le custodian 144 nommé par Larribau]]`
> Objet : Qualification LRH d'une réutilisation de données opérationnelles agrégées (CASU-144,
> HUG) - demande d'avis avant dépôt BASEC

**Why this email exists:** the whole CCER strategy (`../ccer/01-route-strategy.md`) hinges on one
legal qualification - whether daily counts **aggregated at source by the HUG** are anonymous data
outside the LRH, or whether any part of the design pulls the project under Art. 34 LRH. That is a
DPO call, not ours. Their written answer decides whether we file a jurisdictional inquiry
(Route A), a full Art. 34 dossier (Route B), or a hybrid (Route C) - and it is a concrete
feasibility fact for the SNSF application. **Send Thursday 2 October** (CALENDAR.md), attach
`../ccer/01-route-strategy.md` and `../ccer/03-data-specification.md`.

**One primary request:** a written qualification of the route. Everything else is framed as
context or subordinate clarification, per the one-ask rule.

---

Madame, Monsieur,

Je prépare une candidature au subside FNS **Ambizione** (délai 3 novembre 2026), avec l'Institut
de santé globale (UNIGE) comme institution hôte. Le projet réutilise des **données
opérationnelles des HUG** et j'aurais besoin de votre lecture sur la qualification juridique de
cette réutilisation **avant** tout dépôt sur BASEC. Ma question principale tient en un
paragraphe ; le détail figure dans la spécification jointe.

**La configuration.** Le projet a besoin de **comptes journaliers agrégés** issus de la centrale
d'appels sanitaires urgents (CASU-144) : nombre d'appels par jour × motif d'appel (catégories
grossières) × niveau d'urgence × tranche d'âge large. L'agrégation serait effectuée **à la
source, par les HUG**, avant tout transfert. Aucune donnée individuelle, aucun identifiant,
aucun texte libre, aucun enregistrement vocal ne quitterait les HUG ; les cellules à faible
effectif seraient regroupées avant transfert selon la règle du détenteur.

**Question principale.** Dans cette configuration, considérez-vous que les données transférées
sont des **données anonymes au sens de la LRH** (art. 2 al. 2 let. b et c LRH), et que le projet
échappe donc au champ d'application de la loi - auquel cas je documenterais ce constat par une
**demande de clarification de compétence (déclaration de non-soumission)** auprès de la CCER via
BASEC, plutôt que de l'affirmer moi-même ?

**Une exception possible, que je préfère annoncer maintenant.** La validation de la
correspondance pré-enregistrée entre motifs d'appel et classes d'issue pourrait nécessiter un
**échantillon borné** de libellés de motifs pseudonymisés, sans aucun autre champ, détruit après
validation. Si cet échantillon fait basculer cette composante - et elle seule - sous l'**art. 34
LRH** (réutilisation sans consentement), je déposerais un dossier hybride : non-soumission pour
les comptes agrégés, art. 34 pour le sous-échantillon de validation, délimité étroitement.
Partagez-vous cette lecture ?

**Deux clarifications subordonnées**, si vous pouvez y répondre dans le même courrier :

- **Compétence respective des DPO** : les HUG étant détenteurs des données et institution
  publique cantonale, la qualification relève-t-elle de votre bureau, du DPO des HUG, ou des
  deux - et la **LIPA** s'applique-t-elle au transfert même si la LRH ne s'applique pas
  (auquel cas une convention de transfert HUG–UNIGE resterait nécessaire pour des données
  anonymes) ?
- **Rôle de requérant** : pour une demande de clarification de compétence sur BASEC, je serais
  moi-même requérant, avec l'UNIGE/Institut de santé globale comme institution - voyez-vous une
  objection ou une pratique différente ?

Je joins la stratégie de qualification (une page) et la spécification des données (une page).
Une réponse, même préliminaire, d'ici le **`[[13 octobre]]`** me permettrait d'inclure la voie
réglementaire retenue dans la candidature ; je suis disponible pour un échange téléphonique si
c'est plus simple.

Avec mes remerciements et mes meilleures salutations,

Erol Orel
Senior Research Associate, Institut de santé globale, Faculté de médecine
`[[téléphone]]`

**Pièces jointes :** `01-route-strategy.md` (stratégie de qualification, 1 p.),
`03-data-specification.md` (spécification des données, 1 p.) - `[[convertir en PDF avant envoi]]`

---

## What the answer unblocks

| Answer | Consequence |
| --- | --- |
| "Anonymous, out of LRH scope" (Route A) | File the BASEC clarification de compétence immediately; its reference number goes into the feasibility narrative |
| "The validation subsample is Art. 34" (Route C) | File the hybrid dossier; the French synopsis (`../ccer/02-protocol-synopsis-fr.md`) is ready |
| "All of it is Art. 34" (Route B) | Full authorisation dossier - start from the synopsis, budget 6–8 weeks of CCER time, and say so honestly in the plan's timeline (T3.0 already absorbs this) |
| "Ask the HUG DPO" | Forward this same email with the same attachments - nothing to rewrite |
| LIPA applies regardless | Add a HUG–UNIGE transfer agreement to the custodian workstream (Larribau's question 4 already asks who signs) |

## Follow-up rule

If no reply within a week, phone - DPO offices answer qualification questions routinely. If both
DPOs disagree with each other, the CCER clarification de compétence settles it: file it and let
the commission rule. Log the written answer in `05-review/applicant-facts.md` and tick the
"Route settled" box in `../ccer/04-basec-checklist.md`.

## What NOT to do

- Do **not** file anything on BASEC before this answer - a wrongly-routed dossier costs weeks.
- Do **not** let the aggregate request quietly grow individual-level fields "while we're at it" -
  the whole Route A case rests on nothing individual leaving the HUG.
- Do **not** present the route as settled in the SNSF application - state the strategy and the
  inquiry, dated; reviewers reward a named regulatory path, not a claimed approval.
