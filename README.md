# Web Scraping Data Analysis Portfolio

Welcome to my Web Scraping and Data Analytics repository! This repository contains a collection of Python-based web scraping projects developed during my Data Analytics internship. These projects demonstrate my ability to automate data extraction from both static and dynamic websites, bypass anti-bot protections, and structure raw HTML data into clean datasets for analysis.

## 🛠️ Technologies Used
* **Python 3**
* **BeautifulSoup4 (bs4):** For parsing HTML and navigating the DOM tree.
* **Requests:** For handling HTTP GET requests and configuring custom headers.
* **Pandas:** For data structuring, cleaning, and exporting to CSV.

---

## 📁 Projects Included

### 1. NASA Open Data Portal Scraper
* **Target:** `data.nasa.gov`
* **Description:** A robust scraper designed to extract external science data archives from the NASA homepage. NASA actively blocks automated bots, so this project demonstrates how to bypass server firewalls by engineering custom `User-Agent` headers.
* **Output:** `nasa_portal_links.csv`

### 2. World Bank News & Stories Scraper
* **Target:** `data.worldbank.org`
* **Description:** Extracted the latest global development articles, authors, publication dates, and URLs from the World Bank's highly dynamic homepage. Utilized `utf-8-sig` encoding to properly handle special typographical characters (like em-dashes) for Excel compatibility.
* **Output:** `worldbank_news_dataset.csv`

### 3. Bookstore E-Commerce Scraper
* **Target:** `books.toscrape.com`
* **Description:** Extracted e-commerce product data including book titles, prices, star ratings, and product URLs. Implemented dynamic pagination loops to automatically scrape data across multiple consecutive pages.
* **Output:** `books_dataset.csv`

### 4. Famous Quotes Aggregator
* **Target:** `quotes.toscrape.com`
* **Description:** Scraped text-based quote content, authors, and categorical tags. Handled multiple HTML elements within individual containers, joining tags into structured, comma-separated strings for database readiness.
* **Output:** `quotes_dataset.csv`

---

## 🚀 How to Run the Scripts
1. Clone the repository:
   ```bash
   git clone https://github.com/Utkantha/codealpha_webscraping-DA.git
   ```
2. Navigate to the project directory:
   ```bash
   cd codealpha_webscraping-DA
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run any of the individual scripts (e.g., `python "nasa web scrap/nasa_portal_spider.py"`).

---
*Created by Utkantha*
