from .PositionState import PositionState
import math
import random
from enum import Enum


class State(Enum):
    HEALTHY = 1
    INFECTED = 2
    DISEASED = 3


class Person:
    def __init__(self, x, y, speed, state=State.HEALTHY, is_male=True, age=20, rotation=0):
        self.is_male = is_male
        self.age = age
        self.state = state
        self.vaccinated = False
        self.mask = False
        self.immune = False
        self.pregnant = False
        self.position_state = PositionState(x, y, speed, rotation)
        self.other_diseases_factor = 0  # 0 - 100, is used in death calculation
        self.time_to_incubate = None
        self.diseased_time = 0

    def move(self, max_width, max_height, radius):
        d_angle = random.uniform(-1, 1)
        self.position_state.rotation = (self.position_state.rotation + d_angle) % 360
        d_r = random.uniform(0, self.position_state.speed)
        dx = math.cos(self.position_state.rotation) * d_r
        dy = math.sin(self.position_state.rotation) * d_r

        if radius < self.position_state.x + dx < max_width - radius:
            self.position_state.x += int(dx)
        if radius < self.position_state.y + dy < max_height - radius:
            self.position_state.y += int(dy)

    def get_position(self):
        return self.position_state.x, self.position_state.y

    def get_state(self):
        return self.state

    def is_healthy(self):
        return self.state == State.HEALTHY

    def is_diseased(self):
        return self.state == State.DISEASED

    def is_infected(self):
        return self.state == State.INFECTED

    def set_state(self, state):
        self.state = state

    def set_vaccinated(self, value):
        self.vaccinated = value

    def set_mask(self, value):
        self.mask = value

    def has_a_mask(self):
        return self.mask

    def set_immune(self, value):
        self.immune = value

    def set_pregnant(self, value):
        self.pregnant = value

    def set_other_diseases_factor(self, value):
        self.other_diseases_factor = value

    def set_time_to_incubate(self, value):
        self.time_to_incubate = value

    def set_diseased_time(self, value):
        self.diseased_time = value

    def get_death_chance(self):
        chance = self.other_diseases_factor
        if self.is_diseased():
            if self.age < 30:
                chance += 10
            elif 30 <= self.age < 60:
                chance += 30
            else:
                chance += 50

            if self.pregnant:
                chance += 10

            if self.vaccinated:
                chance -= 30

            if self.immune:
                chance -= 10

        return chance
