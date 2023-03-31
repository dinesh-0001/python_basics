with open("sample.txt") as f:
    content = f.read()

# content = content.replace("donkey", "!@#$%^&")

# with open("sample.txt", "w") as f:
#     f.write(content)
# f.close()

if 'dinesh' in content.lower():
    print("Yes")
else:
    print("No")