# Proposal: new summary and revised crisis paragraph (21 October 2026)

Written after the comments of Roxana Vicovanu Bota and Christiane Bezuchet (RGO, 21 Oct) and of
Olivia Keiser (19 and 20 Oct). Not applied to the plan. For the applicant to rework in his own
words. The facts match the plan as it stands. The draft is 6,730 characters including spaces,
against 3,441 for the current summary, about 3,300 more. Page 15 has room for about 16 lines,
so the plan stays at 15 pages if the body edits are neutral.

What the draft does, in order. Who faces the problem and what a crisis does to the services.
What is available from day one and what is missing, and for whom. What published studies hold,
what a systematic review is and why it is too slow, what software now does and the two problems
that remain (extraction errors, transfer), then the idea in plain words. (Applicant, 21 Oct:
Keiser wants the complete story including the literature-review piece, not a summary that skips
it.) The four parts, each with one concrete
example. The three tests, justified by weight on the services and by what can be learnt, with
legionellosis brought in as the rarer environmental case. What comes out for the services. No
career paragraph.

---

## 1. Summary (proposed)

(Paragraphs 1 and 2 approved word for word by the applicant on 21 Oct, frozen. Paragraphs 3 and 4 proposed, under review. Paragraphs 5 to 7 are the earlier draft, still to review.)

Every winter, respiratory infections such as influenza, RSV and COVID-19 push up emergency
calls, emergency-department visits and hospital admissions in Geneva, as everywhere else. In
summer a heat wave does the same within days. The people who run the emergency call centre, the
emergency department and the hospital beds have to decide early whether to open beds, bring in
staff or warn the public, and the earliest decisions are the ones that count most. At that point
the local figures of the new episode are still few, and nobody knows yet whether this season's
virus or this heat wave will behave like the last one.

On the first day of an episode, a lot is already known. The weather, the air quality, the school
holidays, the virus load in the wastewater and the routine surveillance figures are all there.
What is missing is the local outcome, that is enough days of calls, visits or admissions from this
episode to see how these things turn into demand this time. Past seasons help, but no two
episodes are alike, and the reasons are many. The cause itself changes, a new variant, a different
mix of viruses, a heat wave that comes earlier, lasts longer or arrives with pollution. The
population changes, in its immunity, its age, where it lives and how vulnerable it is. Behaviour
and policy change, holidays, travel, mask wearing, vaccination campaigns, warnings that were or
were not given. The services change, in their beds, their staff, how they triage and how they
record their cases. And several of these things can change at once. So the link between what is
observed and what the services will face has to be learnt again, each time, from the first days
of the episode. To start forecasting anyway, a model needs to know many things that the local
data cannot yet tell, such as which signals to watch, how much and how fast a signal moves
demand, how the illness spreads, how long people stay in hospital, which groups are hit first,
what kind of model has worked before for this kind of crisis, and what level of demand counts as
serious for the services.

Much of this has been measured before, in other places or in past seasons, and the results are
in published studies. One study has counted how many more people come to an emergency department
for each extra degree on a hot day. Another has measured how many days pass between a rise in
emergency calls and a rise in admissions. A heat plan states the temperature at which it sends a
warning. A review of past epidemics says which models forecast best in the first weeks. A
hospital has reported how long its COVID-19 patients stayed and what share needed intensive care.
None of this is exactly Geneva, but at the start it is the best starting point there is, and the
local data can correct it day by day. Bringing this knowledge together is what a systematic
review does. It means searching the literature, screening hundreds or thousands of papers,
reading the relevant ones and copying out the numbers, the variables and the definitions by
hand. It takes months, so it is rarely done for forecasting, and it is out of date by the time a
crisis comes. Software can now do a large part of this work.

With colleagues I built LiteRev, a tool that searches the literature and sorts the papers by
topic, and other teams use it. I have since extended it to pull out of each study what a
forecaster needs, the numbers, the variables, the definitions, the kind of model. This extension
is a prototype. It works on test cases but it has not been proven, and two doubts hang over it.
A machine reads papers less carefully than a person. It may take an estimate but miss the range
around it, miss a number altogether, or put together studies that should not be mixed, and it
then makes the evidence look more certain than it is. And a result that held in another city or
another season may not hold in Geneva, because the people, the services, the climate or the way
cases are counted differ. These two doubts, the quality of what is extracted and whether it
applies here, are what this project is about. The idea is to measure the errors and correct
them, to check each finding for how well it fits Geneva, and to use what survives as the starting
point of the local forecast until the local data take over. Finding out when published evidence
misleads matters as much as showing when it helps.

