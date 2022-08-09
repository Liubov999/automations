from SQL.SQL_HW.create_table import CreateTable
from SQL.SQL_HW.orders_repository import OrdersRepository
from SQL.SQL_HW.product_repository import ProductRepository

product_repository = ProductRepository()
create_table_orders = CreateTable()
create_table_products = CreateTable()
orders_repository = OrdersRepository()


create_table_products.create_table_products()
create_table_orders.create_table_orders()

product_repository.insert_many('potato', 60)
product_repository.insert_many('melon', 90)
product_repository.insert_many('onion', 34)
product_repository.insert_many('apple', 23)
product_repository.insert_many('cherry', 77)

orders_repository.insert_many_orders(345, 1, 35)
orders_repository.insert_many_orders(563, 2, 77)
orders_repository.insert_many_orders(884, 3, 55)
orders_repository.insert_many_orders(467, 4, 90)
orders_repository.insert_many_orders(883, 5, 12)

orders_repository.add_column()
product_repository.select_total()

orders_repository.update_total(2100, 1)
orders_repository.update_total(6930, 2)
orders_repository.update_total(1870, 3)
orders_repository.update_total(2070, 4)
orders_repository.update_total(924, 5)


print(orders_repository.get_by_join())





