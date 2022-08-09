from SQL.SQL_HW.base_db import BaseDbConnection


class ProductRepository(BaseDbConnection):
    def __init__(self):
        super().__init__()
        self.table_name = 'products'

    def insert_many(self, name: str, price: int):
        self._cursor.execute("insert into products (name, price) values (%s,%s);", (name, price))
        self._connection.commit()

    def select_total(self):
        self._cursor.execute(f'SELECT p.price*o.quantity as Total from products as p inner join orders as o on p.id = '
                             f'o.product_id;')
        return self._cursor.fetchall()


    def __del__(self):
        if self._connection:
            self._cursor.close()
            self._connection.close()