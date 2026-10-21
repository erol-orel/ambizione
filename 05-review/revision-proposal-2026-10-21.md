# Consolidated revision proposal (21 October 2026)

Brings together, section by section, the comments received since 19 October. Olivia Keiser's
email of 19 Oct (AI language, write for a child), her two points of 20 Oct (explain the crises,
general reasons, not the available data), her 56 Word comments and 17 tracked changes of 20 Oct
(numbered OK-1 to OK-56 as in `keiser-comments-2026-10-20.md`), and the RGO comments of 21 Oct
(Roxana Vicovanu Bota and Christiane Bezuchet, numbered RGO-1 onwards below). Nothing here is
applied to the plan. Each block is for the applicant to approve, rephrase or reject.

Decisions already taken by the applicant on 21 Oct and used throughout. No GESICA label on the
choice of crises, the reasons stand on their own. Drop "eleven years" everywhere. GeoAI4EI row
in 2.3.3 says "UNIGE, IDMM group" without a person. The summary tells the whole story including
the literature-review piece. LiteRev status stated in three tiers (operational, prototype, to be
built). Legionellosis, between reframing and an exploratory extension, decided in block D below.

Layout already applied (RGO-1 to RGO-3). 2 cm margins, Times New Roman 10pt, black headings,
page numbers. 15 pages before the bibliography with about 16 lines free.

RGO comment numbers used below. RGO-4 "what is missing, for whom". RGO-5 "the model, which
model, predicting what". RGO-6 redo the summary for a near-field reader. RGO-7 "the
relationship". RGO-8 "settings". RGO-9 why uncertainty matters. RGO-10 example of registered
criteria. RGO-11 legionellosis named before explained. RGO-12 career paragraph out of the
summary. RGO-13 page numbers. RGO-14 2.2.2 funding not needed. RGO-15 2.2.5 develop the closing
sentence in the applicant's favour. RGO-16 spell out T. RGO-17 2.3.3 risk and mitigation
together. RGO-18 2.3.3 last paragraph not necessary.

---

## Block A. Summary

Answers RGO-4 to RGO-12, OK-18 (what exists and what will be built), Keiser's email points 1
and 2 (explain the crises, general reasons), and her 19 Oct note on language.

The full draft is in `summary-proposal-2026-10-21.md`. One sentence is added after "With
colleagues I built LiteRev, a tool that searches and sorts the literature, and I have extended
it to extract numbers from studies":

> The first part works and is used by other teams. The extension is a prototype, and whether its
> output is reliable enough to forecast with is one of the things this project tests.

Status of legionellosis in the summary follows block D.

---

## Block B. 2.1 State of research, two touches

B1. 2.1.5, after "HEADSTART asks a different question." (Keiser point 2, general reasons):

> The question is general. Every health service meets the first weeks of an epidemic or a heat
> wave with little local data on the new episode and a large body of published experience that
> it does not use in a checked way.

B2. 2.1.1 last sentence, "Published findings may help, provided their uncertainty and their
relevance to the local setting are assessed." No change. It introduces the two words the plan
uses later.

---

## Block C. 2.2 Own research, rewritten as a path

