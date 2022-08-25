import ui
from coordinates import Coordinates
from field import Field
from moves import Moves
from placeholder import Placeholder


board_dim = ui.ask_board_dim()
board = Coordinates(int(board_dim[0]), int(board_dim[1]))
cell_size = board.get_cell_size()

start_position = ui.ask_position(board)
coordinates = Coordinates(int(start_position[0]), int(start_position[1]))

field = Field(board, cell_size)
placeholder = Placeholder(cell_size)
direction = Moves()

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
