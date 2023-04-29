from .classes.Person import Person, State
from .classes.Disease import Disease
import pygame
import random
import math

DOT_RADIUS = 10
SURFACE_COLOR = (255, 255, 255)
HEALTHY_PERSON_COLOR = "#2ede28"
INFECTED_PERSON_COLOR = "#edcd15"
DISEASED_PERSON_COLOR = "#ed381c"
IMMUNE_PERSON_COLOR = "#47a5bf"
VACCINATED_PERSON_COLOR = "#0f5ca8"
BORDER_WIDTH = 3


class Engine:
    def __init__(self, width, height, people_count, diseased_count, infected_count, male_count, vaccinated_count, with_mask_count, immune_count, pregnant_count, disease_spread_radius, max_person_speed, incubation_time, disease_duration):
        self.width = width
        self.height = height
        self.people = []
        self.disease = Disease(disease_spread_radius, incubation_time, disease_duration)

        for _ in range(people_count):
            person = Person(
                x=random.randint(DOT_RADIUS, width - DOT_RADIUS),
                y=random.randint(DOT_RADIUS, height - DOT_RADIUS),
                speed=random.randint(1, max_person_speed),
                age=random.randint(10, 80)
            )

            person.set_other_diseases_factor(random.randint(0, 30))
            self.people.append(person)

        # Setting True/False parameters randomly
        counts = [diseased_count, infected_count, male_count, vaccinated_count, with_mask_count, immune_count, pregnant_count]
        fields = ["diseased", "infected", "is_male", "vaccinated", "mask", "immune", "pregnant"]
        for index in range(len(counts)):
            for _ in range(counts[index]):
                random_person_index = random.randint(0, len(self.people)-1)
                field_name = fields[index]
                if field_name == 'diseased':
                    self.people[random_person_index].set_state(State.DISEASED)
                elif field_name == 'infected':
                    self.people[random_person_index].set_state(State.INFECTED)
                else:
                    self.people[random_person_index].__setattr__(field_name, True)

    @staticmethod
    def get_person_colors(person):
        state = person.get_state()
        if state == state.HEALTHY:
            fill_color = HEALTHY_PERSON_COLOR
        elif state == state.INFECTED:
            fill_color = INFECTED_PERSON_COLOR
        else:
            fill_color = DISEASED_PERSON_COLOR

        border_color = None
        if person.immune is True:
            border_color = IMMUNE_PERSON_COLOR
        elif person.vaccinated is True:
            border_color = VACCINATED_PERSON_COLOR

        return fill_color, border_color

    def draw(self, surface):
        surface.fill(SURFACE_COLOR)
        for person in self.people:
            fill_color, border_color = self.get_person_colors(person)
            pygame.draw.circle(surface, fill_color, (person.get_position()), DOT_RADIUS)
            if border_color is not None:
                pygame.draw.circle(surface, border_color, (person.get_position()), DOT_RADIUS, BORDER_WIDTH)

    def update(self):
        for person in self.people:
            person.move(self.width, self.height, DOT_RADIUS)
            self.possibly_infect_nearby_people(person)
            self.calculate_incubation_time(person)
            self.calculate_diseased_time(person)

    def possibly_infect_nearby_people(self, person):
        x = person.get_position()[0]
        y = person.get_position()[1]
        r = self.disease.spread_radius

        for checked_person in self.people:
            checked_x_pos = checked_person.get_position()[0]
            checked_y_pos = checked_person.get_position()[1]

            if math.sqrt((x - checked_x_pos) ** 2 + (y - checked_y_pos) ** 2) <= r:
                self.disease.infect(person, checked_person)

    @staticmethod
    def calculate_incubation_time(person):
        if person.time_to_incubate is not None:
            if person.time_to_incubate > 0:
                person.set_time_to_incubate(person.time_to_incubate - 1)
            else:
                person.set_time_to_incubate(None)
                person.set_state(State.DISEASED)

    def calculate_diseased_time(self, person):
        if person.is_diseased():
            if person.diseased_time < self.disease.duration:
                person.set_diseased_time(person.diseased_time + 1)
            else:
                if random.randint(0, 100) < person.get_death_chance():
                    self.people.remove(person)
                    print(len(self.people))
                else:
                    person.set_diseased_time(0)
                    person.set_state(State.HEALTHY)
                    person.set_immune(True)
