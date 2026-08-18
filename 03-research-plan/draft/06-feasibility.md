# 6. Feasibility, environment and resources

**Host: Data Science for Digital Health (DS4DH), Department of Radiology and Medical Informatics,
Faculty of Medicine, University of Geneva** (Prof. Douglas Teodoro), with an **associated
affiliation at the Institute of Global Health** `[[Prof. Alexandra Calmy, Director — confirm
title]]` and a formal research collaboration with **HUG emergency medicine** `[[Prof. Thibaut
Desmettre, Dr Robert Larribau — confirm titles and agreed roles]]`.

## 6.1 Why this environment

The project sits at the intersection of three fields and the hosting arrangement reflects that
structure rather than hedging.

**Methodological home — DS4DH.** Biomedical NLP, information retrieval and machine learning for
health are WP1's immediate neighbours, and DS4DH has an established record in clinical text mining
and biomedical entity recognition. This is also a **different department and scientific community**
from the one in which I trained: the move from global-health epidemiological modelling into medical
informatics is deliberate.

**Domain home — Institute of Global Health.** The associated affiliation keeps the project
connected to the community in which its questions are posed and its results must land, and gives
the doctoral researcher that training environment. `[[Under its incoming direction, and independent
of the group in which I previously worked.]]`

**Access to the operational system.** Through GESICA I work directly with HUG emergency medicine
and the Geneva emergency response system. The data WP3 and WP4 require are reachable through
relationships that already exist and produce joint work — the AI-in-EMS systematic review
[Edjinedja 2026] is the concrete output. This is not a proposal to build a collaboration but one
resting on a functioning one.

**Existing infrastructure.** LiteRev-Evidence is operational: 80,000+ publications, 320,000
embedded passages, structured extraction with provenance and quality scoring, quality-weighted
pooling into parameter distributions, and connectors to MeteoSwiss, Copernicus ERA5 and national
surveillance. `[[After the hardening described in §6.4:
state that it runs with transport-layer security, managed secrets, version-controlled schema and
documented disaster recovery. Do not submit this section until that sentence is true — a
data-protection reviewer will ask, and the answer is currently the wrong one.]]`

**Unique linked data** for the waterborne archetype: Geneva legionellosis cases matched to
individual hot water installations with technical and environmental covariates, under ethics
approval BASEC 2026-00324.

**Computing.** `[[UNIGE HPC (Baobab/Yggdrasil) — confirm access and whether the secure analysis
environment for clinical data is separate.]]`

**Teaching and training environment.** I lecture in statistics and epidemiology on the MAS in
Public Health. `[[Confirm the doctoral programme the student would enrol in.]]`

## 6.2 Secured commitments

| Item | Status | Evidence |
| --- | --- | --- |
| Primary host unit (DS4DH) | **Agreed in principle** `[[confirm]]` | Detailed confirmation letter |
| Associated affiliation (ISG) | `[[in discussion]]` | `[[letter of support]]` |
| Institutional confirmation | `[[ ]]` | General confirmation letter, UNIGE |
| Right to supervise doctoral students | `[[ ]]` | Detailed confirmation letter — must be explicit |
| HUG emergency department data | `[[ ]]` | `[[letter of support]]` |
| 144 / CASU dispatch data | `[[ ]]` | `[[letter of support]]` |
| ICU occupancy data | `[[ ]]` | `[[letter of support]]` |
| Legionellosis linked data | **Granted** | BASEC 2026-00324 |
| Ethics for operational data | `[[new CCER submission, PI as applicant]]` | — |
| Mobility host | `[[ ]]` | `[[letter]]` |
| Computing | `[[ ]]` | — |

**Every unresolved row is a weakness a referee will find, and the three data rows are the ones
that matter.** Convert as many as possible into letters before submission; for any that remain,
the WP3 fallback carries the risk and is stated there rather than concealed.

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

Three things are underway and complete before month 1, because data access depends on them:
**infrastructure hardening** of the platform (transport security, secrets management, schema under
migration control, documented recovery) so that data-protection review meets no avoidable
obstacle; **data agreements** with HUG, the 144/CASU and intensive care, initiated now so the
supporting letters accompany this application; and a **CCER submission with myself as applicant**
for the operational data — a practical necessity and concrete evidence of the independence claimed
in §5.
