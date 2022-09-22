class circle:
    def __init__(self):
        self.radius = float(input("Radius "))
        self.colour = input("Colour ")

    def calcArea(self):
        self.area = (self.radius ** 2.0) * 3.14

    def calcCirc(self):
        self.circumference = 2 * 3.14 * self.radius

    def display(self):
        print(self.area, self.circumference)

roundObject = circle()
roundObject.calcArea()
roundObject.calcCirc()
roundObject.display()
