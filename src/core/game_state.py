from src.core.food_system import FoodSystem
from src.core.snake import Snake
from src.effects.particle_system import ParticleSystem
from src.utils import constants as c


class GameState:
    """
    Class to hold the game state

    Attributes:
        snake (Snake): The snake object controlling snake's position and movement
    """

    def __init__(self):
        self.snake: Snake = Snake()
        self.score: int = 0

        self._frame_count: int = 0
        self._move_delay: int = 20

        self.particle_system: ParticleSystem = ParticleSystem(None)
        self.food_system: FoodSystem = FoodSystem(self.snake, self.particle_system)

        self._game_over: bool = False
        self._paused: bool = True
        self._start_screen: bool = True

    @property
    def game_over(self) -> bool:
        return self._game_over

    @property
    def paused(self) -> bool:
        return self._paused

    @property
    def start_screen(self) -> bool:
        return self._start_screen

    def update(self) -> None:
        """
        Update game state including snake movement based on current speed
        """
        self._frame_count += 1
        self._update_speed()

        if not self._game_over and not self._paused:
            tail = self._update_movement()
            if self._check_wall_collision() or self._check_self_collision():
                self._game_over = True

            if self.snake.get_head_position() == tuple(self.food_system.food_pos):
                self._handle_food_collision(tail)

            if self.food_system.update_bonus_food(tail):
                self.score += 3

    def _check_wall_collision(self) -> bool:
        """
        Check if the snake has collided with the wall

        Returns:
            bool: True if the snake has collided with the wall, False otherwise
        """
        head_x, head_y = self.snake.get_head_position()
        return (
            head_x < 0 or head_x >= c.GRID_SIZE or head_y < 0 or head_y >= c.GRID_SIZE
        )

    def _check_self_collision(self) -> bool:
        """
        Check if the snake has collided with itself

        Returns:
            bool: True if the snake has collided with itself, False otherwise
        """
        head_pos = self.snake.get_head_position()
        return head_pos in self.snake.positions[1:]

    def _handle_food_collision(self, tail: list[int]) -> None:
        """
        Handle the collision between the snake and the food
        Grow the snake, increase the score and spawn new food

        Args:
            tail: list[int] - The tail of the snake
        """
        self.snake.grow(tail)
        self.score += 1
        self.food_system._new_food = True
        food_pixel_pos = (
            self.food_system.food_pos[0] * c.CELL_SIZE,
            self.food_system.food_pos[1] * c.CELL_SIZE,
        )
        self.particle_system.spawn_particles(*food_pixel_pos, c.PASTEL_PINK)

    def _update_movement(self) -> list[int]:
        """
        Update the snake movement based on the current speed

        Returns:
            list[int]: The tail of the snake
        """
        if self._frame_count >= self._move_delay:
            tail = self.snake.move()
            self._frame_count = 0
            return tail

    def _update_speed(self) -> None:
        """
        Adjust snake speed based on score
        """
        base_delay = 20
        min_delay = 5

        if self.score < 25:
            new_delay = base_delay - (self.score // 5) * 2
        else:
            first_phase = base_delay - (25 // 5) * 2
            remaining_score = self.score - 25
            new_delay = first_phase - (remaining_score // 5)

        self._move_delay = max(min_delay, new_delay)

    def start_game(self) -> None:
        """
        Start the game
        """
        self.reset()
        self._start_screen = False

    def exit_to_start_screen(self) -> None:
        """
        Exit the game to the start screen
        """
        self._start_screen = True

    def pause_game(self) -> None:
        """
        Pause the game
        """
        self._paused = True

    def continue_game(self) -> None:
        """
        Continue the game
        """
        self._paused = False

    def reset(self) -> None:
        """
        Reset the game state
        Creates a new snake and resets all game parameters
        """
        self.snake = Snake()
        self.score = 0
        self._frame_count = 0
        self._move_delay = 20
        self._game_over = False
        self._paused = False

        self.food_system = FoodSystem(self.snake, self.particle_system)
        self.food_system.reset()
