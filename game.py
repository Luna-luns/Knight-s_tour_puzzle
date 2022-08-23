import ui
from coordinates import Coordinates
from field import Field
from moves import Moves


board_dim = ui.ask_board_dim()
board = Coordinates(int(board_dim[0]), int(board_dim[1]))
cell_size = board.get_cell_size()

start_position = ui.ask_position(board)
coordinates = Coordinates(int(start_position[0]), int(start_position[1]))

field = Field(board, cell_size)
x_placeholder = ' ' * (cell_size - 1) + 'X'
field.set_value(coordinates.x, coordinates.y, x_placeholder)

moves_placeholder = ' ' * (cell_size - 1)
direction = Moves()
direction.set_possible_value(board, coordinates, cell_size, field, x_placeholder)
ui.print_possible_moves()
ui.print_board(field, board, cell_size)
