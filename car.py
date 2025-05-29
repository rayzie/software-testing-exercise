class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def change_speed(self, change):
        if change < 0:
            if self.speed + change < 0:
                self.speed = 0
            else:
                self.speed += change
        else:
            self.speed += change

        self.step()

    def get_current_speed(self):
        return self.speed

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time == 0:
            raise Exception("Divide by 0! Car did not move!")
        else:
            return self.odometer / self.time