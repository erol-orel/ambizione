# Proposal: new summary and revised crisis paragraph (21 October 2026)

Written after the comments of Roxana Vicovanu Bota and Christiane Bezuchet (RGO, 21 Oct) and of
Olivia Keiser (19 and 20 Oct). Not applied to the plan. For the applicant to rework in his own
words. The facts match the plan as it stands. The draft is 4,690 characters including spaces,
against 4,370 for the current summary.

What the draft does, in order. Who faces the problem and what a crisis does to the services.
What is available from day one and what is missing, and for whom. The idea in plain words, with
an example of what a published finding looks like. The four parts, each with one concrete
example. The three tests, justified by weight on the services and by what can be learnt, with
legionellosis brought in as the rarer environmental case. What comes out for the services. No
career paragraph.

---

## 1. Summary (proposed)

Every winter, respiratory infections such as influenza, RSV and COVID-19 push up emergency
calls, emergency-department visits and hospital admissions in Geneva, as everywhere else. In
summer a heat wave does the same within days. The people who run the emergency call centre, the
emergency department and the hospital beds have to decide early whether to open beds, bring in
staff or warn the public, and the earliest decisions are the ones that count most. At that point
the local figures of the new episode are still few, and nobody knows yet whether this season's
virus or this heat wave will behave like the last one.

A great deal of context is available from the first day, such as weather, air quality, school
holidays, wastewater measurements and routine surveillance. What the forecasting models lack at
the start is enough local outcome data, that is enough days of calls, visits or admissions from
the current episode to learn how this context translates into demand this time. Long records of
past seasons help, but a new episode often differs in who is affected and how severe it is, so
the link has to be learnt again as the days come in.

Meanwhile, many published studies describe how demand reacted to similar situations elsewhere,
for example how many extra visits each degree above a temperature threshold produced in another
city, or how quickly admissions rose after the first wave of calls in a past season. This
knowledge is rarely used in forecasting, partly because it is scattered across thousands of
papers and partly because what held elsewhere may not hold here. HEADSTART tests whether it can
be used safely. The idea is to extract such findings automatically from the literature together
with their uncertainty, to assess how well they transfer to the local setting, and to use them as
the starting point of the local model until the local data take over. Detecting when published
evidence misleads matters as much as showing when it helps.

The work has four parts. I will first measure how reliable automated extraction is, by comparing
it with extraction done by hand on the same studies, and correct the uncertainty where the
machine is overconfident, because an overconfident input produces an overconfident forecast. I
will then build a model that expresses demand as levels of pressure on the service, for example
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
