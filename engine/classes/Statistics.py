class Statistics:
    def __init__(self, renderer, x_offset, y_offset, people, initial_people_count):
        self.renderer = renderer
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.people = people
        self.initial_people_count = initial_people_count

    def update(self):
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

        self.renderer.render_text("Statistics:", self.x_offset, self.y_offset, True)

        items_x_offset = self.x_offset + 20
        self.renderer.render_text(f"Alive: {people_count}/{self.initial_people_count}", items_x_offset, self.y_offset + 30)
        self.renderer.render_text(f"Deaths: {deaths}", items_x_offset, self.y_offset + 60)
        self.renderer.render_text(f"Infected: {infected}", items_x_offset, self.y_offset + 90)
        self.renderer.render_text(f"Diseased: {diseased}", items_x_offset, self.y_offset + 120)
        self.renderer.render_text(f"Immune: {immune}", items_x_offset, self.y_offset + 150)
        self.renderer.render_text(f"Vaccinated: {vaccinated}", items_x_offset, self.y_offset + 180)
