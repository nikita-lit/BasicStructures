from itertools import product

class Product:
    def __init__(self, name, price, id):
        self.name = name
        self.price = price
        self.id = id

class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.productscount = {}
        self.carts = []
    
    def add_product(self, product: Product, count: int = 1) -> 
        if not product.id:
            return False
        if product.id not in self.products:
            self.products[product.id] = product
            self.productscount[product.id] = count
        else:
            self.productscount[product.id] += count
            return True
    
    def get_product_count(self, product: Product) -> int:
        if product.id not in self.products:
            return -1
        return self.productscount[product.id]
    
    def move_to_cart(self, product: Product, count = 1) -> bool:
        if product.id not in self.products:
            return False
        if self.productscount[product.id] < count:
            return False
        self.productscount[product.id] -= count
        return True
    
class Cart:
    def __init__(self, shop: Shop):
        self.products = {}
        self.shop = shop

    def add_product(self, product: Product, count = 1) -> int:
        count_in_store = self.shop.get_product_count(product)
        if count_in_store <= 0:
            return count_in_store
        if count_in_store < count:
            count = count_in_store
        self.shop.move_to_cart(product, count)
        # self.products[product.id] = self.products.get(product.id, 0) + count
        return count

if __name__ == "__main__":
    shop1 = Shop("Rama")
    shop2 = Shop("Selma")

    p1 = Product("Milk", 80)
    p2 = Product("Bread", 120)

    shop1.add_product(p1, 10)
    shop1.add_product(p2, 10)

    c1 = Cart(shop1)
    print(c1.add_product(p1, 100))  # print 5
    print(shop1.productscount)   # print 5
