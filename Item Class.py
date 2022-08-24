class item:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def getName(self):
        name = input("Name ")
        return name

    def totalPrice(self):
        self.tPrice = self.quantity * self.price

    def display(self):
        self.totalPrice()
        print(self.getName(), self.tPrice)

p = 400000
q = 2
item1 = item(p, q)
item1.display()
