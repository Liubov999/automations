import psycopg2

from SQL.base_db import BaseDbConnection


class CreateTable(BaseDbConnection):
    def __init__(self):
        super().__init__()
        self.connection = psycopg2.connect(
            user='iarovaliubov',
            password='123',

            host='127.0.0.1',
            port='5432',
            database='testdb'
        )
        self._connection.set_session(autocommit=True)
        self._cursor = self._connection.cursor()

    def create_table_products(self):
        self._cursor.execute(f'create table products (id int generated always as identity primary key, name varchar('
                             f'20), price int);')
        self._connection.commit()

    def create_table_orders(self):
        self._cursor.execute(f'create table orders (id varchar primary key, product_id int, quantity int, constraint '
                             f'fk_product_id '
                             f'foreign key (product_id) references products(id));')
        self._connection.commit()
