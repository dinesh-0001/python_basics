class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

dineshApplication = RailwayForm()
dineshApplication.name = "Dinesh"
dineshApplication.train = "Rajdhani Express"
dineshApplication.printData()