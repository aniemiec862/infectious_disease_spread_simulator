from .Person import Person, State
import random


def calculate_infection_chance(healthy_person: Person, diseased_person: Person, hygiene_level):
    chance = 100

    if healthy_person.has_a_mask():
        chance -= 10
    if diseased_person.has_a_mask():
        chance -= 20
    if healthy_person.immune:
        chance -= 30
    if healthy_person.vaccinated:
        chance -= 60

    chance -= hygiene_level  # hygiene_level should be in range -20 - 20

    return chance


class Disease:
    def __init__(self, spread_radius, incubation_time, duration, hygiene_level):
        self.spread_radius = spread_radius
        self.incubation_time = incubation_time
        self.duration = duration
        self.hygiene_level = hygiene_level

    def infect(self, person_1: Person, person_2: Person):
        if (person_1.is_healthy() and person_2.is_healthy()) or (
                person_1.is_healthy() is False and person_2.is_healthy() is False):
            return

        if person_1.is_healthy():
            healthy_person, diseased_person = person_1, person_2
        else:
            healthy_person, diseased_person = person_2, person_1

        infection_chance = calculate_infection_chance(healthy_person, diseased_person, self.hygiene_level)
        if random.randint(0, 100) < infection_chance:
            healthy_person.set_state(State.INFECTED)
            rand_incubation_time = round(random.uniform(0.7 * self.incubation_time, 1.3 * self.incubation_time))
            healthy_person.set_time_to_next_state(rand_incubation_time)
