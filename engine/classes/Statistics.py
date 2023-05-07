class Statistics:
    def __init__(self, renderer, x_offset, y_offset, people, initial_people_count, initial_infected_count):
        self.renderer = renderer
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.people = people
        self.initial_people_count = initial_people_count
        self.dead = self.immune_not_infected = self.immune = 0
        self.infected_and_diseased = initial_infected_count

    def update(self):
        people_count = len(self.people)
        deaths = self.initial_people_count - people_count
        infected = diseased = immune = vaccinated = immune_not_infected = 0

        for person in self.people:
            if person.is_infected():
                infected += 1
            if person.is_diseased():
                diseased += 1
            if person.immune:
                immune += 1
            if person.vaccinated:
                vaccinated += 1
            if person.immune and not person.is_infected():
                immune_not_infected += 1

        self.infected_and_diseased = infected + diseased
        self.dead = deaths
        self.immune_not_infected = immune_not_infected
        self.immune = immune

        self.renderer.render_text("Statistics:", self.x_offset, self.y_offset, True)

        items_x_offset = self.x_offset + 20
        self.renderer.render_text(f"Alive: {people_count}/{self.initial_people_count}", items_x_offset,
                                  self.y_offset + 30)
        self.renderer.render_text(f"Deaths: {deaths}", items_x_offset, self.y_offset + 60)
        self.renderer.render_text(f"Infected: {infected}", items_x_offset, self.y_offset + 90)
        self.renderer.render_text(f"Diseased: {diseased}", items_x_offset, self.y_offset + 120)
        self.renderer.render_text(f"Immune: {immune}", items_x_offset, self.y_offset + 150)
        self.renderer.render_text(f"Vaccinated: {vaccinated}", items_x_offset, self.y_offset + 180)

    def get_susceptible(self):
        return self.initial_people_count - self.dead - self.infected_and_diseased - self.immune_not_infected

    def get_dead_and_recovered(self):
        return self.dead + self.immune

    def get_infected_and_diseased(self):
        return self.infected_and_diseased
