# with open("another.txt", "w") as f:
#     f.write("")
# f.close()
import os
oldname = "du.txt"
newname = "renamed_by_Dinesh.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)