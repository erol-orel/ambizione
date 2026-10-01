# Response to the external audit of 30 September 2026

Disposition of every substantive point, with what was applied and what was rejected and why.
The audit's overall verdict - strong science, document not yet submission-ready - matches this
repository's own assessment (`final-quality-audit.md`): the remaining gap is applicant inputs
(placeholders, letters, statuses), not writing.

## Accepted and applied (research plan changed)

| # | Audit point | What was done |
| --- | --- | --- |
| 1 | **Novelty claim too broad** (§3) | §2.1.3 now acknowledges that informative priors under sparse local data exist (with a `[[cite examples]]` marker - I could not verify the USGS/Sci Rep 2023 paper from this environment and will not cite unverified) and narrows the gap to the end-to-end test: automatically constructed priors with extraction + transportability uncertainty propagated, strict historical information sets, harmful-borrowing detection |
| 2 | **CASU-144 vs "demand"** (§5) | T3.0 now scopes the primary claim explicitly: the operational demand signal observed by the dispatch system; broader hospital-demand claims only where validated against ED/ICU channels |
| 3 | **Episode-level power** (§8) | T3.3 now states the unit of inference (episode; origins are repeated measures) and that the design is powered by simulation-based operating characteristics - type I error, power, interval width under within-episode dependence - run before registration point 2 |
| 4 | **Literature vs situational intelligence** (§10) | T3.2 now tiers the prior: **confirmatory = peer-reviewed literature + preprints only** under the rolling cut-off; situational reporting (WHO DON, ECDC RRA) is a **pre-specified secondary prior variant**. H3a tests literature borrowing, not dynamic evidence fusion. T1.2's source-type stratum retained |
| 5 | **One concrete decision for H4** (§11) | T4.1 fixes the primary decision: trigger surge-capacity escalation when P(strained/critical) crosses the elicited threshold; its losses anchor T4.2 |
| 6 | **Host tense contradiction** (§15) | §2.6 "is signed" → "will be signed" - the letter is requested, not in hand |
| 7 | **Missing bibliography entries** (§17) - *verified: true* | [Lazer 2014], [Höhle 2014], [McGough 2020] added with full references; [Winters 2018], [Lee 2021] added as flagged skeletons (I will not invent author lists). [Xu 2023] key corrected to [Barber 2023] (our own note had already flagged it; entry is uncited in text - cite or drop) |
| 8 | **Meta-language / defensiveness** (§13, §19) | Roughly a dozen self-referential sentences cut or folded ("the distinction is not cosmetic", "nothing is described above its actual status", "that is the precise claim", etc.). ~1,300 characters recovered, spent on points 1–5 |

## Accepted in part

- **H1 overcommitted (§4).** The directional hypothesis is *kept* - a pre-registered directional
  prediction is scientifically stronger than the audit's neutral rewrite, and H1 already states
  that absence of the effect is informative. What was fixed is the justification: the direction
  is now derived mechanistically (omitted uncertainty statements and missed variance components
  shrink dispersion estimates systematically, not randomly) rather than asserted from error rates.
- **Character target 55–57k (§18).** The audit's counts are of raw markdown and overstate (its
  own caveat concedes this); our stripped counter reads 59,995. The real requirement - margin
  against the binding mySNF counter - is accepted differently: **upload a draft PDF to mySNF
  early and calibrate against its counter**, then set the final target. Cutting 3–5k of substance
  today, before the placeholder fill, would be premature amputation.
- **Simplify the stack (§7).** Largely already done (EVT, CSD, conformal, equity, shadow mode are
  explicitly supporting/secondary). Further trims applied where cheap. **Legionellosis is NOT
  removed**: it is the applicant's own BASEC-approved, uniquely linked dataset, already scoped as
  a year-4 extension whose omission "does not invalidate the main result", and it does real work
  in §2.2 (feasibility, independence). Removing it saves ~400 characters and costs a genuine
  asset.

## Rejected, with reasons

1. **"Aim for 55,000–57,000."** See above - calibrate on mySNF, don't pre-cut substance.
2. **Neutral H1.** A directional, mechanistically justified, falsifiable hypothesis with a
   pre-stated interpretation of its failure is better science and better review optics than
   "extraction will distort dispersion" (which is nearly unfalsifiable - some distortion is
   certain).
3. **Remove legionellosis.** See above.
4. **"49 placeholders" as a defect.** They are the repository's deliberate convention for
   applicant-only facts, catalogued in `placeholders.md` with owners; the audit is right that
   none may survive into the submitted PDF, and that was already the plan.
5. **Em-dash count (139)** - noted, no action; a style preference, not a rule.

## The audit's claims checked against the repository

