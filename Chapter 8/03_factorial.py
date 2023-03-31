def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

a = int(input("Enter a Number\n"))
print("Your Answer is ")
print(factorial_iter(a))