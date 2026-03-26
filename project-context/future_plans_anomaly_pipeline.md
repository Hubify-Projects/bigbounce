# Future Plans: Anomaly Pipeline Enhancement

**Created:** 2026-03-26
**Source:** User brainstorm session during batch processing

---

## Idea 1: Multi-Pass Triage Architecture

**Current state:** Single rule-based pass on 195K anomalies (band ratio classification).

**Proposed architecture:**
```
Pass 1 (DONE): Band ratio classification — fast, rule-based, 195K objects
  ↓
Pass 2 (NEXT): Cross-match enrichment — SIMBAD/NED/AllWISE/Gaia metadata added
  ↓
Pass 3: Morphology from Legacy Survey — PSF/REX/SER/DEV type, colors, magnitudes
  ↓
Pass 4: Redshift estimation — from DESI pipeline z values + quality flags
  ↓
Pass 5: LLM reasoning — Claude/GPT analyzes each object with all Pass 1-4 data + image
  ↓
Pass 6: Pattern discovery — clustering/embedding analysis across the full enriched catalog
```

Each pass adds structured data. By the time we reach Pass 5 (LLM), the model has band ratios + catalog cross-matches + morphology + redshift + image — much richer context than just band ratios alone.

**Could we run Pass 1 on the FULL 18M?**
Yes. The 18M spectra all have band residuals from the autoencoder. We currently threshold at score > 5.0 and only save the 195K anomalies. But we COULD save the band ratios for ALL 18M and classify them — most would be "NORMAL" but the classification itself (which band is dominant, what's the ratio) would create a structured catalog of the entire DESI DR1 that doesn't exist anywhere.

**Is this novel?** Partially. DESI's own pipeline classifies spectra (STAR/GALAXY/QSO) but doesn't produce band-level reconstruction residuals. Our autoencoder adds a different dimension — "how unusual is each part of the spectrum" — which is complementary to the pipeline's template-matching classification.

**Compute:** Re-running the autoencoder on all 18M would take ~6 hours on the H200 again. Saving ALL scores (not just anomalies) would produce a ~2GB catalog. Feasible.

---

## Idea 2: Super-Resolution Image Enhancement for DESI Anomalies

**The vision:** Take the tiny, blurry Legacy Survey cutouts of our 195K anomalies and upscale them to show "never-before-seen objects at the highest resolution they've ever been observed."

**Honest assessment:**

### What's physically possible
- Legacy Survey images are ground-based (~1 arcsec seeing). These are NOT blurry because they're far away — they're blurry because Earth's atmosphere limits resolution.
- HST/JWST achieve ~0.05-0.1 arcsec resolution. Space-based images of the SAME objects would be 10-20x sharper.
- AI super-resolution CAN learn the mapping from ground-based → space-based IF trained on paired data.

### Training data strategy (the user's idea is sound)
1. **Find objects observed by BOTH ground-based surveys AND HST/JWST**
   - HST COSMOS field: ~2 deg² with deep HST imaging + ground-based coverage
   - JWST CEERS/JADES fields: deep NIR imaging + Legacy Survey overlap
   - ~100K paired images may exist
2. **Create training pairs:**
   - Input: Legacy Survey cutout (ground-based, ~1 arcsec, ~64x64 pixels)
   - Output: HST/JWST cutout (space-based, ~0.05 arcsec, ~256x256 or higher)
3. **Train super-resolution model** (ESRGAN, Real-ESRGAN, or diffusion-based)
4. **Apply to our 195K anomalies** — generate enhanced images

### What exists already
- **GalaxyGAN / DeepMerge** — ML models for galaxy image enhancement (but not trained on ground→space pairs at scale)
- **Real-ESRGAN** — general super-resolution that works ok on astronomical images but isn't physics-aware
- **Scarlet** (Melchior+ 2018) — model-based deblending, not ML super-resolution
- No published model specifically trained on Legacy Survey → HST/JWST paired data at scale

### What would be genuinely novel
- A **physics-aware super-resolution model trained specifically on astronomical survey data** with paired ground/space observations
- Applied at scale to 195K objects, producing a **super-resolved anomaly catalog**
- The combination of "AI-discovered anomalies" + "AI-enhanced images" would be visually compelling AND scientifically useful (morphology classification is easier on sharper images)

### Caveats
- **Super-resolution CANNOT create information that isn't there.** It can sharpen features the model learned from training data, but it can genuinely hallucinate features that don't exist.
- For science claims, the original resolution images remain authoritative. Enhanced images are for visualization and preliminary morphology, not for measurement.
- This is a separate paper/project from the anomaly catalog itself.

### Compute
- Training: ~2-4 days on H100/H200 with ~100K paired images
- Inference: ~1 hour for 195K cutouts on GPU
- Storage: ~50GB for 195K enhanced images at 256x256

### Potential training datasets
- HST COSMOS (Koekemoer+ 2007): ~2M objects with HST ACS imaging
- JWST CEERS (Finkelstein+ 2023): ~100K objects with NIRCam + Legacy Survey overlap
- JWST JADES (Eisenstein+ 2023): deep field with broad wavelength coverage
- Hyper Suprime-Cam (HSC) SSP: 0.6 arcsec seeing (intermediate between Legacy and HST)

---

## Idea 3: Full 18M Structured Catalog

**What:** Run the band-ratio classification on ALL 18M DESI spectra, not just the 195K anomalies.

**Output:** A catalog with columns: TARGETID, RA, DEC, anomaly_score, rB, rR, rZ, worst_band, classification, discovery_potential — for every single DESI DR1 spectrum.

**Novel?** Yes. DESI publishes spectral classifications (STAR/GALAXY/QSO) but not autoencoder reconstruction residuals. Our catalog adds a complementary axis: "how well does this spectrum fit ANY known template?"

**Use case:**
- Community resource — anyone can filter for unusual objects in their region of interest
- Pattern discovery — are anomalies clustered spatially? By redshift? By observation conditions?
- Systematic hunting — find objects that are "slightly unusual" (score 3-5) but interesting in aggregate

**Compute:** The autoencoder already ran on all 18M. We just need to save the full output, not just the score > 5.0 threshold. Would need to re-run (or check if the H200 pod still has the full results cached in temp files).

---

## Idea 4: LLM-Powered Deep Analysis of Top Objects

**What:** Use Claude/GPT-4o to analyze each of the top ~1,000 anomalies with the full context: band residuals + Legacy Survey image + cross-match results + DESI pipeline metadata.

**Prompt structure:**
```
You are an expert astronomer analyzing an unusual DESI DR1 spectrum.

Object: TID {tid}, RA={ra}, Dec={dec}
Anomaly score: {score} (top {rank} of 195,829)
Band residuals: B={rB}, R={rR}, Z={rZ}
Worst band: {worst}
Legacy Survey morphology: {type}
SIMBAD match: {simbad_result}
NED match: {ned_result}
AllWISE match: {allwise_result}

[Legacy Survey cutout image attached]

Analyze this object:
1. What is the most likely astrophysical explanation?
2. What makes the spectrum anomalous in the {worst} band?
3. Could this be a previously undiscovered object class?
4. What follow-up observations would confirm its nature?
5. Rate discovery potential: LOW/MEDIUM/HIGH/VERY_HIGH
```

**Novel?** The LLM analysis itself isn't novel (anyone can prompt Claude about astronomy). What would be novel is doing it AT SCALE on a systematically constructed anomaly catalog with structured multi-source data.

**Compute:** ~$5-20 for top 1,000 via API. Not expensive.

---

## Priority Order

1. **Pass 2 (cross-match enrichment)** — already running (SIMBAD/NED 10K)
2. **Document multi-pass methodology** on the website
3. **Pass 3 (morphology)** — query Legacy Survey catalog for each anomaly
4. **LLM deep analysis of top 100** — highest scientific value per object
5. **Full 18M catalog** — check if H200 pod has cached results
6. **Super-resolution** — separate project, needs training data curation first

---

## Key Phrases to Remember

The user's vision: "show never before observed objects for the first time and show objects at this distance in the highest resolution clearest they've ever been seen before"

This is the marketing angle for the super-resolution work. Scientifically it's "AI-enhanced imaging of AI-discovered spectral anomalies from the largest spectroscopic survey ever conducted."
