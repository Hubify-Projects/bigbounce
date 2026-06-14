---
pattern_id: 059
status: active
first_seen: EXT14 (2026-06-13)
papers_observed: [P5]
finding_count: 1
proposed_by: r-round-pattern-mine 2026-06-13
parent_patterns: [057]
---

# pattern-059: math-mode-subscript-miss-after-rename

**Description**: After a global text rename (e.g., V-Web→T-Web), math-mode subscripts (`_{V-Web}`, `_{V\text{-}Web}`, `_{V\mathrm{-Web}}`, etc.) survive in equations and inline math because plain-text body-text greps don't see them. Pattern-057 caught body-text residuals at EXT12 but missed math-mode residuals at EXT14. The subscript forms `_{...}` and inline math delimiters `$...$` and `\(...\)` are structurally distinct from plain prose — a grep for `V-Web` in body prose can return zero hits while `_{V-Web}` persists silently in an equation or inline math span.

**Evidence (EXT14)**:
- P5 §IX B: math-mode subscript `_{V\text{-}Web}` survived the body-text sweep from EXT11/EXT12 closures. The plain-prose grep caught all body residuals (pattern-057 closure) but the subscript inside the math environment was not flagged.
- ChatGPT and Gemini both flagged the subscript form as a residual V-Web reference in EXT14; Grok 6/6 ACCEPT confirmed it was isolated to that site.

**Root cause**: Pattern-057's detection rule greps for the literal token in body text, but math-mode subscripts use LaTeX delimiters that can obscure the old term from a plain-token grep. Specifically:
- `_{V-Web}` — direct hyphen in subscript
- `_{V\text{-}Web}` — \text macro in subscript
- `_{V\mathrm{-Web}}` — \mathrm macro in subscript
- `$...$` inline math containing `V-Web` in any form
- `\(...\)` inline math containing `V-Web` in any form

None of these are guaranteed to be caught by `grep -nE "V-Web"` depending on surrounding context.

**Detection rule (mechanical)** — run AFTER pattern-057 body-text sweep returns zero:

```bash
# Math-mode subscript residuals after rename (extend pattern-057):
TEX="<paper.tex>"
OLD="V-?Web"          # adjust OLD for each rename; covers V-Web and V Web

# 1. Subscript form:
grep -nE "_\{?(V-?Web|V\\\\text\{-\}Web|V\\\\mathrm\{-Web\})\}?" "$TEX"

# 2. Inline math $...$ containing the old term:
grep -nE '\$[^$]*V-?Web[^$]*\$' "$TEX"

# 3. \(...\) inline math:
grep -nE '\\\\([^)]*V-?Web[^)]*\\\\))' "$TEX"

# 4. Display math environments (equation, align, etc.):
# Manual scan of all \begin{equation}...\end{equation} blocks for the old token.
# Mechanical: extract with awk and grep:
awk '/\\begin\{(equation|align|multline|gather)\}/,/\\end\{(equation|align|multline|gather)\}/' "$TEX" \
  | grep -nE "V-?Web"
```

Flag every match. Zero hits across all four commands = math-mode sweep complete.

**Prevention**: extend pattern-057's post-rename sweep to include the math-mode regex commands above. The math-mode sweep MUST run as a required step BEFORE the recompile-and-render gate. Ordering:

1. Body-text sweep (pattern-057)
2. **Math-mode subscript + inline math sweep (pattern-059) ← NEW**
3. Compile and render
4. Visual pdftoppm audit

**Example sites**:
- P5 §IX B: subscript in display equation at v0.1.78 — `\sigma_{V\text{-}Web}` → should be `\sigma_{T\text{-}Web}` after the V-Web→T-Web rename at v0.1.76.

**Severity**: medium (becomes high if a residual math-mode subscript appears in an abstract equation or headline result)

**Cross-reference**: This pattern extends pattern-057 (body-text residuals after global rename). Pattern-057 covers prose; pattern-059 covers math environments. BOTH sweeps are required for any rename closure — run them together, in order, before compiling.
