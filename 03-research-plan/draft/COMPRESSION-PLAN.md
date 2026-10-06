# Compression plan: 24 pages must become 15 (7 October 2026)

## The finding

The guidelines (4.3, verbatim): the plan "must not exceed 15 pages A4 **and** 60'000
characters", with **minimum 10pt font and 1.5 line spacing mandatory**; the bibliography is
excluded from both counts. We policed characters and never rendered pages. At the tightest
compliant layout (1.8 cm margins, compact headings, 10pt, 1.5 spacing) the current 59,974
characters produce **24 pages**. The page cap, not the character cap, is the binding
constraint: real capacity at these specs is roughly **40,000 to 43,000 characters**.

**Check at any time:** `bash draft/pagecheck.sh` (renders without bibliography, prints pages,
leaves the PDF at /tmp/pagecheck-latest.pdf). The mySNF upload remains the final arbiter.

## What this means for the revision week

The own-words revision is now a **compression pass**: rewrite in your voice AND cut about 30%.
This is tractable because compression hurts prose, not science: every hypothesis, number, rule
and safeguard stays; what goes is elaboration, repetition across sections, and secondary
enumeration.

## Per-section quotas (total target ~42,000)

| Section | Now | Target | Where the cuts live |
| --- | --- | --- | --- |
| 00 Title + summary | 3,871 | ~3,100 | Summary must also fit one page; tighten paragraphs 2 and 4 |
| 01 State of the art | 8,544 | ~5,900 | Each subsection's last "what this means" sentences repeat §2.1.6; method name-dropping lists |
| 02 Own work | 5,889 | ~4,200 | 2.2.1 finance narrative; GESICA paragraph overlaps §2.3.3; keep all facts and numbers |
| 03 Objectives | 7,751 | ~5,600 | Keep the hypothesis table and O-blocks intact; cut the connective prose between them |
| 04 Work plan | 20,384 | ~14,000 | The big one. Per-task: keep WHAT and the registered rules, cut HOW-motivation sentences; T3.2/T3.3 paragraphs can lose a third without losing a single rule |
| 05 Environment | 4,770 | ~3,400 | Table stays; prose around it halves |
| 06 Schedule | 1,898 | ~1,500 | Nearly fine; trim the fallback paragraph |
| 07 Impact + career | 6,867 | ~4,800 | 2.5 publication/impact prose; keep §2.6's independence block almost untouched |

## Rules for cutting

1. **Never cut:** hypotheses, the ladder, the two registration points, Δ/N/minimum-episode
   rules, the outcome definitions, the fallbacks, the distinction table, the independence
   block, any number, any citation that supports a claim.
2. **Cut first:** sentences that restate what an adjacent sentence already says; motivations
   for choices a reviewer would accept anyway; third examples where two carry the point.
3. **Tables survive, their introductions shrink.** A table needs one lead-in line, not a
   paragraph.
4. After each section: `bash draft/assemble.sh && bash draft/wordcount.sh && bash
   draft/pagecheck.sh`.
5. Layout still owes us ~1-2 pages: the hypothesis and commitments tables render badly at auto
   width (fix at final formatting, not in the text), and the two figures can lose a third of
   their height.

## Why not 60,000 characters in 15 pages

Arithmetic, for the record: A4 at 1.8 cm margins gives a 25.9 cm text block; 10pt at 1.5
spacing is 5.3 mm per line, so ~49 lines a page; ~100 characters a line gives a theoretical
ceiling near 70k for UNSTRUCTURED text, but ~45 headings, 8 tables, 2 figures, block quotes
and paragraph breaks consume roughly a third of the area. Funded plans at these specs
typically run 40-45k characters. The 60k ceiling is a cap, not an entitlement.
