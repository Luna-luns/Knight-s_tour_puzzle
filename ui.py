from dimension_error import DimensionError
from position_error import PositionError
from field import Field
from coordinates import Coordinates
from move_error import MoveError
from placeholder import Placeholder
from  answer_error import AnswerError


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


def is_valid(coordinates: list, board: Coordinates) -> bool:
    return not coordinates[0].isdigit() and coordinates[1].isdigit() or len(coordinates) != 2 or\
                    (int(coordinates[0]) < 1 or int(coordinates[1]) < 1) or\
                    (int(coordinates[0]) > board.x or int(coordinates[1]) > board.y)


def ask_position(board: Coordinates) -> list:
    while True:
        try:
            coordinates = input("Enter the knight's starting position: ").split()
            if is_valid(coordinates, board):
                raise PositionError
            return coordinates
        except PositionError as error:
            print_error(error)


def ask_next_move(board: Coordinates, placeholder: Placeholder, field: Field, size: int) -> list:
    while True:
        try:
            coordinates = input('Enter your next move: ').split()
            if is_valid(coordinates, board) or\
                    field.get_value(int(coordinates[0]), int(coordinates[1])) == placeholder.x_placeholder or \
                    field.get_value(int(coordinates[0]), int(coordinates[1])) == '_' * size or\
                    field.get_value(int(coordinates[0]), int(coordinates[1])) == placeholder.aster_placeholder:
                raise MoveError
            return coordinates
        except MoveError as error:
            print(error, end='')


def ask_trial() -> str:
    while True:
        try:
            answer = input('Do you want to try the puzzle? (y/n): ').strip()
            if answer not in ('y', 'n'):
                raise AnswerError
            return answer
        except AnswerError as error:
            print(error)


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
    print()


def print_loss(num: int) -> None:
    print(f'\n\nNo more possible moves!\nYour knight visited {num} squares!')


def print_win() -> None:
    print('\n\nWhat a great tour! Congratulations!')


def print_solution_absence() -> None:
    print('No solution exists!')


def print_solution() -> None:
    print('\n' + "Here's the solution!")
