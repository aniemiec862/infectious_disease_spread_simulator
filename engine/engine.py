class Engine:
    human_points = []
    def __init__(self, name):
    # pass starting parameters
        self.name = name

    def next_turn(self):
        for human in self.human_points:
            human.move()
