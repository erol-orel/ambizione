# Final hostile review — five angles

Written against the plan at 58,369 characters. Findings are ordered within each angle by how much
damage they would do if a referee raised them unanswered. **Fixed** means applied to the plan.

---

## 1. Scientific — is H3a novel and falsifiable?

### F1.1 — The baseline may be a straw man **[FIXED]**

The confirmatory contrast is rung 4 (evidence priors) against rung 3 (weakly informative priors).
A hostile referee: *"You chose the weakly informative prior. Of course the informative one wins."*

This is the single most dangerous attack on the design, because it does not require the referee to
doubt anything else. If the vague prior is badly chosen — too diffuse, wrongly centred — rung 4
beats it trivially and the result means nothing.

**Fix applied:** the weakly informative specification is pre-specified and its *choice* is subject
to sensitivity analysis across a declared set of vague alternatives. A win that survives the worst
reasonable vague prior is a real win.

### F1.2 — "A negative result is valuable" is asserted, not shown **[FIXED]**

The plan says a null result establishes a boundary condition. A referee will ask *who would do
anything differently.* Abstract value is weak value.

**Fix applied:** §5 now names the consequence — modellers who currently hand-set parameters from a
few familiar papers, and forecast hubs considering evidence priors, would have a documented reason
not to.

### F1.3 — Novelty rests on integration, not invention *(no change needed)*

Every component exists. The plan already says so and claims only the empirical integration. This
is the right posture and should not be strengthened. Do not let anyone talk you into "the first
to…" language before the LiteRev novelty search is run and recorded.

---

## 2. Statistical — is the confirmatory design valid?

### F2.1 — Two core domains, one "primary" comparison **[FIXED — the most serious finding]**

T3.3 states *"Exactly one comparison is confirmatory"*, but §3 designates **two** core validation
domains, respiratory and heat, each now with its own primary horizon. That is **two confirmatory
comparisons**, and the plan does not say which is primary or how the pair is handled.

A statistical referee finds this immediately, and it undermines the pre-registration claim the
whole design rests on.

**Fix applied:** respiratory is the **primary** confirmatory domain; heat is a **pre-specified
sequential generalisation test**, conducted only if the primary is met, and reported as such. This
is hierarchical testing, so no multiplicity correction is needed and nothing is lost — heat still
carries the generalisation claim.

### F2.2 — Block bootstrap over ~10 blocks **[FIXED]**

With an episode count in the low teens, bootstrap intervals over episode blocks are unreliable and
a referee who resamples for a living will say so.

**Fix applied:** a pre-specified alternative — a permutation test across episodes — is named
alongside the bootstrap, with the choice fixed in the power simulation rather than after seeing
the interval width.

### F2.3 — Onset is estimated, and its uncertainty is ignored *(open — see below)*

The onset rule defines the cold-start window, so onset error shifts the window and therefore the
primary endpoint. The plan treats onset as if it were known.

This should be handled by sensitivity analysis over the onset threshold and persistence criterion,
which the plan already promises in another form. **Not fixed in the text** — it would cost
characters the plan does not have, and it belongs in the analysis plan rather than the proposal.
Record it in `hypothesis-audit.md`.

### F2.4 — Multiplicity across H1, H3b, H3c, H4 *(acceptable as written)*

Only rung 4 vs rung 3 is confirmatory; everything else is explicitly secondary. That is the
correct structure and is already stated.

---

## 3. Feasibility — one PI plus ~45% support in 48 months?

### F3.1 — WP2 is the real risk, and it is PI-executed *(acceptable, with the fallback already in place)*

A hierarchical Bayesian regime-switching model, multivariate across three series, with an
extreme-value tail, resilience covariates, adaptive robust borrowing and a conformal layer, is a
genuinely hard build. It is the least parallelisable part and cannot be delegated to technical
support.

The plan mitigates this correctly: T2.1's identifiability study runs before real data and triggers
a declared ordinal state-space fallback. That is the right structure. **No change** — but be ready
to defend it verbally at interview, because it is where a methods referee will push.

### F3.2 — The PI's own time commitment is unstated **[open — needs a number]**

