import datetime
import sqlite3


class QueryGenerator:
    """Main work is to generate queries to be used by the controller."""

    def __init__(self):
        self.__table = "AMAZON_PRODUCTS"

    # setters
    def set_table_name(self, new_name: str):
        self.__table = new_name

    # getters
    def get_table_name(self) -> str:
        return self.__table

    def create_tbl(self):
        return f"""CREATE TABLE IF NOT EXISTS {self.__table}
            (
                TITLE TEXT NOT NULL,
                CURRENCY TEXT NOT NULL,
                PRICE INTEGER NOT NULL,
                RATING TEXT NOT NULL,
                IMAGE_URL TEXT NOT NULL,
                PRODUCT_URL TEXT NOT NULL
            );
            """

    def add_product_details(
        self, title:str, currency:str, price:int, rating:str, image_url:str,  product_url:str
    ) -> tuple:
        current_datetime = str(datetime.datetime.now())
        if type(price) != int: price = int(price)

        query = f"""INSERT INTO {self.__table} 
            (TITLE, CURRENCY, PRICE, RATING, IMAGE_URL, PRODUCT_URL) 
            VALUES (?, ?, ?, ?, ?, ?);"""
        params = (
            title, currency, price, rating, image_url, product_url
        )
        return (query, params)

    def fetch_all(self):
        query = f"""SELECT * FROM {self.__table};"""
        return query


class QueryExecutor:
    def __init__(self, sqlite_file_path: str, log=1):
        self.conn = sqlite3.connect(sqlite_file_path)
        self.cursor = self.conn.cursor()
        self.log = log
        if self.log:
            print(f"[+] Connect to database at {sqlite_file_path}")

    def create_table(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def modify_data(self, query, params):
        self.cursor.execute(query, params)
        self.conn.commit()
    
    def fetch_all(self, query):
        self.cursor.execute(query)
        fetched_data = self.cursor.fetchall()
        return fetched_data
