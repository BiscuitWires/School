class teacher:
    def __init__(self, dep, name):
        self.dep = dep
        self.name = name

    def getName(self):
        return self.name

    def getDepartment(self):
        return self.dep

    def setSalary(self, sal):
        self.salary = sal

    def getSalary(self):
        return self.salary

    def Display_Details(self):
        print(self.getName(), "is in the", self.getDepartment(), "department with a salary of", self.getSalary())

T = teacher(input("Department "), input("Name "))
T.setSalary(int(input("Salary ")))
T.Display_Details()
