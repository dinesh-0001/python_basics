sub1 = int(input("Enter Subject 1 Marks\n"))
sub2 = int(input("Enter Subject 2 Marks\n"))
sub3 = int(input("Enter Subject 3 Marks\n"))

if(sub1<33 or sub2<33 or sub3<33): print("You are Failed")

elif(sub1+sub2+sub3)/3 <40: print("You are failed in Totaling")

else: print("You are passed")
