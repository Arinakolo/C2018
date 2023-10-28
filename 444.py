class Human:
    def __init__(self, name="Human"):
        self.name = name
class Auto:
    def __init__ (self, brand):
        self.brand =brand
        self.passengers = []
    def add_passengers (self, human):
        self.passengers.append(human)
    def print_passengers_name(self):
        if self.passengers != []:
            print (f"Names of {self.brand} passengers")
            for passenger in self.passengers:
                print(f"{passenger.name}")
            else:
                print (f"There are no passengers in {self.brand}")
nick = Human ("Nick")
kate = Human ("Kate")
oleg = Human ("Oleg")
car = Auto("BMW")
car.add_passengers(nick)
