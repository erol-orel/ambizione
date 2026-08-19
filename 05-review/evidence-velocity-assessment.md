# Assessment — faster-moving text sources and structured APIs as evidence

*Question posed:* instead of only peer-reviewed papers, which appear slowly, also ingest
higher-frequency text (X/Twitter, Google News hourly; ReliefWeb daily/weekly) and structured APIs
(pollution, weather), so the model can move from the prior to current knowledge *during* a crisis,
confronting prior with posterior and re-running priors as new evidence arrives.

## Verdict

**The instinct is right and the framing is wrong.** As stated, the idea would break the project's
central test. Restructured along the correct axis, one part of it is a genuine improvement that
costs almost nothing to add, and the rest is the right *next* project.

## Why the framing as stated breaks H3a

H3a asks whether information about **other** events improves forecasts of **this** event before
local outcomes are informative. The test only means something if the two sides are separable.

Local tweets, local news and local media about the ongoing local crisis are not prior information.
They are **noisy observations of the local outcome itself** — care-seeking, symptom talk and
crowding reported through a different channel. Feeding them in as "evidence" and then scoring the
model against local emergency demand would let a channel derived from the outcome improve the
forecast of that outcome, and the resulting skill gain would be attributed to evidence borrowing.
That is not a hard result to defend; it is an unfalsifiable one. A referee would find it
immediately, and it is exactly the Google Flu Trends failure mode the plan already cites
[Lazer 2014] — high-velocity proxy signal mistaken for information about the quantity of interest.

The confusion is that **velocity was treated as the organising axis**. It is not.

## The correct axis: referent, not velocity

| Category | Example | What it is | Where it belongs |
| --- | --- | --- | --- |
| 1. Analogous **past** events **elsewhere** | Published studies, preprints | Prior information | The prior — this is what H3a tests |
| 2. The **current** event **elsewhere** | WHO Disease Outbreak News, ECDC rapid risk assessments, ReliefWeb, preprints on the ongoing event | Prior information, and fast | **The prior — and this is the free win** |
| 3. The **current** event **locally** | Local news, local social media, local search | Observation of the outcome | An observation channel in the state model — never a prior |
| 4. Structured exogenous drivers | Weather, pollution, mobility | Covariates | Already in the model as covariates |

Category 2 is the real content of the idea, and it was invisible in the plan before. During
COVID-19, quantitative statements about severity, length of stay and surge multipliers from Italy,
Spain and the UK were available to Geneva **weeks** before the peer-reviewed literature caught up,
and they satisfy the origin-bounded rule perfectly: they carry an index timestamp, they concern
populations other than the one being forecast, and they let the prior be refreshed *within* a
crisis rather than only between crises. This is precisely the "move from prior to current
knowledge over the run of the crisis" the question asks for — obtained without contaminating the
test.

Category 4 is not new: weather and pollution are already covariates, and LiteRev-Evidence already
has MeteoSwiss, Copernicus ERA5 and Sentinelles connectors. Adding more structured feeds is
engineering, not a scientific claim, and the plan should not spend characters advertising it.

## What has been changed in the plan

**T3.2** now defines admissibility by referent rather than by venue: category 1 and 2 sources are
admissible prior inputs and pass through the same T1 extraction and measurement-error pipeline;
category 3 is explicitly excluded from the prior and may enter only as an observation channel;
every input carries an index timestamp on which the rolling cut-off is enforced.

**§5.3** carries the full multi-velocity vision as the stated **next step** of the research line —
fusing streams of different velocity in one calibrated state model with continuous conflict
monitoring deciding how much each may say. This is honest about sequence (the boundary has to be
measured before it can be relaxed) and it does real work for the Ambizione narrative, which asks
for a programme rather than a single study.

## What was deliberately not added

**Social media and hourly feeds are not in the confirmatory design.** Beyond the contamination
argument, the operational case is weak on the applicant's own evidence: the GESICA social-media
report documents X API pricing that makes historical retrieval prohibitive, CrowdTangle's
discontinuation, Meta Content Library access restrictions and DSA data-access delays. A
rolling-origin experiment needs the *historical* state of each feed at each past origin —
precisely what these platforms no longer provide. Promising it would create a feasibility risk in
the one work package that must not have one.

## One residual risk to watch

Category 2 sources are not free of the problem that motivates WP1. Situational reports are less
consistently quantified than journal articles, and extraction error on them is likely to be worse,
not better. They should therefore enter the T1.3 error characterisation as their own stratum, so
the measurement-error layer is fitted to them rather than borrowed from the journal stratum. That
is a WP1 sampling decision, not a new work package, and it fits inside the existing stratified
benchmark design.
