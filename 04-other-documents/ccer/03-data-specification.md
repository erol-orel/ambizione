# Data specification: annex to the CCER inquiry and the HUG agreement

Kept **verbatim-consistent** with the Larribau/Desmettre emails and §2.3.2 (T3.0) of the research
plan. Any change here must propagate to both.

## Series 1: CASU-144 regulation data (primary outcome source)

| Field | Specification |
| --- | --- |
| Unit | Daily counts (aggregated at source if Route A/C) |
| Period | `[[2015]]` → 2026 inclusive; earlier if archives allow |
| Dimensions | date × **call reason (coarse categories)** × **urgency level** × **broad age band** `[[bands to agree, e.g. 0–15 / 16–64 / 65–74 / 75+]]` |
| Category coverage | Must span **respiratory** motifs (primary outcome) AND **heat-sensitive** motifs - dehydration, renal, psychiatric (heat-arm outcome) |
| Excluded | Direct identifiers, names, addresses, free text, voice recordings, individual records (unless Route C validation subsample) |
| Holder / custodian | HUG (CASU-144); custodian `[[name from Larribau]]` |
| Known facts | Continuous, daily, near real-time; ~71,000 emergency calls/yr (2026 GESICA inventory, to reconfirm); access established for GESICA (voice excluded) - this project needs its own agreement |
| Quality questions | Coding stability of motifs/urgency across the period; COVID-period completeness; archive depth |

## Series 2: ED presentations (additional observation channel)

Daily counts by presentation category (respiratory / cardiac / trauma / other, ideally incl.
heat-sensitive categories) × broad age band; period as available; holder HUG
`[[custodian via Desmettre]]`; daily historical availability itself to be confirmed.

## Series 3: ICU occupancy (additional observation channel)

Daily occupied and available beds `[[unit/site granularity to agree]]`; holder HUG
`[[custodian via Desmettre's answer to question 3]]`.

## Route C validation subsample (only if needed)

Purpose: validate the pre-registered call-reason → outcome-class mapping. Bounded sample
`[[size]]` of pseudonymised call-reason strings with no other fields; destroyed after mapping
validation; described to the CCER explicitly if requested.

## Small-cell policy

Cells below `[[n<5]]` grouped per the holders' rule before transfer - state it in the agreement
so the extract never carries quasi-identifying rare combinations.
