class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

c1 = Car("BMW", 5000000)
print(c1.name, c1.price)