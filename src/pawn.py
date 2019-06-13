class Pawn:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Pawn):
            return NotImplemented
        return self.x == other.x and self.y == other.y
