from src import constants as c
from src.snake import Snake
from src.utils import get_random_position


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
        self._move_delay = 20

        self._food_pos = [0, 0]
        self._new_food = True

        self._bonus_food_pos = None
        self._bonus_food_spawn_timer = 0
        self._bonus_food_duration_timer = 0
        self._bonus_food_active = False

        self._game_over = False
        self._paused = False
        self._start_screen = True

    @property
    def food_pos(self):
        return tuple(self._food_pos)

    @property
    def new_food(self):
        return self._new_food

    @property
    def bonus_food_pos(self):
        return tuple(self._bonus_food_pos)

    @property
    def bonus_food_active(self):
        return self._bonus_food_active

    @property
    def bonus_food_duration_timer(self):
        return self._bonus_food_duration_timer

    @property
    def bonus_food_spawn_timer(self):
        return self._bonus_food_spawn_timer

    @property
    def game_over(self):
        return self._game_over

    @property
    def paused(self):
        return self._paused

    @property
    def start_screen(self):
        return self._start_screen

    def update(self):
        """Update game state including snake movement based on current speed"""
        self._frame_count += 1
        self._update_speed()

        if not self._game_over and not self._paused:
            tail = self._update_movement()
            if self._check_wall_collision() or self._check_self_collision():
                self._game_over = True
            self._handle_food_collision(tail)
            self._update_bonus_food(tail)

    def _check_wall_collision(self):
        head_x, head_y = self.snake.get_head_position()
        return (
            head_x < 0 or head_x >= c.GRID_SIZE or head_y < 0 or head_y >= c.GRID_SIZE
        )

    def _check_self_collision(self):
        head_pos = self.snake.get_head_position()
        return head_pos in self.snake.positions[1:]

    def _update_bonus_food(self, tail):
        self._bonus_food_spawn_timer += 1 if self._bonus_food_pos is None else 0

        if self._bonus_food_spawn_timer == c.BONUS_FOOD_SPAWN_INTERVAL:
            self._spawn_bonus_food()

        if self._bonus_food_active:
            self._handle_bonus_food(tail)
            if self._bonus_food_duration_timer >= c.BONUS_FOOD_DURATION:
                self._deactivate_bonus_food()

    def _spawn_bonus_food(self):
        self._bonus_food_pos = self._validate_food_position(bonus_food=True)
        self._bonus_food_spawn_timer = 0
        self._bonus_food_active = True
        self._bonus_food_duration_timer = 0

    def _handle_bonus_food(self, tail):
        if self.snake.get_head_position() == tuple(self._bonus_food_pos):
            self._collect_bonus_food(tail)
        else:
            self._bonus_food_duration_timer += 1

    def _collect_bonus_food(self, tail):
        self.snake.grow(tail)
        self.score += 3
        self._deactivate_bonus_food()

    def _deactivate_bonus_food(self):
        self._bonus_food_active = False
        self._bonus_food_pos = None
        self._bonus_food_duration_timer = 0

    def _handle_food_collision(self, tail):
        if self.snake.get_head_position() == tuple(self._food_pos):
            self.snake.grow(tail)
            self.score += 1
            self._new_food = True

    def _update_movement(self):
        if self._frame_count >= self._move_delay:
            tail = self.snake.move()
            self._frame_count = 0
            return tail

    def _update_speed(self):
        """Adjust snake speed based on score"""
        base_delay = 20
        min_delay = 5

        if self.score < 25:
            new_delay = base_delay - (self.score // 5) * 2
        else:
            first_phase = base_delay - (25 // 5) * 2
            remaining_score = self.score - 25
            new_delay = first_phase - (remaining_score // 5)

        self._move_delay = max(min_delay, new_delay)

    def create_food(self):
        if self._new_food:
            self._new_food = False
            self._food_pos = self._validate_food_position()

    def _validate_food_position(self, bonus_food=False):
        attempts = 0
        max_attempts = 100

        while attempts < max_attempts:
            new_pos = get_random_position()
            new_pos_tuple = tuple(new_pos)

            if bonus_food:
                if (
                    self.food_pos == new_pos_tuple
                    or new_pos_tuple in self.snake.positions
                ):
                    attempts += 1
                    continue

            else:
                if (
                    self._bonus_food_active and new_pos_tuple == self._bonus_food_pos
                ) or new_pos_tuple in self.snake.positions:
                    attempts += 1
                    continue

            return new_pos

    def start_game(self):
        self._start_screen = False

    def exit_to_start_screen(self):
        self._start_screen = True

    def pause_game(self):
        self._paused = True

    def continue_game(self):
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
        self._food_pos = [0, 0]
        self._new_food = True
        self._bonus_food_pos = None
        self._bonus_food_spawn_timer = 0
        self._bonus_food_duration_timer = 0
        self._bonus_food_active = False
        self._game_over = False
        self._paused = False
