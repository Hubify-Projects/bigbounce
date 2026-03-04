# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a scientific research paper titled "Geometric Dark Energy from Spin-Torsion Cosmology: Phenomenological Constraints and Correlated Signatures" by Houston Golden. The project is a theoretical physics paper exploring dark energy through quantum gravitational effects in spin-torsion cosmology.

**Current version: v1.0.0** (March 4, 2026) — 31 pages, 51 bibliography entries, 6 revision rounds complete.
All HTML pages synced. PDF compiled with 0 undefined references.

## Repository Structure

- `bigbounce.md` - Complete research paper content in Markdown format (~35,000 words)
- `index.html` - Interactive web presentation of the research paper with password protection
- `paper/` - Individual sections of the paper organized as separate Markdown files:
  - `00-abstract.md` through `11-acknowledgments.md`
  - `metadata.md` - Paper metadata
- `public/images/` - Scientific figures and illustrations (PNG format, Git LFS tracked)
- `public/spreadsheets/` - Supporting data tables (Excel format)
- `interactive-data.html` & `interactive-data-simple.html` - Interactive data visualizations using Chart.js
- `server.js` - Express server for local development

## Commands

### Local Development
```bash
# Install dependencies (only Express is required)
npm install

# Run local server
node server.js
# Server runs at http://localhost:3000

# Alternative: Use any static file server
python -m http.server 8000
# Or simply open index.html directly in a browser
```

### Deployment
- Configured for Netlify deployment via `netlify.toml`
- No build step required - purely static site
- Security headers and caching rules are configured in `netlify.toml`

## Development Environment

This is primarily a static website project. The main deliverable is `index.html` which presents the research paper in an interactive web format.

### Key Features of the Web Interface

- **Password Protection**: Uses session storage with password "houston"
- **Interactive Table of Contents**: Sidebar navigation with smooth scrolling
- **MathJax Integration**: Renders LaTeX mathematical expressions
- **Lightbox Image Viewer**: Click images to view in full screen
- **Responsive Design**: Mobile-friendly layout
- **Scientific Styling**: Academic paper formatting
- **Interactive Data Visualizations**: Separate pages for exploring research data with Chart.js

### Project Dependencies

- **Express.js**: Only for optional local development server
- **MathJax**: Loaded from CDN for mathematical rendering
- **Chart.js**: Loaded from CDN for data visualizations
- No build tools or preprocessors required

## Content Organization

The paper is structured as a comprehensive theoretical physics research paper with:
- Mathematical derivations using LaTeX notation
- Scientific figures with detailed captions
- Extensive references to academic literature
- Systematic analysis and observational predictions
- Timeline for experimental validation

## Working with the Content

When editing the paper content:
- Mathematical expressions use LaTeX syntax within `$$` or `$` delimiters
- Figures are referenced as `public/images/figure_name.png`
- The HTML version in `index.html` should be kept in sync with `bigbounce.md`
- Maintain academic writing style and scientific rigor
- Images are tracked with Git LFS - ensure Git LFS is installed when cloning

## Image Management

- GitHub image URLs are documented in `github-image-mappings.md` and `image-urls.md`
- Local images in `public/images/` are the primary source
- Images use descriptive naming: `figure[number]_[description].png`

## Peer Review & Revision Workflow

**CRITICAL: All peer reviews, audits, and revision requests MUST be saved to `project-context/peer-reviews/`.**

### File Naming Convention
```
YYYY-MM-DD_HHMMtz_description.md
```
Example: `2026-03-02_1917PST_comprehensive-audit.md`

### What to Save
- Full peer review text (every audit, every round)
- Claims tables (Derived vs Assumed vs Fit)
- Revision plans with prioritized issue lists
- Editor prompts / coauthor instructions
- Verification results after each revision round

### Tracking Revisions
- `project-context/peer-reviews/REVISION_TRACKER.md` tracks all issues across rounds
- Update issue status as revisions are completed
- After each revision round:
  1. Recompile PDF and verify 0 undefined references
  2. Run dimensional consistency checks
  3. Grep for removed language patterns
  4. Verify claims table against revised text
  5. Sync website if applicable
  6. Update REVISION_TRACKER.md

### Canonical Source of Truth
- `arxiv/main.tex` is the canonical source — everything else mirrors it
- `version.json` at repo root tracks current version
- `versions/manifest.json` tracks version history

### Version History
- Tracked in `versions/manifest.json` with detailed changelogs
- Displayed on `versions.html` page of the website
- Each major revision should increment the version

## Contact Information

Author: Houston Golden
Email: houston@hubify.com