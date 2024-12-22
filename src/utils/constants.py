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

# GAME OVER SCREEN -------------------------------------------------------------
GAME_OVER_FONT_SIZE = 48
GAME_OVER_FONT = "impact"
GAME_OVER_TEXT = "GAME OVER"
GAME_OVER_TEXT_COLOR = TEXT_COLOR
GAME_OVER_TEXT_POS = 100
OVERLAY_ALPHA = 100

# INSTRUCTIONS -----------------------------------------------------------------
INSTRUCTIONS_FONT_SIZE = 14
INSTRUCTIONS_FONT = "arial"
INSTRUCTIONS_TEXT_0 = (
    "Use the arrow keys or WASD to move the snake"  # only in the start screen
)
INSTRUCTIONS_TEXT_1 = (
    "Press SPACE to start or pause/resume the game"  # only in the start screen
)
INSTRUCTIONS_TEXT_2 = "Press Q to quit the game"  # only in the game over screen
INSTRUCTIONS_TEXT_3 = "Press R to restart"  # only in the game over screen
INSTRUCTIONS_TEXT_4 = "Press Q to quit to main menu"  # only in the game over screen
INSTRUCTIONS_TEXT_5 = "Press Q again to quit the game"  # only in the start screen
INSTRUCTIONS_TEXT_COLOR = TEXT_COLOR
INSTRUCTIONS = [
    INSTRUCTIONS_TEXT_0,
    INSTRUCTIONS_TEXT_1,
    INSTRUCTIONS_TEXT_2,
    INSTRUCTIONS_TEXT_3,
    INSTRUCTIONS_TEXT_4,
    INSTRUCTIONS_TEXT_5,
]
INSTRUCTIONS_POS = 170

# SCOREBOARD -------------------------------------------------------------------
SCORE_FONT_SIZE = 20
SCORE_FONT = "arial bold"
SCORE_TEXT = "SCORE: "
SCORE_PADDING = 5
