def percent(marks):
    # s = marks.count()
    p = (sum(marks)/400)*100
    return p

a = [77, 98, 84, 34]
percentage1 = percent(a)

marks2 = [99, 97, 45, 94]
percentage2 = percent(marks2)
print(percentage1, percentage2)

def mysum(num1, num2):
    return(num1+num2)

b = int(input("Number 1\n"))
c = int(input("Number 2\n"))
s = mysum(b, c)
print(s)