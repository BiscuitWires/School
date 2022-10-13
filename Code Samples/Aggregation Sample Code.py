class FoodItem:
  def __init__(self, nameP, codeP, costP):
    self.name = nameP
    self.code = codeP
    self.cost = costP

  def getCode(self):
    return self.code

  def getCost(self):
    return self.cost

  def getName(self):
    return self.name

class VendingMachine:
  def __init__(self, item1, item2, item3, item4):
    self.items = [item1, item2, item3, item4]
    self.moneyIn = 0.0

  def insertMoney(self, amount):
    self.moneyIn += amount

  def checkValid(self, code):
    for i in range(4):
      if self.items[i].getCode() == code:
        if self.items[i].getCost() <= self.moneyIn:
          return i
        else:
          return -2
    return -1

item1 = FoodItem('a', 1, 25.0)
item2 = FoodItem('b', 2, 35.0)
item3 = FoodItem('c', 3, 45.0)
item4 = FoodItem('d', 4, 55.0)

V = VendingMachine(item1, item2, item3, item4)
V.insertMoney(30.0)
print(V.checkValid(2)) #should return -2
print(V.checkValid(1)) #should return 0
