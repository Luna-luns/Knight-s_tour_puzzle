from coordinates import Coordinates
from field import Field


class Moves:
    def __init__(self):
        self.possible_moves = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

    def set_possible_value(self, board: Coordinates, coord: Coordinates, placeholder: str, field: Field):
        for elem in self.possible_moves:
            if 0 < coord.x + elem[0] <= board.x and 0 < coord.y + elem[1] <= board.y:
                field.set_value(coord.x + elem[0], coord.y + elem[1], placeholder)
