class Person:
    country = "India"

    def name(self):
        print("My Name is Dinesh")

class Employee(Person):
    company = "Honda"
    Salary = 10000
    
    def getSalary(self):
        print(f"Salary is {self.Salary}")

    def name(self):
        print("I am an Employee and My Name is Dinesh")

class Programmer(Employee):
    company = "Hero"

    def getSalary(self):
        print(f"No Salary to Programmers")

    def name(self):
        # super().name()
        print("I am a Programmer and My Name is Dinesh")

p = Person()
p.name()
e = Employee()
e.name()
print(e.company)
pr = Programmer()
pr.name()
pr.getSalary()