class ShoppingCart:
    def __init__ (self):
        self._items_list = []
    def add_to_cart(self, item):
        self._items_list.append(item)

    def add_item(self, item):
        self._items_list.append(item)
    
class AuthenticateUser:
    def __init__ (self, name, email):
        self._name = name
        self._email = email
        self._shopping_cart = None
    def get_shopping_cart(self):
        self._shopping_cart = ShoppingCart()
    def add_to_cart(self, product, quantity):
        item = Item(product, quantity)
        self._shopping_cart.add_to_cart(item)

class Product:
    def __init__ (self, name):
        self._name = name

class Item(Product):
    def __init__ (self, name, quantity):
        super().__init__(name)
        self._quantity = quantity

john = AuthenticateUser("John", "mail")
john.get_shopping_cart()

p1 = Product("Apple")
john.add_to_cart(p1, 2)
