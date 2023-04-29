from .Person import Person, State
import random

class Disease:
    def __init__(self, spread_radius, incubation_time):
        self.spread_radius = spread_radius
        self.incubation_time = incubation_time

    def infect(self, person_1: Person, person_2: Person):
        if (person_1.is_healthy() and person_2.is_healthy()) or (person_1.is_healthy() is False and person_2.is_healthy() is False):
            return

        if person_1.is_healthy() is True:
            healthy_person, diseased_person = person_1, person_2
        else:
            healthy_person, diseased_person = person_2, person_1

        infection_chance = self.calculate_infection_chance(healthy_person, diseased_person)
        if random.randint(0, 100) < infection_chance:
            healthy_person.set_state(State.INFECTED)

    def calculate_infection_chance(self, healthy_person: Person, diseased_person: Person):
        chance = 100
        #TODO improve this calculation system, use other person parameters

        if healthy_person.has_a_mask() is True:
            chance -= 30
        if diseased_person.has_a_mask() is True:
            chance -= 60
        return chance
