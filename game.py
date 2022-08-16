import ui
from coordinates import Coordinates
from field import Field


start_position = ui.ask_position()
coordinates = Coordinates(int(start_position[0]), int(start_position[1]))
field = Field()
field.set_value(coordinates.x, coordinates.y, 'X')
ui.print_board(field)
