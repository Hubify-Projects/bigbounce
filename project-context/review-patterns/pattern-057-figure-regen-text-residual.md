---
pattern_id: 057
status: active
first_seen: EXT12-batch-truth-audit (2026-06-13)
papers_observed: [P5]
finding_count: 3  # 3 residual V-Web tokens in §VIII A, §IX B, App C body text
proposed_by: r-round-pattern-mine 2026-06-13
---

# pattern-057: figure-regen-text-residual

**Description**: When a paper undergoes a global text rename (e.g., V-Web→T-Web at v0.1.76) AND figure plot titles are independently regenerated (v0.1.77), text-only residuals can survive in body sections that weren't covered by the original rename grep. The figure-art verification step (confirming plot titles are correct) is necessary but not sufficient — body-text instances in prose paragraphs, section headers, and appendix text can persist even after all figures are confirmed correct.

**Evidence (EXT12)**:
- P5 §VIII A: residual "V-Web" token in body prose — not in any figure title or caption.
- P5 §IX B: residual "V-Web" token in body prose paragraph.
- P5 Appendix C: residual "V-Web" token in appendix body text.
- All three survived EXT11 figure-art regeneration (pattern-054 closure) because the EXT11 fix verified FIGURE TITLES but did not grep the full .tex body text.

**Root cause**: Rename agents typically grep for occurrences in figure-generating scripts and verify rendered plot titles, but do not perform an exhaustive body-text sweep of the compiled .tex. Historical/citation references (legitimate uses) reduce the signal-to-noise ratio, making "smart" filtered greps underperform exhaustive sweeps.

**Resolution**:
1. After any global rename, perform a final body-text grep against the full .tex source for ALL legacy tokens.
2. Exclude only genuinely legitimate references: historical citations (inside `\cite{}`), label commands (inside `\label{}` / `\ref{}`), file paths in footnotes/Data Availability, and explicit disambiguating parentheticals ("formerly known as V-Web").
3. Every remaining hit is a residual — convert to the new terminology.
4. This sweep must be the LAST step of any rename closure agent, after figure regeneration is confirmed.

**Detection rule (mechanical)**:
```bash
# After a rename from OLD_TERM to NEW_TERM:
OLD_TERM="V-Web"
TEX="<paper.tex>"

# Grep body text, excluding %-commented lines and legitimate protected uses:
grep -nE "$OLD_TERM" "$TEX" \
  | grep -v '^[0-9]*:%' \
  | grep -vE '(\\cite\{|\\label\{|\\ref\{|formerly known as|historical(ly)?|originally called)'
```
Flag every remaining hit. If zero hits → rename is complete.

**Prevention**: include a "post-rename body-text sweep" as the LAST step of any rename closure agent. The detection rule above must appear in the closure checklist, not just the pre-review checklist.

**Severity**: medium (becomes high if a residual token is in the abstract or title)

**Cross-reference**: This pattern extends pattern-054 (σ-mixing, figure-title verification context). Pattern-054 covers verifying the figure art was regenerated; pattern-057 covers verifying body text was swept AFTER figure verification. Both checks are required for any rename closure.
