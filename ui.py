from invalid_input_error import InvalidInputError
from field import Field


def ask_position() -> str:
    while True:
        try:
            coordinates = input("Enter the knight's starting position: ").replace(' ', '')
            if not coordinates.isdigit() or len(coordinates) != 2 or\
                    (int(coordinates[0]) < 1 or int(coordinates[0]) > 8 or
                     int(coordinates[1]) < 1 or int(coordinates[1]) > 8):
                raise InvalidInputError
            return coordinates
        except InvalidInputError as error:
            print_error(error)


def print_error(error: InvalidInputError) -> None:
    print(error)


def print_board(field: Field) -> None:
    frame = ' ' + '-' * 19
    print(frame)
    for y in range(8, 0, -1):
        board_str = ' '.join([field.get_value(x, y) for x in range(1, 9)])
        print(f"{y}| {board_str} |")
    print(frame)
    print(' ' * 3, end='')
    [print(i, end=' ') for i in range(1, 9)]
