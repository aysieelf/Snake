from src.snake import Snake


class GameState:
    """
    Class to hold the game state

    Attributes:
        snake (Snake): The snake object controlling snake's position and movement
    """

    def __init__(self):
        self.snake = Snake()
        self.score = 0
        self._frame_count = 0
        self.move_delay = 30

    def update(self):
        """Update game state including snake movement based on current speed"""
        self._frame_count += 1
        self._update_speed()

        if self._frame_count >= self.move_delay:
            self.snake.move()
            self._frame_count = 0

    def _update_speed(self):
        """Adjust snake speed based on score"""
        base_delay = 30
        min_delay = 5
        delay_step = 5

        new_delay = base_delay - (self.score // 5) * delay_step
        self.move_delay = max(min_delay, new_delay)

    def reset(self) -> None:
        """
        Reset the game state
        Creates a new snake and resets all game parameters
        """
        self.snake = Snake()