- Missing bibliography entries: **confirmed** (5 of 5) - the one genuinely new defect found.
- Xu 2023 mis-key: **confirmed**, though our own entry already carried the fix instruction.
- Host tense contradiction: **confirmed**.
- Zheng et al. non-consortium: already flagged by us; unchanged (flag stands).
- "Proposal claims host confirmation signed while table says requested": partially right -
  wording, not the table, was at fault; fixed.
- Its USGS/Sci Rep 2023 prior-art citation: **not verifiable from this environment** (network
  egress blocks); incorporated as a `[[cite examples - verify]]` marker rather than a citation.

## Where this leaves the dossier

The plan at 59,995/60,000 with the audit's three "essential" scientific changes in place
(novelty narrowed; outcome scoped; episode-level powering stated). The submission blockers are
unchanged and unchanged in ownership: placeholders, letters, statuses, bibliography completion,
the mySNF count - all listed in `final-quality-audit.md` §4 and `TODO.md`.


---

# Round 2 (30 September, second external audit): disposition

The second audit reviewed the revised version, endorsed the earlier disputed decisions
(directional H1 kept, legionellosis kept, no blind pre-cut), and raised new points.

**Applied:**
1. **Minimum-viable-episode rule** - T3.3: the OC simulation fixes the minimum eligible-episode
   count; below it, no confirmatory claim, primary analysis reported as estimation. (The
   auditor's most important statistical point; correct.)
2. **Algorithmic N and Δ** - T3.3: *N* = smallest value in a pre-declared grid meeting the OC
   criterion; Δ by pre-declared rule on the simulated effect distribution; both blind to
   forecast performance. T3.0 cross-references.
3. **H1 dispersion quantity** - hypothesis now targets "the dispersion of the evidence-derived
   distribution - within-study uncertainty and between-study heterogeneity", which is the
   mechanically defensible claim. Directional form kept.
4. **Ongoing-projects landscape** - §2.1.6 names ECDC RespiCast, CDC FluSight, Horizon Europe /
   GeoAI4EI and GESICA, and positions COLDSTART as the complementary inferential question.
5. **Host-signature mechanics removed from the plan** - the plan no longer asserts who signs;
   "the host arrangements … are documented in the required confirmation letters." The signature
   question lives where it belongs: `host-institution-letters.md` + the RGO email. (Correct
   catch: the SNSF template, not the applicant, defines signatories.)
6. **Summary/T3.3 consistency** - "one primary rung-to-rung contrast … repeated once,
   sequentially, as the heat generalisation test."
7. **"Evidence-synthesis and borrowing strategies"** wording in T1.4.
8. **Bibliography closures from auditor-verified records** - Shankar 2026 (Shankar R, Lim A,
   Qian X; JBI 181:105086), Rosenkötter 2013 (7 authors + DOI), EMS-ILI year corrected to
   **2025** (238:239–244) with the text key updated, Cook 2023 added as the §2.1.3 prior-art
   citation (author list still flagged), Lee 2021 skeleton now carries the Lung/Yeh/Hwang 2021
   candidate. Each carries a "confirm once against the publisher record" note - auditor
   verification is second-hand here.
9. **Career-section trim** (~15%) and further meta-language cuts, paying for 1–4.
10. **Budget arithmetic** - `budget.md` now carries the full-cost table for the 50%×48 line and
    a decision rule (shorten duration to M3–M42, not the percentage, if the rate exceeds
    ~CHF 190k full cost). The plan keeps 50%×48 as the requested profile pending the RGO rate.

**Not applied, with reasons:**
- **"Host institute: Requested" statuses** - correct as of today; they flip when letters arrive.
  The audit itself concedes this. The status vocabulary is the honesty mechanism, not a defect.
- **Further stack demotion** - the audit itself concludes the hierarchy is now explicit enough.

Plan after round 2: **59,999 / 60,000**. Zero placeholders in the countable text; bibliography
placeholders reduced to author-list/venue items requiring publisher records.


---

# Round 3 (30 September, third external audit): disposition

The third audit declares the science finished and reproduces our character count exactly
(59,999 at `32b3254`; 59,989 after this round). Its remaining defect claims were checked
mechanically against the current repository:

- **"Cook 2023 cited but missing from the bibliography" - FALSE against the repo.** The entry
  was added in `32b3254`; the auditor reviewed a stale attachment. A full text↔bibliography
  cross-check (multi-key citations parsed) finds **zero cited keys missing**.
- **"[EMS-ILI 2024] still in the bibliography while the text cites 2025" - FALSE against the
  repo**, same cause: the key and year were corrected in `32b3254`.
- The cross-check DID surface a real adjacent defect the audit missed: **five bibliography
  entries were never cited in the text** (Angelopoulos, Barber, Hamilton, Zheng; Orel 2023 is
  cited in prose per the own-work convention). Fixed by anchoring them: Hamilton 1989 in T2.1,
  Angelopoulos/Barber in T2.5's conformal clause, Zheng 2015 in §2.1.5 (with the Swiss
  acute-episode gap it documents).

