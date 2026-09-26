# NASA Open Data Extraction Tool 🚀

This repository hosts a specialized Python web scraping utility designed exclusively to extract and aggregate science archive portals from the NASA Open Data platform (`data.nasa.gov`).

## Project Overview
Automated data collection from government portals often presents unique networking challenges. This project specifically demonstrates how to bypass server-side bot-protection systems (such as `WinError 10060` connection timeouts) by engineering custom HTTP headers to spoof a standard web browser environment (Safari on macOS).

## System Architecture & Flow
1. **Network Authentication Spoofing:** Configures a `requests` session with strict User-Agent strings.
2. **DOM Parsing:** Ingests the raw HTML payload into `BeautifulSoup4`.
3. **Data Filtering:** Iterates through anchor tags, filtering out relative links and capturing absolute HTTP/HTTPS addresses and their corresponding hyperlink text.
4. **Data Deduplication & Export:** Transforms the parsed data into a Pandas DataFrame, cleans duplicate entries, and serializes the final table into `nasa_archives_database.csv`.

## Dependencies
- `Python 3.x`
- `requests`
- `beautifulsoup4`
- `pandas`

## Usage Instructions
Navigate to the extractor directory and run the spider script:
```bash
python nasa_portal_spider.py
```
The console will output the connection status and generate the CSV file in the same directory.
