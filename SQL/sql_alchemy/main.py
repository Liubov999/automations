from SQL.sql_alchemy.models.product_repository.product import Product
from SQL.sql_alchemy.models.product_repository.product_repository import ProductRepository


product_repo = ProductRepository()
#print(product_repo.get_by_id(2))

#product_repo.get_all()

#product_repo.insert_one(Product(name='kokos', price=105))

product_repo.get_all()
