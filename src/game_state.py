from src.snake import Snake


class GameState:
    """
    Class to hold the game state

    Attributes:
        snake (Snake): The snake object controlling snake's position and movement
    """

    def __init__(self):
        self.snake = Snake()


    def reset(self) -> None:
        """
        Reset the game state
        Creates a new snake and resets all game parameters
        """
        self.snake = Snake()
