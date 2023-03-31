class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is Created") 


    def getDetails(self):
        print(f"The Name is {self.name}")
        print(f"The Salary is {self.salary}")
        print(f"The Subunit is {self.subunit}")

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning, Sir")

dinesh = Employee("Dinesh", 100, "Youtube")
dinesh.getDetails()
dinesh.getSalary()