import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

class NasaDataScraper:
    def __init__(self, target_url):
        self.target_url = target_url
        # Using a completely different User-Agent string to bypass security
        self.request_headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        self.extracted_records = []

    def fetch_and_parse(self):
        print(f"[*] Initiating connection to {self.target_url}...")
        
        try:
            res = requests.get(self.target_url, headers=self.request_headers, timeout=20)
            res.raise_for_status()  # Will raise an HTTPError for bad responses
        except requests.exceptions.RequestException as err:
            print(f"[!] Network Error Encountered: {err}")
            sys.exit(1)
            
        print("[*] Page retrieved successfully. Parsing HTML...")
        soup_object = BeautifulSoup(res.text, 'html.parser')
        
        # Isolate all hyperlink elements
        all_anchors = soup_object.find_all('a')
        
        for anchor in all_anchors:
            link_name = anchor.get_text(strip=True)
            link_address = anchor.get('href')
            
            # Validation logic: ensuring we only capture valid external HTTP links that have actual text
            if link_name and link_address and "http" in link_address[0:4]:
                self.extracted_records.append({
                    'Archive_Name': link_name,
                    'Web_Address': link_address
                })

    def export_data(self, output_filename="nasa_archives_database.csv"):
        if not self.extracted_records:
            print("[!] No records to export.")
            return
            
        # Convert to Pandas DataFrame for data manipulation
        dataset = pd.DataFrame(self.extracted_records)
        
        # Deduplicate the dataset based on Web_Address
        dataset.drop_duplicates(subset=['Web_Address'], inplace=True)
        
        dataset.to_csv(output_filename, index=False, encoding='utf-8')
        print(f"[*] Success: {len(dataset)} unique records exported to '{output_filename}'")

if __name__ == '__main__':
    URL = "https://data.nasa.gov/?utm_source=chatgpt.com"
    spider = NasaDataScraper(URL)
    spider.fetch_and_parse()
    spider.export_data()
