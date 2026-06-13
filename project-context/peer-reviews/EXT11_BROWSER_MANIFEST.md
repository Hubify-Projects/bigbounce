# EXT11 Browser Submission Manifest

**Round:** EXT11  
**Goal:** Verify EXT10-closure-wave closures cleared all MINOR items → 18/18 ACCEPT  
**EXT10-closure SHA:** 0c72a942  
**Submitted:** 2026-06-13 ~16:07–16:47 PDT  
**Harvest ETA:** ≥30 min from last submission = 17:17 PDT or later  

---

## Site-Deploy Status

- Site returned HTTP 200 at submission time: `https://bigbounce.hubify.app/papers/paper-1a`
- Live site version checking skipped (fallback to local mirrors per protocol)
- Per skill protocol: used local `site/public/` mirror PDFs with matching md5s (except P3: used pipeline PDF which is v3.1.107)

## PDF Verification (Phase 1)

| Paper | File | md5 (full) | Expected (prefix 8) | Match |
|-------|------|-----------|---------------------|-------|
| P1A | paper1a_ech_nogo_v1A.0.73_26a40893.pdf | 26a40893df655ad5e2b1cd1e427a76d0 | 26a40893 | ✅ |
| P1B | paper1b_mcmc_companion_v1B.0.70_03c33444.pdf | 03c334443eaf3d4d4399eed37cb09940 | 03c33444 | ✅ |
| P2 | paper2_fnl_forecast_v1.7.64_ab99c187.pdf | ab99c18721eecc579b7fb6562ea1b51c | ab99c187 | ✅ |
| P3 | paper3_anomaly_catalog_v3.1.107_17c9296b.pdf | 17c9296bcf668c73dea0f19c79032fa9 | 17c9296b | ✅ (from pipelines/p3_anomaly_engine/paper3_draft.pdf — site/public was stale v3.1.106/d1258558) |
| P4 | chirality_catalog_paper_v1.0.187_1ed10d38.pdf | 1ed10d380d7b678acbb182f38dead0f0 | 1ed10d38 | ✅ |
| P5 | p5_desi_chirality_v0.1.76-2026-06-13_5af39737.pdf | 5af39737a462f22edb16808184f8c47c | 5af39737 | ✅ |

Staged at: `/private/tmp/bigbounce-ext-review/EXT11/`

**P3 note:** `site/public/paper3_anomaly_catalog.pdf` = d1258558 (v3.1.106 stale). Correct v3.1.107 PDF found at `pipelines/p3_anomaly_engine/paper3_draft.pdf` (md5 verified).

---

## Submission Log (Phase 2)

### ChatGPT — Big Bounce Book Project (`/g/g-p-6881c7f354808191a36860ff4d29fa69`)
Model/effort: **Pro Extended** (verified in bottom bar screenshots)
Protocol: delta-prompt + new PDF uploaded to EXISTING EXT10 chat URLs (same-chat in-thread)

| Paper | PDF md5 (prefix) | Chat URL (SAME as EXT10) | Submitted (PDT) | Harvest | Verdict |
|-------|---------|----------|-----------------|---------|---------|
| P1A | 26a40893 | [link](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc597-d61c-83e8-ac93-8f3bf7f139fb) | ~16:14 | TBD | TBD |
| P1B | 03c33444 | [link](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc5cf-db00-83e8-b824-21b626a0d9ab) | ~16:16 | TBD | TBD |
| P2 | ab99c187 | [link](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc5f2-5e8c-83e8-9318-b7aefa847ee0) | ~16:18 | TBD | TBD |
| P3 | 17c9296b | [link](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc617-2480-83e8-bf48-cc78a7bce891) | ~16:20 | TBD | TBD |
| P4 | 1ed10d38 | [link](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc65e-2488-83e8-90f8-fcacbf9d4378) | ~16:22 | TBD | TBD |
| P5 | 5af39737 | [link](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc684-5918-83e8-b53e-28fde5fca69a) | ~16:24 | TBD | TBD |

### Grok — BigBounce-Papers Project (`/project/e6c9ce77-4f86-4d94-b440-1062a78171c1`)
Model/effort: **Heavy** (Team of Experts, confirmed in bottom bar)
Protocol: delta-prompt + new PDF uploaded to EXISTING EXT10 chat URLs

| Paper | PDF md5 (prefix) | Chat URL (SAME as EXT10) | Submitted (PDT) | Harvest | Verdict |
|-------|---------|----------|-----------------|---------|---------|
| P1A | 26a40893 | [link](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=7f12a3a9-339f-4a0d-a258-3d7224b02a7e) | ~16:27 | TBD | TBD |
| P1B | 03c33444 | [link](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=6fede933-742f-423b-b1d8-bbbf7254d6c1) | ~16:29 | TBD | TBD |
| P2 | ab99c187 | [link](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=1d8e1fbc-6a0e-4917-b1a5-cf389b307141) | ~16:30 | TBD | TBD |
| P3 | 17c9296b | [link](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=df8b502c-8c32-408f-9509-82be147fccbe) | ~16:31 | TBD | TBD |
| P4 | 1ed10d38 | [link](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=9b06db9f-adeb-4928-8b88-8b17655b095d) | ~16:32 | TBD | TBD |
| P5 | 5af39737 | [link](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=52437983-41f2-4016-ac45-ad392572ce46) | ~16:34 | TBD | TBD |

