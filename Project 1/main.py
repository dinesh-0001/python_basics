import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False
    

print("Comp Turn: Snake{s} Water{w} or Gun{g}?")    
randNo = random.randint(1, 3)
# print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp ='g'

you = input("Your Turn: Snake{s} Water{w} or Gun{g}?")

a = gameWin(comp, you)

print(f"Computer Choose\n{comp}")
print(f"Computer Choose\n{you}")

if a == None:
    print("It's a Tie")
elif a == True:
    print("You Win")
elif a == False:
     print("You Lose!")