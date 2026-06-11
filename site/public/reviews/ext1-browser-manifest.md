# EXT1 — External browser-tier review round · chat-link manifest

**Round**: EXT1 (first fully automated web-app-tier external round)
**Submitted**: 2026-06-10, ~15:30–16:05 PDT, via `/external-review-browser-loop` (gstack browse, logged-in GStack Chromium profile)
**Papers**: all six, current live versions (md5-verified against site mirrors pre-submission)
**Providers/models**: ChatGPT GPT-5.5 **Pro Extended** (slowest, deepest) · Grok **Heavy** (Team of Experts) · Gemini **3.5 Thinking**
**Reuse policy**: for the EXT2 follow-up after revisions, return to these SAME chat URLs and post the revised PDF + delta-prompt in-thread to keep referee context.

## Chat links

| Paper | Version | PDF (md5) | ChatGPT · Pro Extended | Grok · Heavy | Gemini · 3.5 Thinking |
|-------|---------|-----------|------------------------|--------------|------------------------|
| P1A | v1A.0.56 | `paper1a_ech_nogo_v1A.0.56.pdf` (96f18a36) | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e5e8-96cc-83e8-918f-3b1dd3f96d96) | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=5abdb89c-8b7d-4ec0-8839-c39f5a634f03) | [chat](https://gemini.google.com/app/4f6bdc99c91dc1d2) |
| P1B | v1B.0.54 | `paper1b_mcmc_companion_v1B.0.54.pdf` (bd19ee37) | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded) | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=33f977da-4a3e-44b6-a6e4-599ae00d5c3e) | [chat](https://gemini.google.com/app/2ba6d99c84794eb7) |
| P2 | v1.7.48 | `paper2_fnl_forecast_v1.7.48.pdf` (4cb0963e) | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e646-8510-83e8-8999-77b849c6519d) | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=0c4cb7d1-7bc6-4033-a4ac-f4605ec99269) | [chat](https://gemini.google.com/app/c01bc000d0305271) |
| P3 | v3.1.87 | `paper3_anomaly_catalog_v3.1.87.pdf` (acde55ca) | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e669-b608-83e8-9c0c-e7f247ff271a) | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=de56f195-4cae-4dc6-bc3e-f9dbf4de9b54) | [chat](https://gemini.google.com/app/b10514f2f6e2ff2f) |
| P4 | v1.0.171 | `chirality_catalog_paper_v171.pdf` (2f0317c4) | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6c4-0764-83e8-b198-03092b27ba37) | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=411d5219-2864-4196-8d60-da2c97771cc0) | [chat](https://gemini.google.com/app/8340abb820aada09) |
| P5 | v0.1.60 | `p5_desi_chirality_v0.1.60.pdf` (20ffc154) | [chat](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6e9-b9a4-83e8-9624-ec9291ae8064) | [chat](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=edd1963e-cc7e-4a86-b288-1a7834c9e45a) | [chat](https://gemini.google.com/app/3cbe98b65fe83d40) |

All 18 submissions carried the paper page's calibration-armed referee prompt (scraped live from bigbounce.hubify.app per-paper pages) with model/effort verified in the UI before each send (pre-submit screenshots were captured in the session log for each send).

## Harvest status

| Paper | ChatGPT Pro Extended | Grok Heavy | Gemini 3.5 Thinking |
|-------|----------------------|------------|----------------------|
| P1A | HARVESTED — **REJECT** | HARVESTED — MAJOR | HARVESTED — MAJOR |
| P1B | HARVESTED — MAJOR | HARVESTED — MINOR | HARVESTED — MINOR |
| P2 | HARVESTED — MAJOR | HARVESTED — MINOR | HARVESTED — MINOR |
| P3 | HARVESTED — MAJOR | HARVESTED — MAJOR | HARVESTED — MAJOR |
| P4 | HARVESTED — MAJOR | HARVESTED — MINOR | HARVESTED — MINOR |
| P5 | HARVESTED — MAJOR | HARVESTED — MINOR | HARVESTED — MAJOR |

All 18 reports harvested 2026-06-10 16:40–17:25 PDT → `EXT1_<paper>_<Provider>.md` (this directory). Next: `/peer-review-truth-audit`.

**Operational note (encoded in skill)**: Gemini discards a conversation if you navigate away before its first response completes — the original P1A–P4 Gemini chats were lost and resubmitted sequentially (URLs above are the persisted resubmissions). ChatGPT/Grok persist immediately.
