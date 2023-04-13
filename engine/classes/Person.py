from PositionState import PositionState


class Person:
    def __init__(self, name, sex, age, x=0, y=0, velocity=0, rotation=0):
        self.name = name
        self.sex = sex
        self.age = age
        self.is_infected = False
        self.is_diseased = False
        self.is_vaccinated = False
        self.has_a_mask = False
        self.is_immune = False
        self.is_pregnant = False
        self.position_state = PositionState(x, y, velocity, rotation)
        self.other_diseases_factor = 0

    def move(self):
        None


    def set_infected(self, value):
        if self.is_infected is True and value is False:
            self.is_immune = True
        self.is_infected = value

    def set_diseased(self, value):
        self.is_diseased = value

    def set_vaccinated(self, value):
        self.is_vaccinated = value

    def set_mask(self, value):
        self.is_mask = value

    def set_pregnant(self, value):
        self.is_pregnant = value

    def set_other_diseases_factor(self, value):
        self.other_diseases_factor = value
