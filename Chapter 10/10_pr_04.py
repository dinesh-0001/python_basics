class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the Train is {self.name}")
        print(f"The seats avaialble on this train are {self.seats}")
        print(f"The fare of the Ticket is Rs:{self.fare}")
    
    def bookTicket(self):
        if(self.seats>0):
            print("Ticket Confirmed")
            self.seats = self.seats-1
        else:
            print("Failed! No Seat available")
    
intercity = Train("Intercity Express:54656", 90, 300)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()