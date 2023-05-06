from engine.classes.Person import State

BORDER_WIDTH = 3
HEALTHY_PERSON_COLOR = "#2ede28"
INFECTED_PERSON_COLOR = "#edcd15"
DISEASED_PERSON_COLOR = "#ed381c"
IMMUNE_PERSON_COLOR = "#47a5bf"
VACCINATED_PERSON_COLOR = "#0f5ca8"


class Legend:
    def __init__(self, renderer, x_offset, y_offset):
        self.renderer = renderer
        self.x_offset = x_offset
        self.y_offset = y_offset

    def draw_legend(self):
        self.renderer.render_text("Legend:", self.x_offset, self.y_offset, True)

        items_x_offset = self.x_offset + 20
        self.renderer.render_text("Healthy person", items_x_offset, self.y_offset + 30)
        self.renderer.draw_person(State.HEALTHY, False, False, (items_x_offset + 110, self.y_offset + 40))

        self.renderer.render_text("Infected person", items_x_offset, self.y_offset + 60)
        self.renderer.draw_person(State.INFECTED, False, False, (items_x_offset + 110, self.y_offset + 70))

        self.renderer.render_text("Diseased person", items_x_offset, self.y_offset + 90)
        self.renderer.draw_person(State.DISEASED, False, False, (items_x_offset + 115, self.y_offset + 100))

        self.renderer.render_text("Immune person", items_x_offset, self.y_offset + 120)
        self.renderer.draw_person(None, True, False, (items_x_offset + 110, self.y_offset + 130))

        self.renderer.render_text("Vaccinated person", items_x_offset, self.y_offset + 150)
        self.renderer.draw_person(None, False, True, (items_x_offset + 125, self.y_offset + 160))
