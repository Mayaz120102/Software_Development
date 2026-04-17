class Vehicle:
    def __init__(self, name,price):
        self.name = name
        self.price = price

    def move(self):
        pass
    
    def __repr__(self):
        return f'{self.name} {self.price}'

class Bus(Vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        super().__init__(name, price)

class Truck(Vehicle):
    def __init__(self, name, price, weight):
        self.weight =weight
        super().__init__(name, price)

class PickUpTruck(Truck):
    def __init__(self, name, price, weight,):

        super().__init__(name, price, weight)

class AcBus(Bus):
    def __init__(self, name, price, seat):
        super().__init__(name, price, seat)
    def __repr__(self):
        return super().__repr__()

green_line = AcBus('shona moni', 1200, 34)
print(green_line)