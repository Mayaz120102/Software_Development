class Shop:
    # cart = []  class attribute
    shopping_mall = 'Bashundhora'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  #instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)

mayaz = Shop("Mayaz")
mayaz.add_to_cart("watch")
mayaz.add_to_cart("shoes")
print(mayaz.cart)

Abrar = Shop("abrar")
Abrar.add_to_cart("Car")
print(Abrar.cart)