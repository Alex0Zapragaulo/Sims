import random

class Live:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.energy = 50
        self.alive = True
        print(f'{self.name}')

    def to_stroll(self):
        print("Strolling")
        self.gladness += 3
        self.energy -= 2

    def to_chill(self):
        print("Chilling")
        self.gladness -= 2
        self.energy += 1.2

    def to_play(self):
        print("Playing")
        self.gladness += 5
        self.energy -= 3.5

    def to_sleep(self):
        print("Sleeping")
        self.gladness -= 5
        self.energy += 4

    def is_alive(self):
        if self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.energy <= 0:
            print("Overstrain...")
            self.alive = False

    def end_day(self):
        print(f"Gladness = {round(self.gladness, 2)}")
        print(f"Energy = {round(self.energy, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:^50}")
        live_cube = random.randint(1,4)
        if live_cube == 1:
            self.to_stroll()
        elif live_cube == 2:
            self.to_play()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_sleep()

        self.end_day()
        self.is_alive()

Luna = Live(name = "Luna")

for day in range(365):
    if Luna.alive == False:
        break
    Luna.live(day)