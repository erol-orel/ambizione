# Candidate D — evidence-informed early warning and surge forecasting

Your hesitation, worked through. Short answer: **this is the better Ambizione, and I would switch
to it — but not in the form you described it.** The idea contains an excellent proposal and a
weak one, and which of the two ends up on the page decides the outcome.

---

## What you have that I did not know about

`gesica-interreg-application-form.pdf`, `gesica-social-media-data-sources-report.pdf` and
`ai-in-ems-systematic-review-2026.pdf` change the picture in three ways.

**1. A second scientific home, independent of Keiser.** GESICA (Interreg VI France–Suisse,
Sept 2024 – Feb 2027) runs through HUG Emergency (Prof. Thibaut Desmettre, Dr Robert Larribau),
UNIGE (Prof. Douglas Teodoro), HES-SO, Université de Franche-Comté and Techwan. Olivia Keiser
does not appear anywhere in it. Combined with your willingness to be hosted outside ISG, this is
the cleanest available answer to the independence problem I flagged — and independence was the
single biggest risk in the dossier.

**2. The line already exists and you are already on it.** You are third author on the AI-in-EMS
systematic review (submitted Feb 2026), and **LiteRev is named in its methods** as the tool used
to structure 138 papers. Your own first-author tool, in an emergency-medicine review, with the
HUG emergency network. That is a research line with your fingerprints on it.

**3. Timing works better than Legionella.** GESICA ends **Feb 2027**. An Ambizione starting
mid-to-late 2027 *succeeds* it rather than duplicating it — a much easier story to tell than the
Legionella project, which runs to May 2027 with Keiser as project leader and sponsor.

---

## The problem with the idea as you described it

You described a system that automatically extracts evidence from the literature, **automatically
finds data, automatically builds the best model on the best risk-factor variables**, and emits a
normal/tense/alarming state for emergency services.

As engineering, that is a coherent product. As an Ambizione research plan it has a specific and
serious weakness: **it is a tool, not a question.** The panel scores scientific relevance,
originality, feasibility and suitability of methods. A referee reading "the system will select
the best algorithm on the best variables" will ask two things you must be able to answer:

- *What is the scientific claim, and how would we know if it were false?* "The tool works" is not
  falsifiable in the way a panel needs.
- *Why would literature-derived risk factors transport to Geneva in 2027?* Published effect sizes
  are context-specific, selectively reported, and estimated in other populations under other
  policies. The step from "the literature reports X as a risk factor" to "X belongs in a surge
  forecast for HUG" is the entire scientific problem — and in the version you described, it is
  assumed rather than studied.

There is also a competitive point. Automated model building is crowded and industrially funded.
Epidemic forecasting has organised hubs — the US and European forecast hubs, ensemble
infrastructure, large teams. Entering that space as "another forecasting system" is not a fight
worth picking on CHF 250k.

**None of this kills the idea.** It says the proposal has to be about the hard part rather than
the automation around it.

---

## The version I would write

> **When a health crisis begins, the local data needed to forecast it does not yet exist — and
> that is exactly when decisions are most consequential and least reversible. The only
> information available is prior evidence from analogous events elsewhere. Can that evidence,
> extracted systematically from the literature, be turned into quantitative priors that measurably
> improve early-crisis forecasting — and if so, when does it help, when does it mislead, and how
> should a clinician act on it?**

This is the cold-start problem in crisis forecasting, and it is a real, open, testable question.
Reframing from *automation* to *the cold-start problem* changes everything about how the proposal
reads:

| Your framing | The reframing |
| --- | --- |
| A system that builds models automatically | A study of whether prior evidence improves forecasts when local data is scarce |
| Success = the tool works | Success = a measured improvement in forecast skill, with the conditions under which it fails |
| Competes with forecasting hubs | Addresses the regime the hubs are weakest in |
| Literature extraction is plumbing | Literature-to-prior elicitation is the scientific contribution |
| Not falsifiable | Falsifiable by proper scoring rules against pre-registered baselines |

### The part that is distinctively yours

