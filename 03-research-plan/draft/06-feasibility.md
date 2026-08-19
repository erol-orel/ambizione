# 6. Feasibility, environment and resources

**Host: Data Science for Digital Health (DS4DH), Department of Radiology and Medical Informatics, Faculty of Medicine, University of Geneva** (Prof. Douglas Teodoro), with an **associated affiliation at the Institute of Global Health** `[[Prof. Alexandra Calmy, Director — confirm title]]` and a formal research collaboration with **HUG emergency medicine** `[[Prof. Thibaut Desmettre, Dr Robert Larribau — confirm titles and agreed roles]]`.

## 6.1 Why this environment

The project requires three capabilities that are rarely housed together: quantitative methods, evidence synthesis and access to a functioning emergency/public-health system. The hosting arrangement provides them without making the project dependent on any one collaborator.

**Methodological home — DS4DH.** Biomedical NLP, information retrieval and machine learning for health are directly relevant to WP1, while the group's medical-informatics environment provides the technical setting for reproducible data and software work. This is a different department and scientific community from the one in which I trained, supporting the independence transition central to Ambizione.

**Domain home — Institute of Global Health.** The associated affiliation keeps the project connected to epidemiology and global-health methodology while leaving the research programme independent of my previous group.

**Operational access — HUG and Geneva emergency services.** Through GESICA I already work with emergency-medicine and public-health partners. The existing AI-in-EMS systematic review [Edjinedja 2026] is concrete evidence of a functioning collaboration. The project therefore does not depend on creating a new relationship after the grant starts.

**Existing infrastructure.** LiteRev-Evidence is operational, with 80,000+ publications, structured quantitative extraction, provenance and quality scoring, quality-weighted pooling into parameter distributions, and connectors to MeteoSwiss, Copernicus ERA5 and surveillance sources. Ambizione does not fund construction of this platform; it uses the platform to test the scientific question it raises.

**Linked data.** The Geneva legionellosis study (BASEC 2026-00324) provides a contrasting crisis archetype and is already under ethics approval.

**Computing.** `[[UNIGE HPC (Baobab/Yggdrasil) — confirm access and secure-analysis arrangement]]`.

## 6.2 Commitments, by status

Each row is labelled **secured**, **agreed**, **requested** or **fallback**. Nothing is described above its actual status.

| Item | Status | Evidence / action |
| --- | --- | --- |
| Legionellosis linked data | **Secured** | Ethics approval BASEC 2026-00324 |
| Primary host unit (DS4DH) | **Agreed** `[[confirm]]` | Detailed confirmation letter to follow |
| Associated affiliation (ISG) | `[[requested]]` | `[[letter of support]]` |
| Institutional confirmation | `[[requested]]` | General confirmation letter, UNIGE |
| 144 / CASU dispatch data (HUG-operated) | `[[requested]]` | `[[letter of support]]`. Documented in my GESICA inventory: continuous, daily, ~71,000 emergency calls/year in Geneva |
| HUG emergency department presentations | `[[requested]]` | `[[letter of support]]`. Daily historical availability **to be confirmed**; hospital statistics via the OFS are annual |
| ICU occupancy data | `[[requested]]` | `[[letter of support]]`; fallback in WP3 |
| Operational-data ethics | `[[requested]]` | CCER submission, PI as applicant |
| Mobility host | `[[requested]]` | `[[letter of invitation]]` |
| Computing | `[[requested]]` | `[[UNIGE HPC]]` |

The three operational-data rows are the most important remaining feasibility items, and §4 states explicitly what their absence would cost the primary outcome claim. Nothing in this proposal is described as a collaboration or commitment beyond the status recorded here.

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

**Division of labour.** I execute WP2 and the confirmatory evaluation design because they are the methodological core. The collaborator carries defined technical and extraction work under my direction. WP4 is conducted with operational partners and remains scientifically led by me.

## 6.4 Preparatory work before the grant starts

Three activities are being advanced before month 1: **data agreements** with HUG, 144/CASU and intensive care; **CCER preparation with myself as applicant** for the operational data; and **infrastructure hardening** of LiteRev-Evidence. The latter must include transport security, managed secrets, version-controlled schemas and documented recovery procedures before clinical data are connected. These are preparatory conditions, not work packages funded by the grant.

## 6.5 Feasibility logic

Feasibility rests on four safeguards:

1. **The instrument already exists.** The grant does not spend its first year building the evidence-synthesis platform.
2. **The central experiment is modular.** WP3 can compare weakly informative and evidence-derived priors even if WP1 finds that some parameter classes are unusable.
3. **Data access has a real fallback.** If operational records are delayed, the same rolling-origin experiment can be conducted on open surveillance series, with the claim narrowed appropriately.
4. **Methodological failure is itself informative.** If the regime model is not identifiable, the pre-specified ordinal state-space fallback preserves the central test; if evidence borrowing is harmful, that is the scientific result rather than a reason to relax the evaluation.

The proposal therefore does not depend on every component succeeding. Its main scientific question remains answerable under the principal foreseeable failures.
