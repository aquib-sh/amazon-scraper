from bs4 import BeautifulSoup

class AmazonParser:
    def __init__(self, source):
        self.source = source
        self.soup = BeautifulSoup(self.source, 'lxml')

    def update_source(self, source):
        self.source = source
        self.soup = BeautifulSoup(self.source, 'lxml')

    def get_product_links(self):
        links = []
        image_elements = self.soup.find_all("span", {"data-component-type":"s-product-image"})
        for elem in image_elements:
            link = elem.find("a")['href']
            links.append(link)
        return links

    def get_product_info(self, link):
        pass
