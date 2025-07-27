import argparse
import requests
import xml.etree.ElementTree as ET
import pandas as pd

def fetch_papers(query):
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

    headers = {
        "User-Agent": "JesvinPubMedFetcher/1.0 (mailto:jesvinblaze@gmail.com)",
        "Accept": "application/json"
    }

    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10,
        "tool": "JesvinPubMedFetcher",
        "email": "jesvinblaze@gmail.com"
    }

    try:
        response = requests.get(search_url, params=search_params, headers=headers, timeout=10)
        print("[DEBUG] Status:", response.status_code)
        print("[DEBUG] First 300 chars:", response.text[:300])
        response.raise_for_status()

        if "html" in response.text.lower():
            raise RuntimeError("Blocked or redirected: received HTML instead of JSON.")

        data = response.json()
        ids = data.get("esearchresult", {}).get("idlist", [])

    except Exception as e:
        raise RuntimeError(f"Search API failed: {e}")

    if not ids:
        return []

    fetch_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "json",
        "tool": "JesvinPubMedFetcher",
        "email": "jesvinblaze@gmail.com"
    }

    try:
        summary = requests.get(fetch_url, params=fetch_params, headers=headers, timeout=10).json()
    except Exception as e:
        raise RuntimeError(f"Summary API failed: {e}")

    papers = []
    for uid in summary["result"]["uids"]:
        item = summary["result"][uid]
        papers.append({
            "PubmedID": item.get("uid"),
            "Title": item.get("title"),
            "Publication Date": item.get("pubdate"),
        })

    return papers
