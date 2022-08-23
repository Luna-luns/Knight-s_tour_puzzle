from dimension_error import DimensionError
from position_error import PositionError
from field import Field
from coordinates import Coordinates


def ask_board_dim() -> list:
    while True:
        try:
            coordinates = input("Enter your board dimensions: ").split()
            if not coordinates[0].isdigit() and coordinates[1].isdigit() or len(coordinates) != 2 or \
                    (int(coordinates[0]) < 1 or int(coordinates[1]) < 1):
                raise DimensionError
            return coordinates
        except DimensionError as error:
            print_error(error)


def ask_position(coord: Coordinates) -> list:
    while True:
        try:
            coordinates = input("Enter the knight's starting position: ").split()
            if not coordinates[0].isdigit() and coordinates[1].isdigit() or len(coordinates) != 2 or\
                    (int(coordinates[0]) < 1 or int(coordinates[1]) < 1) or\
                    (int(coordinates[0]) > coord.x or int(coordinates[1]) > coord.y):
                raise PositionError
            return coordinates
        except PositionError as error:
            print_error(error)


def print_possible_moves():
    print('\n' + 'Here are the possible moves:')


def print_error(error: Exception) -> None:
    print(error)


def print_board(field: Field, board: Coordinates, size: int) -> None:
    frame = ' ' + '-' * (board.x * (size + 1) + 3)
    print(frame)
    for y in range(board.y, 0, -1):
        board_str = ' '.join([field.get_value(x, y) for x in range(1, board.x + 1)])
        print(f"{y}| {board_str} |")
    print(frame)
    print(' ' * 3, end='')
    [print(' ' * (size - 1) + f'{i}', end=' ') for i in range(1, board.x + 1)]
