import logging
from typing import List, Dict
import time

class ProductScraper:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrape_products(self, niche: str) -> List[Dict]:
        """
        Scrapes product data from e-commerce sites for a given niche.
        Returns a list of product dictionaries.
        """
        products = []
        try:
            response = requests.get(f"{self.config['base_url']}/{niche}", headers=self.headers)
            response.raise_for_status()
            product_list = response.json()['products']
            for product in product_list:
                product_data = {
                    'name': product['title'],
                    'price': product['price'],
                    'url': product['productUrl']
                }
                products.append(product_data)
                time.sleep(1)  # To avoid overwhelming the server
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Scraping failed for niche {niche}: {str(e)}")
        return products