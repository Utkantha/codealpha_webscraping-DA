import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

class WorldBankHarvester:
    def __init__(self, target_portal):
        self.portal = target_portal
        self.spoof_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        self.harvested_news = []

    def run_harvest(self):
        print(f"[*] Targeting World Bank portal: {self.portal}")
        
        try:
            req = requests.get(self.portal, headers=self.spoof_headers, timeout=15)
            req.raise_for_status()
        except Exception as e:
            print(f"[!] Network failure: {e}")
            return
            
        parser = BeautifulSoup(req.text, 'html.parser')
        
        # News items are stored in li tags with class 'item'
        news_nodes = parser.find_all('li', class_='item')
        
        for node in news_nodes:
            # Extract header
            title_node = node.find('h4', class_='item-title')
            headline = title_node.get_text(strip=True) if title_node else "N/A"
            
            # Extract author
            author_node = node.find('span', class_='author')
            writer = author_node.get_text(strip=True).rstrip(',') if author_node else "Anonymous"
            
            # Extract publish date
            date_node = node.find('span', class_='date')
            pub_date = date_node.get_text(strip=True) if date_node else "N/A"
            
            # Extract URL
            anchor = node.find('a')
            story_url = anchor.get('href') if anchor else ""
            if story_url and not story_url.startswith('http'):
                story_url = "https://data.worldbank.org" + story_url
                
            self.harvested_news.append({
                'Headline': headline,
                'Writer': writer,
                'Publication_Date': pub_date,
                'Story_URL': story_url
            })

    def save_dataset(self, filename="wb_harvested_news.csv"):
        if not self.harvested_news:
            print("[!] Harvest yielded 0 results.")
            return
            
        data_table = pd.DataFrame(self.harvested_news)
        data_table.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"[*] Harvest complete. {len(self.harvested_news)} articles saved to {filename}")

if __name__ == "__main__":
    harvester = WorldBankHarvester("https://data.worldbank.org/?utm_source=chatgpt.com")
    harvester.run_harvest()
    harvester.save_dataset()
