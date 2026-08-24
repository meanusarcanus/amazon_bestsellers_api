# 📦 Amazon Bestsellers & Product Intelligence Scraper Pro

Scrape Amazon Best Sellers categories, subcategories, top 100 ranked products, ASINs, prices, ratings, and image URLs across .com, .co.uk, .de, .fr, .es, .it. Enriched with AI Market Opportunity scores. Just $2.99/1k items—50% cheaper than legacy scrapers!

## 🚀 Usage & Input Parameters

| Field | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `category_url` | string | Amazon Best Sellers URL | `https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/` |
| `domain` | string | Amazon TLD | `.com` |
| `search_keyword` | string | Keyword query | `wireless earbuds` |
| `max_results` | integer | Max products to extract | `20` |

## 📤 Output Format

```json
{
  "asin": "B08N5WRWNW",
  "rank": 1,
  "title": "Echo Dot (5th Gen) | Smart Speaker with Alexa",
  "price": 49.99,
  "currency": "USD",
  "rating": 4.7,
  "reviews_count": 184500,
  "category": "Electronics",
  "product_url": "https://www.amazon.com/dp/B08N5WRWNW",
  "thumbnail_url": "https://m.media-amazon.com/images/I/6182S7MYCBL._AC_SL1000_.jpg",
  "is_prime": true,
  "availability": "In Stock",
  "ai_market_opportunity": "High Demand Bestseller (#1 Rank)."
}
```
