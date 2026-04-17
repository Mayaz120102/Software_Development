from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        print("hello nanak kanana ")
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name):
        self.category = 'Moneky'
        self.name = name
        super().__init__()
    def eat(self):
        print("helll o nama afdefd")

mnky = Monkey('kyc')
mnky.eat()