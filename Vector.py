class Vec2:
    x = 0
    y = 0
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def to_string(self):
        return f"({self.x}, {self.y})"