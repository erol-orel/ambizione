# "When local data are scarce" — is that the right framing?

You are partly right, and the part you are right about is worth fixing. But the objection sharpens
the project rather than dissolving it.

## The imprecision you spotted

"Local data are scarce" is loose, and a referee could attack it exactly as you just did: *there is
an enormous amount of data available at crisis onset.* ERA5 reanalysis back to 1940, MeteoSwiss,
pollution, demographics, mobility, SITG territorial layers, Sentinelles, federal and European
surveillance, the entire published literature — your platform already ingests most of it. The
premise, stated that way, looks false.

## The precise statement

**Covariates are abundant. Outcome observations are not.**

At the onset of a crisis you can assemble terabytes of *X* and you have perhaps eight noisy
observations of *y* — the thing you actually need to forecast, in this population, under this
health system, for this event. No amount of automated acquisition changes that, because the
quantity is not yet in the world to be acquired. It arrives one day at a time.

So the cold-start problem is not a **data** problem. It is a **labelled-outcome** problem, and it
is worse than ordinary small-*n* because the covariate space is simultaneously enormous. That
combination — many predictors, almost no outcomes — is the classic recipe for models that fit
beautifully and forecast disastrously.

Your platform's data-gathering is therefore not a refutation of the premise. **It is what creates
the sharpest version of it.**

## Which makes the project bigger, not smaller

There are three sources of information at crisis onset, with genuinely different properties:

| Source | Availability at onset | Problem |
| --- | --- | --- |
| **Context and covariates** — weather, pollution, demography, mobility | Abundant, machine-readable, automatable | Enormous space, almost no outcomes to select against |
| **Published evidence** — effect sizes, surge magnitudes, parameters | Abundant but heterogeneous | Extraction error; unknown transportability |
| **Local outcome observations** | Near zero, growing daily | The only source unambiguously about *this* event |

The project's real question, stated properly, is **how these three should be combined, what each
is worth, and how the weighting should change as the third accumulates.** That is a better
question than the one currently on the page, and it is the one your platform is built to ask.

So: keep the cold-start framing, and make it precise — **before the outcome is observable**, not
"when data are scarce".

## Two traps your framing walks into — both become contributions if handled

### 1. SEIR-generated data is not new information

You wrote that the platform can *produce* data using SEIR+ models when none is available. Be
careful here; this is the most dangerous idea in the set.

If you simulate trajectories from a compartmental model whose parameters came from the literature,
then fit a statistical model to those simulations and treat the result as evidence, **you have
counted the same prior twice.** The apparent precision is manufactured: the posterior tightens
because you generated more rows, not because you learned anything. In the cold-start regime, where
the prior dominates by construction, this produces exactly the failure H3b is meant to detect —
confident and wrong — while removing the diagnostic that would catch it, since prior–data
discrepancy cannot flag a conflict between a prior and its own output.

Legitimate uses of simulation exist, and the distinction *is* the contribution:

- **Simulation-based inference / emulation** — simulate to characterise an intractable likelihood,
  then confront it with *real* observations. Legitimate.
- **Structural regularisation** — mechanistic constraints (conservation, monotonicity, plausible
  trajectory shapes) restricting the hypothesis space. Legitimate, and it *is* prior information,
  declared as such.
- **Prior predictive checking** — simulate to see whether your priors imply absurd epidemics. Not
  merely legitimate but obligatory, and cheap.
- **Generating pseudo-observations and treating them as data.** Not legitimate. This is the trap.

**Recommendation:** state this explicitly in WP2. A paragraph distinguishing simulation-as-prior
from simulation-as-data, with prior predictive checks as standard practice, turns a vulnerability
into evidence of methodological maturity. Referees notice when an applicant names the trap they
could have fallen into.

### 2. "Find any data that is findable" is the Google Flu Trends failure mode

Automated acquisition of an unbounded covariate space, selected against a short outcome series, is
precisely how Google Flu Trends came to overestimate influenza by more than a factor of two — the
canonical cautionary tale in this literature [Lazer 2014]. With hundreds of candidate covariates
and twenty outcome observations, something will always correlate, and out of sample it will not.

**Recommendation:** the covariate space must be **pre-specified and justified** — weather,
demography, calendar, epidemic indicators, each with a stated rationale — rather than discovered.
Anything found automatically is reported as exploratory and validated on a held-out crisis. This
costs nothing you actually wanted and pre-empts a fatal objection.

Note the symmetry: this is the *same* problem as H1, one level up. There, automated extraction of
published estimates risks priors that are too confident; here, automated acquisition of covariates
risks associations that are too confident. The project's stance is consistent — automation makes
scale possible and overconfidence likely, and quantifying that trade-off **is the research**.

### 3. Private data upload — governance, not science

Allowing partners to upload private data is a useful platform capability and not a research
contribution, so it belongs nowhere in the research plan. It does sharpen the infrastructure
issue: a platform receiving third-party health data over plain HTTP, with secrets in a systemd
override, will not pass a data-protection review. Same conclusion as before, now with a second
reason.

## Your GESICA report already had the precise version

`Rapport_GESICA_final.docx` §2 divides surveillance variables into four classes: **outcome**
(confirmed incidence, hospitalisations — what the model must predict), **early-signal** (144 call
symptoms, wastewater, web search), **susceptibility** (vaccination, seroprevalence) and
**covariates** (environment, contacts, calendar). That is a sharper version of the distinction I
was reaching for, and the plan now uses your four classes rather than my two. Only the first is
scarce at onset.

**Wastewater deserves its own paragraph, and I added one.** Switzerland has monitored SARS-CoV-2,
influenza and RSV in wastewater since 2020 (Eawag, on mandate from the BAG, and national reference
centre since early 2026), and the signal leads clinical presentation. It looks like an escape from
the cold-start problem. It is not — converting viral load into expected presentations needs a
shedding-to-incidence calibration, and that calibration is a quantitative parameter drawn from
published studies of uncertain transportability. **Wastewater relocates the problem into exactly
the place this project studies**, which makes it a good test case rather than a counterexample.
It is now an extractable parameter class in T1.1.

Two caveats from your own report, worth keeping in view: the national programme shrank from 100+
treatment plants to about 10 since summer 2023, and Geneva coverage is confirmed while Vaud is
not. So wastewater is a strong supporting signal, not a load-bearing one.

Pharmaceutical markers (dextromethorphan, pheniramine, clarithromycin in wastewater) and OTC
pharmacy sales are the same shape: genuinely leading, non-clinical, aggregate — and, in your
inventory, still *pistes à explorer* on access. They belong in the covariate set as opportunistic
rather than assumed.

## What I changed in the plan

1. **Subtitle and summary** — "before the outcome is observable" rather than "when local data are
   scarce", plus a sentence conceding that context data is abundant. **Conceding the point in the
   text is what disarms it.**
2. **§1.2** — the many-covariates/few-outcomes combination stated explicitly, with [Lazer 2014] as
   the documented failure mode.
3. **WP2** — a paragraph on simulation-as-prior versus simulation-as-data, with prior predictive
   checks.

## Why this is a good sign

You found the objection before a referee did — the purpose of the hostile-reader test in
the hostile-reader test. It is also the second time interrogating your own platform produced the sharper
question; the first was the literature-prior problem itself. That pattern is worth trusting.
