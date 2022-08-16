class Field:
    def __init__(self):
        self.field = [['_' for _ in range(0, 8)] for _ in range(0, 8)]

    def get_value(self, x: int, y: int) -> str:
        """Возвращает то, что лежит в поле ("Х" или "_")"""
        return self.field[x - 1][y - 1]

    def set_value(self, x: int, y: int, value: str) -> None:
        self.field[x - 1][y - 1] = value
