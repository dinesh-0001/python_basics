class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary is {self.salary}")

dinesh = Employee()
dinesh.salary = 100000
dinesh.getSalary()
# Employee.getSalary(dinesh)