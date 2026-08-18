# 4. Detailed research plan

Four work packages over 48 months. WP1 and WP2 run in parallel from the start and are
**deliberately independent**: WP2's methodological development does not wait on WP1's extraction
results, and WP3 can be executed with weakly informative priors if WP1 concludes that
evidence-derived priors are unusable. That negative result would itself answer O1 and O3.

Staffing: PI `[[Erol Orel, XX%]]` and one doctoral researcher (`[[months]]`). The PI executes
WP2 personally — it is the methodological core and the source of the project's distinctiveness.

---

## WP1 — From published evidence to quantitative priors *(M1–M24)*

**Question.** Can quantitative parameters be extracted from the literature reliably enough to
serve as priors, and what is the structure of the error?

### Tasks

**T1.1 — Define the extractable parameter classes (M1–M4).**
Not all quantities are equally extractable. Fix, in advance and with justification, the classes
in scope: weather–demand associations (relative risk or percentage change per unit exposure),
surge magnitudes (peak-to-baseline ratios), epidemic transmission parameters, length-of-stay and
occupancy distributions. Register the extraction protocol before running it.

**T1.2 — Build a gold-standard benchmark (M3–M10).**
Two independent expert extractors manually extract the target parameters from a stratified random
sample of `[[n ≈ 300–500]]` publications drawn from the LiteRev-Evidence corpus, with adjudication
of disagreements. Stratify by parameter class, reporting quality and publication venue. This
benchmark is a deliverable in its own right: no such reference set exists for quantitative
extraction, and it is reusable by others.

**T1.3 — Characterise automated extraction against the benchmark (M8–M16).**
Evaluate the platform's extraction against the gold standard: agreement on point estimates,
agreement on reported uncertainty, and — the substantive test of H1 — whether the *dispersion* of
extracted estimates reproduces the dispersion of manually extracted ones. Decompose error by
parameter class, reporting completeness and study design. Assess sensitivity to the underlying
language model, since the platform's behaviour must not be an artefact of one model version.

**T1.4 — Model the extraction error and construct corrected priors (M14–M22).**
Represent extraction error explicitly as a measurement-error layer above the evidence synthesis,
so that a prior carries both between-study heterogeneity and extraction uncertainty. Compare
pooling strategies: naive inverse-variance, quality-weighted (as currently implemented),
random-effects meta-analytic-predictive, and power-prior discounting.

**T1.5 — Transportability assessment (M18–M24).**
For each parameter class, assess formally whether the study populations support transport to the
Geneva setting: characterise effect-modifier distributions, and where transport is not supported,
quantify the resulting bias rather than assuming it away.

**Deliverables.** D1.1 gold-standard benchmark dataset (open). D1.2 characterisation of automated
extraction error, with correction. D1.3 open library converting corpus queries into prior
distributions with documented provenance.

**Risk.** Manual extraction is slow and expensive. *Mitigation:* the sample size is set by the
precision needed to detect the heterogeneity bias in H1, not by ambition; a simulation-based
sample-size justification is done in T1.1. If expert time is the binding constraint, narrow to
two parameter classes and say so.

---

## WP2 — Regime-switching forecasting with an extreme-value tail *(M1–M30)*

**Question.** Does representing health-system state as a latent regime process, rather than as a
threshold on a point forecast, anticipate escalation better?

### Tasks

**T2.1 — Specify the state process (M1–M8).**
A Bayesian hierarchical **Markov regime-switching model** over the joint series of emergency call
volume, emergency department presentations and intensive care occupancy. Three to four latent
regimes with an ordinal interpretation (routine / elevated / strained / critical); regime-dependent
level, trend and dispersion; transition probabilities allowed to depend on covariates (weather,
epidemic indicators, calendar structure). Fitted by MCMC or variational approximation depending
on dimension; identifiability handled by ordering constraints on regime means, with label-switching
diagnostics reported.

**T2.2 — Tail behaviour (M6–M14).**
The critical regime is by construction rarely observed, so the regime model alone will estimate it
poorly. Complement it with a peaks-over-threshold generalised Pareto representation of exceedances
in the operational series, and couple the two so that the probability of entering the critical
regime is informed by the tail model rather than by the handful of observed transitions.
Threshold selection by standard stability diagnostics, with sensitivity reported rather than a
single chosen value.

**T2.3 — Prior structure (M10–M20).**
Define how WP1's evidence-derived distributions enter: as priors on covariate effects, on regime
means, and on transition intensities. Implement **adaptive discounting** so the weight on the
prior declines as local data accumulate, with the discount rate itself estimated. This is the
machinery that H3b tests.

**T2.4 — Baselines and comparators (M12–M22).**
Pre-specify the comparison set so the evaluation cannot be tuned after the fact: seasonal
naive; Farrington-style detection; SARIMA/Prophet with thresholding; gradient boosting with
weather features; an ensemble; and the regime-switching model with weakly informative priors.
The last isolates the contribution of the priors from the contribution of the representation.

**T2.5 — Implementation (M18–M30).**
Reference implementation, documented and open, integrated with the existing platform.

**Deliverables.** D2.1 model specification and identifiability analysis. D2.2 open implementation.
D2.3 methodological paper on regime-switching with evidence-derived priors for health-system
surge.

**Risk.** Regime models can be weakly identified when regimes are not well separated.
*Mitigation:* simulation study in T2.1 establishing the separation and series length needed for
recovery, run **before** application to real data; if the diagnostics fail, fall back to an
ordinal state-space formulation, which is weaker but identifiable. Report this honestly either
way — a negative identifiability result is a genuine contribution to a literature that mostly
does not check.

---

## WP3 — Retrospective cold-start evaluation *(M12–M42)*