**Normal / tense / alarming is a regime-switching model.** You reached for a multinomial outcome;
what you are actually describing is a latent state process with persistent regimes and abrupt
transitions — Markov regime-switching, which is *your* field from fifteen years in quantitative
finance. Add extreme value theory for the tail behaviour of the alarming state, and stress
testing and scenario analysis for the decision layer, and you have a methodological approach that
**neither an epidemiology group nor a machine-learning group would produce.**

That is the answer to "why you". It is not that you can build the tool — many can. It is that you
are one of very few people who would model a hospital surge the way a risk manager models a
market crisis, and who has the literature-synthesis tool to build the priors. Make that the
argument, because it is genuinely true and genuinely rare.

A related point worth building in: the alarming state is rare, so a purely accuracy-based
evaluation will be underpowered and will reward a model that never cries wolf. Confronting this
directly — rare-event estimation, proper scoring rules, decision-analytic evaluation rather than
AUC — turns your biggest statistical vulnerability into a section that demonstrates expertise.

### Thresholds are a contribution, not a parameter

Where "tense" ends and "alarming" begins is not a modelling choice — it is a decision-theoretic
one, and it depends on what HUG and the 144/CASU can actually *do* differently at each level.
Eliciting those thresholds with the people who would act on them, and evaluating on **decisions
changed and outcomes affected rather than prediction accuracy**, is both the most useful part of
the project and a strong differentiator. Most forecasting papers stop at discrimination metrics.
Stopping there is why most forecasting tools are never used.

### Work packages, sketched

- **WP1 — Evidence to priors.** Extend LiteRev from retrieval and clustering to structured
  extraction of quantitative effect estimates, with the uncertainty and the risk of bias carried
  through. Deliverable: a reproducible literature-to-prior pipeline. *The scientific question
  here is whether extracted estimates are fit to serve as priors at all* — and a negative answer
  is a publishable, valuable result, which is what makes this a research WP rather than a build.
- **WP2 — Regime-switching surge forecasting.** Hierarchical Bayesian regime-switching models of
  ED presentations, 144/CASU call volume and ICU occupancy, with EVT for the tail. Priors from
  WP1 versus weakly informative baselines.
- **WP3 — Retrospective evaluation across crisis archetypes.** Where the cold-start claim is
  tested: fit at the point where a real crisis began, forecast forward, score honestly against
  what happened. COVID waves, influenza seasons, the 2003 and 2022 heat waves.
- **WP4 — Decision layer and prospective evaluation.** Threshold elicitation with HUG and 144,
  decision-curve and value-of-information analysis, and a prospective shadow-mode deployment in
  the final year.

### Scope warning

Four work packages, one PhD student and about CHF 250k. **Two crisis archetypes in WP3, not
four.** Respiratory epidemic and heat wave give you a genuine generalisability claim; adding more
buys marginal credibility at real feasibility cost, and a referee counting person-months will
notice before you do.

---

## The elegant use of your Legionella data

You do not have to abandon the Legionella work — and it is better used here than as its own
proposal. A **waterborne outbreak is a third crisis archetype with completely different dynamics**
from a respiratory epidemic or a heat wave, and you hold linked case–installation data for it that
nobody else has, with ethics already granted.

Used this way, the Legionella data stops competing with this proposal and starts strengthening it:
it becomes the hardest test of the framework's generalisability, on data unique to you. If you
want a third archetype, that is the one to add — and it is a much better argument than adding
another respiratory dataset.

This also resolves your hesitation without loss. The Legionella study continues under Keiser as
funded, ends May 2027, produces papers, and supplies a validation domain. Nothing is wasted.

---

## Honest comparison

| | Legionella (Candidate A) | Crisis forecasting (Candidate D) |
| --- | --- | --- |
| **Independence from Keiser** | Poor — her project, her sponsorship | **Strong** — different network entirely |
| **Host unit options** | ISG, awkward | HUG / Teodoro's group / medical informatics |
| **Fit to your biography** | Good | **Excellent** — time series, rare events, econometrics |
| **Data secured** | **Excellent** — ethics granted | Moderate — needs HUG, 144, ICU agreements |
| **Originality** | Good, narrow field | **Strong if reframed**, weak if pitched as a tool |
| **Field crowding** | Low | High — needs the sharp differentiator |
| **Ambition / visibility** | Moderate | **High** |
| **Risk of failure** | Low | Moderate — validation is genuinely hard |
| **Your own enthusiasm** | Moderate | **Evident** |