The work has four parts. I will first compare automated extraction with extraction done by hand
on the same studies, measure the errors and widen the uncertainty where the machine is
overconfident, because an overconfident input produces an overconfident forecast. I will then
build a model that expresses demand as levels of pressure on the service, for example
routine, elevated, strained and critical, with the thresholds taken from published definitions
where they exist. I will replay past Geneva episodes day by day, using only what was known on
each day, and compare two forecasting strategies that share the same local data and context and
differ only in whether they use the published evidence. Finally I will ask the emergency services
what a wrong decision costs them, and judge the forecasts by the decisions they would have
triggered, not by statistics alone.

The tests are chosen by how much the crisis weighs on the services and by how much can be
learnt. Respiratory epidemics come first. They carry most of the seasonal pressure on emergency
services and hospitals, they are followed by several fast signals at once (emergency calls,
sentinel practices, wastewater) and the literature on them is large. Heat waves come second,
because they strain the same services and can be forecast from the same kind of data.
Legionellosis, a lung infection caught from water systems rather than from other people, is a
third and rarer case. It is tested in the last year on a different question, forecasting monthly
case counts from ten years of cases linked to building data, to see whether the method carries
over to an outbreak with an environmental source. The exact outcome of each test, for example
calls classified by the symptoms recorded or hospital admissions, is chosen before any forecast is
made, by criteria registered in advance such as data access, completeness and reporting delay.

At the end the project will say, for each type of crisis, whether published evidence improves
early forecasts, by how much and for how long, and where it should not be trusted. For the demand
forecasts that pass these checks and that the services authorise, a daily dashboard will run
alongside their work in observation mode, with no role in clinical care. The methods, the
extraction benchmark and the code will be open for other services and other places to reuse.

---

## 2.3.1, crisis paragraph (proposed opening, the rest of the paragraph unchanged)

HEADSTART covers three Geneva crisis types, chosen by how much they weigh on the services and by
how much can be learnt from them. (1) Respiratory epidemics (SARS-CoV-2, influenza and RSV,
together or one of them) are the main test. They carry most of the seasonal pressure on emergency
services and hospitals, they are followed by several high-frequency signals at once (emergency
calls, sentinel practices, wastewater) and the published evidence on them is comparatively rich.
(2) Heat events are the second test, because they strain the same services and can be forecast
from the same kind of data, with ozone and PM10 as co-exposures or effect modifiers rather than
separate domains [Schulte 2024; Ragettli 2019]. (3) Legionellosis is the third test, in year
four, on the linked case-environment data. It spreads from water systems rather than from person
to person, and the test forecasts case incidence rather than demand, to see whether the method
carries over to an outbreak with an environmental source. No fourth domain is planned.

Current text, for comparison. "HEADSTART covers three Geneva crisis types. (1) Respiratory
epidemics (SARS-CoV-2, influenza and RSV, together or one of them) are the main test because the
published evidence is comparatively rich. (2) Heat events are the second test, with ozone and
PM10 as co-exposures or effect modifiers rather than separate domains [Schulte 2024; Ragettli
2019]. (3) Legionellosis is the third test, in year four, on the linked case-environment data,
and forecasts case incidence rather than demand. No fourth domain is planned."

---

## 2.1.5, one sentence (proposed, optional)

After "HEADSTART asks a different question." add: "The question is general. Every health service
meets the first weeks of an epidemic or a heat wave with little local data on the new episode and
a large body of published experience it does not use in a checked way."

---

## Checks on the draft

- Facts against the plan. Two strategies with the same local data and context. Four parts as in
  2.3.2. Levels of pressure with thresholds from published definitions. Replay with information
  available on the day. Costs elicited from the services. Legionellosis in year four, monthly or
  weekly case counts, ten years of cases, linked case-environment data. Outcome chosen before
  any forecast by registered criteria (access, completeness, reporting delay). Dashboard in
  observation mode where authorised, no clinical role. Open benchmark and code.
- Not in the plan and added here as illustration only. The two examples of published findings
  (extra visits per degree above a threshold, speed of admissions after calls). They are generic
  examples, not citations.
- Removed. The definition of a prior, the career paragraph, the word "settings" without
  explanation, the sentence on the model having to "estimate this relationship".
- Style. First person, sentences of uneven length, two "for example", no colon or semicolon
  inside sentences, no em-dash.
