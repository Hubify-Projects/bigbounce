#!/usr/bin/env python3
"""
Unified Literature Search Pipeline

Searches across NASA ADS, Semantic Scholar, arXiv, and Perplexity
with a single interface.

Usage:
    from research.agents.literature_search import search, search_ads, search_arxiv
    results = search("cosmic birefringence Planck 2024")
    ads_results = search_ads("spin-torsion dark energy", rows=20)
"""

import os
import json
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Optional

from . import OUTPUT_DIR


# ── NASA ADS ──────────────────────────────────────────────────────────

ADS_BASE = "https://api.adsabs.harvard.edu/v1"

def search_ads(query: str, rows: int = 10, sort: str = "date desc",
               year_range: Optional[str] = None,
               fields: str = "title,author,year,bibcode,abstract,citation_count,doi") -> list[dict]:
    """
    Search NASA ADS.

    Args:
        query: ADS query string (supports full ADS query syntax)
        rows: Number of results
        sort: Sort order (e.g., "date desc", "citation_count desc")
        year_range: Optional year filter (e.g., "2024-2026")
        fields: Comma-separated fields to return
    """
    key = os.environ.get("NASA_ADS_API_KEY", "")
    if not key:
        raise ValueError("NASA_ADS_API_KEY not set")

    q = query
    if year_range:
        q += f" year:{year_range}"

    params = urllib.parse.urlencode({
        "q": q, "rows": rows, "sort": sort, "fl": fields,
    })
    req = urllib.request.Request(
        f"{ADS_BASE}/search/query?{params}",
        headers={"Authorization": f"Bearer {key}"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())

    return data.get("response", {}).get("docs", [])


def ads_citations(bibcode: str, rows: int = 50) -> list[dict]:
    """Get papers that cite a given paper."""
    return search_ads(f"citations(bibcode:{bibcode})", rows=rows,
                      sort="citation_count desc")


def ads_references(bibcode: str, rows: int = 50) -> list[dict]:
    """Get papers referenced by a given paper."""
    return search_ads(f"references(bibcode:{bibcode})", rows=rows,
                      sort="date desc")


# ── Semantic Scholar ──────────────────────────────────────────────────

S2_BASE = "https://api.semanticscholar.org/graph/v1"

def search_s2(query: str, limit: int = 10,
              fields: str = "title,authors,year,abstract,citationCount,url,externalIds") -> list[dict]:
    """
    Search Semantic Scholar.

    Args:
        query: Search query
        limit: Number of results (max 100)
        fields: Comma-separated fields
    """
    key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
    headers = {"Content-Type": "application/json"}
    if key:
        headers["x-api-key"] = key

    params = urllib.parse.urlencode({
        "query": query, "limit": limit, "fields": fields,
    })
    req = urllib.request.Request(f"{S2_BASE}/paper/search?{params}", headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())

    return data.get("data", [])


def s2_paper(paper_id: str,
             fields: str = "title,authors,year,abstract,citationCount,references,citations") -> dict:
    """
    Get detailed info for a single paper.
    paper_id can be: S2 ID, DOI, arXiv ID, etc.
    """
    key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
    headers = {}
    if key:
        headers["x-api-key"] = key

    params = urllib.parse.urlencode({"fields": fields})
    req = urllib.request.Request(f"{S2_BASE}/paper/{paper_id}?{params}", headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def s2_citation_graph(paper_id: str, depth: int = 1) -> dict:
    """Get citation graph (citations + references) for a paper."""
    paper = s2_paper(paper_id, fields="title,year,citations.title,citations.year,references.title,references.year")
    return {
        "paper": {"title": paper.get("title"), "year": paper.get("year")},
        "citations": paper.get("citations", [])[:50],
        "references": paper.get("references", [])[:50],
    }


# ── arXiv ─────────────────────────────────────────────────────────────

ARXIV_BASE = "http://export.arxiv.org/api/query"

def search_arxiv(query: str, max_results: int = 10,
                 sort_by: str = "submittedDate",
                 category: Optional[str] = None) -> list[dict]:
    """
    Search arXiv.

    Args:
        query: Search query
        max_results: Number of results
        sort_by: submittedDate, lastUpdatedDate, or relevance
        category: Optional arXiv category filter (e.g., "gr-qc", "astro-ph.CO")
    """
    search = query
    if category:
        search = f"cat:{category} AND all:{query}"
    else:
        search = f"all:{query}"

    params = urllib.parse.urlencode({
        "search_query": search,
        "max_results": max_results,
        "sortBy": sort_by,
        "sortOrder": "descending",
    })
    req = urllib.request.Request(f"{ARXIV_BASE}?{params}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        xml_data = resp.read()

    root = ET.fromstring(xml_data)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    results = []
    for entry in root.findall("atom:entry", ns):
        title = entry.find("atom:title", ns)
        summary = entry.find("atom:summary", ns)
        published = entry.find("atom:published", ns)
        arxiv_id = entry.find("atom:id", ns)
        authors = entry.findall("atom:author/atom:name", ns)
        categories = entry.findall("{http://arxiv.org/schemas/atom}primary_category")

        results.append({
            "title": title.text.strip() if title is not None else "",
            "abstract": summary.text.strip() if summary is not None else "",
            "published": published.text if published is not None else "",
            "arxiv_id": arxiv_id.text.split("/abs/")[-1] if arxiv_id is not None else "",
            "authors": [a.text for a in authors],
            "category": categories[0].get("term", "") if categories else "",
            "url": arxiv_id.text if arxiv_id is not None else "",
        })
    # arXiv rate limit: 1 request per 3 seconds
    time.sleep(3)
    return results


# ── Perplexity (web-grounded search) ─────────────────────────────────

def search_perplexity(query: str, model: str = "sonar-pro") -> dict:
    """
    Ask Perplexity for a web-grounded research answer.
    Returns synthesized answer with citations.
    """
    import requests as req

    key = os.environ.get("PERPLEXITY_API_KEY", "")
    if not key:
        raise ValueError("PERPLEXITY_API_KEY not set")

    resp = req.post(
        "https://api.perplexity.ai/chat/completions",
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a scientific research assistant. Provide precise, citation-backed answers about astrophysics, cosmology, and mathematical physics. Always cite specific papers by author and year."},
                {"role": "user", "content": query},
            ],
            "max_tokens": 2048,
            "temperature": 0.1,
        },
        timeout=60,
    )
    resp.raise_for_status()
    data = resp.json()
    return {
        "content": data["choices"][0]["message"]["content"],
        "model": data.get("model", model),
        "citations": data.get("citations", []),
    }


# ── Unified Search ───────────────────────────────────────────────────

def search(query: str, sources: list[str] = None,
           max_results: int = 5, category: Optional[str] = None) -> dict:
    """
    Unified search across all configured sources.

    Args:
        query: Search query
        sources: List of sources to search (ads, s2, arxiv, perplexity).
                 Default: all configured.
        max_results: Results per source
        category: arXiv category filter

    Returns:
        Dict with results keyed by source name
    """
    if sources is None:
        sources = ["ads", "arxiv"]
        if os.environ.get("SEMANTIC_SCHOLAR_API_KEY"):
            sources.append("s2")
        if os.environ.get("PERPLEXITY_API_KEY"):
            sources.append("perplexity")

    results = {}
    for src in sources:
        try:
            if src == "ads":
                results["ads"] = search_ads(query, rows=max_results)
            elif src == "s2":
                results["s2"] = search_s2(query, limit=max_results)
            elif src == "arxiv":
                results["arxiv"] = search_arxiv(query, max_results=max_results,
                                                category=category)
            elif src == "perplexity":
                results["perplexity"] = search_perplexity(query)
        except Exception as e:
            results[src] = {"error": str(e)}

    return results


def save_results(results: dict, filename: str = None) -> str:
    """Save search results to JSON file in outputs directory."""
    if filename is None:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"search_{ts}.json"
    path = OUTPUT_DIR / filename
    with open(path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    return str(path)


if __name__ == "__main__":
    print("Testing unified literature search...\n")
    r = search("spin-torsion cosmology dark energy", max_results=3,
               category="gr-qc")
    for src, data in r.items():
        if isinstance(data, dict) and "error" in data:
            print(f"  [{src}] ERROR: {data['error']}")
        elif isinstance(data, list):
            print(f"  [{src}] {len(data)} results")
            for p in data[:2]:
                title = p.get("title", ["Unknown"])
                if isinstance(title, list):
                    title = title[0]
                print(f"    - {title[:80]}")
        else:
            print(f"  [{src}] response received")
    path = save_results(r)
    print(f"\nResults saved to {path}")
