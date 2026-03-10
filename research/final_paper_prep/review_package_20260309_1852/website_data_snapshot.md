# Website & Data Snapshot — BigBounce

**Generated:** 2026-03-09
**Site:** Netlify deployment (netlify.toml configured)

---

## PDF Downloads

| File | Path | Size | Date | Status |
|------|------|------|------|--------|
| Paper PDF | public/downloads/golden-2026-geometric-dark-energy-spin-torsion.pdf | 1.69 MB | Mar 4 | v1.2.0, current |
| arXiv source | arxiv/main.pdf | 1.69 MB | Mar 4 | Identical to above |

**Issue:** No `bigbounce_latest.pdf` symlink/copy exists. The public download uses the full filename.

## Dataset Catalog

**File:** public/data/dataset_catalog.json
**Version:** 1.0.0 (generated 2026-03-06)
**Total datasets:** 32 (4 raw_public, 6 derived_public, 3 reconstructed, 19 internal_summary)

**Galaxy spin entries:**
- `galaxy_spin_bins` — marked DEPRECATED (downloadable: false) ✓
- `galaxy_zoo_decals_spins` — new entry (derived_public, reproducible) ✓
- `galaxy_spin_counts_wp5` — aggregate Shamir counts (paper: "both") ✓

**Issue:** The deprecated entry is correctly flagged but still present in the JSON. This is fine for transparency.

## Website Pages (16 HTML files)

| Page | Status | Notes |
|------|--------|-------|
| index.html | Current | Home page, v1.2.0 references |
| paper.html | Current | Full paper presentation, synced Mar 4 |
| datasets.html | Current | Data explorer, references catalog JSON |
| methodology.html | Current | Methods documentation |
| versions.html | Current | Shows 13 versions through v1.2.0 |
| interactive-data.html | Current | Chart.js visualizations |
| galaxy-zoo.html | Current | Galaxy Zoo DECaLS interface |
| mathematics.html | Current | Mathematical content |
| sources.html | Current | Bibliography |
| explained.html | Current | Summary page |
| animations.html | Current | SVG/Canvas visualizations |
| bigbounce-md.html | Current | Markdown version |

## Deprecated File Exposure Check

| Item | Exposed Publicly? | Status |
|------|-------------------|--------|
| galaxy_spin_data.csv (old) | NO — file renamed to _DEPRECATED | ✓ Safe |
| galaxy_spin_bins_example.csv (old) | NO — renamed to _DEPRECATED | ✓ Safe |
| galaxy_zoo_decals_spins.csv (new) | YES — at data/public_mirror/ | ✓ Correct |
| galaxy_spin_counts.csv (Shamir) | YES — at research/paper2/wp5_.../data/ | ✓ Correct |

## Galaxy Spin Provenance on Website

**Issue:** The website HTML (paper.html) was last synced with the v1.2.0 paper text on March 4. The galaxy spin provenance updates (aggregate CW/CCW counts from Shamir, Galaxy Zoo DECaLS build script) are in the uncommitted tex changes but have NOT been synced to the website HTML yet.

**Impact:** Minor — the website still references the v1.2.0 wording. The structural framing ("contested anomaly") is the same. Only the specific data source description differs slightly.

**Action needed:** Sync paper.html with the updated galaxy spin wording after the next PDF compile.

## ΔNeff Viability Figure

**File:** public/images/dneff_viability.png (230.7 KB)
**Exposed on website:** YES — accessible via public/images/ path
**Embedded in paper:** NO — not in main.tex \includegraphics (this is a supplementary figure)
**Also at:** paper/figures/fig_dneff_viability.pdf (69.6 KB, PDF version)

## Spreadsheet Data Files

5 Excel files in public/downloads/ (figure data for figures 2, 3a, 3b, 6, 7)
7 Excel files in public/spreadsheets/ (complete data for figures 1-3, 6-7)
All current and matching v1.2.0 paper figures.

## Stale/Inconsistent Items

1. **Website galaxy spin wording** — not yet synced with uncommitted tex changes (minor)
2. **version.json** shows v1.2.0 (2026-03-04) — correct for current release
3. **No latest.pdf alias** — only the full filename exists in downloads
4. **paper2-p7-cnn pod** is running on RunPod but idle (0% util) — cost waste, not a website issue
5. **Figure 7 and 8** exist in public/images/ but are not embedded in main.tex — intentional?

## Recommendation

The website and public data are clean and consistent with v1.2.0. The only sync needed is:
1. Update paper.html with galaxy spin provenance wording after next compile
2. Copy recompiled PDF to public/downloads/
3. Consider adding a `bigbounce_latest.pdf` copy for easy linking
