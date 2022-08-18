class Coordinates:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_cell_size(self) -> int:
        return len(str(self.x * self.y))
