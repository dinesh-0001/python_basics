# story = "Dinesh is 19 years old. \nHe\t loves to code"
# print(story)

# a = input("Enter your Name\n")
# b = "Good Afternoon, "
# print(b + a)

letter = '''Dear <|Name|>, \n \tYou are Selected\nDate: <|Date|>'''
name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)