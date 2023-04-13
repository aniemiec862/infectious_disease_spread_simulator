class PositionState:
    def __init__(self, x, y, speed, rotation):
        self.x = x
        self.y = y
        self.speed = speed
        self.rotation = rotation

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_speed(self, speed):
        self.speed = speed

    def set_rotation(self, rotation):
        self.rotation = rotation
