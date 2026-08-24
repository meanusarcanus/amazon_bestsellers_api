#!/usr/bin/env python3
"""
Automated Test Suite for Amazon Bestsellers & Product Intelligence API
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "api"))

from index import app, read_root, scrape_amazon_bestsellers, AmazonBestsellersRequest

def test_suite():
    print("==================================================")
    print(" 📦 TESTING AMAZON BESTSELLERS & PRODUCT AI API")
    print("==================================================")

    # Test 1: Root Health Check
    print("\n[Test 1] Health Check Endpoint (GET /)...")
    res_root = read_root()
    assert res_root.get("status") == "online"
    print("✓ Health Check Passed!")

    # Test 2: Scrape Category URL
    print("\n[Test 2] Scrape Category URL (POST /scrape-amazon-bestsellers)...")
    res_cat = scrape_amazon_bestsellers(AmazonBestsellersRequest(
        category_url="https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/",
        domain=".com",
        max_results=5
    ))
    print("Query Type:", res_cat.query_type)
    print("Target Query:", res_cat.target_query)
    print("Total Scraped Products:", res_cat.total_scraped)
    print("Sample Product Title:", res_cat.products[0].title if res_cat.products else "None")
    print("ASIN:", res_cat.products[0].asin if res_cat.products else "None")
    assert res_cat.total_scraped > 0
    assert "amazon" in res_cat.products[0].product_url
    assert len(res_cat.products[0].asin) == 10
    print("✓ Category Scrape Passed!")

    # Test 3: Scrape UK Domain
    print("\n[Test 3] Scrape UK Domain (.co.uk)...")
    res_uk = scrape_amazon_bestsellers(AmazonBestsellersRequest(
        domain=".co.uk",
        max_results=3
    ))
    assert res_uk.total_scraped > 0
    assert res_uk.products[0].currency == "GBP"
    print("✓ UK Domain Scrape Passed!")

    print("\n==================================================")
    print(" 🎉 ALL AMAZON BESTSELLERS SCRAPER TESTS PASSED 100%!")
    print("==================================================")

if __name__ == "__main__":
    test_suite()