**Applied from the audit:**
- §2.1.6's universal "none tests…" softened to the falsifiability-safe form: "their stated
  objectives do not include testing whether automatically synthesised external evidence should
  enter a forecast as formal prior information at local cold start."
- **Scientific freeze recorded** - banner and six-step release-QA checklist now head `TODO.md`.
- The 59,999→calibrate framing adopted verbatim: the source count is a trigger to upload to
  mySNF, not a margin.

**Unchanged by design:** the bibliography's remaining `[[…]]` flags and editorial notes are the
working convention for exactly the publisher-record QA the audit prescribes; they are stripped
in release-QA step 1, not before, because removing the flags before the records exist would
hide unfinished work rather than finish it.

**Downstream propagation (this round):** the Larribau and Desmettre data requests and the
one-page project note now specify that call-reason/presentation categories must cover **both**
outcome arms (respiratory-related and heat-sensitive: dehydration, renal, psychiatric) plus
broad age bands for the 75+ sensitivity - without this, the extract could satisfy the letter of
the request and still not support the heat arm.

---

## Round 4 (1 October 2026): "defensive to visionary" tone audit

A fourth external audit argued the proposal's tone is too defensive and supplied full rewrites
of the Summary and §2.6. Disposition below. The freeze rule applied throughout: tone is a
reader-round question, and one opinion does not break the freeze - if two of the four external
readers (replies due 16 Oct) independently converge on "too defensive", that is the trigger to
revisit.

**Applied (label-level only, no science, no claims changed):**
- The "stated plainly" tic appeared three times across documents the panel reads side by side.
  Fixed: §2.4 "What the data fallback costs." / §2.6 "Collaborators and their roles." /
  mobility statement "The choice of host." Content unchanged; 19 characters recovered
  (now 59,612/60,000).

**Rejected, with reasons:**
- *Summary rewrite.* Drops the falsifiability sentence ("The outcome is intentionally
  falsifiable... either way, the deliverable is a validated answer"), which is among the
  strongest Ambizione signals in the document; adds puffery ("vast, largely untapped resource",
  "critical paradox", "positions me optimally"); and closes on "establish my independent
  research group", which overclaims against the 2026 rules (no doctoral students or postdocs
  can be employed - "independent research programme" was chosen deliberately). It is also
  written throughout with em-dashes, which this repository bans.
- *§2.6 rewrite.* Contains factual errors: it asserts "the intellectual property... under my
  sole scientific direction" when the IP is UNIGE's (the plan states this correctly); "my role
  has been to build the infrastructure for broader consortium goals" contradicts the record
  (led LiteRev, data/scientific lead on the legionellosis study, senior-author paper) and would
  *weaken* the independence case; "my doctoral and postdoctoral supervisors (e.g., Prof. Olivia
  Keiser)" implies an undisclosed plurality of supervisors; "To be absolutely clear on
  organizational independence" tells what the current text shows; naming "SNSF Starting Grant"
  commits to a specific follow-on instrument gratuitously.
- *"A confidently wrong prior is worse than no prior."* Not tone - a scientific claim that
  motivates H3b and the harm-detection arm. Removing it removes the reason half the design
  exists.
- *"Not another untested forecasting platform" / "does not build another epidemic-intelligence
  platform."* These carry the distinctness argument against GESICA/GeoAI4EI overlap (Art. 13
  and §2.5's distinction table). Softening them reopens the overlap question three audit
  rounds closed.
- *"Earlier would be guesswork; after any look at performance, indefensible."* The suggested
  replacement ("to prevent data leakage and ensure unbiased evaluation...") restates the
  paragraph's content in boilerplate and loses the justification for *where* the second
  registration point sits.
- *Simulation sentence.* The proposed passive rewrite drops the double-counting argument, which
  is the substantive reason simulation is not data.
- *Renaming "What the project does not claim" to "Scope and Boundaries".* The explicit
  non-claims list is a strength reviewers reward; the generic heading hides it.
- *Wholesale tone shift.* The candor was engineered across three hostile-review rounds; SNSF
  evaluation rewards feasibility and honesty over vision rhetoric. The audit itself rates the
  hypothesis matrix, the fallback logic and the work packages "already excellent" - all written
  in the voice it asks to replace.
