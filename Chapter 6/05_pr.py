text = input("Enter the Text\n")

if("make a lot of money" in text): spam = True
elif("Subscribe this" in text): spam = True
elif("Click This" in text): spam = True
else: spam = False

if(spam):
    print("This is Spam")
else: print("This is not Spam")