`[[Erol Orel, XX%]]` is still a placeholder. Given that WP2 and the confirmatory design are
PI-executed, a referee needs to see a serious fraction. This is a placeholder that changes how the
whole feasibility case reads.

### F3.3 — Compute volume is real but tractable *(no change)*

Six ladder rungs × episodes × origins × horizons × archetypes is a large number of model fits.
Worth one sentence in the resources table if room appears; not worth characters now.

---

## 4. Independence — is this genuinely his programme?

### F4.1 — Silence about the former supervisor reads as evasion **[FIXED]**

The plan now never mentions Prof. Keiser. Given that the CV shows every publication with her
group, *omission* is more conspicuous than a clean statement would be. A referee who notices the
gap fills it themselves, unfavourably.

**Fix applied:** §5 names the relationship in one sentence and states the delimitation, rather than
leaving it to be inferred.

### F4.2 — Who owns LiteRev-Evidence? *(open — one line needed)*

The platform was developed alongside GESICA and a Horizon consortium. A referee may reasonably ask
whether the instrument is the applicant's or a consortium asset. One sentence on authorship and
availability would close it. `[[Confirm the position, then add it.]]`

---

## 5. SNSF — why fund this applicant specifically?

### F5.1 — No first-author output in the target domain **[the honest structural weakness]**

First-author work is HIV/ML, LiteRev and COVID severity. The AI-in-EMS review — the one paper in
emergency medicine — is third author. A referee assessing "expertise with regard to the project"
will notice.

**Mitigation, in order of value:** (i) get one first-author output from the Legionella or GESICA
work submitted before November; (ii) ensure the CV narrative connects the *methods* lineage rather
than claiming domain seniority, which it now does; (iii) do not overstate the emergency-medicine
track record — the honest framing is that the methods are his and the domain access is real.

### F5.2 — Mobility remains the weakest criterion *(unchanged)*

Nothing in this review changes it. One confirmed UNIL invitation converts it from argument to fact.

---

## Verdict

The design is sound and the remaining weaknesses are mostly outside the text: the PI's time
fraction, one first-author domain output, and the mobility invitation.

**F2.1 was a genuine defect** — two core domains with one declared confirmatory comparison — and it
would have been found. It is now hierarchical testing, which is stronger than the multiplicity
correction the alternative would have required.

**What I would not do now:** add anything. Every remaining improvement is legwork, not writing.

---

## Application status

All five `[FIXED]` items above are now **applied to the draft sections**, not merely proposed:

| Finding | Where applied |
| --- | --- |
| F1.1 baseline | T3.3 — "Rung 3 is pinned in the registration", with a pre-declared sensitivity band |
| F1.2 null-result value | §5.1 — "A null result changes identifiable practice", naming who acts differently |
| F2.1 two domains | §3 "Ordering across the two core domains", domain table roles, T3.3, T3.5, §0 summary, `draft/README.md` |
| F2.2 small-block inference | T3.3 — paired permutation over episodes as the primary inferential statement, block bootstrap alongside |
| F4.1 former supervisor | §5.3 — "On my publication record" |

F2.3 (onset-rule uncertainty) is recorded as an **open** methodological uncertainty in
`hypothesis-audit.md`, with the position taken: register at the second registration point, report
a pre-declared onset-threshold sensitivity band.

**Character cost.** The fixes added ~4,200 characters and the plan was at 58,369 of 60,000. The
budget was recovered by removing duplication rather than by cutting the fixes: staffing and
division-of-labour text repeated across §4/§5/§6, the two separate statements of the data-access
fallback, §6.5's restatement of §4's risk logic, and the §1.6 recapitulation of §1.1–1.5. Net
position: **59,495 of 60,000, ~500 reserve** — tighter than before, and the placeholder-filling
pass will need roughly that much again. Expect one more compression pass at fill time; §1.3 and
T4.2–T4.3 are the next candidates.

Separately, the multi-velocity evidence idea is assessed in `evidence-velocity-assessment.md`;
only its defensible part (external situational reporting on the ongoing event) entered the plan,
via T3.2, T1.2 and a future-direction paragraph in §5.3.
