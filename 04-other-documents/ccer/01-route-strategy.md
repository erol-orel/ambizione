# Route strategy — settle this before drafting anything else

The project needs **daily aggregate counts, no identifiers, no free text, no voice**. Which LRH
route applies depends on one fact: **whether the aggregation is performed by the data holder
before transfer.**

## The three possible routes

| Route | When it applies | Consequence |
| --- | --- | --- |
| **A. Non-soumission (out of LRH scope)** | HUG aggregates internally and transfers only daily counts by category — **anonymous data**, no individual-level processing by the project | No authorisation needed; request a **déclaration de non-soumission / clarification de compétence** from the CCER (jurisdictional inquiry via BASEC) so the fact is documented, not asserted |
| **B. Art. 34 LRH — further use without consent** | HUG transfers individual-level records (even pseudonymised) that the project aggregates itself | Full CCER authorisation; justification that consent is impracticable (~10 years, >1M calls, no contact channel), interests balance, DPO involvement |
| **C. Hybrid** | Aggregates for the main series + limited individual-level access for the classification-validation subsample (checking the call-reason mapping) | Route A for the counts + a narrow Art. 34 component for the validation subsample |

## Recommendation

**Design for Route A, expect Route C.** Ask HUG's custodian to aggregate at source — the emails
already request exactly that, and the plan's methods never require individual records for the
confirmatory analysis. The one honest exception: validating the pre-registered call-reason →
outcome-class mapping (respiratory; heat-sensitive) may need a bounded individual-level sample.
State it now rather than discover it later — Route C scoped narrowly is cleaner than Route A
that quietly grows.

## Immediate actions (before the Ambizione deadline)

1. Ask the data protection officer which route they read this as — **drafted:
   `../emails/07-dpo.md`** (to the UNIGE DPO, cc HUG DPO once the 144 custodian is named), with
   this file and `03-data-specification.md` attached. Their answer determines everything
   downstream.
2. File the **jurisdictional inquiry** on BASEC if the DPO concurs with Route A/C — it is cheap,
   fast, and its reference number is a concrete feasibility fact for the application.
3. Name HUG's data custodian for the 144 (Larribau's answer to question 4 in his email).

## Why the applicant is requérant

On BASEC 2026-00324 the applicant is data lead under another PI. Here he holds the requérant
role himself — a checkable fact of independence the research plan already points to. Nothing in
the LRH requires the requérant to hold a clinical title for data-reuse studies; the sponsor line
`[[UNIGE / Institute of Global Health — confirm with the RGO how sponsor is declared]]`.
