# Two-page project note (EN) - mirror of Erol's final French version (8 Oct)

**COLDSTART: Anticipating and quantifying health-system crises before the outcome is observable**

SNSF Ambizione application (submission: 3 November 2026) · Applicant: Dr Erol Orel · Host:
Institute of Global Health, Faculty of Medicine, University of Geneva · Duration: 4 years

## The problem

When a health crisis begins, the local data needed to forecast it do not yet exist. The
best-performing models require years of history; they are therefore weakest exactly where
decisions - arming ambulances, opening beds, triggering an escalation - are most costly and
least reversible.

Yet quantitative information is available from day one: the published literature on analogous
events - weather-demand associations, surge magnitudes and delays, lengths of stay and
occupancy, transmission parameters. It is almost never used as formal prior information,
because nobody has established whether doing so helps or harms.

## The question

The project poses the question end to end: can published evidence be reliably extracted and
transported to the local setting to forecast the state of the care system when local data are
missing; can we detect early when it misleads; does any gain change operational decisions;
and can the complete chain run automatically, verified against observed outcomes, under
pre-registered rules?

The project builds on existing ground: LiteRev-Evidence, the extraction and modelling
prototype under development; the data cartography built for GESICA; and the ongoing Geneva
legionellosis study (BASEC 2026-00324).

## Five strands

1. **Extraction** - measure the reliability of automated extraction of quantitative
   parameters from the literature, against a dual human-extraction benchmark, and correct the
   identified biases; the literature also supplies explanatory variables, recommended model
   families and outcome and threshold definitions.
2. **Modelling** - represent the state of the care system as a latent regime process
   (routine / elevated / strained / critical) rather than a threshold applied to a point
   forecast; epidemiological models (SEIR-type) enter only for epidemiological crises,
   environmental crises being driven by exposure-response structures.
3. **Evaluation** - test, historical episode by historical episode, whether literature-derived
   priors improve early-crisis forecasts, using at each moment only the data and the
   literature available at that date, with automated selection of the best model under
   pre-registered rules.
4. **Decision** - evaluate not statistical accuracy but decision benefit, from escalation
   thresholds elicited in a structured way (SHELF protocol) from dispatchers, emergency
   physicians and capacity managers.
5. **Automation and living review** - public data connected automatically; models re-run at
   each variable's cadence; statistical assumptions checked; daily literature monitoring; at
   the end of the project, for validated event types and subject to authorisation, a daily
   observation-mode dashboard, recorded and evaluated prospectively, never decisional during
   the project.

## How it will be tested

Three Geneva archetypes, fixed for the whole project: **respiratory epidemics** (SARS-CoV-2,
influenza, RSV) carry the confirmatory test; **heatwaves** (with air pollution as
co-exposure) carry the generalisation test, run only if the first succeeds; Geneva
**legionellosis** is the contrasting fourth-year extension (case incidence). Two arms - with
and without evidence - pass through the same pre-registered automated selection; the
machinery is validated first, end to end, on **open public data** (a public benchmark), then
on Geneva's operational series.

## The data

Only **retrospective extracts aggregated to daily counts**: no identifiers, no
individual-level data, no voice recordings, no free text. The scope is the canton of Geneva:
CASU-144 dispatch data; emergency-department presentations and ICU occupancy; the cantonal
physician and pharmacist and SIG for the environmental strands. Plus all other freely
available data (climate, demographics, etc.). Operational access would follow the official
route: a CCER submission.
