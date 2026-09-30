# To do: Ambizione, deadline 3 November 2026

> ## ❄ SCIENTIFIC TEXT FROZEN (30 September 2026)
>
> Three audit rounds (two external, one internal) now converge: the science is finished. **Do not
> reopen the architecture** - no new methods, domains, literature or restructuring. Remaining
> work is **release QA**, in this order:
>
> 1. **Bibliography records** - every author list, DOI, venue and status from the publisher
>    record; then strip all editorial notes/flags. (`placeholders.md` lists them.)
> 2. **Letters** - host confirmation (two SNSF-template signatures), general confirmation,
>    three collaboration letters. Statuses in §2.3.3.2 flip to *secured* only when in hand.
> 3. **Budget** - the RGO/HR rate into `budget.md`'s decision table; lock the CHF 250k
>    line-items; adjust the 50%×48 duration only if the rate forces it.
> 4. **Data** - CASU-144 agreement scope confirmed (incl. cause categories covering BOTH
>    respiratory and heat-sensitive classes, and broad age bands).
> 5. **Episode inventory** - run the eligibility rules; replace the provisional 13–14.
> 6. **mySNF calibration** - upload the draft PDF **early**; the source count (59,989) is a
>    trigger to calibrate, not a margin. Then 15-page/visual QA of the final PDF.
>
> Prose edits after this point only if forced by one of the six items above.
>
> **Day-by-day pacing for all of this: `CALENDAR.md`** (readers ping 1 Oct → replies 16 Oct;
> submission target Fri 30 Oct). The CCER package for the operational data is drafted in
> `04-other-documents/ccer/` - the DPO route question goes out Thu 2 Oct.

Settled and no longer open: eligibility (RGO-confirmed), host (Institute of Global Health,
independent programme), no research stay (equivalent mobility via short visits/collaborations,
Art. 9 §4c), IP (UNIGE), no doctoral student or postdoc (2026 rules), one scientific/technical
collaborator from project funds, structure of the plan (SNSF Guidelines 4.3), hierarchical
confirmatory testing (respiratory primary, heat sequential).

---

## Blocked on other people: start all of these now

- [ ] **⚠ RGO, one email:** internal deadline; salary standards for the applicant (~CHF 115k
      indicative) and for support personnel; whether one person can sign the detailed host
      confirmation as both contact person and head of institute; budget-entry guidance.
- [ ] **⚠ Host confirmation, two signatures** (contact person + head of institute, SNSF template
      verbatim, institute letterhead): resolve who signs as contact person; confirm **nobody else
      at ISG applies under the same person** (Art. 8 §6 - one applicant per contact person);
      confirm the "independent programme within ISG" wording the Faculty can actually sign.
      Send `04-other-documents/emails/02-ray-host.md`.
- [ ] **⚠ Data-access letters:** HUG emergency (Desmettre), CASU-144 (Larribau), ICU. Letters of
      collaboration only - **no praise of applicant or project, or the SNSF discards them**
      (Guidelines 2.17). Send `04-other-documents/emails/03-…`, `04-…`.
- [ ] DS4DH collaboration letter, WP1 (Teodoro) - `04-other-documents/emails/01-teodoro.md`.
- [ ] General confirmation from the Vice-Rectorate (routed via the institute - automatic once the
      detailed confirmation exists, but chase it).

## mySNF / portal mechanics (your account, start early)

- [ ] Create/check the mySNF account, role "grant applicant" - processing takes days.
- [ ] Compile the **CV + major achievements on portal.snf.ch** (fixed template; include your
      contribution per publication; present **LiteRev-Evidence as a research output** under DORA).
- [ ] Update the **ORCID profile** - its public content goes to reviewers.
- [ ] Download the **statement-of-mobility form** from mySNF; fill in **Adobe Acrobat only**.
      Content plan: `04-other-documents/statement-of-mobility.md` (Art. 9 §3 makes the prospective
      part mandatory - name 2–3 short visits + running collaborations; argue all four
      institution-choice triggers).
- [ ] No cover letter, no career plan - they are deleted if uploaded.

## The one empirical task that gates the registration numbers

- [ ] **Build the episode inventory** (respiratory, then heat) once CASU-144 series access is
      confirmed - template in `05-review/applicant-facts.md`. Then fix `[[N]]`, horizons, `[[Δ]]`,
      run the design/power simulation, and replace `[[expected order of ten]]` with the count.

## Writing that remains (all under your control)

- [ ] Fill the ~30 `[[…]]` placeholders. **Reserve is ~0 and the counter excludes placeholder
      text - every fill needs an offsetting cut.** Cut list in `03-research-plan/draft/README.md`.
- [ ] Bibliography: full author lists (no "et al." except >50-author consortia), DOIs everywhere
      possible, verify against publisher records. Flags are in `draft/99-bibliography.md`.
- [ ] Novelty audit via LiteRev (documented search for prior evidence-priors + cold-start work).
- [ ] Verify the summary fits **one page** in the rendered PDF (the cap is a page, not characters).
- [ ] Final budget in mySNF categories: ≤ CHF 250k; **no open-access costs** (separate mechanism);
      **Open Research Data costs must be in now**; equipment ≤ CHF 100k; budget frozen at
      submission. Rules: `04-other-documents/budget.md`.
- [ ] Declare GESICA, GeoAI4EI, legionellosis funding in mySNF; delimitation table is in §2.6.
- [ ] Exclusion list for external reviewers (optional - decide; Guidelines 2.12).
- [ ] Final consistency audit: plan ↔ budget ↔ portal CV ↔ mobility form ↔ host letters ↔ data
      letters. Then upload, and **check the character count in mySNF - its counter is binding**.

## Dates ahead (from the call documents)

| When | What |
| --- | --- |
| ~Oct (RGO) | UNIGE internal deadline for confirmations |
| 30 Oct | Target submission |
| 3 Nov 2026, 17:00 | SNSF deadline |
| Early Apr 2027 | Phase 1 outcome |
| **3–4 Jun 2027** | **Life Sciences panel interview** (project presentation + Q&A - the confirmatory design and failure map must survive a live panel) |
| Mid-Jul / early Aug 2027 | Phase 2 outcome / decision letter |
| 1 Sep 2027 – 1 Sep 2028 | Grant start window |

## Where things are

| | |
| --- | --- |
| Research plan (assembled) | `03-research-plan/FINAL-research-plan.md` - edit `draft/`, run `sh draft/assemble.sh` |
| Compliance audit vs call documents | `05-review/snsf-compliance-audit.md` |
| Applicant decisions log | `05-review/applicant-facts.md` |
| Hypothesis audit | `05-review/hypothesis-audit.md` |
| Host letters guidance | `04-other-documents/host-institution-letters.md` |
| Budget rules + table | `04-other-documents/budget.md` |
| Mobility content plan | `04-other-documents/statement-of-mobility.md` |
| Emails ready to adapt | `04-other-documents/emails/` |
| Call documents (primary sources) | `00-source-documents/call-documents/` |
