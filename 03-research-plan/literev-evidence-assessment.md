# LiteRev-Evidence — what it means for the application

Read from `github.com/erol-orel/LiteRev-Evidence` (clone; not vendored into this repo — it is a
separate project with its own history, and its git history contains credential material).

## What is actually built

This is not a prototype. It is a running production system.

| | |
| --- | --- |
| **Corpus** | 81,209 literature documents; 323,868 embedded chunks (1536-dim), 99.99% populated |
| **Stack** | FastAPI + uvicorn, PostgreSQL 14 + pgvector 0.8.2, React 19 SPA, nginx, systemd, live server |
| **Ingestion** | PubMed, PMC, OpenAlex, CrossRef, medRxiv/bioRxiv; **living-review scheduler** that re-runs scenario queries on a daily cadence |
| **Evidence layer** | PICO extraction, screening status, dedup, quality scoring, per-scenario article sets |
| **Modelling** | AutoML with Optuna tuning, model-family leaderboard, bootstrap CIs, SHAP explanations, guardrails; time-series (Prophet, seasonal); **SEIR with vaccination and quarantine compartments**, RK4 integration, ensemble simulation with uncertainty bands, and calibration to observed data |
| **Operational data** | MeteoSwiss, Open-Meteo, Copernicus ERA5, Sentinelles, OSM/OSRM, Google Trends |
| **Scenarios** | 31 scenarios elaborated, 10 prioritised — epidemic early warning, OHCA prediction, EMS demand forecasting, heatwave impact, response-time optimisation, triage, mass casualty, surge, pandemic preparedness, cross-border coordination |
| **Activity** | 240+ merged pull requests |

## The three findings that matter for the Ambizione

### 1. You have already built the mechanism I proposed as WP1

`seir_model.py` contains `normalize_extracted_parameters()` with provenance tracking,
`pool_weighted(observations, quality_by_id)` — pooling of literature-extracted estimates weighted
by study quality — and `params_to_distributions()`, which converts pooled literature estimates
into parameter **distributions**, then `simulate_ensemble()` propagates them.

That is **literature-to-prior elicitation, implemented and running**. In the previous note I
proposed it as the scientific core of WP1 without knowing you had a working version. This is the
strongest possible position: the mechanism exists, so the proposal is not "I will build this" but
**"I built this; here is the open question about whether it is sound."** That is exactly what
Section 2 of an SNSF research plan is for, and very few Ambizione applicants can write it.

Similarly, `model_trainer.py:_level_from_value(v, orange, red)` already implements the
normal/orange/red banding you described. Again: built, not hypothetical.

### 2. Because the tool exists, the proposal *must* be about the question

This is now decisive rather than advisory. If you propose to build an evidence-to-prediction
platform, a referee who looks at literev-scenario.com will observe that you have largely built it
— and the proposal collapses into asking the SNSF to fund work already done, or a maintenance
and hardening exercise. Neither is fundable at Ambizione level.

The system is what makes the *hard* proposal credible. It buys you the right to ask:

> Literature-derived parameters can be pooled into priors — I have implemented this. **But should
> they be?** When does evidence synthesised across heterogeneous studies improve forecasting in
> the cold-start regime, when does it actively mislead, and how should a clinician act on the
> result?

Four years of an Ambizione spent answering that, with an existing platform as the instrument, is
a strong application. Four years spent building the platform is not — you would be proposing your
own past work.

### 3. Two problems on the critical path to data access

The repo's own audit (`AUDIT_REPORT.md`, 16 June 2026) is candid, and two findings are not just
engineering debt — they gate the thing the Ambizione depends on.

**The exposed credential.** The audit records that the OpenAI API key was stored in plaintext in
the systemd override and was **printed into a public GitHub Actions log** (log since deleted).
If that key has not been rotated, rotate it today. A deleted log is not a revoked credential, and
public CI logs are scraped continuously. I could not check whether the repository is public from
this environment — the GitHub API is blocked by the egress proxy — so verify that too.

**No TLS.** nginx listens on `:80` only, and the `WRITE_API_KEY` travels as a cleartext header.

Why this is a grant issue and not just an ops issue: **you will not obtain a data agreement for
HUG emergency department, 144/CASU or ICU occupancy data for a system in this state.** Those
agreements are the load-bearing assumption of the whole proposal. A CCER submission and a UNIGE
data-protection review will both ask about transport security, secret management and disaster
recovery, and the honest current answers are the wrong ones.

The inverse is the opportunity. Fixed — TLS, secrets in a proper store, schema under migration
control, ANN index, dedup constraints — the same infrastructure becomes a **strong feasibility
argument**: audited, reproducible infrastructure already handling a six-figure corpus, ready to
receive sensitive operational data. That sentence in a research plan is worth a great deal, and
it is roughly two weeks of work away.

## A caution on the generated documentation

`GESICA_Scientific_Base.md` and `ROADMAP.md` are marked as automatically generated
("LiteRev-Evidence (génération automatique)", "Manus AI"). They contain specific performance
claims with citations — "LightGBM + météo, AUC 0.85, Nakashima 2025", "Ensemble RMSE −30%",
"Pál-Jakab et al., *Public Health*, 2026".

**Verify every one of these before any of it reaches the research plan.** Automatically generated
literature summaries produce citations that are plausible, well-formatted and sometimes wrong —
wrong year, wrong journal, wrong number, occasionally a paper that does not exist. A referee in
emergency medicine will recognise the literature you are citing at them. One fabricated reference
in a state-of-the-art section does more damage than a weak paragraph, because it calls the
applicant's judgement into question rather than their prose.

This is also, incidentally, a research question sitting inside your own project: how reliable is
automated evidence extraction when the extracted quantities are going to be used as priors? You
are in an unusually good position to study it, having built the extractor.

## Revised feasibility picture for Candidate D

| Element | Before seeing the repo | Now |
| --- | --- | --- |
| Evidence extraction pipeline | To be built | **Built, running, 81k documents** |
| Literature-to-prior mechanism | Proposed as WP1 | **Prototype implemented** |
| Forecasting models | To be built | Prophet, AutoML, SEIR ensemble in place |
| Alert banding | Proposed | Implemented |
| Operational data feeds | To be secured | Weather, Sentinelles, OSRM connected |
| **HUG / 144 / ICU data** | To be secured | **Still the gap — and now gated on security hardening** |
| Preliminary-work section | Thin | **Exceptionally strong** |

The single remaining gap is the same one as before — clinical operational data — and it has
acquired a prerequisite. That ordering is now the plan: harden, then request data, then write.

## Actions

- [ ] **Rotate the OpenAI key** if not already done; confirm repository visibility
- [ ] TLS on the live host; move secrets out of the systemd override
- [ ] Bring the schema under Alembic properly; add unique constraints on DOI/PMID; ANN index
- [ ] Then approach HUG, 144/CASU and the ICU for data agreements, with the hardened
      infrastructure as part of the ask
- [ ] Verify every citation in the generated documents before reusing any of it
- [ ] Decide what LiteRev-Evidence *is* in the application: preliminary work and instrument,
      never a deliverable