### Gemini — `gemini.google.com/u/0/` (Houston Golden · Work · Ultra account)
Model/effort: **Thinking** (Solves complex problems = 2.5 Thinking, confirmed in mode picker)
Account: `/u/0/` confirmed correct (showed "What's next, Houston?" / "Work · Ultra" avatar)
Protocol: Per EXT7 lesson — fresh home page per submission; wait for growth-based confirmation (> BASE+2500) before navigating away; file input discovered via `input[type=file]` after clicking Upload & tools → Upload files
Note: EXT10 chat URLs CANNOT be reused for Gemini (Gemini backend silently drops uploads on existing chats per EXT7 lesson). NEW chat URLs minted each submission.

| Paper | PDF md5 (prefix) | NEW Chat URL (fresh submit) | Submitted (PDT) | Growth-confirmed | Harvest | Verdict |
|-------|---------|----------|-----------------|-----------------|---------|---------|
| P1A | 26a40893 | [link](https://gemini.google.com/u/0/app/56233246092d5209) | ~16:35 | ✅ 24971→28337 (stable) | TBD | TBD |
| P1B | 03c33444 | [link](https://gemini.google.com/u/0/app/62749069bd0a5dea) | ~16:38 | ✅ 16972→20266 (stable) | TBD | TBD |
| P2 | ab99c187 | [link](https://gemini.google.com/u/0/app/1ed5eac442bc1b16) | ~16:41 | ✅ 17036→20971 (stable) | TBD | TBD |
| P3 | 17c9296b | [link](https://gemini.google.com/u/0/app/0caba47ff4592563) | ~16:43 | ✅ 16996→22700 (stable) | TBD | TBD |
| P4 | 1ed10d38 | [link](https://gemini.google.com/u/0/app/c5d014470f013c8d) | ~16:44 | ✅ 17029→21154 (stable) | TBD | TBD |
| P5 | 5af39737 | [link](https://gemini.google.com/u/0/app/deaf4b19cfd7127e) | ~16:46 | ✅ 17085→20704 (stable) | TBD | TBD |

**Gemini P2 note:** First attempt at chat `d350fbd30c5bf78f` FAILED (chat not loadable — Gemini persistence bug). Resubmitted from fresh home at ~16:41 → new URL `1ed5eac442bc1b16`. Fresh-chat flag: FRESH-RESUBMIT (1 occurrence).

---

## Summary

| Provider | Submitted | Model/Effort | All 6 growth-confirmed |
|----------|-----------|--------------|------------------------|
| ChatGPT | 6/6 | Pro Extended | ✅ (generating at nav-away; same-thread persists) |
| Grok | 6/6 | Heavy | ✅ (generating at nav-away; same-thread persists) |
| Gemini | 6/6 | 2.5 Thinking (/u/0/) | ✅ (growth-confirmed before nav-away) |
| **Total** | **18/18** | | ✅ |

**Fresh-chat fallback count:** 1 (Gemini P2 — persistence bug on first attempt).  
**No chat refusals. No upload size rejections (P4 33MB accepted by all 3 providers).**  
**No missing chips — all 18 PDF attachments confirmed via DOM/screenshot before send.**

---

## EXT10 vs EXT11 Chat URL Changes

- **ChatGPT:** Same chat URLs as EXT10 (in-thread delta) ✅
- **Grok:** Same chat URLs as EXT10 (in-thread delta) ✅
- **Gemini:** NEW URLs minted (EXT7 lesson — fresh-home required for Gemini uploads)

## Technical Notes (for SKILL.md update)

- **Gemini file input trick**: Gemini DOES have a hidden `input[type=file]` element that appears when the "Upload files" menuitem is clicked. Using `$B upload 'input[type=file]' <path>` immediately after clicking the menuitem works reliably. This is faster and more reliable than the osascript native-dialog approach. The native dialog (osascript) approach failed for us — the file selection didn't register properly.
- **Gemini persistence bug**: Confirmed again — if the Chat URL returned by browser nav (`window.location.href`) is from a failed navigation (`d350fbd30c5bf78f`), that chat is dead/invalid. Growth-based poll starting from BASE before send + verification of `document.body.textContent.includes('EXT11')` confirms real submission.
- **Gemini growth threshold**: Base lengths ~17000 chars; response completion adds ~3000-5500 chars (P3 largest at +5700). Threshold of BASE+2500 is reliable.
- **P3 site/public stale PDF**: `site/public/paper3_anomaly_catalog.pdf` = v3.1.106 (d1258558) NOT v3.1.107 (17c9296b). Correct file lives at `pipelines/p3_anomaly_engine/paper3_draft.pdf`. Site sync required.

---

## Harvest Instructions

Wait until **17:17 PDT or later** (≥30 min from last submission at 16:47).

For each row: open the chat URL, confirm no streaming indicator, copy the complete referee report, save to:
`project-context/peer-reviews/EXT11_<paper>_<Provider>.md`

Header format:
```
# EXT11 Harvest — <Paper> — <Provider>
- Provider: <ChatGPT/Grok/Gemini>
- Model/Effort: <Pro Extended / Heavy / 2.5 Thinking>
- Chat URL: <url>
- PDF md5: <hash>
- Harvested: <PST timestamp>
```

Verify verdict regex hits (ACCEPT|MAJOR|MINOR|REJECT) before saving.

**Gemini P1A early read (captured during submission wait):** "Updated Headline Verdict: MINOR REVISIONS" — still flagging style/wording items per the model's calibration.
