from .classes.Person import Person
import pygame
import random

MAX_SPEED = 20
DOT_RADIUS = 10
SURFACE_COLOR = (255, 255, 255)
HEALTHY_PERSON_COLOR = (0, 255, 0)
INFECTED_PERSON_COLOR = (255, 255, 0)
DISEASED_PERSON_COLOR = (255, 0, 0)

class Engine:
    def __init__(self, width, height, people_count, diseased_count, infected_count, male_count, vaccinated_count, with_mask_count, immune_count, pregnant_count):
        self.width = width
        self.height = height
        self.people = []

        for i in range(people_count):
            person = Person(
                x=random.randint(DOT_RADIUS, width - DOT_RADIUS),
                y=random.randint(DOT_RADIUS, height - DOT_RADIUS),
                speed=random.randint(1, MAX_SPEED))

            self.people.append(person)

        # Setting True/False parameters randomly
        counts = [diseased_count, infected_count, male_count, vaccinated_count, with_mask_count, immune_count, pregnant_count]
        fields = ["diseased", "infected", "is_male", "vaccinated", "with_mask", "immune", "pregnant"]
        for index in range(len(counts)):
            for i in range(counts[index]):
                random_person_index = random.randint(0, len(self.people)-1)
                field_name = fields[index]
                self.people[random_person_index].__setattr__(field_name, True)


    def draw(self, surface):
        surface.fill(SURFACE_COLOR)
        for person in self.people:
            color = HEALTHY_PERSON_COLOR if not person.diseased else DISEASED_PERSON_COLOR
            pygame.draw.circle(surface, color, (person.get_position()), DOT_RADIUS)

    def update(self):
        for person in self.people:
            person.move(self.width, self.height, DOT_RADIUS)

