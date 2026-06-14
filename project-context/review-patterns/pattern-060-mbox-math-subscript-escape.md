---
pattern_id: 060
status: active
first_seen: EXT16 (2026-06-13)
papers_observed: [P5]
finding_count: 1
proposed_by: r-round-pattern-mine 2026-06-13
parent_patterns: [057, 059]
---

# pattern-060: mbox-math-subscript-escape

**Description**: After a global text rename (e.g., V-Web→T-Web), math-mode subscripts using `\mbox{-}` as the hyphen escape survive even after pattern-057 (body-text sweep) and pattern-059 (`\text{-}` / direct-hyphen subscript sweep). The `\mbox{}` wrapper is a third form used to inhibit hyphen-breaks in math mode and is structurally distinct enough that the pattern-059 regexes (`V\\text\{-\}Web`, `V\\mathrm\{-Web\}`, `V-Web`) do not catch it.

**Evidence (EXT16)**:
- P5 l.2864: `V\mbox{-}Web` survived the pattern-057+pattern-059 double sweep performed at EXT15-closure. ChatGPT flagged it in EXT16 as a residual V-Web reference.
- Root form: `_{V\mbox{-}Web}` inside inline math or a display equation subscript.

**Root cause**: Pattern-059 enumerates `\text{-}`, `\mathrm{-}`, and direct-hyphen forms but omits `\mbox{-}`. The `\mbox{}` command is semantically equivalent in this context but lexically distinct. A post-rename grep that catches all three of the pattern-059 forms still returns zero hits while `\mbox{-}` persists.

**Detection rule (mechanical)** — replaces pattern-059's sweep with a unified union regex covering all four hyphen-escape forms:

```bash
# Union sweep: body-text + math-mode subscripts after any V-Web→T-Web rename.
# Run AFTER pattern-057 body-text sweep returns zero.
TEX="<paper.tex>"

# 1. All subscript/inline forms — union of direct hyphen + \text + \mathrm + \mbox:
grep -nE '_\{?V(\\(text|mbox|mathrm)\{-\})?-?Web\}?' "$TEX"

# Simplified equivalent (covers all four forms):
grep -nE 'V(\\(text|mbox|mathrm)\{-\}|-)Web' "$TEX"

# 2. Inline math $...$:
grep -nE '\$[^$]*V(\\(text|mbox|mathrm)\{-\}|-)Web[^$]*\$' "$TEX"

# 3. Display math environments:
awk '/\\begin\{(equation|align|multline|gather|eqnarray)\}/,/\\end\{(equation|align|multline|gather|eqnarray)\}/' "$TEX" \
  | grep -nE 'V(\\(text|mbox|mathrm)\{-\}|-)Web'
```

Zero hits across all three commands = sweep complete (pattern-057 + pattern-059 + pattern-060 union).

**Prevention**: replace the pattern-059 sweep steps with the union regex above. The combined regex catches:
- `V-Web` (direct hyphen, pattern-057)
- `V\text{-}Web` (pattern-059)
- `V\mathrm{-Web}` (pattern-059)
- `V\mbox{-}Web` (pattern-060, NEW)

**Ordering** (replaces pattern-059's four-step ordering):

1. Body-text sweep — `grep -nE "V-Web" "$TEX"` (pattern-057)
2. **Union math-mode sweep — run the combined regex above (patterns 059+060 merged)** ← use this step instead of the pattern-059 four-command block
3. Compile and render
4. Visual pdftoppm audit

**Example site**:
- P5 l.2864: `\sigma_{V\mbox{-}Web}` → `\sigma_{T\mbox{-}Web}` (EXT16 closure, v0.1.80)

**Severity**: medium (becomes high if the residual appears in an abstract equation or headline result)

**Cross-reference**: Extends pattern-057 (body-text residuals) and pattern-059 (math-mode subscript residuals). Pattern-057 covers prose; pattern-059 covers `\text{-}` and `\mathrm{-}` math forms; pattern-060 adds the `\mbox{-}` form. Run the union grep (pattern-059+060 combined) in lieu of the pattern-059 four-command block for any rename closure going forward.
