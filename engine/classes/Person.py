from .PositionState import PositionState
import random

class Person:
    def __init__(self, x, y, speed, diseased=False, sex='M', age=20, rotation=0):
        self.sex = sex
        self.age = age
        self.x = x
        self.y = y
        self.speed = speed
        self.infected = False
        self.diseased = diseased
        self.vaccinated = False
        self.has_a_mask = False
        self.immune = False
        self.pregnant = False
        self.position_state = PositionState(x, y, speed, rotation)
        self.other_diseases_factor = 0

    def move(self, max_width, max_height, radius):
        dx = random.uniform(-self.speed, self.speed)
        dy = random.uniform(-self.speed, self.speed)
        if radius < self.x + dx < max_width - radius:
            self.x += dx
        if radius < self.y + dy < max_height - radius:
            self.y += dy


    def set_infected(self, value):
        if self.infected is True and value is False:
            self.immune = True
        self.infected = value

    def set_diseased(self, value):
        self.diseased = value

    def set_vaccinated(self, value):
        self.vaccinated = value

    def set_mask(self, value):
        self.has_a_mask = value

    def set_pregnant(self, value):
        self.pregnant = value

    def set_other_diseases_factor(self, value):
        self.other_diseases_factor = value
