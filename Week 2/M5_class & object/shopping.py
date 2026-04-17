class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item , price, quantity):
        product ={'item':item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self,amount):
        total =0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print(f'total price: ', total)
        if amount <total:
            print(f'give me more {total - amount}')
        else:
            print(f'take you change {amount- total}')

    def remove_item(self, item_name):
        for product in self.cart:
            if product['item'] == item_name:
                self.cart.remove(product)
                break

mayaz = Shopping('Abrar')
mayaz.add_to_cart('rice', 55, 2)
mayaz.add_to_cart('egg' ,8, 1)
print(mayaz.cart)

# mayaz.checkout(150)

mayaz.remove_item('rice')
print("after removing: ",mayaz.cart)