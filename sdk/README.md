# 📦 Amazon Bestsellers & Product Intelligence Scraper Pro Python SDK

Official Python SDK for `amazon-bestsellers-api`. Extract Amazon Best Sellers categories, top 100 ranked products, ASINs, prices, ratings, and AI market opportunity scores in 1 line of Python code.

## 🚀 Installation
```bash
pip install amazon-bestsellers-api
```

## 💻 Quick Usage
```python
from amazon_bestsellers import AmazonBestsellersClient

client = AmazonBestsellersClient(api_key="YOUR_RAPIDAPI_KEY")
res = client.scrape_amazon_bestsellers(domain=".com", max_results=10)

for product in res["products"]:
    print(f"Rank #{product['rank']} | ASIN: {product['asin']} | Title: {product['title']} | Price: ${product['price']}")
```
