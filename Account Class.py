class account:
    def __init__(self):
        self.id = int(input("ID "))
        self.name = input("Name ")
        self.balance = float(input("Balance "))

    def credit(self, amount):
        return (self.balance + amnount)

    def debit(self, amount):
        if amount <= self.balance:
            return (self.balance - amount)
        else:
            print("Amount exceeded balance")
            return self.balance

    def display(self):
        action = input("Credit or debit? ")
        if action.lower() == 'credit':
            print(self.id, self.name, self.credit(int(input("Credit Amount "))))
        else:
            print(self.id, self.name, self.debit(int(input("Debit Amount "))))

acc1 = account()
acc1.display()
