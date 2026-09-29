import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

class QuotesMiner:
    def __init__(self, endpoint_url, pages_to_mine=5):
        self.endpoint = endpoint_url
        self.pages_to_mine = pages_to_mine
        self.mined_quotes = []

    def execute_mining(self):
        print(f"[*] Commencing mining operation on {self.endpoint}")
        
        for p in range(1, self.pages_to_mine + 1):
            req_url = f"{self.endpoint}page/{p}/"
            print(f" -> Accessing page {p}...")
            
            response = requests.get(req_url)
            if response.status_code != 200:
                print(f"[!] Access denied or page missing on {req_url}")
                break
                
            soup = BeautifulSoup(response.content, 'html.parser')
            quote_blocks = soup.find_all('div', class_='quote')
            
            if not quote_blocks:
                break
                
            for block in quote_blocks:
                q_text = block.find('span', class_='text').get_text(strip=True)
                q_author = block.find('small', class_='author').get_text(strip=True)
                
                tag_list = block.find('div', class_='tags').find_all('a', class_='tag')
                unified_tags = " | ".join([t.get_text(strip=True) for t in tag_list])
                
                self.mined_quotes.append({
                    'Quote_Content': q_text,
                    'Author_Name': q_author,
                    'Associated_Categories': unified_tags
                })
                
            sleep(1.2)

    def write_csv(self, out_file="mined_quotes_dataset.csv"):
        if self.mined_quotes:
            dataframe = pd.DataFrame(self.mined_quotes)
            dataframe.to_csv(out_file, index=False, encoding='utf-8-sig')
            print(f"[*] Successfully mined and saved {len(self.mined_quotes)} records to {out_file}")
        else:
            print("[!] No data was mined.")

if __name__ == "__main__":
    miner = QuotesMiner("http://quotes.toscrape.com/")
    miner.execute_mining()
    miner.write_csv()
