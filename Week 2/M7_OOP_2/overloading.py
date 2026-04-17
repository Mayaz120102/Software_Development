class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("khay day ghumay")
    


class Cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):
        # return super().eat()
        print("exercise kore tarpor khay o ghumay")

    def __add__(self, other):  # overloading dandar function
        return self.age + other.age


mayaz = Cricketer("mayaz", 24, 5.4, 56, "foreded")
abrar = Cricketer("abrar", 23, 5.6, 57, "Bd")

mayaz.eat()
# print(mayaz.name, mayaz.age, mayaz.height)

print(1 + 3)
print(mayaz + abrar)
