a= int(input("Enter a Number: "))
 
for i in range (2, a):
    if (a%i == 0):
        print("This is not a Prime Number")
        break
else:
    print("This is a Prime Number")