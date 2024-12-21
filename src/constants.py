# WINDOW -----------------------------------------------------------------------
WINDOW_SIZE = 600  # width and height of the window
GRID_SIZE = 30  # number of cells in the grid (30x30)
CELL_SIZE = WINDOW_SIZE // GRID_SIZE  # size of each cell (20x20)

# SNAKE -----------------------------------------------------------------------
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

EYE_SIZE = 4
EYE_OFFSET_SIDE_FAR = 1
EYE_OFFSET_SIDE_NEAR = 13
EYE_OFFSET_NEAR = 3
EYE_OFFSET_FAR = 17
EYE_DEPTH = 4

# COLORS -----------------------------------------------------------------------
PASTEL_GREEN = (167, 217, 172)  # for snake
DARKER_PASTEL_GREEN = (126, 168, 130)  # for head of snake
PASTEL_PINK = (255, 198, 214)  # for food
PASTEL_BLUE = (173, 216, 230)  # for special effects
PASTEL_YELLOW = (253, 253, 150)  # for special effects

SOFT_LAVENDER = (230, 230, 250)  # for obstacles
MINT_GREEN = (152, 255, 152)  # for bonus food
PEACH = (255, 218, 185)  # for obstacles
BABY_BLUE = (137, 207, 240)  # for borders

TEXT_COLOR = (105, 105, 105)  # for text
SCORE_COLOR = (147, 112, 219)  # for score
GAME_OVER_COLOR = (255, 182, 193)  # for game over

GRID_COLOR = (240, 240, 240)  # for grid
BACKGROUND = (253, 245, 230)  # for background
