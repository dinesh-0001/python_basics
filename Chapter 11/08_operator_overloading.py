class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num1):
        return self.num + num1.num
    def __mul__(self, num1):
        return self.num * num1.num

n1 = Number(6)
n2 = Number(4)
sum = n1+n2
mul = n1*n2
print(mul)
print(sum)

