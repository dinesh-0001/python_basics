from typing import Reversible


num = int(input("Enter a number\n"))
c = num
print("Here is Your Answer")
for i in range(1,11):
    print(str(num), "x", str(i), "=", str(i*num))

# z = num*10
# while num <= z:
#     print(num)
#     num = c + num