# Working calendar — 1 October → 3 November 2026

**Rule of the calendar:** every working day has at most ~30–60 minutes of application work, so
nothing piles up. Items in **bold** are the day's must-do; the rest slides if life happens.
Target submission **Friday 30 October**; the SNSF deadline (Tue 3 Nov, 17:00) is buffer, not plan.
The science is frozen — nothing here reopens it.

**External readers: start NOW.** The plan froze on 30 September, which is exactly when external
reading becomes useful rather than churn. With a two-week reply window, the only send date that
leaves time to incorporate feedback is **this week**. Later than ~6 October and the replies
collide with final assembly.

---

## Week 1 — Wed 1 to Fri 3 October: everything leaves your desk

| Day | Do |
| --- | --- |
| **Wed 1** | **Send the RGO email** (`emails/00-rgo.md`; reply-by 9 Oct). **Create/verify the mySNF account** ("grant applicant" role — takes days, so today). Pick your **3–4 external readers** (see profiles below) and send the availability ping (`emails/06-readers.md`, part 1). |
| **Thu 2** | **Send the Ray email** (`02-ray-host.md`, SNSF template attached; reply-by 13 Oct). Update your **ORCID** public profile (goes to reviewers). Email the **DPO** with the CCER route question (**drafted: `04-other-documents/emails/07-dpo.md`**; attach `ccer/01` + `ccer/03` as PDF; reply-by 13 Oct). |
| **Fri 3** | **Send the plan to the readers who said yes** (assembled PDF + the 5 focused questions; **reply-by Friday 16 October**). **Send Teodoro, Desmettre, Larribau** (`01/03/04`, project note + collaboration-letter draft attached; reply-by 13 Oct). |

## Week 2 — Mon 6 to Fri 10 October: portal mechanics, nothing blocking others

| Day | Do |
| --- | --- |
| Mon 6 | Start the **portal CV** (portal.snf.ch): paste Module 1 + output list; 30 min only. |
| Tue 7 | Portal CV: Modules 2–4. Write your one-line **senior-author contribution** (output list item 5). |
| Wed 8 | Download the **mobility form** from mySNF; paste dimensions 1 + 3 from `statement-of-mobility-draft.md`. |
| Thu 9 | Mobility form: dimensions 2, 4, 5. **Decide the 2–3 named short visits** — the last blank that is purely yours. |
| Fri 10 | **Upload the draft plan PDF to mySNF and read its character counter.** (Source count 59,989 is a trigger, not a margin.) Log the delta in `05-review/applicant-facts.md`. Send the **Calmy courtesy note** if Ray has replied. |

## Week 3 — Mon 13 to Fri 17 October: chase, numbers, inventory

| Day | Do |
| --- | --- |
| Mon 13 | Reply-by date for Ray/Teodoro/Desmettre/Larribau: **phone anyone silent.** Ten minutes each. |
| Tue 14 | RGO numbers should be in: fill the **budget decision table** (`budget.md`) — keep 50%×48 or shorten to M3–M42 per the rule. If the DPO answer is in and concurs with Route A/C: **file the BASEC clarification de compétence** (text ready: `04-other-documents/ccer/05-clarification-competence-fr.md`; attach the DPO answer as annex 2). |
| Wed 15 | Draft the full **mySNF budget line-items** (≤ CHF 250k; ORD in; no OA costs; equipment <100k). |
| Thu 16 | **Reader replies due.** Acknowledge each same-day. If Larribau's data facts arrived: start the **episode inventory** (template in `05-review/applicant-facts.md`). |
| Fri 17 | Triage reader feedback into: (a) prose fixes, (b) frozen-science challenges → only act if two readers agree, (c) interview material → `05-review/interview-prep` notes. |

## Week 4 — Mon 20 to Fri 24 October: incorporate and close

| Day | Do |
| --- | --- |
| Mon 20 | Apply reader prose fixes (character-neutral; re-run `wordcount.sh` after each). |
| Tue 21 | Finish the **episode inventory**; replace "13–14 candidates" with the real count if it differs. |
| Wed 22 | **Bibliography release-QA**: every author list/DOI/venue from publisher records; then strip ALL editorial notes and flags (release step 1). |
| Thu 23 | Letters status check: host confirmation routing at the Vice-Rectorate? Collaboration letters signed? Flip §2.3.3.2 statuses **only for letters in hand**. |
| Fri 24 | Second **mySNF counter check** with the near-final PDF. Fix any overage now, not next week. |

## Week 5 — Mon 27 to Fri 30 October: release

| Day | Do |
| --- | --- |
| Mon 27 | Assemble the final PDF: figures render, tables unbroken, **≤15 pages**, no `[[…]]` anywhere, bibliography clean. |
| Tue 28 | Upload everything to mySNF: plan, CV PDF, mobility form, confirmations, collaboration letters, budget. Full-form walkthrough for empty fields. |
| Wed 29 | One full read of the submitted-state PDF, printed. Fix only typos. |
| **Fri 30** | **SUBMIT.** Confirmation email archived; tag the repo (`git tag submitted-2026`). |

## Buffer — Mon 2 to Tue 3 November

Only for disasters: a letter arriving late, an upload failure. **Do not touch content.**
Deadline: **Tuesday 3 November, 17:00 Swiss time.**

---

## External readers — who and how

**Profiles to cover (3–4 people, each reads once):**
1. **A statistician** — sends them to §2.3.1/T3.3 (fixed-sequence test, permutation, OC
   simulation). *Natural candidate: Prof. Eva Cantoni — knows you, no Keiser overlap.*
2. **An infectious-disease epidemiologist / forecaster** — §2.1 + validation domains. Ideally
   someone outside Geneva `[[GeoAI4EI or GESICA-adjacent contact you trust]]`.
3. **An emergency clinician** — WP4 and the operational claims `[[Desmettre or Larribau read it
   anyway for their letters; a third clinician avoids double-hatting]]`.
4. **A grant-seasoned senior** who has sat on SNSF-type panels — reads it as a juror, 30 minutes
   `[[name]]`.

**Mechanics:** availability ping first (Wed 1), PDF to those who accept (Fri 3), **reply by
Fri 16 October** — exactly two weeks, stated in the email, with the 5 questions so feedback
arrives structured. Request email: `04-other-documents/emails/06-readers.md`.

**Freeze discipline:** reader feedback lands in week 4 as prose fixes and interview prep.
A science change happens only if two readers independently hit the same load-bearing problem —
then it is a real defect, not an opinion.

## Standing items (weekly, Friday, 10 minutes)

- Chase any outstanding letter or number. Silence is the enemy, not refusal.
- Re-run `sh 03-research-plan/draft/assemble.sh && sh 03-research-plan/draft/wordcount.sh`.
- Commit and push, so the repo always reflects reality.
