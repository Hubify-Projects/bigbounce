# EXT7 — in-thread delta round 7 · manifest

**Round**: EXT7 (2026-06-13 ~00:53–02:30 PT; versions v1A.0.67 / v1B.0.64 / v1.7.59 / v3.1.102 / v181 / v0.1.71)
**Round headline**: first external read of the R36conf wave — R36conf (OpenAI gpt-5/o3, Gemini 2.5-pro, Grok-4.3, Perplexity sonar-pro) closed all EXT6-verified items. New this round: P1A §IV E synthesis-paragraph rewrite + §X D decomposition footnote, P1B one-sided ΔNeff 95% upper limits, P2 consolidated systematics Table IV, P3 binomial p-value for Planck 152/48 split, P4 A_95,nq rename + 2-line Fisher-scaling derivation, P5 Table X n_CW typo fix.
**Thread policy change**: ALL Gemini chats moved to FRESH threads (see §Operational notes). Prior Gemini P3 thread `2b33106610ec2401` permanently dropped after EXT6. All other prior Gemini threads also abandoned due to thread-overload/persistence failures during EXT7 attempt on `4f6bdc99c91dc1d2` (30 user turns / 12 model turns accumulated). EXT7 Gemini submissions used new fresh chats for all 6 papers.

## Submissions (all 18 verified: chip/version-presence + model/effort + generation + growth gate)

