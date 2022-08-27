class order:
    def __init__(self, ID, name):
        self.order_id = ID
        self.cust_name = name
        self.Prod_Names = []
        self.Prod_Quan = []
        self.Prod_Price = []

    def Accept_Order(self):
        for i in range(3):
            name = input("Item Name ")
            quantity = int(input("Item Quantity "))
            price - int(input("Item Price "))

            self.Prod_Names.append(name)
            self.Prod_Quan.append(quantity)
            self.Prod_Price.append(price)

    def Cal_Cost(self):
        for i in range(3):
            self.totalPrice = self.totalPrice + (self.Prod_Price[i] * self.Prod_Quan[i])
