class Employee:
    company = "Google"

    def ShowDetails(self):
        print("This is an Employee")
    
class Programmer (Employee):
    language = "Python"
    # company = "Youtube"

    def getLanguage(self):
        print(f"The Language is {self.language}")

    def ShowDetails(self):
        print("This is a Programmer")

e = Employee()
e.ShowDetails()
p = Programmer()
p.ShowDetails()
p.getLanguage()
print(e.company)