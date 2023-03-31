import random
randNumber = random.randint(1,100)

# print(randNumber)
userGuess = None
guesses = 0
while(userGuess != randNumber):

    userGuess = int(input("Enter your Guess : "))

    if(userGuess==randNumber):
        print("You gussed it right!")
    else: 
        if(userGuess>randNumber):
            print("You gussed it wrong! Enter a Smaller Number") 

        elif(userGuess<randNumber):
            print("You gussed it wrong! Enter a Larger Number") 
    guesses +=1

print(f"Your guessed the number in {guesses} guesses")

with open("hiscore.txt", "r") as f:
    hiscore= int(f.read())

if (guesses<hiscore):
    print("High Score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))