## Recommendation

**Switch to Candidate D, reframed as the cold-start problem, with Legionella as a validation
domain.** Independence was the biggest threat to this application, and D solves it in a way that
A cannot. It also happens to be the project you clearly want to do, which matters more than it
sounds — you have eleven weeks and then four years of it.

The reservation is real and I want it on the record: **D is only stronger than A if the reframing
holds.** Written as an automated model-building platform, D scores worse than A, because A at
least has secured data and a clean question. The whole bet is on the proposal being about the
cold-start problem and the regime-switching methodology rather than about the tool. If you find
when drafting that you keep sliding back into describing the system rather than the question,
that is a signal to reconsider.

## What has to happen in the next two weeks

| # | Action | Why it is urgent |
| --- | --- | --- |
| 1 | Decide the **host unit** — Teodoro's group, an HUG-affiliated unit, or another | Drives both confirmation letters, the longest lead time in the process |
| 2 | Secure **written data-access commitments**: HUG ED, 144/CASU, ICU occupancy | The load-bearing assumption. Verbal links are not evidence; a referee needs letters |
| 3 | Talk to **Desmettre, Larribau and Teodoro** about roles — collaborators, not leaders | Their support letters are strong; their leadership would undo the independence gain |
| 4 | Confirm what GESICA will and will not have delivered by Feb 2027 | The proposal must start where GESICA stops. Overlap is the obvious referee objection and you should pre-empt it explicitly |
| 5 | Check the **ethics route** — new BASEC as PI, or amendment | Being PI on your own ethics submission is concrete evidence of independence |
| 6 | Sketch WP2 on paper — the regime-switching specification | If the methodological core does not hold up, better to know now |

Item 2 is the one that can kill the application. Do it first.

---

## Addendum 2 — LiteRev-Evidence is far more built than I assumed

See `literev-evidence-assessment.md`. In short: 81,209 documents, 323,868 embedded chunks, a
live production stack, SEIR ensemble modelling, AutoML, and — critically —
`pool_weighted()` / `params_to_distributions()` in `seir_model.py`, which is
**literature-to-prior elicitation already implemented**. WP1 as I sketched it above is not work
to be done; it is work you have a prototype of.

Two consequences:

1. **The preliminary-work section becomes exceptionally strong.** Section 2 of the research plan
   writes itself, and it is the section that establishes both expertise and independence.
2. **The argument against pitching a tool becomes decisive rather than advisory.** A referee who
   visits literev-scenario.com will see the platform largely exists. Proposing to build it means
   proposing your own completed work. The system is precisely what earns you the right to ask the
   harder question instead.

There is also a **prerequisite on the critical path** that was not visible before: the live system
has no TLS and had a credential exposed in a public CI log. You will not get an HUG / 144 / ICU
data agreement in that state, and those agreements are the load-bearing assumption of this whole
proposal. Harden first, then request data. Details and actions in the assessment file.

---

## Addendum — the Horizon proposal changes one thing materially

`Internal_Hject5.xlsx` is a Horizon Europe consortium proposal on AI for pandemic preparedness
and epidemic intelligence (ATHINA/HERA-facing, MOOD lineage; CIRAD, INRAE, ISS, Avia-GIS, FEM,
IFGI and others). Two facts in it matter for the Ambizione:

- **UNIGE participates with Olivia Keiser as main contact**, leading the "EI Models" task at
  ~EUR 1.12M, with Janne Estill on modelling.
- **You are listed on it, with your contribution recorded as "LLM".**

So of your three active lines, two are Keiser-led — the Legionella study and the Horizon
consortium. **GESICA is the only one that is not.** That reinforces the recommendation to build
from GESICA, and it makes the choice of host unit more consequential, not less.

### The real risk: thematic overlap

The Horizon proposal covers LLM-based knowledge extraction from literature for epidemic
preparedness and prediction. That is close enough to Candidate D that a referee — or the UNIGE
research office — will ask how the two differ. Two distinct problems follow, and both are
manageable if handled deliberately:

**1. Declaration.** The SNSF requires you to declare related and overlapping applications and
ongoing projects. Declare GESICA and the Horizon proposal, in full, with their roles and budgets.
Non-declaration of a substantially overlapping application is a research-integrity issue, not a
formatting slip, and it is the kind of thing that surfaces late and badly. Declaring it early and
clearly costs you nothing — panels expect active researchers to have several irons in the fire.

**2. Delimitation.** You need a paragraph in the research plan that a sceptical referee reads
and accepts. Fortunately the honest distinction is a clean one:

| | Horizon consortium | GESICA | **Your Ambizione** |
| --- | --- | --- | --- |
| Question | Build pan-European epidemic-intelligence infrastructure | Build a cross-border EMS decision system | **Does literature-derived evidence improve forecasting when local data is scarce?** |
| Scale | Continental, 1 km grids, EO/Copernicus | France–Suisse border region | Health-system operational, Geneva |
| Output | Platform, datasets, dashboards | Prototype system | **Inferential result plus method** |
| Methods | GeoAI, spatial risk mapping, LLM extraction | Multi-model "Patient–Moyens–Territoire" | **Regime-switching, EVT, Bayesian prior elicitation, decision analysis** |
| Your role | Contributor ("LLM") | Contributor | **PI** |

Note what this table does: it makes the delimitation argument *and* the independence argument at
the same time. The distinction is not "different topic" — it is **different kind of question**.
The consortia build platforms; your Ambizione asks whether the central assumption underneath
those platforms is true, and under what conditions it fails. That is a genuinely different
intellectual act, and it is one a person does as a PI rather than as a contributor.

### The consequence for how you write it

This is now the second independent reason not to pitch the Ambizione as a tool or platform. If
the proposal reads as "build a system that extracts evidence and produces forecasts", it is
neither clearly distinct from the Horizon work nor clearly yours — and the two weaknesses
compound. The reframing to the cold-start question is not a stylistic preference at this point.
It is what makes the application viable.

### Also worth noticing

Being named on a Horizon consortium proposal and holding a role in an Interreg project is
**evidence for the CV**, and you should use it. It shows you operate in international consortia
and attract funded collaboration — PI-shaped behaviour. Put it in the narrative CV. Just make
sure the Ambizione reads as the thing you lead, not the fourth item on a list.


---

## Addendum 3 — a precedent, and a possible collaborator

The citation-verification pass turned up the closest published precedent to WP2, and it is Swiss:

> Ranjbar S, **Cantoni E**, **Chavez-Demoulin V**, Marra G, Radice R, Jaton-Ogay K. Modelling the
> extremes of seasonal viruses and hospital congestion: the example of flu in a Swiss hospital.
> *J R Stat Soc Ser C* 2022. doi:10.1111/rssc.12559

They fit a discrete generalised Pareto model to the extremes of influenza-like hospital visits
using three years of daily data from a large Swiss hospital (CHUV). Two consequences:

**Cite it, and position against it.** §1.4 now does. The distinction is real and clean: they model
the tail as a stand-alone description of congestion; this project makes the tail the *tail of a
latent state process*, coupled to regime transitions and informed by literature-derived priors.
Not citing the nearest precedent — in the same country, on the same kind of data — would have been
the worst available outcome.

**Consider approaching them.** Eva Cantoni is at the **Research Center for Statistics, University
of Geneva**; Valérie Chavez-Demoulin is at UNIL and works on extreme value theory. This is the
Swiss extreme-value-in-hospital-data community, it is on your doorstep, and it is outside both
Keiser's and Teodoro's orbits.

Three things that could come from it, in increasing order of value:

1. A sanity check on the WP2 tail specification from people who have done it on Swiss hospital
   data — worth a coffee regardless.
2. A named methodological collaborator in the proposal, which strengthens the feasibility of the
   part of WP2 furthest from your published record.
3. A **mobility component** that is scientifically load-bearing rather than decorative — a stay
   at UNIL with Chavez-Demoulin would be a genuine change of institution, tied to a work package,
   and would address the weakest criterion in your dossier.

Option 3 is the one worth pursuing this month, because it needs someone else to say yes.
