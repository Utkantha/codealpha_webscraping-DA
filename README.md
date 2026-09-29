# Advanced Web Scraping & Data Engineering Portfolio 🚀

Welcome to my professional data engineering portfolio. This repository showcases four specialized, object-oriented Python web scrapers designed to extract, sanitize, and structure data from a variety of complex web environments.

These projects were engineered to solve real-world extraction challenges, including dynamic pagination, anti-bot security bypassing, and complex DOM tree traversal.

## 🛠️ Core Technology Stack
- **Language:** Python 3 (Object-Oriented Programming Patterns)
- **Networking:** `Requests` (with custom headers and strict timeouts)
- **DOM Parsing:** `BeautifulSoup4` & `lxml`
- **Data Structuring:** `Pandas` (for deduplication and CSV generation with `utf-8-sig`)

---

## 📁 Included Extraction Modules

### 1. NASA Data Archive Extractor 
*(Folder: `NASA web scrap`)*
- **Target:** `data.nasa.gov`
- **Challenge:** High-security government servers that actively drop connections from automated requests (`WinError 10060`).
- **Solution:** Spoofed a macOS/Safari environment using custom HTTP headers to securely bypass the firewall and extract 34 verified external science archive links.

### 2. World Bank News Harvester 
*(Folder: `World Bank News Webscrap`)*
- **Target:** `data.worldbank.org`
- **Challenge:** Extracting dynamic, real-time development news and dealing with special typographical characters that break standard CSV files.
- **Solution:** Traversed complex nested `<article>` lists to extract headlines, writers, and dates. Implemented `utf-8-sig` encoding to ensure perfect spreadsheet compatibility for em-dashes and quotes.

### 3. Global Quotes Miner 
*(Folder: `Quotes wb scrap`)*
- **Target:** `quotes.toscrape.com`
- **Challenge:** Aggregating multiple variable-length elements (tags) nested within a single parent node.
- **Solution:** Created an intelligent loop that captures all nested categorical `<a class="tag">` elements and concatenates them into a unified, pipe-separated string (`|`) for clean database ingestion across 5 paginated layers.

### 4. E-Commerce Book Spider 
*(Folder: `Books Webscrap`)*
- **Target:** `books.toscrape.com`
- **Challenge:** Navigating e-commerce pagination and structuring retail pricing and metadata.
- **Solution:** Engineered a dynamic URL generator to cycle through product catalog pages, throttling requests to ensure polite server interaction. Extracted absolute product URLs, retail pricing, and star ratings into a structured Pandas DataFrame.

---
*Developed by Utkantha during Data Analytics Internship*
