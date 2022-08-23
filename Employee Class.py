class employee():
    def __init__(self):
        self.id = int(input("ID "))
        self.firstName = input("First name ")
        self.lastName = input("Last name ")
        self.salary = int(input("Salary "))

    def getName(self):
        return (self.firstName + " " + self.lastName)

    def annualSalary(self):
        self.salary = self.salary * 12

    def calculateTax(self):
        if self.salary < 200000:
            self.tax = 0
        elif self.salary >=200000 and self.salary < 400000:
            self.tax = 0.1 * self.salary
        elif self.salary >= 400000 and self.salary < 600000:
            self.tax = 0.15 * self.salary
        elif self.salary >= 600000 and self.salary < 800000:
            self.tax = 0.2 * self.salary
        else:
            self.tax = 0.25 * self.salary

    def display(self):
        self.calculateTax()
        self.salary = self.salary - self.tax
        self.annualSalary()
        print(self.id, self.getName(), self.salary, self.tax)

emp1 = employee()
emp1.display()
