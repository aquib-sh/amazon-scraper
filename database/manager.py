from database.sql import QueryExecutor, QueryGenerator


class DBManager:
    def __init__(self, db_path, log=1):
        self.query_exec = QueryExecutor(db_path)
        self.query_gen = QueryGenerator()
        self.log = log
        self.__setup()

    def __setup(self):
        self.query_exec.create_table(self.query_gen.create_tbl())

    def add_product_info(self, title:str, currency:str, price:int, 
        rating:str, image_url:str,  product_url:str
    ):
        query, param = self.query_gen.add_product_details(
            title, currency, price, 
            rating, image_url, product_url
        )
        self.query_exec.modify_data(query, param)
        if self.log: print(f"[+] ADDED {title}")

    def fetch_all(self):
        query= self.query_gen.fetch_all()
        data = self.query_exec.fetch_all(query)
        return data
