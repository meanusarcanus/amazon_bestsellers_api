# 📦 Amazon Bestsellers & Product Intelligence Scraper Pro API

High-performance API engine and Apify Actor designed to scrape Amazon Best Sellers categories, top 100 ranked products, ASINs, prices, ratings, image URLs, and AI market opportunity scores across global Amazon domains (.com, .co.uk, .de, .fr, .es, .it).

---

## 🚀 Quick Start

### 1. Run Locally
```bash
pip install -r requirements.txt
uvicorn api.index:app --reload
```

### 2. Run Tests
```bash
python3 test_api.py
```

### 3. API Endpoint (`POST /scrape-amazon-bestsellers`)
```json
{
  "domain": ".com",
  "max_results": 10
}
```