Answers OK-1 (drop the duration), OK-2 and OK-3 (unclear, say what was found and its medical
use), OK-4 (a career path, problems solved, where next), OK-5 to OK-8 (PRISMA, certainty grade,
reviewed by whom, model selection step unclear, what is new), OK-9 (do not name her, say you
lead the respiratory work in GESICA), OK-10 ("LiteRev cannot have meetings"), OK-11
(legionellosis dataset unique, why it matters), RGO-14 (funding out), RGO-15 (closing paragraph
in the applicant's favour). Citations stay as they are, the text around them changes.

### 2.2.1 From econometrics and finance to public health

> I studied quantitative economics and econometrics at the University of Geneva, then worked in
> quantitative finance on risk. My job was to put numbers on rare and costly events, with
> extreme-value methods, models that switch between calm and turbulent regimes, and stress tests,
> and I became a certified Financial Risk Manager. I left that career in 2019 for a doctorate in
> biomedical sciences, because I wanted the same tools to serve health decisions. A health crisis
> is a rare event whose cost depends on a decision taken early, and that is how this project
> looks at it.

### 2.2.2 Doctorate, prediction where data are scarce, and LiteRev

> My doctoral work asked where to look for people living with HIV who do not know it, in
> countries where testing everyone is not possible. In [Orel 2022] I showed that a small number of
> social and behavioural characteristics, collected in routine household surveys, predicted
> individual HIV status well enough to guide where testing is offered, and I measured how well a
> model learnt in one country held in another. Related work in the group addressed treatment
> interruption in South Africa [Esra 2023] and country groupings by behaviour [Merzouki 2021].
> The lesson I kept is that a model built elsewhere can be useful locally, and that one has to
> check it rather than trust it.
>
> The second problem of the doctorate was practical. A systematic review of the literature took
> us months. With Aziza Merzouki (PhD, computer science) and Prof. Olivia Keiser I conceived and
> built LiteRev [Orel 2023], a tool that searches the literature from a plain-language or Boolean
> query, removes duplicates, groups the studies by topic and supports screening by two reviewers
> with a full record of what was kept and why. In its published evaluation it saved 56% of the
> screening work compared with a manual review. Other teams use it, including the GESICA review
> of artificial intelligence in emergency medical services [Edjinedja 2026], which I co-authored.

(RGO-14. The funding sentence is removed. OK-1. No duration in 2.2.1.)

### 2.2.3 Outbreak and health-system work during the pandemic

> During the pandemic I worked on questions that services needed answered quickly. In
> [Orel 2024] I compared the clinical severity of Delta and Omicron in a Swiss university
> hospital, a comparison the hospital needed to plan beds and staff for the Omicron wave. In
> [Estill 2020] we built age-structured scenarios of the Swiss epidemic for planning under time
> pressure. I helped build the COVID-19 dashboard of the WHO African Region and, as senior
> statistician, I guided the analysis of a seroprevalence study in Cameroon [Nwosu 2021]. More
> recently, as last author of [Ng'ambi 2026] (accepted), I supervised the analysis and the code
> of a machine-learning classification of cardiovascular disease across harmonised WHO STEPS
> surveys from several African countries. These projects taught me how forecasts and estimates
> are used, and misused, when a service is under pressure and the data are incomplete.

### 2.2.4 Since 2024, LiteRev-Evidence, GESICA and GeoAI4EI

> Since 2024 I have extended LiteRev into LiteRev-Evidence. The state of the two tools matters
> for this plan, so I state it plainly. LiteRev is operational, evaluated and used by others. The
> extension is a prototype. It extracts from each study the population, the setting and the
> outcome, keeps each extracted number with its source and a grade of how certain the extraction
> is, pools the numbers from several studies into a distribution of plausible values, lists the
> explanatory variables and the outcome definitions that studies use, and fits first forecasting
> models. Each new piece of evidence is shown to me before it enters a model. These parts run on
> test cases and have not been validated, alone or as one pipeline. What does not exist yet, and
> what HEADSTART builds and tests, is the measurement and correction of extraction errors, the
> screening of each finding for transfer to the local setting, a way of choosing the model that
> uses only what was known at the forecast date, and the registered comparison that says whether
> any of this improves a forecast. Many tools now read the literature. The difference here is not
> the reading but the test, whether what is read can be trusted as the input of a forecast.
>
> In GESICA, the Franco-Swiss consortium on health crises, I lead the work of the Geneva group on
> respiratory infectious diseases, starting with influenza, COVID-19 and RSV. I built the
> inventory of the variables and data sources for these diseases and for heat waves, 28
> surveillance sources described by coverage, resolution, latency, access and quality. HEADSTART
> uses this inventory, and the data table in T3.1 comes from it. Within GeoAI4EI (Horizon Europe,
> 2026 to 2030) I contribute to the European epidemic-intelligence toolbox. Working on these two
> projects showed me the gap this plan addresses. The partners want early warning of crises, the
> tools to read the literature exist, and nobody has checked whether the two can be joined safely.

(OK-9. The sentence "I lead the work of the Geneva group on respiratory infectious diseases" is
Keiser's own instruction. The applicant confirms it is true before it enters the plan. OK-10. The
"meeting between LiteRev and these two projects" is gone. The closing paragraph of the current
2.2.4 on development risk is merged into the three-tier sentence above.)

### 2.2.5 The legionellosis study

> I carry out the full analysis of a cantonal study already under way (BASEC 2026-00324, ethics
> granted, PI Prof. Olivia Keiser) that links every confirmed legionellosis case in Geneva over
> ten years to the hot-water installation of the building where the person lived. No comparable
> dataset exists, because case registers and building registers are not normally joined. For this
> plan it offers something the respiratory and heat tests cannot, an outbreak with few cases and
> an environmental source, where the local data will always be scarce and published evidence is
> the main thing a forecaster has. That is why it is used in year four as an exploratory test of
> whether the method carries over, on monthly or weekly case counts, with its own horizon.

(OK-11, RGO-11. Wording follows the decision in block D.)

### 2.2.6 Closing paragraph (replaces "Together these steps give me ...")

> Together these steps give me what HEADSTART needs and what few people combine. I built, with
> colleagues, the extraction tool the project starts from and I know its limits from the inside.
> I have modelled rare and costly events for a living and forecast infectious diseases for six
> years. I work every week with the Geneva services and the data the tests depend on. The next
> step for me is to lead a programme of my own, and this is it, from the first registered protocol
> to the final decision analysis.

(RGO-15. Variant without "what few people combine" if the applicant prefers.)

---

## Block D. Legionellosis and the place of the tests

Answers OK-11 and Keiser's point 2 (the tests should not be the centre), with RGO-11.

Recommendation. Keep the structure, change the framing in three places.

1. The objectives and hypotheses (2.3.1) are written as general questions about forecasting at
   the start of a crisis. Geneva and the three tests appear only in the last paragraph of 2.3.1,
   under a heading "Where the question is tested" instead of "Scope. Three Geneva crisis types".
2. Respiratory epidemics and heat waves are "the two tests". Legionellosis is "an exploratory
   extension in year four", on a different outcome, outside the confirmatory comparison and the
   decision analysis, kept because the dataset is unique and because it is the case where
   published evidence matters most. It leaves the milestone wording as "heat test and
   legionellosis extension done" and the Figure 1 chip as "Legionellosis, exploratory extension".
3. The summary names it in one sentence in that role, after the two tests.

Why not remove it. It is the only test where the outcome is a case count rather than service
demand, so it is the only check that the method is not tied to one kind of outcome. It costs
little space. It is already registered with ethics approval and its data are in hand.

Why not keep it as a full third test. Keiser is right that a disease with about forty cases a
year is not a crisis in the sense of the plan, and a reviewer will say so.

If the applicant prefers the full downgrade (one paragraph in WP3, out of the milestones and
Figure 1), the changes are listed at the end of this file.

---

## Block E. 2.3.1 Objectives and hypotheses, rewritten in prose

Answers OK-12 to OK-38 (27 comments). Labels are explained before use, every paragraph names its
terms, the scope paragraph comes last. The tracked changes OK made in this section are taken
into account (few outcome data, improve an operational decision, extracting, types of models,
"seen so far" and "How long it lasts is secondary" removed).

> ### 2.3.1 Objectives and hypotheses
>
> The central hypothesis is that published studies can improve a forecast in the first weeks of
> an epidemic or a heat wave, when the local data of the new episode are still few, provided two
> things are checked first, how much uncertainty the automated extraction has lost, and how well
> each finding applies to the local setting. The plan is organised in four objectives. Each has
> one main question, stated below in plain words, and a hypothesis or a criterion that says what
> would count as an answer. H stands for hypothesis, C for a criterion that a model must meet.
>
> | | Question in plain words |
> |---|---|
> | H1 | When a machine extracts numbers from studies, does it keep the uncertainty the studies report, or does it make the numbers look more certain than they are? |
> | C2 | Can a model express the pressure on an emergency service as a few ordered levels, from routine to critical, and give a reliable probability for each level each day? |
> | H3a | In the first weeks of an episode, does a forecast that uses published studies beat the same forecast without them? |
> | H3b | When the published studies disagree with what the local data show, does the model notice and reduce their weight, so that the evidence does not do harm? |
> | H3c | Do two simple warning signs, how much demand jumps from day to day and how closely each day resembles the day before, add anything to the forecast? |
> | H4 | Does a better forecast lead the services to a better decision, once the cost of acting too early, too late or for nothing is counted? |
>
> ![Framework](figures/fig1-framework.svg)
>
> *Figure 1. What is available when a crisis starts, the gap, what HEADSTART does (WP1 to WP4), the test, and where it is tested in Geneva.*
>
> #### O1. Make published evidence usable, with its uncertainty
>
> Studies report their results with uncertainty, a confidence interval around each estimate and
> differences between studies that looked at the same thing. Hypothesis H1 says that automated
> extraction loses part of this uncertainty. A machine may read the estimate but not its interval,
> may miss the number altogether, or may pool results from studies that should not be pooled, and
> the distribution of plausible values it produces is then too narrow. If the machine is
> overconfident, every forecast built on its output will be overconfident too. The correction
> proposed in WP1 treats these losses as measurement error and widens the distributions
> accordingly. To test H1, a set of studies is extracted by hand by two people and serves as the
> reference. The studies come from the systematic reviews run for each crisis type under the
> registered protocol (task T1.2), all of them when the set is small, otherwise a random sample
> covering the different kinds of numbers and sources. The automated extraction, with and without
> the correction, is compared with this reference on held-out studies, and the test is repeated
> for each version of the extraction software. The correction passes if it brings the width of the
> automated distributions back towards the width of the manual ones and if the stated uncertainty
> covers the true values as often as it claims. Numbers are the subject of this benchmark. The
> other things studies offer, which variables matter, which kinds of models work and how outcomes
> and warning thresholds are defined, are compared with published reviews instead.
>
> #### O2. Express the state of the service as levels of pressure
>
> Emergency services do not act on a number of calls. They act when demand reaches a level that
> calls for a response, more staff, more beds, a public warning. The model of WP2 therefore
> forecasts, for each day, the probability that the service is at each of a few ordered levels of
> pressure, for example routine, elevated, strained and critical, with the number of levels and
> their thresholds taken from published definitions where they exist. Criterion C2 says what the
> model must achieve before it is used in the main comparison. The levels must make sense to the
> services, and the probabilities must be right on average, so that a day given a 20% chance of
> "strained" is strained about one day in five. All candidate models are judged on this same
> scale and at the same rate of false alarms, which makes them comparable in the terms the
> services use. This does not assume that the proposed model beats simpler threshold rules. It
> is tested first on simulated data, to see whether the levels and the moves between them can be
> recovered at all from the available data, then on its calibration. If it fails either check, a
> simpler model that predicts the ordered levels directly, registered in advance as the fallback,
> takes its place and the main comparison goes ahead.
>
> #### O3. Test whether published evidence improves the forecast, and when it harms
>
> This is the main test of the project, and it compares two forecasting strategies. Both use the
> same context data (weather, air quality, calendar, wastewater, surveillance), the same local
> history of past seasons and the same outcomes already observed in the current episode. Only the
> evidence-informed strategy also uses what the published studies say, as extracted in WP1, to set
> its starting parameter values, to choose its explanatory variables and time lags, and to choose
> among types of models. The reference strategy is what a careful forecaster does today without
> the literature. Hypothesis H3a says that in the first weeks of an episode the evidence-informed
> strategy forecasts better. Both strategies are scored with the same rule, the continuous ranked
> probability score, which rewards a forecast that puts high probability near what then happened
> and penalises one that is confident and wrong. The comparison is run on past episodes replayed
> day by day with only the information available on each day (WP3).
>
> Hypothesis H3b is the safety check. Published evidence can be wrong for Geneva. The model
> therefore lowers the weight of the evidence when the local outcomes contradict it, and the
> question is whether this protects the forecast without throwing away evidence that was right.
> "Right" is defined by construction. In simulated episodes where the data are generated to agree
> with the evidence, the adaptive model should do no worse than a model that trusts the evidence
> fully, within a margin set at half the smallest gain counted as meaningful under H3a. In
> simulated episodes where the evidence is deliberately shifted, in its values, its spread or its
> relevance to the setting, the adaptive model should do better.
>
> Hypothesis H3c is secondary. Two simple signals, the recent day-to-day variability of demand and
> how strongly each day resembles the day before, are known to rise before some epidemic
> transitions. They are tested as extra predictors, to see whether they add anything to the
> context data, the local trend and the published evidence.
>
> The tests run in a fixed order. Respiratory epidemics are tested first. Heat waves are tested in
> any case, but their result counts as a confirmation only if the respiratory test has passed.
> Testing two things and claiming whichever succeeds would raise the chance of a false claim, and
> this order keeps that chance where it was set. A secondary analysis follows how the difference
> between the two strategies changes as more local outcomes arrive, to show for how long the
> published evidence matters.
>
> #### O4. Establish whether a better forecast changes a decision
>
> The forecast with the best score is not always the most useful one. Hypothesis H4 says that
> the gain from published evidence, if there is one, should show in the decisions the Geneva
> emergency services would take. The decision studied is fixed in advance, whether to escalate
> surge capacity when the forecast probability of the upper levels of pressure passes a threshold.
> The costs of escalating too early, too late or for nothing are elicited from two to five
> experienced people in the HUG emergency department, the 144 call centre and capacity management
> (WP4), and the forecasts of both strategies are judged on the decisions they would have
> triggered in the replayed episodes. An evidence-informed forecast counts as useful only if it
> changes a decision that matters in practice.
>
> #### Where the question is tested
>
> The question is general, and it is tested in Geneva on the crises that weigh most on the
> services and from which most can be learnt. Respiratory epidemics (SARS-CoV-2, influenza and
> RSV, together or one of them) are the main test. They carry most of the seasonal pressure on
> emergency services and hospitals, they are followed by several fast signals at once (emergency
> calls, sentinel practices, wastewater) and the published evidence on them is large. Heat events
> are the second test, because they strain the same services and can be forecast from the same
> kind of data, with ozone and PM10 as co-exposures or effect modifiers rather than separate
> domains [Schulte 2024; Ragettli 2019]. Legionellosis, an infection from water systems with few
> cases a year, is an exploratory extension in year four on a unique dataset that links ten years
> of cases to the buildings where people lived. It forecasts case counts rather than demand, on
> its own time scale, and stays outside the confirmatory comparison and the decision analysis. It
> is the case where local data will always be scarce and published evidence is the main thing a
> forecaster has.
>
> Within each test, the exact outcome is not fixed in this plan. The candidates are the series the
> Geneva services record, emergency calls classified by the symptoms recorded, emergency-department
> visits by cause, hospital admissions, bed or intensive-care occupancy, and for legionellosis the
> case counts. They are listed at the first registration (month 4), with the criteria for choosing
> among them, access, completeness, cause coding, reporting delay, time resolution and usefulness
> for the services. At month 12 I apply these criteria to the data actually obtained, under the
> registered rules and before any forecast is made, and the highest-ranked series that passes
> becomes the outcome of the test. It does not change afterwards. Open national series (federal
> respiratory surveillance, national wastewater data, weekly deaths, MeteoSwiss weather) support
> the validation of the methods and are the fallback if no local series passes, in which case the
> claim of the project is narrowed to the methods.
>
> Three things the project does not claim. It is not intended to outperform established
> forecasting hubs once long outcome histories are available. It does not assume that published
> evidence improves forecasts in every setting. It does not hand decisions to an automated system.
> For the tests that pass their checks and that the services authorise, the forecasts run on a
> daily dashboard that the services can look at while they work, in observation mode only, and
> this dashboard is described in WP4.

(OK-12 to OK-17 table rows reworded. OK-18 three tiers in 2.2.4 and summary. OK-19 "H stands for
hypothesis". OK-20 why uncertainty is lost, interval not read, number missed, wrong pooling.
OK-21 reference for the loss of uncertainty, [Shankar 2026] stays in the sentence that follows the
box in the current plan and moves into O1. OK-22 what studies, from where, how many, how selected,
how often. OK-23 "will" throughout. OK-24 and OK-25 C2 explained, pressure defined. OK-26 which
forecasts. OK-27 and OK-28 H3a spelled out, reference strategy defined. OK-29 "right" defined by
construction. OK-30 to OK-32 heat test, respiratory test and false-positive rate explained in
the "fixed order" paragraph. OK-33 score introduced in O3 and recalled in O4. OK-34 which
services. OK-35 "together or one of them" kept, it means the pathogen is chosen at registration,
the next sentence now says so. OK-36 candidates listed. OK-37 audit by me under registered rules.
OK-38 dashboard introduced and pointed to WP4. RGO-16 "task T1.2" spelled out at its first use.)

---

## Block F. 2.3.2 Work packages, targeted edits

F1. Before T1.1 (RGO-16), one sentence after the WP1 heading:

> Each work package (WP) is divided into tasks (T), with their months (M) in brackets.

F2. T1.1 (OK-39 to OK-41). Replace "such as how demand responds to temperature" by "such as
how the demand for emergency care responds to temperature", and the last two sentences by:

> The numbers are what the extraction benchmark of T1.2 and T1.3 measures. The other three kinds
> of evidence, variables, model families and outcome definitions, are recorded with their source
> and a grade of certainty and compared with published reviews.

F3. T1.2 (OK-42). Replace the sentence "The manual benchmark covers the parameters that the main
models actually use ... need them" by:

> The benchmark covers the numbers that the forecasting models of WP2 actually use, not every
> number reported in each field.

F4. T2.1 (OK-43). After "Weather, air quality, calendar effects and epidemic indicators are the
explanatory variables", add "each test uses the subset that applies to it, listed in the data
table of T3.1".

F5. T2.2 (OK-44). Add one sentence: "Geneva has one public hospital group, the HUG, so capacity
and occupancy refer to its services, and the levels are defined for that setting."

F6. T2.3 (OK-45) and T2.5 (OK-46). Add "(see the data table in T3.1)" after "local outcomes" and
after "Partner data".

F7. T3.0 (OK-47 to OK-50). "The other candidates" becomes "The candidate series not chosen as the
outcome". "single-canton" becomes "The design covers the canton of Geneva only, on purpose".
"open Swiss data (federal respiratory surveillance ...)" becomes "the open national series listed
in the data table". "Horizons follow what the services need, not results." becomes "The horizon
is the one the services say they need, and it is fixed before any result is seen."

F8. T3.1 (OK-51, OK-45, OK-46, RGO-5). New data table at the start of T3.1. Partner data are
those under agreement or in discussion with named partners. Open data are public. Literature is
what WP1 extracts for that test.

> | Test | Outcome candidates (partner data) | Context inputs (open data) | What is extracted from the literature |
> |---|---|---|---|
> | Respiratory epidemics | 144 emergency calls by recorded symptoms (CASU-144), emergency-department visits by cause and admissions (HUG), bed and intensive-care occupancy (HUG) | Federal respiratory surveillance and Sentinella consultations, national wastewater viral loads (SARS-CoV-2, influenza, RSV), MeteoSwiss weather, school calendar, population by age | Effects of weather and calendar on demand, size and speed of surges, admission shares and lengths of stay, transmission parameters, useful lags and variables, model families, outcome and threshold definitions |
> | Heat events | The same service series restricted to heat-related causes, then a hospital outcome | MeteoSwiss temperature and humidity, cantonal heat warnings, ozone and PM10, weekly deaths, population by age | Exposure-response of demand to temperature and heat days, lag structure, effect modification by ozone and PM10, threshold definitions used in heat plans |
> | Legionellosis (extension) | Confirmed cases over ten years, linked to building hot-water installations (cantonal study, BASEC 2026-00324) | MeteoSwiss temperature, humidity and rainfall, building and population registers | Environmental risk factors and their lags, seasonal patterns, incubation and reporting delays |

F9. T3.2 (OK-52). Replace the last sentence by "The early window of each episode starts on a date
set by a rule that uses only what was known at the time, for example the first week in which
the chosen series exceeds its seasonal baseline."

F10. T3.5 heading and text follow block D. "Heat test and legionellosis extension (M34 to M42)".

---

## Block G. 2.3.3 Environment, team and resources

Answers OK-53 (not PI), OK-54 (budget out, who does what in), RGO-17, RGO-18.

G1. Table rows. GESICA row, person in charge "UNIGE partner, IDMM group (Prof. Olivia Keiser),
Prof. Douglas Teodoro (Swiss data inventory)". GeoAI4EI row, person in charge "UNIGE, IDMM
group". Legionellosis row unchanged, she is the study PI there.

G2. Replace the risk sentence and the two paragraphs around the budget table, and the budget
table itself, by:

> The emergency-department and intensive-care extraction and the project-specific CASU-144
> agreement are not yet secured. Each rests on an existing relationship, and before month 1 and
> outside the grant I will finalise the data agreements with the HUG and CASU-144, confirm data
> reuse under the applicable governance rules, and harden LiteRev-Evidence before clinical data
> are connected.
>
> Who does what. I lead the four work packages, design the studies, build the models and carry
> out the confirmatory analyses. Two research assistants (master's students, part-time) support
> the specified technical work. One is the second extractor of the manual benchmark (T1.2) and
> then helps with the manual checks and the episode inventory. The other handles the context
> feeds, the alignment of the series, the replay pipeline and the dashboard runs. The DS4DH group
> advises on text mining in WP1, and the emergency services take part in the elicitation of WP4.
> The budget entered in mySNF details these positions, the database and dashboard services, and
> travel.

(OK-54 and RGO-17, RGO-18. The budget table and the last paragraph disappear, the staff
description stays, as Keiser asks and as Guidelines 4.3 require.)

---

## Block H. 2.4 and 2.6

H1. 2.4 first paragraph, "Research assistants (master's students) provide the second extraction
arm from months 3 to 9 and support data handling and the evaluation pipeline." No change.

H2. 2.6, replace "That question, the design that answers it and the confirmatory analyses are
mine." (OK-55) by "I defined that question and the design that answers it, and I will carry out
the analyses that test it."

H3. 2.6, Keiser sentence, with her roles as she states them: "Prof. Olivia Keiser, my contact
person at the Institute, co-built LiteRev with me and leads the legionellosis study. We work
together in GESICA, where I lead the respiratory-disease work of the Geneva group, in GeoAI4EI
and on the MAS in Public Health, where I have taught statistics and epidemiology since 2024."

H4. 2.6 last sentence (OK-56). Replace "By month 48, a validated answer and a first-author record
will be the basis for leading a group or a professorship." by:

> By month 48 the project will have produced a tested answer to its question, an open benchmark
> and an open software pipeline that others can use, a method for judging forecasts by the
> decisions they change, four to six first-author or senior-author papers, and working relations
> with the Geneva services and with the European epidemic-intelligence networks. That is the basis
> on which I intend to lead a group or apply for a professorship.

H5. 2.6 table, GeoAI4EI row "Contributor" stays. GESICA row "My role" becomes "Lead of the
Geneva respiratory-disease work, data sourcing".

---

## Block I. Tracked changes by Keiser

Accept all, with two exceptions.

- Keep "The three crisis types are fixed." in the scope paragraph (now "Where the question is
  tested"), because the registration logic and the figures depend on it. In the rewrite above the
  sentence reads "The two tests and the extension are fixed in this plan."
- Her H1 wording "would reduce this source of bias" is kept in substance but the rewrite of O1
  says "widens the distributions accordingly", which is what the correction does.

---

## Block J. Figures

If block D is accepted, Figure 1 chip 3 becomes "Legionellosis, exploratory extension, case
counts" and the caption changes as in block E. Figure 2 legend MS6 becomes "heat test and
legionellosis extension done". No other change.

---

## If the applicant prefers the full downgrade of legionellosis

Remove it from the summary, from the Figure 1 chips, from the milestones (MS6 "heat test done"),
from the 2.6 table and from 2.2.5, which becomes one sentence at the end of 2.2.4. Keep one
paragraph in WP3 as T3.5b "Exploratory extension to a case-count outcome", with the dataset and
the question, and keep the legionellosis row of the 2.3.3 table. Saves about half a page.

---

## Order of application once approved

1. Blocks E, F, G (2.3.1, 2.3.2, 2.3.3) in one pass, then page and character count.
2. Blocks C and H (2.2, 2.6).
3. Block A (summary) and B.
4. Figures (block J), then the own-voice read by the applicant of the first two pages.
