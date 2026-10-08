# Two-page project note (single neutral version, EN): mirror of the French note

**COLDSTART: Anticipating and quantifying health-system crises before the outcome is observable**

SNSF Ambizione application (submission: 3 November 2026) · Applicant: Dr Erol Orel · Proposed
host: Institute of Global Health, Faculty of Medicine, University of Geneva (independent
research programme) · Duration: 4 years

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
prototype I developed; the data cartography built for GESICA; and the ongoing Geneva
legionellosis study (BASEC 2026-00324), whose data work I lead.

## What I will do (five strands, 48 months)

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
   each variable's cadence; statistical assumptions checked on every fit; daily literature
   monitoring; at the end of the project, for validated event types and subject to
   authorisation, a daily observation-mode dashboard, recorded and evaluated prospectively,
   never decisional during the project.

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
CASU-144 dispatch data as the primary outcome series; emergency-department presentations and
ICU occupancy as complementary channels; the cantonal physician and pharmacist and SIG for
the environmental strands. Operational access would follow the **official route: a CCER
submission with me as applicant**, preceded by institutional data agreements prepared before
month 1.

## Team and timeline

An independent programme hosted at the Institute of Global Health, under the SNSF template
guarantees (the applicant's scientific direction, team supervision, budget authority, senior
authorship). Team: the applicant, one scientific/technical collaborator (50%) and a
contracted independent extractor; SNSF project budget of CHF 250,000 over 4 years, the
applicant's salary covered separately. **Timeline**: submission 3 November 2026 · decision
August 2027 · start between September 2027 and September 2028.
