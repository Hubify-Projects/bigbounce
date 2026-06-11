# EXT4 — in-thread delta round 4 · manifest

**Round**: EXT4 (2026-06-11 ~14:45–15:14 PT, same 18 threads; versions v1A.0.61 / v1B.0.58 / v1.7.53 / **v3.1.95** / v1.0.175 / v0.1.65)
**Round headline**: first external read of the P3 TARGETTYPE recount (≈0.9× Liang restricted, not 73×) + the full EXT3-closure deltas on all six papers.
**Delta-prompt**: references/delta-prompt-template.md (closure verification → fresh pass → updated verdict), with one calibration addition: explicit superscript-extraction example (F₀ = 1/8.98² extracts as "1/8.982") after that artifact was falsified 4 internal rounds running.

## Submissions (all 18 verified: attachment chip + model/effort + generation started)

| Paper | Version (md5) | ChatGPT Pro Extended | Grok Heavy | Gemini Thinking |
|---|---|---|---|---|
| P1A | v1A.0.61 (6f4384a8) | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e5e8-96cc-83e8-918f-3b1dd3f96d96) ✅ | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=5abdb89c-8b7d-4ec0-8839-c39f5a634f03) ✅ Heavy | [chat](https://gemini.google.com/app/4f6bdc99c91dc1d2) ✅ ver+gen+growth |
| P1B | v1B.0.58 (74e0cc28) | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded) ✅ | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=33f977da-4a3e-44b6-a6e4-599ae00d5c3e) ✅ Heavy | [chat](https://gemini.google.com/app/2ba6d99c84794eb7) ✅ ver+gen+growth |
| P2 | v1.7.53 (ecf2f6fe) | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e646-8510-83e8-8999-77b849c6519d) ✅ | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=0c4cb7d1-7bc6-4033-a4ac-f4605ec99269) ✅ Heavy | [chat](https://gemini.google.com/app/c01bc000d0305271) ✅ ver+gen+growth |
| P3 | **v3.1.95** (799d13fc) | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e669-b608-83e8-9c0c-e7f247ff271a) ✅ | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=de56f195-4cae-4dc6-bc3e-f9dbf4de9b54) ✅ Heavy | [chat](https://gemini.google.com/app/b10514f2f6e2ff2f) ✅ ver+gen+growth |
| P4 | v1.0.175 (8ad2cdfb) | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37) ✅ | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=411d5219-2864-4196-8d60-da2c97771cc0) ✅ Heavy | [chat](https://gemini.google.com/app/8340abb820aada09) ✅ ver+gen+growth |
| P5 | v0.1.65 (f265c319) | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6e9-b9a4-83e8-9624-ec9291ae8064) ✅ | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=edd1963e-cc7e-4a86-b288-1a7834c9e45a) ✅ Heavy | [chat](https://gemini.google.com/app/3cbe98b65fe83d40) ✅ ver+gen+growth |

PDFs downloaded from the live site and md5-cross-verified against local mirrors before submission (`~/Downloads/bigbounce-ext-review/EXT4/`). Pre-send screenshots: `/tmp/ext4_*_pre.png`.

## Operational notes (for the skill)

- Gemini account index drifted /u/2/ → **/u/0/** this round (chats resolve fine; avatar verified Houston "Work · Pro"; recipe updated).
- One focus-race during the Gemini P3 native dialog: Houston was typing on the machine, keystrokes landed in the terminal twice. Mitigation now encoded: frontmost-app guard in the osascript (`ABORT` if Chrome for Testing is not frontmost) + Escape-first to clear stray Go-To overlays + ask Houston for a quiet window before the Gemini phase.
- First ChatGPT upload after a fresh `goto` fails silently while the page hydrates — retry after 10–12s succeeds (2 occurrences; now always wait ≥12s post-goto before uploading).

## Harvest

Wait ≥30 min from 15:14 PT (Pro Extended + Heavy are slow). Harvest each chat → `EXT4_<paper>_<Provider>.md` → truth-audit → closures → gap metric vs EXT3 (27).
