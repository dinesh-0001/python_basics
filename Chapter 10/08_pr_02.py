class Calculator:
    def __init__(self, num):
        self.number = num
        
    def square(self):
        print(f"The Value of {self.number} square is {self.number**2}")

    def squareRoot(self):
        print(f"The Value of {self.number} squareroot is {self.number**0.5}")


    def cube(self):
        print(f"The Value of {self.number} cube is {self.number**3}")


a = Calculator(int(input("Enter a Number\n")))
a.square()
a.squareRoot()
a.cube()