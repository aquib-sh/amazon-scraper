from bot import BotMaker
import config

class Browser:
    def __init__(self):
        self.__kernel = BotMaker(browser='Chrome')
        self.xpaths = config.MAPPINGS['xpaths']

    def goto(self, url):
        self.__kernel.move(url)

    def goto_homepage(self):
        self.goto(config.HOMEPAGE)

    def search(self, term, log=1):
        search_box = self.__kernel.get_element(
                self.xpaths['amazon_product_search_box'])
        search_btn = self.__kernel.get_element(
                self.xpaths['amazon_product_search_btn'])

        if log: print(f"[+] Searching {term}")
        self.__kernel.send_human_keys(search_box, term)
        search_btn.click()

    def get_page_source(self):
        return self.__kernel.page_source()

    def close(self):
        self.__kernel.shutdown()
