from abc import ABC
from orders import Order


class User(ABC):  # base class or parent class
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print(f"total item is {item.quantity} so exceeeded")
            else:
                # item.quantity = quantity
                self.cart.add_item(item, quantity)
                print("item added")
        else:
            print("item not found")

    def view_cart(self):
        print("view cart")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():  # items() python function
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"total price: {self.cart.total_price}")

    def pay_bill(self):
        for item, quantity in self.cart.items.items():
            item.quantity -= quantity  # ✅ reduce actual stock
        print(f"total price : {self.cart.total_price} payed succesful")
        self.cart.clear()


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)

    def view_employee(self, restaurent):
        restaurent.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)
