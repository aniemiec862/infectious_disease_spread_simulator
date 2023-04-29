import pygame


class Statistics:
    def __init__(self, offset, people, initial_people_count):
        self.x_offset = offset
        self.y_offset = 10
        self.people = people
        self.initial_people_count = initial_people_count
        self.font = pygame.font.SysFont("Arial", 16)

    def update(self, surface):
        people_count = len(self.people)
        deaths = self.initial_people_count - people_count
        infected = diseased = immune = vaccinated = 0

        for person in self.people:
            if person.is_infected():
                infected += 1
            if person.is_diseased():
                diseased += 1
            if person.immune:
                immune += 1
            if person.vaccinated:
                vaccinated += 1

        self.render_text(surface, f"Alive: {people_count}", self.x_offset, self.y_offset)
        self.render_text(surface, f"Deaths: {deaths}", self.x_offset, self.y_offset + 20)
        self.render_text(surface, f"Infected: {infected}", self.x_offset, self.y_offset + 40)
        self.render_text(surface, f"Diseased: {diseased}", self.x_offset, self.y_offset + 60)
        self.render_text(surface, f"Immune: {immune}", self.x_offset, self.y_offset + 80)
        self.render_text(surface, f"Vaccinated: {vaccinated}", self.x_offset, self.y_offset + 100)

    def render_text(self, surface, text, x, y):
        text = self.font.render(text, True, 'black')
        surface.blit(text, (x, y))


