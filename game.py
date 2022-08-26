import ui
from coordinates import Coordinates
from field import Field
from moves import Moves, AutomaticMoves
from placeholder import Placeholder


board_dim = ui.ask_board_dim()
board = Coordinates(int(board_dim[0]), int(board_dim[1]))
cell_size = board.get_cell_size()

start_position = ui.ask_position(board)
coordinates = Coordinates(int(start_position[0]), int(start_position[1]))

field = Field(board, cell_size)
placeholder = Placeholder(cell_size)
direction = Moves()
auto_direction = AutomaticMoves()

answer = ui.ask_trial()

if answer == 'n':
    a_count = 1

    while True:
        a_placeholder = ' ' * (cell_size - len(str(a_count))) + str(a_count)

        field.set_value(coordinates.x, coordinates.y, a_placeholder)
        auto_direction.set_possible_value(board, coordinates, cell_size, field, placeholder)
        a_count += 1

        if bool(auto_direction.numbers) is False and field.is_full():
            ui.print_solution()
            ui.print_board(field, board, cell_size)
            break
        elif auto_direction.moves is False:
            ui.print_solution_absence()
            break

        next_move = auto_direction.get_min_coord()
        coordinates = Coordinates(int(next_move[0]), int(next_move[1]))
        auto_direction.numbers = {}
        auto_direction.moves = False
else:
    if auto_direction.is_solvable(coordinates, cell_size, field, board, placeholder):
        field = Field(board, cell_size)
        count = 0

        while True:
            field.set_value(coordinates.x, coordinates.y, placeholder.x_placeholder)

            direction.set_possible_value(board, coordinates, cell_size, field, placeholder)
            ui.print_board(field, board, cell_size)
            count += 1

            if field.is_win(placeholder, board):
                ui.print_win()
                break
            elif direction.moves is False:
                ui.print_loss(count)
                break

            next_move = ui.ask_next_move(board, placeholder, field, cell_size)
            direction.del_possible_value(board, coordinates, cell_size, field, placeholder)
            field.set_value(coordinates.x, coordinates.y, placeholder.aster_placeholder)
            coordinates = Coordinates(int(next_move[0]), int(next_move[1]))

            direction.moves = False
    else:
        ui.print_solution_absence()
