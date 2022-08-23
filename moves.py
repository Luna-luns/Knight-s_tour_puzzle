from coordinates import Coordinates
from field import Field


class Moves:
    def __init__(self):
        self.possible_moves = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
        self.new_coord_x = None
        self.new_coord_y = None

    def set_possible_value(self, board: Coordinates, coord: Coordinates, size: int, field: Field, x_placeholder: str):
        for elem in self.possible_moves:
            self.new_coord_x = coord.x + elem[0]
            self.new_coord_y = coord.y + elem[1]
            if 0 < self.new_coord_x <= board.x and 0 < self.new_coord_y <= board.y:
                number = self.count_possible_moves(board, field, coord, x_placeholder)
                moves_placeholder = ' ' * (size - 1) + number
                field.set_value(coord.x + elem[0], coord.y + elem[1], moves_placeholder)

    def count_possible_moves(self, board: Coordinates, field: Field, coord: Coordinates, x_placeholder: str) -> str:
        count = 0
        for elem in self.possible_moves:
            x = self.new_coord_x + elem[0]
            y = self.new_coord_y + elem[1]
            if 0 < x <= board.x and 0 < y <= board.y and field.get_value(x, y) != x_placeholder:
                count += 1
        return str(count)
