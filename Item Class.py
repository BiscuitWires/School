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

item1 = item(400000, 2)
item1.display()
