import random

class Person:
    # age
    # sex
    # other_diseases_factor / Disease class
    # is_vaccinated
    # has_a_mask
    # is_immune
    # is_pregnant

    def __init__(self, x, y, speed, infected=False, diseased=False):
        self.x = x
        self.y = y
        self.speed = speed
        self.infected = infected
        self.diseased = diseased

    def move(self, max_width, max_height, radius):
        dx = random.uniform(-self.speed, self.speed)
        dy = random.uniform(-self.speed, self.speed)
        if radius < self.x + dx < max_width - radius:
            self.x += dx
        if radius < self.y + dy < max_height - radius:
            self.y += dy
