import random


class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
    def get_home(self):
        self.home = House()
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def get_car(self):
        self.car = Auto(brands_of_car)
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            self.satiety >= 100
            self.satiety = 100
            return
        self.satiety += 5
        self.home.food -=5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        if manage == "fuel":
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print('Bought food!')
            self.money -= 50
            self.home.food += 50
    def chill(self):
        pass
    def clean_home(self):
        pass
    def to_repair(self):
        pass
    def day_indexes(self, day):
        day = f"Today the {day} of {self.name}'s life"
        print(f"{day:=^50}", '\n')
        human_indexes = self.name + " 's indexes"
        print(f"{human_indexes:^50}", '\n')
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        print(f"{"Home_indexes":^50}", '\n')
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", '\n')
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        if self.gladness <0:
            print('Depression')
            return False
        if self.satiety <0:
            print('Dead...')
            return False
        if self.money < -500:
            print('Bankrupt...')
            return False
        pass
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:

            self.get_job()
            print(f"I do not have a job? i am going to get a job {self.job.job} with salary {self.job.salary}")
        self.day_indexes(day)
        dice = random.randint(1,4)

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel=brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']
        pass

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.strength -= 1
            self.fuel -= self.consumption
            return True
        else:
            print("The car can not move")
            return False

brands_of_car = {
    "BMW": {"fuel": 100, "strength":100, "consumption":8},
    "Lada": {"fuel": 80, "strength":40, "consumption":12},
    "Volvo": {"fuel": 60, "strength":150, "consumption":6},
    "Ford": {"fuel": 50, "strength":120, "consumption":9},
}

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

job_list = {
    "Java developer": {"salary": 50, "gladness_less":10},
    "C++ developer": {"salary": 70, "gladness_less":20},
    "Python developer": {"salary": 40, "gladness_less":50},
    "Rust developer": {"salary": 60, "gladness_less":40}
}

nick = Human(name = "Nick")
for day in range (1, 8):
    if nick.live(day) == False:
        break


