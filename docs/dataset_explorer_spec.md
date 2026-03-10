# BigBounce Dataset Explorer — Specification

## Overview

A public-facing page on the BigBounce website that provides full transparency into every dataset used in the research. Serves as both a reproducibility tool and an evidence room.

URL: `/datasets.html` or `/evidence-room.html`

## Design Principles

1. **Radical transparency**: Every dataset labeled honestly (raw / derived / reconstructed / summary)
2. **Reproducibility first**: Download links, checksums, citations for everything
3. **Warnings visible**: Reconstructed or contested data flagged prominently
4. **Cross-linked**: Every dataset linked to the figures, tables, and scripts that use it

## Page Structure

### Header
- Title: "Datasets & Reproducibility"
- Subtitle: "Every dataset used in this research, with full provenance"
- Total dataset count badge
- Breakdown badges: X raw, Y derived, Z reconstructed, W summary

### Searchable Dataset Table
Interactive table (using DataTables.js or similar) with columns:
- Dataset ID (clickable, opens detail panel)
- Name
- Status tag (color-coded: green=raw_public, blue=derived, orange=reconstructed, gray=summary)
- Paper section
- Figures using it
- Row count
- Download button (or "N/A" for non-downloadable)

Filters:
- By status (raw / derived / reconstructed / summary)
- By paper (Paper 1 / Paper 2)
- By figure
- Free text search

### Per-Dataset Detail Panel

When a dataset row is clicked, expand to show:

#### Metadata
- Full name and description
- Status badge with explanation
- Original source URL (clickable)
- Citation (formatted, with BibTeX copy button)
- License
- SHA256 checksum
- File size / row count / column count

#### Data Preview
- First 10 rows rendered as an HTML table
- Column names with types
- For very large datasets: "Showing 10 of N rows"

#### Provenance
- How the data was obtained
- Any transforms applied
- Whether a third party can reproduce it
- Warnings (orange boxes) for reconstructed or contested data

#### Cross-Links
- Figures that use this dataset (thumbnail + link)
- Tables that use this dataset
- Scripts that process this dataset (link to repo)
- Paper section reference

#### Download
- Direct download button (for files < 50 MB in repo)
- Download command (for large external datasets)
- "Not available" with explanation (for internal-only data)

### Warning Banners

For any dataset with status `reconstructed`:
```
This dataset was reconstructed from published figures/tables,
not from a machine-readable data release. Small differences from
the original are possible. See provenance notes for details.
```

For any dataset with contested results:
```
The observational signal in this dataset is contested.
Independent reanalyses have found results consistent with null.
See the paper's discussion in Section X for details.
```

### Reproducibility Checklist Section

At the bottom of the page, a checklist:
- [ ] All MCMC chains reproducible via Cobaya YAML configs
- [ ] All parameter scans reproducible via Python scripts
- [ ] All figure data available as CSV
- [ ] All citations verified
- [ ] Checksums provided for all downloadable files
- Status of each item (with links)

## Data Format

The explorer is powered by a single JSON file:

### `public/data/dataset_catalog.json`

```json
{
  "version": "1.0.0",
  "generated_at": "2026-03-06",
  "datasets": [
    {
      "id": "string — unique identifier",
      "name": "string — human-readable name",
      "description": "string — one paragraph",
      "status": "raw_public | derived_public | reconstructed | internal_summary",
      "status_label": "string — human-readable status",
      "paper": "paper1 | paper2 | both",
      "sections": ["string — paper section references"],
      "figures": ["string — figure identifiers"],
      "scripts": ["string — script paths"],
      "file": {
        "path": "string — path relative to repo root",
        "name": "string — filename",
        "type": "string — csv, xlsx, json, fits, etc.",
        "size_bytes": "number",
        "size_human": "string — e.g. '1.3 KB'",
        "row_count": "number | null",
        "columns": ["string — column names"],
        "checksum_sha256": "string | null",
        "downloadable": "boolean",
        "download_url": "string | null"
      },
      "provenance": {
        "source_url": "string | null",
        "citation_key": "string — BibTeX key",
        "citation_text": "string — formatted citation",
        "license": "string",
        "method": "string — how data was obtained",
        "reproducible_by_third_party": "boolean",
        "transforms": "string | null — any processing applied"
      },
      "warnings": [
        {
          "level": "info | caution | critical",
          "message": "string"
        }
      ],
      "preview": [
        {"col1": "val1", "col2": "val2"}
      ],
      "tags": ["string"]
    }
  ]
}
```

## Implementation Notes

### Technology
- Static HTML page (consistent with existing site)
- JavaScript for filtering/search (vanilla JS or lightweight library)
- No build step required
- MathJax for any LaTeX in descriptions
- Responsive design matching existing site style

### Data Loading
- Load `dataset_catalog.json` via fetch() on page load
- Render table dynamically
- Detail panels expand in-place (accordion style)

### File Hosting
- Small CSV/JSON files served directly from `public/data/`
- Large files: provide external URLs only
- MCMC chains: provide download instructions post-convergence

### Security
- Same password protection as main site (session storage, password "houston")
- No server-side data processing

## Content Source

All data populated from `research/data_audit/master_dataset_inventory.csv` via a build script that converts the CSV to the JSON format described above.
