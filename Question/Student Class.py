class student:
    def __init__(self):
        self.name = input("Name ")
        self.marks1 = int(input("Subject 1 marks "))
        self.marks2 = int(input("Subject 2 marks "))
        self.marks3 = int(input("Subject 3 marks "))

    def calculate(self):
        self.totalMarks = self.marks1 + self.marks2 + self.marks3

    def display(self):
        print(self.totalMarks)

s1 = student()
s1.calculate()
s1.display()
