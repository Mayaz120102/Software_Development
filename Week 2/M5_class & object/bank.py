class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw =10000

    def get_balance(self):
            return self.balance
        
    def deposit(self,amount):
            if amount >0:
                self.balance += amount
                print(f'deposited {amount} and new balance {self.balance} ')
            else:
                print(f'you have to deposit atleast more than 0 ')
        
    def withdraw(self, amount):
            if amount < self.min_withdraw:
                  print(f'you cannot withdraw less then {self.min_withdraw}')
            elif amount >self.max_withdraw:
                  print(f'you cannot withdraw more than {self.max_withdraw}')
            else:
                  self.balance -= amount
                  print(f'withdraw succesfull, remaining balance {self.balance}')

sibl = Bank(150000)
sibl.withdraw(1000)
total_balance = sibl.get_balance()
print(total_balance)

sibl.deposit(.23)
total_balance = sibl.get_balance()
print("after deposit:",total_balance)
