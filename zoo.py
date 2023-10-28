class Zoo:
    zoo_name = "zoo"
    total_animals = 0

    def init(self, animal_type, name, can_fly=False, can_swim=False):

        self.animal_type = animal_type
        self.name = name
        self.can_fly = can_fly
        self.can_swim = can_swim
        Zoo.total_animals += 1

    def fly(self):
        if self.can_fly:
            print(f"{self.name} полетів!")
        else:
            print(f"{self.name} не може літати!")

    def swim(self):
        if self.can_swim:
            print(f"{self.name} поплив!")
        else:
            print(f"{self.name} не може плавати!")


fish = Zoo("риба",  can_swim=True)
crocodile = Zoo("лев", can_swim=True )
bird = Zoo("птах", can_fly=True)
turtle = Zoo("черепаха", can_swim=True)

fish.swim()
crocodile.swim()
bird.fly()
turtle.swim()

print(f"Назва зоопарку: {Zoo.zoo_name}")
print(f"Загальна кількість тварин: {Zoo.total_animals}")