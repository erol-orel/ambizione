# 6. Feasibility, environment and resources

> **Drafted under an assumption you need to confirm or overturn.** I have written this for a host
> in **Prof. Douglas Teodoro's group (medical informatics, Faculty of Medicine, UNIGE), with a
> formal collaboration with HUG emergency medicine**. Reasoning: it moves you out of the institute
> and the supervisor that make the independence argument hard; medical informatics is the natural
> disciplinary home for evidence extraction and predictive modelling; and it sits inside the
> GESICA network that carries the clinical data access. The alternative — a directly
> HUG-affiliated unit — is stronger on data proximity and weaker on methodological home; a third
> option, remaining at ISG, is the one I would advise against, for reasons in
> `02-profile/erol-orel-profile.md`. Change the names and this section survives; change the
> institution and §5 and the mobility statement need rewriting too.

## 6.1 Why this environment

**Disciplinary home.** `[[Host unit]]` combines biomedical natural language processing,
information retrieval and machine learning for health — the methodological neighbours of WP1 —
with an established record in epidemic intelligence. It is where the extraction half of this
project belongs, and it is a different scientific community from the one in which my doctoral and
postdoctoral work was conducted, which is the point.

**Access to the operational system.** Through GESICA I work directly with HUG emergency medicine
`[[Prof. Thibaut Desmettre, Dr Robert Larribau — confirm naming and their agreed roles]]` and with
the Geneva emergency response system. The dispatch, emergency department and intensive care data
that WP3 and WP4 require are reachable through relationships that already exist and produce joint
work — the AI-in-EMS systematic review [Edjinedja 2026] is the concrete output. This is not a
proposal to build a collaboration; it is a proposal that rests on one already functioning.

**Existing infrastructure.** LiteRev-Evidence is operational: a continuously updated corpus of
over 80,000 publications with 320,000 embedded passages, structured extraction with provenance
and quality scoring, quality-weighted pooling into parameter distributions, and connectors to
MeteoSwiss, Copernicus ERA5 and national surveillance. `[[After the hardening described in §6.4:
state that it runs with transport-layer security, managed secrets, version-controlled schema and
documented disaster recovery. Do not submit this section until that sentence is true — a
data-protection reviewer will ask, and the answer is currently the wrong one.]]`

**Unique linked data** for the waterborne archetype: confirmed legionellosis cases in Geneva
matched to individual hot water installations with technical, meteorological and territorial
covariates, under ethics approval BASEC 2026-00324.

**Computing.** `[[UNIGE HPC (Baobab/Yggdrasil) — confirm access and whether the secure analysis
environment for clinical data is separate.]]`

**Teaching and training environment.** I lecture in statistics and epidemiology on the MAS in
Public Health, which provides both a supervision context and a route for the doctoral researcher's
training. `[[Confirm the doctoral programme the student would enrol in.]]`

## 6.2 Secured commitments

| Item | Status | Evidence |
| --- | --- | --- |
| Host institution and unit | `[[ ]]` | Detailed and general confirmation letters |
| Right to supervise doctoral students | `[[ ]]` | Detailed confirmation letter — must be explicit |
| HUG emergency department data | `[[ ]]` | `[[letter of support]]` |
| 144 / CASU dispatch data | `[[ ]]` | `[[letter of support]]` |
| ICU occupancy data | `[[ ]]` | `[[letter of support]]` |
| Legionellosis linked data | **Granted** | BASEC 2026-00324 |
| Ethics for operational data | `[[new CCER submission, PI as applicant]]` | — |
| Mobility host | `[[ ]]` | `[[letter]]` |
| Computing | `[[ ]]` | — |

**Every unresolved row in this table is a weakness a referee will find, and the three data rows
are the ones that matter.** Convert as many as possible into letters before submission. For any
that remain open, the fallback design in WP3 is what carries the risk, and it is stated there
rather than concealed.

## 6.3 Resources requested

`[[Complete with the grants office. Constraints: total project funds must fit the 2026 ceiling of
approximately CHF 250,000 over four years, on top of the applicant's salary; confirm both the
ceiling and current SNSF doctoral salary rates before finalising.]]`

| Item | Rationale |
| --- | --- |
| Doctoral researcher, `[[~42 months]]` | Carries WP1 (benchmark construction and extraction evaluation) and WP3 (evaluation pipeline) under supervision |
| Expert extraction time, WP1 | Two independent extractors for the gold standard — `[[budget as consultancy or as student assistants]]` |
| Computing and storage | Corpus embedding, MCMC for the regime models, rolling-origin refitting |
| Travel and research stays | Conferences plus the mobility component `[[see statement of mobility]]` |
| Open access and data publication | Benchmark dataset release |

**Declared co-funding.** The cantonal Legionella study is funded by Services Industriels de
Genève, the Office cantonal de l'énergie and the Service du Médecin Cantonal
(`[[~CHF 90,000]]`), and supports the data underlying the WP3 extension. `[[Declare this, and
declare the GESICA and Horizon roles, in the mySNF form.]]`

**Division of labour.** I execute WP2 personally — it is the methodological core and the source
of the project's distinctiveness. The doctoral researcher carries WP1 and WP3 under supervision.
WP4 is conducted jointly with the operational partners. `[[Check this against the milestone dates
in §4: the WP2 timeline assumes a substantial fraction of my own time.]]`

## 6.4 Preparatory work before the grant starts

Three things are underway and must be complete before month 1, because the project's data access
depends on them:

1. **Infrastructure hardening** of the LiteRev-Evidence platform — transport security, secrets
   management, schema under migration control, documented recovery — so that a data-protection
   review of the clinical data request meets no avoidable obstacle.
2. **Data agreements** with HUG, the 144/CASU and the intensive care service, initiated now so
   that the supporting letters accompany this application rather than following it.
3. **A CCER submission with myself as applicant** for the operational data, which is both a
   practical necessity and concrete evidence of the independence claimed in §5.
