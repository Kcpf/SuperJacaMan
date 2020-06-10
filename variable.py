from funcoes import *

# Only square resolutions
RESOLUTION = (600, 600)

# Division can only be integer and even numbers
DIVISIONS = (15, 15)
WIDTH_SQUARE = (RESOLUTION[0] // DIVISIONS[0])
HEIGHT_SQUARE = (RESOLUTION[1] // DIVISIONS[1])
SQUARE_DIMENSIONS = (WIDTH_SQUARE, HEIGHT_SQUARE)
EXPLO_DIMENSIONS = (WIDTH_SQUARE*3, HEIGHT_SQUARE*3)
SQUARE_COLOR = (140, 140, 140) # Define the background color 

MAP = create_map(DIVISIONS)
MAP = modify_map(MAP, round(DIVISIONS[0]/2))
PLAYER_WIDTH = WIDTH_SQUARE
PLAYER_HEIGHT = HEIGHT_SQUARE

# 0 - Start screen
# 1 - Main game screen
# 2 - Game over screen (player 2)
# 3 - Game over screen (player 1)
SCREEN = 0

# Player states
STILL = 0
RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4