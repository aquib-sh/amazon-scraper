import os
import sys

HOMEPAGE = "https://www.amazon.in"

MAPPINGS = {
        "xpaths":
        {
            "amazon_product_search_box":"//input[@type='text'][@id='twotabsearchtextbox']",
            "amazon_product_search_btn":"//input[@type='submit'][@id='nav-search-submit-button']"
        },

        "selectors":{}
}
__path = sys.argv[0]
__dir = os.path.abspath(os.path.dirname(__path))
DATA_DIR = os.path.join(__dir, "internal")
DB_FILE = "products.db"
DB_PATH = os.path.join(DATA_DIR, DB_FILE)
