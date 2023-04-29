from .classes.Person import Person, State
from .classes.Disease import Disease
import pygame
import random
import math

DOT_RADIUS = 10
SURFACE_COLOR = (255, 255, 255)
HEALTHY_PERSON_COLOR = (0, 255, 0)
INFECTED_PERSON_COLOR = (255, 255, 0)
DISEASED_PERSON_COLOR = (255, 0, 0)


class Engine:
    def __init__(self, width, height, people_count, diseased_count, infected_count, male_count, vaccinated_count, with_mask_count, immune_count, pregnant_count, disease_spread_radius, max_person_speed, incubation_time):
        self.width = width
        self.height = height
        self.people = []
        self.disease = Disease(disease_spread_radius, incubation_time)

        for _ in range(people_count):
            person = Person(
                x=random.randint(DOT_RADIUS, width - DOT_RADIUS),
                y=random.randint(DOT_RADIUS, height - DOT_RADIUS),
                speed=random.randint(1, max_person_speed))

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

    def draw(self, surface):
        surface.fill(SURFACE_COLOR)
        for person in self.people:
            state = person.get_state()
            if state == state.HEALTHY:
                color = HEALTHY_PERSON_COLOR
            elif state == state.INFECTED:
                color = INFECTED_PERSON_COLOR
            else:
                color = DISEASED_PERSON_COLOR
            pygame.draw.circle(surface, color, (person.get_position()), DOT_RADIUS)

    def update(self):
        for person in self.people:
            person.move(self.width, self.height, DOT_RADIUS)
            self.find_nearby_people(person)

    def find_nearby_people(self, person):
        x = person.get_position()[0]
        y = person.get_position()[1]
        r = self.disease.spread_radius

        for checked_person in self.people:
            checked_x_pos = checked_person.get_position()[0]
            checked_y_pos = checked_person.get_position()[1]

            if math.sqrt((x - checked_x_pos) ** 2 + (y - checked_y_pos) ** 2) <= r:
                self.disease.infect(person, checked_person)
