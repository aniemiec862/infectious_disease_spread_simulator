from .classes.Person import Person
import pygame
import random

MAX_SPEED = 10
DOT_RADIUS = 10
SURFACE_COLOR = (255, 255, 255)
HEALTHY_PERSON_COLOR = (0, 255, 0)
INFECTED_PERSON_COLOR = (255, 255, 0)
DISEASED_PERSON_COLOR = (255, 0, 0)

class Engine:
    def __init__(self, width, height, no_people, no_diseased_people):
        self.width = width
        self.height = height
        self.people = []

        for i in range(no_people):
            person = Person(
                x=random.randint(DOT_RADIUS, width - DOT_RADIUS),
                y=random.randint(DOT_RADIUS, height - DOT_RADIUS),
                speed=random.randint(1, MAX_SPEED))

            if i < no_diseased_people:
                person.diseased = True

            self.people.append(person)

    def draw(self, surface):
        surface.fill(SURFACE_COLOR)
        for person in self.people:
            color = HEALTHY_PERSON_COLOR if not person.diseased else DISEASED_PERSON_COLOR
            pygame.draw.circle(surface, color, (person.get_position()), DOT_RADIUS)

    def update(self):
        for person in self.people:
            person.move(self.width, self.height, DOT_RADIUS)

