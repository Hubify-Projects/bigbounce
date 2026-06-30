# RREXT Round — DE-BIASED External Browser Sweep Manifest

Round: RREXT (post-restructure, de-biased prompt)
Date: 2026-06-30
Sweep completed: 2026-06-30
Tiers: ChatGPT default, Grok Expert, Gemini Thinking/Ultra
PDF source: /tmp/RREXT_*.pdf
Browser: GStack headed Chromium (Houston's logged-in session, u/1/ for Gemini)

## PDF md5s (at staging)

| Paper | File | md5 |
|-------|------|-----|
| P5 | RREXT_P5.pdf | f4c7a0f6212613cd6262bc03638f8f53 |
| P4 | RREXT_P4.pdf | b585cc9c3021e03a8293c3f6fe2ed490 |
| P1B | RREXT_P1B.pdf | d8a9529453687fa3b38dc5f414ba7e5d |
| P2 | RREXT_P2.pdf | db185208c6a455f5708f7b7eb75516c2 |
| P1A | RREXT_P1A.pdf | 275936446f099b242824a27f6ee25373 |
| P3 | RREXT_P3.pdf | e83a4a6668e5c9ff324205267f8c46b8 |

## RCEXT baselines (for comparison)
| Paper | ChatGPT | Grok | Gemini |
|-------|---------|------|--------|
| P1A | MAJOR | MAJOR | MAJOR |
| P1B | MAJOR | MINOR | MINOR |
| P2 | MAJOR | MAJOR | MINOR |
| P3 | MAJOR | MAJOR | MAJOR |
| P4 | MAJOR | MINOR | MINOR |
| P5 | MAJOR | MINOR | ACCEPT |

## Legs — COMPLETE

| # | Tag | Provider | Tier | Chat URL | PDF | Status | Verdict |
|---|-----|----------|------|----------|-----|--------|---------|
| 1 | P5 | ChatGPT | default | https://chatgpt.com/c/6a443450-a688-83e8-911f-1210c0edf7f8 | RREXT_P5.pdf | DONE | MAJOR REVISIONS |
| 2 | P5 | Grok | Expert | https://grok.com/c/f54393f9-388f-4724-b723-4397f390ff29 | RREXT_P5.pdf | DONE | MINOR REVISIONS |
| 3 | P5 | Gemini | Thinking | https://gemini.google.com/u/1/app/bad564d225d9f723 | RREXT_P5.pdf | DONE | MINOR REVISIONS |
| 4 | P4 | ChatGPT | default | https://chatgpt.com/c/6a4437ea-764c-83e8-beae-8607412fd989 | RREXT_P4.pdf | DONE | MINOR REVISIONS |
| 5 | P4 | Grok | Expert | https://grok.com/c/c4787fe0-d85c-4098-b4f3-1cda0b127629 | RREXT_P4.pdf | DONE | MINOR REVISIONS |
| 6 | P4 | Gemini | Thinking | https://gemini.google.com/u/1/app/62a57c2b5548ac04 | RREXT_P4.pdf | DONE | MINOR REVISIONS |
| 7 | P1B | ChatGPT | default | https://chatgpt.com/c/6a443ad9-a018-83e8-9c95-57502ea78296 | RREXT_P1B.pdf | DONE | MAJOR REVISIONS |
| 8 | P1B | Grok | Expert | https://grok.com/c/6ccfc1bc-196f-42f7-a6d5-5ee002d554bd | RREXT_P1B.pdf | DONE | MINOR REVISIONS |
| 9 | P1B | Gemini | Thinking | https://gemini.google.com/u/1/app/60e78415770e9c3b | RREXT_P1B.pdf | DONE | MINOR REVISIONS |
| 10 | P2 | ChatGPT | default | https://chatgpt.com/c/6a443d3f-ae3c-83e8-9273-423927ae474d | RREXT_P2.pdf | DONE | MINOR REVISIONS |
| 11 | P2 | Grok | Expert | https://grok.com/c/26440300-c5a1-4a32-ac3e-62b7f287c08d | RREXT_P2.pdf | DONE | MINOR REVISIONS |
| 12 | P2 | Gemini | Thinking | https://gemini.google.com/u/1/app/b103ee33183967cc | RREXT_P2.pdf | DONE | MINOR REVISIONS |
| 13 | P1A | ChatGPT | default | https://chatgpt.com/c/6a443ebd-bee0-83e8-b390-9f3057508bd8 | RREXT_P1A.pdf | DONE | MINOR REVISIONS |
| 14 | P1A | Grok | Expert | https://grok.com/c/ed4f04e9-6695-492b-9126-58827f02f68b | RREXT_P1A.pdf | DONE | MAJOR REVISIONS |
| 15 | P1A | Gemini | Thinking | https://gemini.google.com/u/1/app/f452d6c07bd3bd4d | RREXT_P1A.pdf | DONE | MAJOR REVISIONS |
| 16 | P3 | ChatGPT | default | https://chatgpt.com/c/6a44401e-5170-83e8-a758-73fe833f7bfa | RREXT_P3.pdf | DONE | MAJOR REVISIONS |
| 17 | P3 | Grok | Expert | https://grok.com/c/67c41a6e-b9df-4ea8-a4de-3c13f75c71d3 | RREXT_P3.pdf | DONE | MAJOR REVISIONS |
| 18 | P3 | Gemini | Thinking | https://gemini.google.com/u/1/app/8071ea27a7887837 | RREXT_P3.pdf | DONE | MINOR REVISIONS |

## Results matrix

| Paper | ChatGPT (RREXT) | Grok (RREXT) | Gemini (RREXT) | vs RCEXT |
|-------|-----------------|--------------|-----------------|----------|
| P1A | MINOR ↑ | MAJOR = | MAJOR = | 1 improved |
| P1B | MAJOR = | MINOR = | MINOR = | no change |
| P2 | MINOR ↑ | MINOR ↑ | MINOR = | 2 improved |
| P3 | MAJOR = | MAJOR = | MINOR ↑ | 1 improved |
| P4 | MINOR ↑ | MINOR = | MINOR = | 1 improved |
| P5 | MAJOR = | MINOR = | MINOR ↓* | *ACCEPT→MINOR |

## MAJOR count: RCEXT=14 → RREXT=6 (net -8 MAJORs)

Note on P5-Gemini: RCEXT returned ACCEPT; RREXT returns MINOR. Likely attributable
to the stricter de-biased prompt and/or Gemini Thinking vs Flash used in RCEXT.
The paper itself is unchanged on the environmental-null result. The shift is not
a regression in paper quality.