**Question.** Do evidence-derived priors improve forecast skill when local data are scarce, and
when do they mislead?

### Tasks

**T3.1 — Assemble the retrospective operational record (M12–M20).**
`[[HUG emergency department presentations; 144/CASU call and dispatch records; ICU occupancy;
MeteoSwiss; cantonal and federal surveillance. Specify years and granularity once agreements are
in place.]]` Harmonise into a reproducible pipeline with documented completeness.

**T3.2 — Rolling-origin evaluation respecting the true information set (M18–M32).**
The methodological heart of the evaluation. For each historical crisis onset, refit at successive
origins using **only** data available at that moment — including only literature published before
that date, which the corpus's indexing makes enforceable. Forecast forward at operationally
relevant horizons (`[[7, 14, 28 days]]`). This constraint is what makes the cold-start claim
meaningful and it is routinely violated in retrospective forecasting studies.

**T3.3 — Skill and calibration (M24–M36).**
Evaluate with proper scoring rules — continuous ranked probability score, logarithmic score —
plus calibration (PIT histograms, coverage) and sharpness. Report skill **as a function of
elapsed time since onset**, which is the quantity H3a is about; a single aggregate number would
average away the effect being tested.

**T3.4 — Failure analysis (M28–M38).**
Deliberately adversarial. Identify episodes where priors degraded performance; characterise them;
test whether the divergence was detectable early from prior–data discrepancy diagnostics (H3b).
Include stress tests with deliberately misspecified priors — drawn from a different pathogen, a
different health system, a different era — to bound the damage.

**T3.5 — Waterborne archetype (M34–M42, extension).**
Apply the framework to Geneva legionellosis using the linked case–installation data. Scoped as an
extension: it strengthens the generalisability claim and its omission does not invalidate O3.

**Deliverables.** D3.1 reproducible evaluation pipeline. D3.2 the cold-start result. D3.3 failure
and stress-test analysis.

**Risk — and this is the project's principal risk.** Clinical operational data may be delayed or
refused. *Mitigation, in order:* (i) agreements initiated before the grant starts, with the
supporting letters in this application; (ii) infrastructure hardening completed in advance so
that data-protection review is not the obstacle; (iii) **fallback design** — the cold-start
hypothesis can be tested on openly available surveillance series (federal and cantonal
notifications, Sentinelles, European surveillance) plus the Legionella linkage already covered by
ethics. This is a weaker test, because it loses the operational endpoint, but it is a real one,
and it means the project cannot fail outright on data access.

---

## WP4 — Decision relevance and prospective evaluation *(M24–M48)*

**Question.** Would this change what anyone does?

### Tasks

**T4.1 — Threshold elicitation (M24–M32).**
Structured elicitation with emergency physicians, dispatch supervisors and hospital capacity
managers `[[HUG, 144/CASU]]`: what action becomes available at each escalation level, what it
costs, what a false alarm costs, and what a missed escalation costs. The output is an explicit
loss structure, not a preference survey.

**T4.2 — Consequence-weighted evaluation (M30–M40).**
Re-evaluate WP3's comparisons under the elicited loss structure using net benefit and
decision-curve analysis. Test H4 by comparing elicited thresholds with statistically optimal ones
and determining whether the ranking of methods changes.

**T4.3 — Value of information (M34–M42).**
Quantify what a perfect forecast would be worth under the elicited loss structure — an upper
bound on the value of any further methodological work, and a discipline on the field's tendency
to pursue marginal skill improvements of unknown worth.

**T4.4 — Prospective shadow-mode deployment (M36–M48).**
Run the framework prospectively alongside routine operations, issuing forecasts that are recorded
but **not** used for decisions. Compare prospective skill with retrospective estimates — the gap
between the two is one of the most useful and least reported quantities in this literature.

**Deliverables.** D4.1 elicited loss structure and threshold analysis. D4.2 decision-analytic
evaluation. D4.3 prospective validation report.

**Risk.** Shadow deployment may not be authorised, or the observation period may contain no
crisis. *Mitigation:* shadow mode involves no clinical action and is the least demanding form of
deployment; if it is refused, T4.2 and T4.3 stand alone and the project's claims are retrospective,
which is stated rather than concealed. A quiet observation period is a real possibility and is why
T4.4 is scoped as validation of calibration in routine conditions, not as a crisis test.

---

## Dependencies, milestones and timing

`[[Insert Gantt figure.]]`

**No work package is contingent on another succeeding.** WP2 proceeds under weakly informative
priors if WP1 returns a negative result; WP3 proceeds on open surveillance data if operational
data are delayed; WP4's core analysis is retrospective and does not require deployment. This is
deliberate: serial dependency on an uncertain result is the standard feasibility objection to
four-year plans, and the design removes it.

| Milestone | Month | Criterion |
| --- | --- | --- |
| M1 — Extraction benchmark complete | 10 | D1.1 released |
| M2 — Regime model identifiable in simulation | 12 | Recovery demonstrated; else fallback triggered |
| M3 — Operational data in place | 20 | Agreements executed and data harmonised; else fallback triggered |
| M4 — Cold-start result | 32 | H3a tested with pre-specified comparators |
| M5 — Decision-analytic evaluation | 40 | H4 tested |
| M6 — Prospective validation | 48 | T4.4 reported |

## Methods, data protection and reproducibility

All analyses in R and Python, version-controlled, with a registered analysis plan for the
confirmatory comparisons in WP3. Clinical data processed under `[[CCER approval — new submission
with the PI as applicant]]` in the University of Geneva secure environment. Code released open
source; the extraction benchmark released openly; clinical data not shareable, with synthetic
equivalents provided for reproducibility.
