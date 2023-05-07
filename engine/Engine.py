from .classes.Legend import Legend
from .classes.Person import Person, State
from .classes.Disease import Disease
from .classes.Renderer import Renderer
from .classes.Statistics import Statistics
from .classes.StatsGraph import StatsGraph
import random
import math

SURFACE_COLOR = (255, 255, 255)
DOT_RADIUS = 10

STATS_OFFSET_X = 40
STATS_OFFSET_Y = 10
LEGEND_OFFSET_Y = 230
GRAPH_OFFSET_X = 200
GRAPH_OFFSET_Y = 10

class Engine:
    def __init__(self, surface, width, height, people_count, diseased_count, infected_count, male_count,
                 vaccinated_count, with_mask_count, immune_count, pregnant_count, disease_spread_radius,
                 max_person_speed, incubation_time, disease_duration, hygiene_level, display_graph):
        self.surface = surface
        self.width = width
        self.height = height
        self.people = []
        self.disease = Disease(disease_spread_radius, incubation_time, disease_duration, hygiene_level)
        self.renderer = Renderer(surface, DOT_RADIUS, SURFACE_COLOR)

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
        counts = [diseased_count, infected_count, male_count, vaccinated_count, with_mask_count, immune_count,
                  pregnant_count]
        fields = ["diseased", "infected", "is_male", "vaccinated", "mask", "immune", "pregnant"]
        for index in range(len(counts)):
            for _ in range(counts[index]):
                random_person_index = random.randint(0, len(self.people) - 1)
                field_name = fields[index]
                if field_name == 'diseased':
                    self.people[random_person_index].set_state(State.DISEASED)
                    rand_disease_time = round(random.uniform(0.7 * disease_duration, 1.3 * disease_duration))
                    self.people[random_person_index].set_time_to_next_state(rand_disease_time)
                elif field_name == 'infected':
                    self.people[random_person_index].set_state(State.INFECTED)
                    rand_incubation_time = round(random.uniform(0.7 * incubation_time, 1.3 * incubation_time))
                    self.people[random_person_index].set_time_to_next_state(rand_incubation_time)
                else:
                    self.people[random_person_index].__setattr__(field_name, True)

        self.statistics = Statistics(self.renderer, STATS_OFFSET_X + width, STATS_OFFSET_Y, self.people, people_count, diseased_count + infected_count)
        self.legend = Legend(self.renderer, STATS_OFFSET_X + width, LEGEND_OFFSET_Y)

        if display_graph:
            self.stats_graph = StatsGraph(self.renderer, width + GRAPH_OFFSET_X, GRAPH_OFFSET_Y)
        else:
            self.stats_graph = None

    def draw(self):
        self.surface.fill(SURFACE_COLOR)
        for person in self.people:
            self.renderer.draw_person(person.state, person.immune, person.vaccinated, (person.get_position()))

        self.statistics.update()
        self.legend.draw_legend()
        if self.stats_graph is not None:
            self.stats_graph.update(self.statistics.get_susceptible(), self.statistics.get_infected_and_diseased(), self.statistics.get_dead_and_recovered())

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

    def calculate_incubation_time(self, person):
        if person.is_infected():
            if person.time_to_next_state > 0:
                person.set_time_to_next_state(person.time_to_next_state - 1)
            else:
                if person.immune:
                    person.set_state(State.HEALTHY)
                    person.set_time_to_next_state(None)
                else:
                    person.set_state(State.DISEASED)
                    rand_disease_time = round(random.uniform(0.7 * self.disease.duration, 1.3 * self.disease.duration))
                    person.set_time_to_next_state(rand_disease_time)

    def calculate_diseased_time(self, person):
        if person.is_diseased():
            if person.time_to_next_state > 0:
                person.set_time_to_next_state(person.time_to_next_state - 1)
            else:
                if random.randint(0, 100) < person.get_death_chance():
                    self.people.remove(person)
                else:
                    person.set_time_to_next_state(None)
                    person.set_state(State.HEALTHY)
                    person.set_immune(True)
