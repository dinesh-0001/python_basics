class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning, Sir")

dinesh = Employee()
dinesh.salary = 100000
dinesh.greet() 