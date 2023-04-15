from .PositionState import PositionState
import random

class Person:
    def __init__(self, x, y, speed, diseased=False, sex='M', age=20, rotation=0):
        self.sex = sex
        self.age = age
        self.infected = False
        self.diseased = diseased
        self.vaccinated = False
        self.has_a_mask = False
        self.immune = False
        self.pregnant = False
        self.position_state = PositionState(x, y, speed, rotation)
        self.other_diseases_factor = 0

    def move(self, max_width, max_height, radius):
        dx = random.uniform(-self.position_state.speed, self.position_state.speed)
        dy = random.uniform(-self.position_state.speed, self.position_state.speed)
        if radius < self.position_state.x + dx < max_width - radius:
            self.position_state.x += dx
        if radius < self.position_state.y + dy < max_height - radius:
            self.position_state.y += dy

    def get_position(self):
        return self.position_state.x, self.position_state.y

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