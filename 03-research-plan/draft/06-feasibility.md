# 6. Feasibility, environment and resources

**Host: Institute of Global Health, Faculty of Medicine, University of Geneva** `[[responsible person and signature level — confirm with the Faculty]]`, with a formal methodological collaboration with **Data Science for Digital Health** (Prof. Douglas Teodoro, Department of Radiology and Medical Informatics) and a clinical collaboration with **HUG emergency medicine** `[[Prof. Thibaut Desmettre, Dr Robert Larribau — confirm titles and agreed roles]]`.

## 6.1 Why this environment

The project requires three capabilities that are rarely housed together — quantitative methods, evidence synthesis and access to a functioning emergency and public-health system — and the arrangement below provides them without depending on any one collaborator.

**Domain and infectious-disease expertise — Institute of Global Health.** Epidemiology, infectious-disease modelling and automated evidence extraction sit in the same institute, together with the surveillance and global-health methodology the project consumes. This is the environment in which the scientific gap became visible, and hosting here is a choice for feasibility over optics: independence is established by dedicated time and a delimited agenda (§5.3), not by distance from colleagues.

**Methodological collaboration — DS4DH.** Biomedical NLP, information retrieval and machine learning for health are directly relevant to WP1's extraction work, and the group's medical-informatics environment supports reproducible data and software engineering.

**Operational access — HUG and Geneva emergency services.** Through GESICA I already work with emergency-medicine and public-health partners; the AI-in-EMS systematic review [Edjinedja 2026] is concrete evidence of a functioning collaboration. No new relationship has to be created after the grant starts.

**Existing infrastructure.** LiteRev-Evidence is operational: 80,000+ publications, structured quantitative extraction with provenance and quality scoring, quality-weighted pooling into parameter distributions, and connectors to MeteoSwiss, Copernicus ERA5 and surveillance sources. Ambizione does not fund its construction; it uses it to test the question the platform raises. The Geneva legionellosis study (BASEC 2026-00324), already under way with ethics granted, supplies the contrasting crisis archetype.

**Computing.** `[[UNIGE HPC (Baobab/Yggdrasil) — confirm access and secure-analysis arrangement]]`.

## 6.2 Commitments, by status

Each row is labelled **secured**, **agreed**, **requested** or **fallback**. Nothing is described above its actual status.

| Item | Status | Evidence / action |
| --- | --- | --- |
| Legionellosis linked data | **Secured** | Ethics approval BASEC 2026-00324 |
| Host institute (ISG) | `[[requested]]` | `[[host confirmation letter]]` |
| DS4DH methodological collaboration | **Agreed** `[[confirm]]` | `[[letter of support]]` |
| Institutional confirmation | `[[requested]]` | General confirmation letter, UNIGE |
| **CASU-144 records (HUG-operated) — primary outcome** | `[[requested]]` | `[[letter of support]]`. Documented in my GESICA inventory: continuous, daily, ~71,000 emergency calls/year in Geneva |
| ED presentations — additional channel | `[[requested]]` | `[[letter of support]]`. Daily historical availability to be confirmed; OFS hospital statistics are annual |
| ICU occupancy data | `[[requested]]` | `[[letter of support]]`; fallback in WP3 |
| Operational-data ethics | `[[requested]]` | CCER submission, PI as applicant |
| Mobility host | `[[requested]]` | `[[letter of invitation]]` |
| Computing | `[[requested]]` | `[[UNIGE HPC]]` |

The three operational-data rows are the most important remaining feasibility items, and §4 states what their absence would cost the primary outcome claim. Nothing here is described above its actual status.

## 6.3 Resources requested

The 2026 regulations cap project funds at **CHF 250,000 over four years**, with the applicant's salary covered separately. Doctoral students and postdocs cannot be employed from these funds; other staff can. Since no student or postdoctoral salary is charged to the grant, the ceiling supports a substantial **scientific/technical collaborator** alongside computing, data and mobility costs.

| Item | Rationale |
| --- | --- |
| Scientific/technical collaborator, `[[FTE and duration]]` | WP1 benchmark extraction (one of two independent extractors), WP3 harmonisation and evaluation pipeline, reproducibility |
| Second independent extractor | `[[contracted or in-kind]]` — required for the dual-extraction design in T1.2 |
| Computing and data access | Evidence processing, Bayesian estimation, rolling-origin evaluation |
| Travel and research stays | Scientific exchange and the mobility component |
| Other eligible direct costs | As justified in the final SNSF budget |

`[[Confirm institutional salary rates with the grants office and set the FTE. The scale should be
stated concretely enough that a referee can see the work is resourced.]]`

## 6.4 Preparatory work before the grant starts

Three activities are advanced before month 1: **data agreements** with HUG, 144/CASU and intensive care; **CCER preparation with myself as applicant** for the operational data; and **infrastructure hardening** of LiteRev-Evidence — transport security, managed secrets, version-controlled schemas and documented recovery before clinical data are connected. These are preparatory conditions, not grant-funded work packages.

## 6.5 Feasibility logic

Feasibility rests on one structural property: **the instrument already exists**, so the grant does not spend its first year building the evidence-synthesis platform, and on the fallbacks set out in §4 — modular work packages, an open-data route if operational access is delayed, and an ordinal state-space formulation if the regime model proves weakly identifiable. Each failure mode leaves the central question answerable, with the claim narrowed and the narrowing stated.
