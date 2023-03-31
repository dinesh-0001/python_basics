class Employee:
    company = "Google"
    salary = 100

dinesh = Employee()
rajan = Employee()
dinesh.salary = 300
# dinesh.salary = 500
rajan.salary = 200
print(dinesh.company)
print(dinesh.salary) #first check in object then in class.
Employee.company = "Youtube"
print(dinesh.company)