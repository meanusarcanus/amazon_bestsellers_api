# 📦 RapidAPI Master Listing & Documentation Kit: Amazon Bestsellers Pro

Complete, standalone documentation kit for publishing **Amazon Bestsellers & Product Intelligence Scraper Pro (`POST /scrape-amazon-bestsellers`)** on **RapidAPI Studio** ([provider.rapidapi.com](https://provider.rapidapi.com)).

---

## 📌 1. RapidAPI Listing Metadata

- **API Name**: `Amazon Bestsellers & Product Intelligence Scraper Pro`
- **Category**: `E-Commerce` / `Data` / `Shopping`
- **Base URL**: `https://microsaas-agent-api.vercel.app`
- **Endpoint**: `POST /scrape-amazon-bestsellers`

---

## 📝 2. Short Description (Tagline / Summary - Under 250 Chars)

```text
Scrape Amazon Best Sellers categories, top 100 ranked products, ASINs, prices, ratings, and image URLs across global TLDs (.com, .co.uk, .de). Enriched with AI Market Opportunity scores.
```

---

## 📜 3. Long Description (RapidAPI Overview Tab)

```markdown
# 📦 Amazon Bestsellers & Product Intelligence Scraper Pro

Extract Amazon Best Sellers category charts, top 100 ranked products, ASIN identifiers, real-time pricing, ratings, review counts, and AI Market Opportunity scores across global Amazon domains in real-time.

---

## 🚀 Key Features & Extracted Data Fields

* **📦 Product Identifiers & Ranking**: ASIN, Bestseller Category Rank (#1–#100), Product Title, and Direct Product Link.
* **💲 Real-Time Pricing & Stock**: Price, Currency (`USD`, `GBP`, `EUR`), Prime Badge indicator, and Availability status.
* **⭐ Review & Reputation Metrics**: Average Rating (out of 5.0) and Total Customer Reviews Count.
* **🎯 AI Market Opportunity Score**: Automated demand rating and category competitiveness index.
* **🌍 Multi-Domain Support**: Works across `.com`, `.co.uk`, `.de`, `.fr`, `.es`, and `.it`.

---

## 📥 Sample Request JSON

```json
{
  "category_url": "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/",
  "domain": ".com",
  "max_results": 10
}
```

## 📤 Sample Response JSON

```json
{
  "status": "success",
  "query_type": "url",
  "target_query": "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/",
  "domain": ".com",
  "total_scraped": 1,
  "products": [
    {
      "asin": "B08N5WRWNW",
      "rank": 1,
      "title": "Echo Dot (5th Gen) | Smart Speaker with Alexa & Vibrant Sound | Charcoal",
      "price": 49.99,
      "currency": "USD",
      "rating": 4.7,
      "reviews_count": 184500,
      "category": "Electronics",
      "product_url": "https://www.amazon.com/dp/B08N5WRWNW",
      "thumbnail_url": "https://m.media-amazon.com/images/I/6182S7MYCBL._AC_SL1000_.jpg",
      "is_prime": true,
      "availability": "In Stock",
      "ai_market_opportunity": "High Demand Bestseller (#1 Rank). Extremely high review velocity (184k+ reviews)."
    }
  ]
}
```
```

---

## 💰 4. Recommended RapidAPI Pricing Tiers

| Plan Tier | Monthly Price | Included Requests | Overage Fee / Request |
| :--- | :--- | :--- | :--- |
| **BASIC (Free)** | `$0.00 / mo` | 20 requests | Hard Cap (No Overages) |
| **PRO** | **`$29.00 / mo`** | 2,500 requests | `$0.015 / request` |
| **ULTRA** | **`$79.00 / mo`** | 10,000 requests | `$0.010 / request` |
| **MEGA** | **`$199.00 / mo`** | 30,000 requests | `$0.008 / request` |
