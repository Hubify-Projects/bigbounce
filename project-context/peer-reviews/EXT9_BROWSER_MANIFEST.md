# EXT9 — Ship-Mode External Review Round (Browser Manifest)

**Date**: 2026-06-13 PT
**Round**: EXT9 (ninth external review round)
**Provider mix**: ChatGPT (Pro Extended) + Grok (Heavy) + Gemini (3.5 Thinking)
**Submission method**: gstack `/browse` skill driving Houston's persistent
Chrome-for-Testing profile (`~/.gstack/chromium-profile`)

## Headline

**Ship-mode round.** Closure summaries explicitly address the load-bearing
ChatGPT Class-D residuals from EXT7/8 — P4 harmonic-completeness figure
trail, P5 VoidFinder abstract framing, P1B w0wa finalization. **An
HONEST VERDICT CALIBRATION block was deployed for the first time** in
every per-paper prompt, instructing referees to apply real MNRAS / PRD
standards rather than fishing for polish, treating MAJOR REVISIONS as
reserved for substantive scientific rework, and noting that catalog-class
papers are extensive by nature.

**The recalibrated prompt is the round's load-bearing experimental change.**
Expectation: ChatGPT shifts off baseline-MAJOR if the calibration block +
real closure substance are doing what we believe they should. If ChatGPT
still returns MAJOR, the residual structurally lives in the paper, not in
referee mis-calibration — and we know exactly what to fix next.

