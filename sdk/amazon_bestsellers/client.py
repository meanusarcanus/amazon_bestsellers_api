"""
Official Python SDK Client for Amazon Bestsellers & Product Intelligence Scraper Pro
"""

import requests
from typing import Optional, Dict, Any

class AmazonBestsellersClient:
    """
    Python SDK Client for Amazon Bestsellers Scraper API.
    """
    def __init__(self, api_key: str, base_url: str = "https://microsaas-agent-api.vercel.app"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "Content-Type": "application/json"
        }

    def scrape_amazon_bestsellers(self, category_url: Optional[str] = None, domain: str = ".com", search_keyword: Optional[str] = None, max_results: int = 10) -> dict:
        """
        Scrape Amazon Best Sellers categories, top 100 ranked products, ASINs, prices, ratings, and image URLs.
        """
        url = f"{self.base_url}/scrape-amazon-bestsellers"
        payload = {
            "category_url": category_url,
            "domain": domain,
            "search_keyword": search_keyword,
            "max_results": max_results
        }
        response = requests.post(url, json=payload, headers=self.headers, timeout=30)
        response.raise_for_status()
        return response.json()
