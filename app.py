from os import link
from parser import AmazonParser

from browser import Browser
from log import Logger

log = Logger()
browser = Browser()
parser = AmazonParser(None)

def run_search():        
    """Gets a list of links and runs through them."""
    log.info("Entering Search Method")
    keyword = input("S> Enter the product name: ")
    browser.goto_homepage()

    log.info(f"Searching for {keyword}")
    browser.search(keyword, log=0)
    source = browser.get_page_source()
    parser.update_source(source)
    links = parser.get_product_links()
    log.info(f"Found {len(links)} links with {keyword}")

    for link in links:
        log.info(f"Opening {link}")
        browser.goto(link)
        info = parser.get_product_info()

def run_link():
    """Gets the product info through link."""
    log.info("Entering Link Method")
    link = input("L> Enter the product link: ")
    log.info(f"Opening {link}")

    browser.goto(link)
    source = browser.get_page_source()
    parser.update_source(source)
    info = parser.get_product_info()

# function mappings
run_choice = {
    1:run_search,
    2:run_link
}

while (True):
    print("1. Get Product by Searching\n2.Get Product by Link")
    choice = input("Enter the number corresponding to option")
    run_choice[choice]()
