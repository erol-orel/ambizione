# Two-page project note, English: for Teodoro (and any English-speaking recipient)

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
because nobody has established whether doing so helps or harms. That is the project's central
question, posed falsifiably, from extraction all the way to a running, prospectively verified
system.

## Where the project comes from

- **LiteRev-Evidence**, the prototype I developed at the Institute (federated search of the
  open literature, screening, provenance-tracked extraction, pooling into parameter
  distributions, automated fitting and ranking of candidate models), already walks this
  pipeline; the project turns it into a validated instrument and puts it to the test.
- **GESICA** supplies the data cartography (a referenced inventory of 28 surveillance sources)
  and the working relationships with HUG emergency medicine and the CASU-144 dispatch centre;
  our joint systematic review of AI in prehospital emergency medicine (submitted 2026) shows
  that forecasting is the most-addressed task and that uncertainty, transparency and
  explainability are rarely treated.
- **The Geneva legionellosis study** (BASEC 2026-00324, ethics granted), whose data work I
  lead, supplies the contrasting extension archetype.

## What the project does (five strands, 48 months)

1. **Extraction** - measure the reliability of automated extraction of quantitative parameters
   from the literature (against a dual human-extraction benchmark) and correct the identified
   biases; the literature also supplies explanatory variables, recommended model families and
   outcome and threshold definitions, transported to the local setting.
2. **Modelling** - represent the state of the care system as a **latent regime process**
   (routine / elevated / strained / critical) rather than a threshold applied to a point
   forecast; epidemiological models (SEIR-type) enter only for epidemiological crises,
   environmental crises being driven by exposure-response structures.
3. **Evaluation** - test, historical episode by historical episode, whether literature-derived
   priors improve early-crisis forecasts, using at each moment only the data *and the
   literature* available at that date, with automated selection of the best model under
   pre-registered rules.
4. **Decision** - evaluate not statistical accuracy but **decision benefit**, from escalation
   thresholds elicited in a structured way (SHELF protocol) from dispatchers, emergency
   physicians and capacity managers.
5. **Automation and living review** - public data connected automatically; models re-run at
   each variable's cadence; statistical assumptions checked on every fit; daily literature
   monitoring; at the end of the project, for validated event types and subject to
   authorisation, a **daily observation-mode dashboard**, recorded and evaluated prospectively
   against observed outcomes, never decisional during the project.

## Data and the regulatory route

The project uses only **retrospective extracts aggregated to daily counts** (no identifiers,
no individual-level data, no free text). The scope is the canton of Geneva: CASU-144 dispatch
data as the primary outcome series, emergency-department presentations and ICU occupancy as
complementary channels, the cantonal physician and pharmacist and SIG for the environmental
strands. The machinery is validated first, end to end, on **open public data** (a public
benchmark); feasibility therefore rests on no single agreement. Operational access would
follow the **official route: a CCER submission with me as applicant**, preceded by
institutional data agreements prepared before month 1.

## Hosting and independence

The programme would run as an **independent research programme alongside the Institute of
Global Health's groups**, under the SNSF template guarantees (the applicant's scientific
direction, selection and supervision of team members, budget authority, senior authorship),
with a methodological collaboration with DS4DH on the evidence-extraction work package. **No
financial implication for the partners**: the SNSF covers the applicant's salary and a project
budget (CHF 250,000 over 4 years; doctoral students and postdocs excluded under the 2026
rules). What remains afterwards: the validated open instruments (extraction benchmark, public
cold-start benchmark, evidence-to-prior library), the dashboard nucleus, and joint
publications.

**Timeline.** Submission: 3 November 2026 · Decision: August 2027 · Start: between September
2027 and September 2028.
