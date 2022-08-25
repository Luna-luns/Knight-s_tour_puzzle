class Placeholder:
    def __init__(self, cell_size: int):
        self.cell_size = cell_size
        self.x_placeholder = ' ' * (self.cell_size - 1) + 'X'
        self.aster_placeholder = ' ' * (self.cell_size - 1) + '*'
