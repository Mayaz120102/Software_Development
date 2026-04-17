class Bank:
    def __init__(self, holder_name, initial_deposite):
        self.holder_name = holder_name
        self.__balance = initial_deposite

    def deposite(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance



abrar = Bank('Abrar',10000)
abrar.deposite(30000)
print(abrar.get_balance())