| Paper | Version (md5) | ChatGPT Pro Extended | Grok Heavy | Gemini Thinking |
|---|---|---|---|---|
| P1A | v1A.0.67 (a66372893ac8594d) | ✅ chip+gen+ProExt | ✅ Heavy chip+gen | ✅ FRESH thread (chip+growth) [chat](https://gemini.google.com/app/5ba8d55a1cec9191) |
| P1B | v1B.0.64 (0f28d3489d369eb9) | ✅ chip+gen+ProExt | ✅ Heavy chip+gen | ✅ FRESH thread (chip+growth) [chat](https://gemini.google.com/app/54c264414af25c50) |
| P2 | v1.7.59 (cb97ec6b84256e38) | ✅ chip+gen+ProExt | ✅ Heavy chip+gen | ✅ FRESH thread (chip+growth) [chat](https://gemini.google.com/app/96027ccee8f27e82) |
| P3 | v3.1.102 (60e26e5ec3afcd56) | ✅ chip+gen+ProExt | ✅ Heavy chip+gen | ✅ **FRESH thread (P3_fresh.txt full referee prompt)** [chat](https://gemini.google.com/app/8f88d28fa5d8d911) |
| P4 | v181 (f5867e653f02488a) | ✅ chip+gen+ProExt | ✅ Heavy chip+gen | ✅ FRESH thread (chip+growth) [chat](https://gemini.google.com/app/fc828b487d766514) |
| P5 | v0.1.71 (d2b33c8a376f93b8) | ✅ chip+gen+ProExt | ✅ Heavy chip+gen | ✅ FRESH thread (chip+growth) [chat](https://gemini.google.com/app/07511af2323551ba) |

All PDFs md5-verified byte-exact against local mirrors. ChatGPT and Grok PDFs delivered via $B upload (chip confirmed pre-send). Gemini PDFs delivered via native macOS file dialog (osascript Cmd+Shift+G + Enter × 2 → chip confirmed visually).

## Submissions table (chat URLs)

| Paper | ChatGPT Pro Extended | Grok Heavy | Gemini Thinking |
|---|---|---|---|
| P1A | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e5e8-96cc-83e8-918f-3b1dd3f96d96) | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=5abdb89c-8b7d-4ec0-8839-c39f5a634f03) | [chat](https://gemini.google.com/app/5ba8d55a1cec9191) **FRESH** |
| P1B | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded) | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=33f977da-4a3e-44b6-a6e4-599ae00d5c3e) | [chat](https://gemini.google.com/app/54c264414af25c50) **FRESH** |
| P2 | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e646-8510-83e8-8999-77b849c6519d) | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=0c4cb7d1-7bc6-4033-a4ac-f4605ec99269) | [chat](https://gemini.google.com/app/96027ccee8f27e82) **FRESH** |
| P3 | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e669-b608-83e8-9c0c-e7f247ff271a) | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=de56f195-4cae-4dc6-bc3e-f9dbf4de9b54) | [chat](https://gemini.google.com/app/8f88d28fa5d8d911) **FRESH + P3_fresh.txt** |
| P4 | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37) | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=411d5219-2864-4196-8d60-da2c97771cc0) | [chat](https://gemini.google.com/app/fc828b487d766514) **FRESH** |
| P5 | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6e9-b9a4-83e8-9624-ec9291ae8064) | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=edd1963e-cc7e-4a86-b288-1a7834c9e45a) | [chat](https://gemini.google.com/app/07511af2323551ba) **FRESH** |

## Operational notes

### Gemini thread policy change (CRITICAL for EXT8)
All 6 Gemini threads are now FRESH (new URLs). The original EXT1–EXT6 Gemini thread IDs (`4f6bdc99c91dc1d2`, `2ba6d99c84794eb7`, `c01bc000d0305271`, `2b33106610ec2401`, `8340abb820aada09`, `3cbe98b65fe83d40`) are **permanently retired** as of EXT7. EXT8 must use these EXT7 Gemini URLs for in-thread deltas.

**Why fresh threads**: The EXT1–EXT6 Gemini P1A thread accumulated 30 user turns / 12 model turns due to failed upload retry attempts during this session. Gemini's threading architecture silently drops pending responses when a thread has too many unmatched user turns. Fresh threads clean this up.

**Gemini upload recipe (EXT7 discovery — must be encoded in SKILL.md)**:
- The proven recipe: navigate to `https://gemini.google.com/app` (home, NOT an existing chat) → click `[aria-label="Upload & tools"]` → click `@ref [menuitem] "Upload files"` → native macOS dialog opens (sheet count = 1) → osascript: activate Chrome for Testing → Cmd+Shift+G → type full path → Enter × 2 → dialog closes (sheet count = 0) → chip appears in composer → fill prompt → click send. Growth gate: `stop_button_visible=false AND len > base+3000`.
- **CRITICAL**: Do NOT attempt CSS manipulation of hidden file inputs (`display:none→block` trick). The file registers client-side but Gemini's backend never receives it, causing silent stuck states with no model response.
- **CRITICAL**: Submit on the fresh Gemini HOME (not existing thread) to avoid the persistence kill rule. After send, the URL changes to the new chat ID which is the permanent thread URL.

### Gemini P3 fresh thread
`https://gemini.google.com/app/8f88d28fa5d8d911` — submitted with P3_fresh.txt (FULL MNRAS referee prompt, NOT delta). This is the THIRD consecutive fresh P3 thread (EXT6 was `2b33106610ec2401`, now EXT7 is `8f88d28fa5d8d911`). The EXT6 thread `2b33106610ec2401` is permanently dropped as instructed.

### ChatGPT and Grok
Zero retries on ChatGPT and Grok. Both confirmed generating within 6s of submit. ChatGPT used same thread URLs as EXT1–EXT6. Grok used same thread URLs as EXT1–EXT6.

### Submit window
- ChatGPT phase: ~00:53 PDT (6 papers, ~18 min)
- Grok phase: ~01:03 PDT (6 papers, ~18 min)
- Gemini phase: 01:15–02:30 PDT (90 min including recovery from thread-overload issue)
- Total submit window: 00:53–02:30 PDT

## Harvest — COMPLETE (2026-06-13 ~03:32 PT)

All 18 reports saved to `project-context/peer-reviews/EXT7_<paper>_<Provider>.md`.
Zero URL mismatches. Zero still-generating chats. Zero retries needed.
Gemini fresh-thread recipe: all 6 threads loaded cleanly (1 model-response each, no rendering issues).

## Verdicts — EXT7

| Paper | ChatGPT Pro Ext | Grok Heavy | Gemini Thinking |
|---|---|---|---|
| P1A | MAJOR REVISIONS | ACCEPT | ACCEPT WITH MINOR REVISIONS |
| P1B | MAJOR REVISIONS | ACCEPT | ACCEPT |
| P2 | MAJOR REVISIONS | ACCEPT | MINOR REVISION |
| P3 | MAJOR REVISIONS | ACCEPT | MAJOR REVISIONS |
| P4 | MAJOR REVISIONS | ACCEPT | ACCEPT WITH MINOR REVISIONS |
| P5 | MAJOR REVISIONS | ACCEPT | MINOR REVISION |

## EXT6 → EXT7 Verdict Transitions

| Paper | Provider | EXT6 | EXT7 | Delta |
|---|---|---|---|---|
| P1A | ChatGPT | MAJOR REVISIONS | MAJOR REVISIONS | no change |
| P1A | Grok | ACCEPT | ACCEPT | stable |
| P1A | Gemini | ACCEPT WITH MINOR REVISIONS | ACCEPT WITH MINOR REVISIONS | stable (fresh thread, same verdict) |
| P1B | ChatGPT | MAJOR REVISIONS | MAJOR REVISIONS | no change |
| P1B | Grok | ACCEPT | ACCEPT | stable |
| P1B | Gemini | ACCEPT | ACCEPT | stable (fresh thread, verdict held) |
| P2 | ChatGPT | MAJOR REVISIONS (body: "minor revisions") | MAJOR REVISIONS | no change |
| P2 | Grok | ACCEPT | ACCEPT | stable |
| P2 | Gemini | MINOR REVISIONS | MINOR REVISION | stable (fresh thread, verdict held) |
| P3 | ChatGPT | MAJOR REVISIONS | MAJOR REVISIONS | no change |
| P3 | Grok | ACCEPT | ACCEPT | stable |
| P3 | Gemini | MAJOR REVISIONS | MAJOR REVISIONS | stable (fresh thread, verdict held — new blocker on data leakage) |
| P4 | ChatGPT | MAJOR REVISIONS | MAJOR REVISIONS | no change |
| P4 | Grok | ACCEPT | ACCEPT | stable |
| P4 | Gemini | ACCEPT (raw body) → EXT6 unclear | ACCEPT WITH MINOR REVISIONS | Gemini fresh gave cleaner signal |
| P5 | ChatGPT | MAJOR REVISIONS | MAJOR REVISIONS | no change |
| P5 | Grok | ACCEPT | ACCEPT | stable |
| P5 | Gemini | MINOR REVISIONS | MINOR REVISION | stable (fresh thread, verdict held) |

**New ACCEPTs EXT6 → EXT7**: none (Grok was already ACCEPT across all 6 in EXT6; no new upgrades)
**Gemini fresh-thread stability**: 5/6 verdicts held or clarified cleanly. P4 Gemini produced cleaner ACCEPT WITH MINOR REVISIONS vs. unclear EXT6 signal. Gemini fresh-home recipe vindicated — zero rendering or upload issues, all 6 threads delivered responses with model-response count = 1.
**Grok pattern-009 note**: Grok held ACCEPT on all 6 papers in EXT7 (consistent with EXT6 pattern). No swing observed. The pattern-009 calibration concern (ACCEPT-EXT6 → REJECT swing) did not materialize.
