from coordinates import Coordinates
from field import Field
from placeholder import Placeholder


class Moves:
    def __init__(self):
        self.possible_moves = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
        self.new_coord_x = None
        self.new_coord_y = None
        self.moves = False

    def set_possible_value(self, board: Coordinates, coord: Coordinates, size: int, field: Field, placeholder: Placeholder) -> None:
        for elem in self.possible_moves:
            self.new_coord_x = coord.x + elem[0]
            self.new_coord_y = coord.y + elem[1]
            if 0 < self.new_coord_x <= board.x and 0 < self.new_coord_y <= board.y and\
                    field.get_value(self.new_coord_x, self.new_coord_y) != placeholder.aster_placeholder:
                number = self.count_possible_moves(board, field, placeholder)
                if number != 0:
                    self.moves = True
                moves_placeholder = ' ' * (size - 1) + number
                field.set_value(coord.x + elem[0], coord.y + elem[1], moves_placeholder)

    def count_possible_moves(self, board: Coordinates, field: Field, placeholder: Placeholder) -> str:
        count = 0
        for elem in self.possible_moves:
            x = self.new_coord_x + elem[0]
            y = self.new_coord_y + elem[1]
            if 0 < x <= board.x and 0 < y <= board.y and field.get_value(x, y) != placeholder.x_placeholder and\
                    field.get_value(x, y) != placeholder.aster_placeholder:
                count += 1
        return str(count)

    def del_possible_value(self, board: Coordinates, coord: Coordinates, size: int, field: Field, placeholder: Placeholder) -> None:
        for elem in self.possible_moves:
            self.new_coord_x = coord.x + elem[0]
            self.new_coord_y = coord.y + elem[1]
            if 0 < self.new_coord_x <= board.x and 0 < self.new_coord_y <= board.y and\
                    field.get_value(self.new_coord_x, self.new_coord_y) != placeholder.aster_placeholder:
                field.set_value(coord.x + elem[0], coord.y + elem[1], '_' * size)
