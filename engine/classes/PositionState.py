class PositionState:
    def __init__(self, x, y, velocity, rotation):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.rotation = rotation

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_velocity(self, velocity):
        self.velocity = velocity

    def set_rotation(self, rotation):
        self.rotation = rotation
