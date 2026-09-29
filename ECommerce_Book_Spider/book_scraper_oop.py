import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

class BookstoreSpider:
    def __init__(self, start_url, limit_pages=3):
        self.base_endpoint = start_url
        self.page_limit = limit_pages
        self.book_inventory = []

    def run_extraction(self):
        print(f"[*] Starting extraction on {self.base_endpoint}")
        
        for pg_num in range(1, self.page_limit + 1):
            if pg_num == 1:
                target_url = self.base_endpoint + "index.html"
            else:
                target_url = self.base_endpoint + f"catalogue/page-{pg_num}.html"
                
            print(f" -> Fetching page {pg_num}...")
            resp = requests.get(target_url)
            
            if resp.status_code != 200:
                print(f"[!] Warning: Page {pg_num} failed to load.")
                break
                
            dom_tree = BeautifulSoup(resp.text, 'lxml' if 'lxml' in sys.modules else 'html.parser')
            product_nodes = dom_tree.find_all('article', class_='product_pod')
            
            if not product_nodes:
                break
                
            for node in product_nodes:
                header_node = node.h3.a
                book_name = header_node.get('title')
                
                cost_node = node.find('div', class_='product_price').find('p', class_='price_color')
                book_cost = cost_node.text.strip() if cost_node else "Unknown"
                
                rating_node = node.find('p', class_='star-rating')
                stars = rating_node.get('class')[1] if rating_node and len(rating_node.get('class')) > 1 else "None"
                
                rel_link = header_node.get('href')
                absolute_link = self.base_endpoint + rel_link if not rel_link.startswith('catalogue/') else self.base_endpoint + rel_link
                
                self.book_inventory.append({
                    'Product_Name': book_name,
                    'Retail_Price': book_cost,
                    'Star_Rating': stars,
                    'Product_Link': absolute_link
                })
                
            sleep(1.5) # Throttling request

    def save_to_disk(self, filename="ecommerce_books_data.csv"):
        df = pd.DataFrame(self.book_inventory)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"[*] Exported {len(self.book_inventory)} items to {filename}")

if __name__ == '__main__':
    import sys
    spider = BookstoreSpider("https://books.toscrape.com/")
    spider.run_extraction()
    spider.save_to_disk()
