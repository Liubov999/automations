from SQL.base_db import BaseDbConnection


class OrdersRepository(BaseDbConnection):
    def __init__(self):
        super().__init__()
        self.table_name = 'orders'

    def get_by_join(self):
        self._cursor.execute('select p.name,p.price,o.quantity, o.total from products as p inner join orders as o on '
                             'p.id = o.product_id order by product_id;')
        return self._cursor.fetchall()

    def insert_many_orders(self, id: int, product_id: int, quantity: int):
        self._cursor.execute("insert into orders (id, product_id, quantity) values (%s, %s, %s);", (id, product_id, quantity))
        self._connection.commit()

    def update_total(self, total: int, product_id: int):
        self._cursor.execute("update orders set total = (%s) where product_id = (%s);", (total, product_id))
        self._connection.commit()

    def add_column(self):
        self._cursor.execute(f"alter table orders add column total int;")
        self._connection.commit()

    def __del__(self):
        if self._connection:
            self._cursor.close()
            self._connection.close()