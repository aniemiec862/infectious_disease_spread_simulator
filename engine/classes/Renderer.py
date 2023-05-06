import pygame

from engine.classes.Person import State

BORDER_WIDTH = 3
HEALTHY_PERSON_COLOR = "#2ede28"
INFECTED_PERSON_COLOR = "#edcd15"
DISEASED_PERSON_COLOR = "#ed381c"
IMMUNE_PERSON_COLOR = "#47a5bf"
VACCINATED_PERSON_COLOR = "#0f5ca8"


class Renderer:
    def __init__(self, surface, dot_radius, surface_color):
        self.surface = surface
        self.dot_radius = dot_radius
        self.surface_color = surface_color
        self.font_normal = pygame.font.SysFont("Arial", 16)
        self.font_big = pygame.font.SysFont("Arial", 20)

    def get_person_colors(self, state, immune, vaccinated):
        if state == State.HEALTHY:
            fill_color = HEALTHY_PERSON_COLOR
        elif state == State.INFECTED:
            fill_color = INFECTED_PERSON_COLOR
        elif state == State.DISEASED:
            fill_color = DISEASED_PERSON_COLOR
        else:
            fill_color = self.surface_color

        border_color = None
        if immune is True:
            border_color = IMMUNE_PERSON_COLOR
        elif vaccinated is True:
            border_color = VACCINATED_PERSON_COLOR

        return fill_color, border_color

    def draw_person(self, state, immune, vaccinated, position):
        fill_color, border_color = self.get_person_colors(state, immune, vaccinated)
        pygame.draw.circle(self.surface, fill_color, position, self.dot_radius)
        if border_color is not None:
            pygame.draw.circle(self.surface, border_color, position, self.dot_radius, BORDER_WIDTH)

    def render_text(self, text, x, y, header = False):
        font = self.font_big if header else self.font_normal
        text = font.render(text, True, 'black')
        self.surface.blit(text, (x, y))