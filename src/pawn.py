class Pawn:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Pawn):
            return NotImplemented
        return self.x == other.x and self.y == other.y


def translate_x(pawn, dx):
    return translate(pawn, dx, 0)


def translate_y(pawn, dy):
    return translate(pawn, 0, dy)


def translate(pawn, dx, dy):
    return Pawn(pawn.x + dx, pawn.y + dy)