ChatGPT and Grok are EXT7/8 chat deltas (continued history, "since your
prior report" framing). Gemini is six fresh-home submissions per the
skill's EXT7 backend-drops-uploads-on-existing-chats rule.

## Submissions table (18/18 verified in-flight)

| Paper | Provider | Model/Effort | PDF (md5) | Chat URL | Submitted (PT) | Verification |
|---|---|---|---|---|---|---|
| P1A | ChatGPT | Pro Extended | paper1a_ech_nogo_v1A.0.70.pdf · `4e24501f…0a7f` | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e5e8-96cc-83e8-918f-3b1dd3f96d96) | 12:02:49 | chip ✓ model ✓ version ✓ calibration ✓ |
| P1B | ChatGPT | Pro Extended | paper1b_mcmc_companion_v1B.0.66.pdf · `065d0962…b4f1` | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded) | 12:03:46 | chip ✓ model ✓ version ✓ calibration ✓ |
| P2 | ChatGPT | Pro Extended | paper2_fnl_forecast_v1.7.61.pdf · `6b413c94…f539f` | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e646-8510-83e8-8999-77b849c6519d) | 12:04:39 | chip ✓ model ✓ version ✓ calibration ✓ |
| P3 | ChatGPT | Pro Extended | paper3_anomaly_catalog_v3.1.104.pdf · `359a733d…56fb` | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e669-b608-83e8-9c0c-e7f247ff271a) | 12:05:38 | chip ✓ model ✓ version ✓ calibration ✓ |
| P4 | ChatGPT | Pro Extended | chirality_catalog_paper_v183.pdf · `34b06870…08d6` | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37) | 12:06:51 | chip ✓ model ✓ version ✓ calibration ✓ |
| P5 | ChatGPT | Pro Extended | p5_desi_chirality_v0.1.73.pdf · `4109fb18…d87c` | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6e9-b9a4-83e8-9624-ec9291ae8064) | 12:07:46 | chip ✓ model ✓ version ✓ calibration ✓ |
| P1A | Grok | Heavy | paper1a_ech_nogo_v1A.0.70.pdf · `4e24501f…0a7f` | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=5abdb89c-8b7d-4ec0-8839-c39f5a634f03) | 12:11:47 | chip ✓ model ✓ version ✓ calibration ✓ (1 retry — see ops notes) |
| P1B | Grok | Heavy | paper1b_mcmc_companion_v1B.0.66.pdf · `065d0962…b4f1` | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=33f977da-4a3e-44b6-a6e4-599ae00d5c3e) | 12:13:01 | chip ✓ model ✓ version ✓ calibration ✓ |
| P2 | Grok | Heavy | paper2_fnl_forecast_v1.7.61.pdf · `6b413c94…f539f` | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=0c4cb7d1-7bc6-4033-a4ac-f4605ec99269) | 12:13:57 | chip ✓ model ✓ version ✓ calibration ✓ |
| P3 | Grok | Heavy | paper3_anomaly_catalog_v3.1.104.pdf · `359a733d…56fb` | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=de56f195-4cae-4dc6-bc3e-f9dbf4de9b54) | 12:14:56 | chip ✓ model ✓ version ✓ calibration ✓ |
| P4 | Grok | Heavy | chirality_catalog_paper_v183.pdf · `34b06870…08d6` | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=411d5219-2864-4196-8d60-da2c97771cc0) | 12:16:19 | chip ✓ model ✓ version ✓ calibration ✓ |
| P5 | Grok | Heavy | p5_desi_chirality_v0.1.73.pdf · `4109fb18…d87c` | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=edd1963e-cc7e-4a86-b288-1a7834c9e45a) | 12:17:12 | chip ✓ model ✓ version ✓ calibration ✓ |
| P1A | Gemini | 3.5 Thinking | paper1a_ech_nogo_v1A.0.70.pdf · `4e24501f…0a7f` | [chat](https://gemini.google.com/u/0/app/9329c8701ab9c8a2) **FRESH** | 12:20:39 | chip ✓ model ✓ growth ✓ version ✓ calibration ✓ |
| P1B | Gemini | 3.5 Thinking | paper1b_mcmc_companion_v1B.0.66.pdf · `065d0962…b4f1` | [chat](https://gemini.google.com/u/0/app/aae77cbec4b016ae) **FRESH** | 12:22:37 | chip ✓ model ✓ growth ✓ version ✓ calibration ✓ |
| P2 | Gemini | 3.5 Thinking | paper2_fnl_forecast_v1.7.61.pdf · `6b413c94…f539f` | [chat](https://gemini.google.com/u/0/app/756828c3d1c6d0da) **FRESH** | 12:24:55 | chip ✓ model ✓ growth ✓ version ✓ calibration ✓ |
| P3 | Gemini | 3.5 Thinking | paper3_anomaly_catalog_v3.1.104.pdf · `359a733d…56fb` | [chat](https://gemini.google.com/u/0/app/a2fe3164ed9dfc44) **FRESH** | 12:27:05 | chip ✓ model ✓ growth ✓ version ✓ calibration ✓ |
| P4 | Gemini | 3.5 Thinking | chirality_catalog_paper_v183.pdf · `34b06870…08d6` | [chat](https://gemini.google.com/u/0/app/a66faf5b1892b7ad) **FRESH** | 12:29:41 | chip ✓ model ✓ growth ✓ version ✓ calibration ✓ |
| P5 | Gemini | 3.5 Thinking | p5_desi_chirality_v0.1.73.pdf · `4109fb18…d87c` | [chat](https://gemini.google.com/u/0/app/90bf624c0f388002) **FRESH** | 12:31:59 | chip ✓ model ✓ growth ✓ version ✓ calibration ✓ |

**Submit window**: 12:02:49 PT → 12:31:59 PT (~30 min wall-clock).

## NEW Gemini chat URLs (for EXT10 reuse policy decisions)

Per skill's EXT7 lesson: Gemini's backend silently drops uploads on EXISTING
chats. Every Gemini round must mint fresh URLs and record them here. EXT9's
six new URLs (also embedded in the table above):

- **P1A**: https://gemini.google.com/u/0/app/9329c8701ab9c8a2
- **P1B**: https://gemini.google.com/u/0/app/aae77cbec4b016ae
- **P2**:  https://gemini.google.com/u/0/app/756828c3d1c6d0da
- **P3**:  https://gemini.google.com/u/0/app/a2fe3164ed9dfc44
- **P4**:  https://gemini.google.com/u/0/app/a66faf5b1892b7ad
- **P5**:  https://gemini.google.com/u/0/app/90bf624c0f388002

EXT10 should NOT attempt in-thread delta on these URLs — see skill note;
re-fresh-home for the next round and treat the calibration framing as
self-contained.

## Honest-verdict-calibration block (load-bearing change)

Every per-paper prompt now contains:

> HONEST VERDICT CALIBRATION (this is a ship-mode round — please apply real
> publication standard, not a search for polish):
> - Apply MNRAS / Physical Review D referee standards rigorously.
> - Base the verdict on whether the paper requires substantial scientific
>   rework before publication — not on whether polish items can be found.
> - If the remaining items are style preferences, future-work pointers, or
>   submission-day actions, MINOR REVISIONS or ACCEPT is the appropriate verdict.
> - Catalog-class and methodology papers are extensive by nature and should
>   NOT default to MAJOR REVISIONS for that reason alone. Default to MAJOR
>   only when a load-bearing claim is unsupported, a critical control is
>   missing, or the paper cannot be reproduced from its committed artifacts.

In-thread verification confirmed the block rendered correctly in every
chat history (matched twice in ChatGPT/Grok threads — once in the user
turn, once in the model's prompt echo / acknowledgment — and once
verbatim in every fresh-home Gemini thread).

## Verification methodology

For every of the 18 submissions, the four-point pre/post gate ran:
1. **Chip** — `document.body.innerText.includes('<pdf-filename>')` after upload settle.
2. **Model/effort** — read back from the UI button text (Pro Extended / Heavy / 3.5 Thinking).
3. **Calibration block in composer pre-send** — `composer.textContent.includes('HONEST VERDICT CALIBRATION')`.
4. **Version-string-in-thread post-send** — `body.innerText.includes('<paper-version>')`.

Gemini submissions additionally cleared a **growth gate**: post-send body
length must exceed pre-send + 2500 chars (and the streaming indicator
must be idle) before the next chat opens — the EXT3 persistence-bug
fix encoded in the skill. All six Gemini growth gates passed.

## Operational notes

- **Grok composer**: `$B fill 'textarea'` timed out on the first attempt
  (the visible composer is a `[contenteditable]` DIV with
  `aria-label="Ask Grok anything"`, not the hidden textarea). One empty
  submit fired before the issue was caught; PDF chip survived. The fix
  was a JS `execCommand('insertText', …)` injection that triggers React's
  internal state updates, then the standard `button[aria-label="Submit"]`
  click. Applied uniformly to all 6 Grok legs after that. **Encoding this
  as a skill update for the next round** (`ce-via-execCommand` recipe in
  the Grok block).
- **Gemini native dialog**: the first P1A osascript attempt didn't
  trigger the upload — the picker hadn't fully rendered by the time
  Cmd+Shift+G fired. Extended the post-menu-click delay from 1.0 s to
  2.0 s and the post-Cmd+Shift+G delay from 1.5 s to 2.0 s; subsequent
  five Gemini uploads landed first-try. **Encoding as a skill update**
  (`gemini-dialog-render-delay: 2.0s minimum`).
- **Daemon hiccup**: one transient "headed server running but not
  responding" mid-poll on Gemini P4 (likely a Chromium IPC pause during
  large-PDF chunk processing). Self-recovered before the next poll
  interval; no data loss.
- **Frontmost-app guard fired correctly on all 6 Gemini osascripts** —
  no keyboard-focus theft incidents this round.
- **Time-of-day**: All submissions landed within Houston-quiet-keyboard
  window (midday weekday); the round did not require explicit quiet-window
  coordination.

## Round purpose recap

EXT7 + EXT8 measured ChatGPT pegged at MAJOR REVISIONS on most papers
across multiple revisions where Grok + Gemini had moved off MAJOR. The
empirical question for EXT9: **is ChatGPT MAJOR-pegging on scientific
substance, on referee miscalibration, or on prompt framing?** The
calibration block isolates the third channel. If ChatGPT MAJORs persist
under the calibrated prompt and against the documented residual closures
(P4 harmonic-completeness fig trail, P5 VoidFinder abstract, P1B w0wa),
the residual is structurally in the paper — not in framing — and the
next iteration plan writes itself. If ChatGPT shifts to MINOR / ACCEPT,
EXT8's MAJOR pegging was a calibration artifact and the calibration
block will be the standing prompt addition going forward.

## Next phase

Harvest target: **≥30 min after last submission** per skill — earliest
harvest window starts ~13:02 PT (Gemini P5 + 30 min). Pro Extended +
Heavy traces can run 10–40 min; poll, don't assume. Harvest output
files: `project-context/peer-reviews/EXT9_<paper>_<Provider>.md` per
the skill's Phase 3 spec, followed by `/peer-review-truth-audit` over
all 18 reports before any closure-edit work begins.
