class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of Programmer is {self.name} and the product is {self.product}")
dinesh = Programmer("Dinesh", "Skype")
rajan = Programmer("Rajan", "Github")
dinesh.getInfo()