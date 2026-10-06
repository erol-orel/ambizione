# Episode inventory scaffold (v1, 7 October 2026)

Pre-built so Larribau's data facts drop into ready rows. Sources: `step0-evaluation-set.md`
(provisional candidates), the **September 2026 GESICA respiratory report + table** (episode
rules, source facts), public surveillance seasons. Status: SCAFFOLD; nothing here is
registered until the CASU-144 archive depth and coding stability are confirmed.

## The two facts the new GESICA report settles

1. **Heat episodes must be recomputed from measured temperature (D10, MeteoSwiss), not taken
   from the warning archive.** The report states it plainly: warnings used a heat index until
   2020 and daily mean temperature since summer 2021 (degree 3 at >=25 C for 3 days, degree 4
   at >=27 C for 3 days); the two periods do not chain. The pre-registered episode rule should
   therefore be: fixed thresholds applied to measured daily mean temperature over the whole
   period, with the official warning degrees kept as a sensitivity. Geneva's cantonal levels
   (activation at 25 C for five days or 27 C for three) are a second sensitivity.
2. **Only COVID-19, influenza and RSV have multichannel high-frequency surveillance**
   (144, Sentinella, wastewater, web signals): the respiratory episode set is anchored on
   exactly the diseases the evidence channels can support. Caveats for covariate/validation
   series: Sentinella region 1 pools GE+NE+VD+VS (no cantonal split); wastewater is one
   station per canton (Aire for GE).

## A. Respiratory episodes (unit = distinct demand surge, NOT pathogen-season)

| # | Candidate episode | Period | Status | Fills in when Larribau answers |
| --- | --- | --- | --- | --- |
| R1 | Influenza season 2015-16 | winter 2015-16 | candidate | archive reaches back this far? |
| R2 | Influenza season 2016-17 | winter 2016-17 | candidate | |
| R3 | Influenza season 2017-18 | winter 2017-18 | candidate | |
| R4 | Influenza season 2018-19 | winter 2018-19 | candidate | |
| R5 | Influenza season 2019-20 | winter 2019-20 | candidate | truncated by COVID onset: one surge or two? |
| R6 | COVID wave 1 | spring 2020 | candidate | completeness during lockdown (known issue) |
| R7 | COVID autumn-winter | 2020-21 | candidate | NPI period coding stability |
| R8 | COVID Delta | autumn 2021 | candidate | |
| R9 | COVID Omicron | winter 2021-22 | candidate | overlap with R8: one block or two? |
| R10 | COVID + flu + RSV | winter 2022-23 | candidate | tripledemic = ONE demand surge |
| R11 | Influenza season 2023-24 | winter 2023-24 | candidate | |
| R12 | Influenza season 2024-25 | winter 2024-25 | candidate | |
| R13 | Influenza season 2025-26 | winter 2025-26 | candidate | |
| NC1 | Suppressed flu season | 2020-21 | negative control | method should NOT alarm |
| NC2 | Suppressed flu season | 2021-22 | negative control | |

Counting rule (step0): overlapping pathogen-seasons merge into one demand surge; R9/R10-type
merges are decided by the pre-registered rule, not by eye. Realistic confirmatory count after
merging and eligibility screening: **on the order of 10-13 episodes plus 2 negative controls**.

## B. Heat episodes (rule: recomputed from D10 temperature, thresholds fixed at registration)

| # | Candidate | Year | Status | To confirm against recomputation |
| --- | --- | --- | --- | --- |
| H1 | Summer heatwave | 2015 | candidate | |
| H2 | Summer heatwave | 2017 | to verify | flagged in step0 |
| H3 | Summer heatwave | 2018 | candidate | |
| H4 | Two distinct events | 2019 | candidate x2 | separation criterion decides 1 vs 2 |
| H5 | Summer heatwave | 2022 | candidate | |
| H6 | Summer heatwave | 2023 | candidate | |
| H7 | Summer events | 2024, 2025 | to verify | recompute from D10 |

Provisional count: **6-9 episodes**, settled only by running the fixed-threshold rule on the
MeteoSwiss daily series (open data; can be run before any HUG agreement).

## C. Eligibility gates (fix before counting, per T3.0)

- [ ] Real-time-computable onset criterion fires;
- [ ] minimum pre-onset baseline available in the series;
- [ ] no block-breaking overlap with an adjacent episode;
- [ ] outcome coding stable across the episode (Larribau Q: motif/urgency coding changes);
- [ ] COVID-period completeness documented (R6-R7 may fail this gate: acceptable, say so).

## D. What only the custodians can supply

| Fact | Who | Blocks |
| --- | --- | --- |
| Archive depth of CASU-144 (GE) | Larribau | R1-R4 existence; start year in all documents |
| Motif/urgency coding stability | Larribau | gate 4; respiratory + heat-sensitive class maps |
| COVID-period completeness | Larribau | R6-R7 eligibility |
| ED daily historical availability | Desmettre | validation channel only |

**Next concrete step that needs nobody:** run the heat-episode recomputation on MeteoSwiss
open data with the registered thresholds; it fixes section B and is a worked example of a
pre-registered episode rule for the interview.
