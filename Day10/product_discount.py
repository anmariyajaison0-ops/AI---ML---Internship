class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percent):
        return self.price - (self.price * percent / 100)

p1 = Product("Phone", 20000)
print(p1.discount(10))