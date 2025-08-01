from typing import List, Dict

import requests


def fetch_jobs(query: str = "") -> List[Dict]:
    """Fetch jobs from the Remotive API. Falls back to a sample job if the
    network request fails."""

    url = f"https://remotive.com/api/remote-jobs?search={query}"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        jobs = []
        for item in data.get("jobs", [])[:5]:
            jobs.append(
                {
                    "title": item.get("title", ""),
                    "company": item.get("company_name", ""),
                    "link": item.get("url", ""),
                    "description": item.get("description", ""),
                }
            )
        if jobs:
            return jobs
    except Exception as e:
        print(f"Failed to fetch jobs from Remotive: {e}")

    # Fallback sample job if API call fails or returns nothing
    return [
        {
            "title": "Software Engineer",
            "company": "ExampleCorp",
            "link": "https://example.com",
            "description": "Example job description",
        }
    ]

