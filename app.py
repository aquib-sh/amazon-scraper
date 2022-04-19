import sys
from parser import AmazonParser

import config
from browser import Browser
from database.manager import DBManager
from log import Logger


class AmazonScraper:
    def __init__(self):
        print("$$$$$$ AMAZON SCRAPER $$$$$$$$")
        print("Author: Shaikh Aquib\n\n")
        
        self.log = Logger()
        self.db_manager = DBManager(config.DB_PATH)
        self.browser = Browser() 
        self.parser = AmazonParser(None)

        # function mappings
        self.switch = {
            1:self.run_search,
            2:self.run_link,
            3:sys.exit
        }

        self.host = "https://amazon.in/"

    def __fetch_from_url(self, url):
        # Opening link in browser and get the HTML source
        self.log.info(f"Opening {url}")
        self.browser.goto(url)
        source = self.browser.get_page_source()
        self.parser.update_source(source)
        # Parse the HTML source and get the data
        info = self.parser.get_product_info()
        return info

    def __add_to_db(self, info:dict, abs_link):
        # Add the info to DB
        self.db_manager.add_product_info(info["title"], info["currency"], info["price"], 
            info["customer_ratings"], info["image_url"], abs_link
        )
        self.log.info(str(info))
        self.log.info(f"Added record to DB")

    def run_search(self):        
        """Gets a list of links and runs through them."""
        self.log.info("Entering Search Method")
        keyword = input("S> Enter the product name: ")
        self.browser.goto_homepage()

        self.log.info(f"Searching for {keyword}")
        self.browser.search(keyword, log=0)
        source = self.browser.get_page_source()
        self.parser.update_source(source)
        links = self.parser.get_product_links()
        self.log.info(f"Found {len(links)} links with {keyword}")
        limit = int(input("How many products do you want to get? "))
        i = 0

        # Add all the product info uptil limit products
        for link in links:
            if i >= limit: 
                break
            abs_link = self.host + link
            info = self.__fetch_from_url(abs_link)
            self.__add_to_db(info, abs_link)
            print("\n\n")
            i += 1

    def run_link(self):
        """Gets the product info through link."""
        self.log.info("Entering Link Method")
        link = input("L> Enter the product link: ")
        abs_link = self.host + link
        info = self.__fetch_from_url(abs_link)
        self.__add_to_db(info, abs_link)
        print("\n\n")
    
    def run(self):
       while (True):
            print("1. Get Product by Searching\n2. Get Product by Link\n3. Quit")
            choice = int(input("Enter the number corresponding to option: "))
            self.switch[choice]()

if __name__ == "__main__":
    app = AmazonScraper()
    app.run()
        