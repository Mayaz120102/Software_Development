class Device:
    def __init__(self, brand, color, price) -> None:
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        return f"running :{self.brand}"


class Laptop:
    def __init__(self, memory):
        self.memory = memory

    def coding(self):
        return f"learning ds algorithm {self.memory}"


class Phone(Device):
    def __init__(self, brand, color, price, dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand, color, price)

    def phone_call(self, number, text):
        return f"Sending sms to: {number} with {text}"

    def __repr__(self):
        return f"phone:{self.brand} price: {self.price} mode: {self.dual_sim}"


class Camera:
    def __init__(self, pixel):
        self.pixel = pixel

    def change_lens(self):
        pass


my_phone = Phone("iphone", "silver", 129999, "dualsim")

print(my_phone)
