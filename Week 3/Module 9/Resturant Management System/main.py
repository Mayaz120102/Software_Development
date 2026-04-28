from food_item import FoodItem
from menu import Menu
from users import Customer, Admin, Employee
from restaurent import Restaurent
from orders import Order


rst = Restaurent("flagman Restaurent")


def customer_menu():
    name = input("Enter the name: ")
    email = input("Enter the email: ")
    phone = input("Enter the phone number: ")
    address = input("Enter the Address: ")
    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"welcome {customer.name}")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Paybill")
        print("5. Exit")

        choice = int(input("Enter the choice: "))

        if choice == 1:
            customer.view_menu(rst)
        elif choice == 2:
            item_name = input("enter the item name:  ")
            item_quantity = int(input("enter the quantity: "))
            customer.add_to_cart(rst, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("invalid choice")


def admin_menu():
    name = input("Enter the name: ")
    email = input("Enter the email: ")
    phone = input("Enter the phone number: ")
    address = input("Enter the Address: ")
    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"welcome {admin.name}")
        print("1. Add new item")
        print("2. Add new Employee")
        print("3. View Employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. EXit")

        choice = int(input("Enter the choice: "))

        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("enter item price: "))
            item_quantity = int(input("enter item quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(rst, item)
        elif choice == 2:
            name = input("enter the employee name:  ")
            phone = int(input("enter the number: "))
            email = input("enter the email: ")
            des = input("enter the designation: ")
            age = int(input("enter the age: "))
            salary = int(input("enter the salary:  "))
            address = input("enter the address: ")
            employee = Employee(name, email, phone, address, age, des, salary)
            admin.add_employee(rst, employee)

        elif choice == 3:
            admin.view_employee(rst)
        elif choice == 4:
            admin.view_menu(rst)
        elif choice == 5:
            item_name = input("enter the item name: ")
            admin.remove_item(rst, item_name)
        elif choice == 6:
            break
        else:
            print("invalid choice")


while True:
    print("Welcome")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("enter choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("invalid")
