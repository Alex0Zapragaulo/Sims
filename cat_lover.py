import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 100
        self.energy = 100
        self.alive = True

    def to_chill(self):
        print("Cat chilling")
        self.gladness -= 10
        self.energy += 20

    def to_sleep(self):
        print("Cat sleeping")
        self.gladness -= 5
        self.energy += 32

    def is_alive(self):
        if self.gladness <= 0:
            self.alive = False
        elif self.energy <= 0:
            self.alive = False

    def end_day(self):
        print(f"Cat gladness = {self.gladness}")
        print(f"Cat energy = {self.energy}")

Bonya = Cat(name="Bonya")

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 100
        self.energy = 100
        self.progress = 50
        self.alive = True

    def to_study(self):
        print("Student studying")
        self.gladness -= 25
        self.energy -= 20
        self.progress += 10

    def to_stroll(self):
        print("Student strolling with cat")
        self.gladness += 15
        self.energy -= 25
        self.progress -= 5
        Bonya.gladness += 15
        Bonya.energy -= 30

    def to_chill(self):
        print("Student chilling")
        self.gladness += 25
        self.energy += 15
        self.progress -= 2.5

    def to_sleep(self):
        print("Student sleeping")
        self.gladness -= 5
        self.energy += 30
        self.progress -= 1

    def to_petting(self):
        print("Student petting his cat")
        self.gladness += 25
        self.energy -= 5
        self.progress -= 0.5
        Bonya.gladness += 25
        Bonya.energy += 5

    def is_alive(self):
        if self.gladness <= 0:
            print("Student in depression...")
            self.alive = False
        elif self.energy <= 0:
            print("Student overstrained...")
            self.alive = False
        elif self.progress <= 0:
            print("Student cast out...")
            self.alive = False
        elif self.progress >= 100:
            print("Student graduated!")
            self.alive = False
        elif Bonya.alive == False:
            print("Student in depression...")
            self.alive = False

    def end_day(self):
        print(f"Student gladness = {self.gladness}")
        print(f"Student energy = {self.energy}")
        print(f"Student progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " and " + Bonya.name + " life"
        print(f"{day:^50}")
        live_cube_student = random.randint(1, 5)
        if live_cube_student == 1:
            self.to_stroll()
        elif live_cube_student == 2:
            self.to_study()
        elif live_cube_student == 3:
            self.to_chill()
        elif live_cube_student == 4:
            self.to_sleep()
        elif live_cube_student == 5:
            self.to_petting()
        live_cube_cat = random.randint(1, 2)
        if live_cube_cat == 1:
            Bonya.to_sleep()
        elif live_cube_cat == 2:
            Bonya.to_chill()

        self.end_day()
        Bonya.end_day()
        self.is_alive()
        Bonya.is_alive()

Gregory = Student(name="Gregory")

for day in range(365):
    if Gregory.alive == False:
        break
    Gregory.live(day)
