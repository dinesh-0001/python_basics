myDict = {
    "Fast": "In a Quick Manner",
    "Dinesh": "A Student",
    "Marks": [1, 2, 3, 4],
    "anotherdict": {"Dinesh":"A player"},
    1: 2
}
print(myDict.keys())
print(myDict.values())
print(myDict.items())
a = {"Lovish": "A Freind"
}
myDict.update(a)
print(myDict)
print(myDict.get("Dinesh"))