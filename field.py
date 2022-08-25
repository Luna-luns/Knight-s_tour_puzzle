from coordinates import Coordinates
from placeholder import Placeholder


class Field:
    def __init__(self, board: Coordinates, size: int):
        self.field = [['_' * size for _ in range(0, board.y)] for _ in range(0, board.x)]

    def get_value(self, x: int, y: int) -> str:
        """Возвращает то, что лежит в поле ("Х" или "_")"""
        return self.field[x - 1][y - 1]

    def set_value(self, x: int, y: int, value: str) -> None:
        self.field[x - 1][y - 1] = value

    def is_win(self, placeholder: Placeholder, board: Coordinates) -> bool:
        result = 0
        matrix_size = board.x * board.y

        for elem in self.field:
            result += elem.count(placeholder.aster_placeholder)

        return result == matrix_size - 1
