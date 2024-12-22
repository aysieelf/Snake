# WINDOW -----------------------------------------------------------------------
WINDOW_SIZE = 400  # width and height of the window
CELL_SIZE = 20  # number of cells in the grid (30x30)
GRID_SIZE = WINDOW_SIZE // CELL_SIZE  # size of each cell (20x20)

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

# SNAKE -----------------------------------------------------------------------
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

EYE_SIZE = 4
EYE_OFFSET_SIDE_FAR = 1
EYE_OFFSET_SIDE_NEAR = 13
EYE_OFFSET_NEAR = 2
EYE_OFFSET_FAR = 14
EYE_DEPTH = 4
EYE_DEPTH_UP = 1

# FOOD ------------------------------------------------------------------------
FOOD_SIZE = CELL_SIZE  # size of the food
BONUS_FOOD_SIZE = CELL_SIZE  # size of the bonus food

BONUS_FOOD_SPAWN_INTERVAL = 1200  # 20 seconds * 60 FPS
BONUS_FOOD_DURATION = 300  # 5 seconds * 60 FPS

# START SCREEN -----------------------------------------------------------------
# Title
TITLE_FONT = "impact"
TITLE_FONT_SIZE = 50
TITLE_TEXT = "SNAKE"
TITLE_COLOR = TEXT_COLOR
TITLE_Y_POS = 80

# Start Button
START_BUTTON_TEXT = "start game"
START_BUTTON_WIDTH = 180
START_BUTTON_HEIGHT = 50
START_BUTTON_TITLE_COLOR = TEXT_COLOR
START_BUTTON_TITLE_HOVER_COLOR = TEXT_COLOR
START_BUTTON_COLOR = SOFT_LAVENDER
START_BUTTON_HOVER_COLOR = PEACH
START_BUTTON_FONT_SIZE = 35



