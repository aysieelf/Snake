from src.core.snake import Snake
from src.effects.particle_system import ParticleSystem
from src.utils import constants as c
from src.utils.helpers import get_random_position


class FoodSystem:
    """
    The FoodSystem class is responsible for managing the food items in the game
    """
    def __init__(self, snake: Snake, particle_system: ParticleSystem):
        self._snake = snake
        self._particle_system = particle_system

        self._food_pos: list[int] = [0, 0]
        self._new_food: bool = True

        self._bonus_food_pos: list[int] | None = None
        self._bonus_food_spawn_timer: int = 0
        self._bonus_food_duration_timer: int = 0
        self._bonus_food_active: bool = False

    @property
    def food_pos(self) -> tuple[int, ...]:
        return tuple(self._food_pos)

    @property
    def new_food(self) -> bool:
        return self._new_food

    @property
    def bonus_food_pos(self) -> tuple[int, ...] | None:
        return tuple(self._bonus_food_pos) if self._bonus_food_pos else None

    @property
    def bonus_food_active(self) -> bool:
        return self._bonus_food_active

    @property
    def bonus_food_duration_timer(self) -> int:
        return self._bonus_food_duration_timer

    @property
    def bonus_food_spawn_timer(self) -> int:
        return self._bonus_food_spawn_timer

    def update_bonus_food(self, tail: list[int]) -> bool:
        """
        Update the bonus food state
        If the bonus food is active, handle the bonus food state
        If the bonus food spawn timer has reached the interval, spawn the bonus food

        Params:
            tail: list[int] - The tail of the snake

        Returns:
            bool - Whether the bonus food was collected or not
        """
        self._bonus_food_spawn_timer += 1 if self._bonus_food_pos is None else 0

        if self._bonus_food_spawn_timer == c.BONUS_FOOD_SPAWN_INTERVAL:
            self._spawn_bonus_food()

        if self._bonus_food_active:
            bonus_food_collected = self._handle_bonus_food(tail)
            if self._bonus_food_duration_timer >= c.BONUS_FOOD_DURATION:
                self.deactivate_bonus_food()
            return bonus_food_collected
        return False

    def _handle_bonus_food(self, tail: list[int]) -> bool:
        """
        Handle the bonus food state.
        If the bonus food was collected, grow the snake and deactivate the bonus food
        If the bonus food duration timer has reached the duration, deactivate the bonus food

        Params:
            tail: list[int] - The tail of the snake

        Returns:
            bool - Whether the bonus food was collected or not
        """
        if self._snake.get_head_position() == tuple(self._bonus_food_pos):
            self._collect_bonus_food(tail)
            return True
        else:
            self._bonus_food_duration_timer += 1
            return False

    def _collect_bonus_food(self, tail: list[int]) -> None:
        """
        Collect the bonus food
        Spawn particles at the bonus food position
        Grow the snake and deactivate the bonus food

        Params:
            tail: list[int] - The tail of the snake
        """
        bonus_pixel_pos = (
            self._bonus_food_pos[0] * c.CELL_SIZE,
            self._bonus_food_pos[1] * c.CELL_SIZE,
        )
        self._particle_system.spawn_particles(*bonus_pixel_pos, c.MINT_GREEN)

        self._snake.grow(tail)
        self.deactivate_bonus_food()

    def _spawn_bonus_food(self) -> None:
        """
        Spawn the bonus food
        Validate the bonus food position and set the bonus food state
        """
        self._bonus_food_pos = self._validate_food_position(bonus_food=True)
        self._bonus_food_spawn_timer = 0
        self._bonus_food_active = True
        self._bonus_food_duration_timer = 0

    def spawn_food(self) -> None:
        """
        Spawn the food
        Validate the food position and set the food state
        """
        if self._new_food:
            self._new_food = False
            self._food_pos = self._validate_food_position()

    def _validate_food_position(self, bonus_food: bool=False) -> list[int]:
        """
        Validate the food position
        Generate random positions until a valid position is found
        A valid position is one that is not occupied by the snake or another food item

        Params:
            bonus_food: bool - Whether the food is a bonus food or not

        Returns:
            list[int] - The valid food position
        """
        attempts = 0
        max_attempts = 100

        while attempts < max_attempts:
            new_pos = get_random_position()
            new_pos_tuple = tuple(new_pos)

            if bonus_food:
                if (
                    self.food_pos == new_pos_tuple
                    or new_pos_tuple in self._snake.positions
                ):
                    attempts += 1
                    continue

            else:
                if new_pos_tuple in self._snake.positions or (
                    self._bonus_food_active and new_pos_tuple == self._bonus_food_pos
                ):
                    attempts += 1
                    continue

            return new_pos

        return [1, 1]

    def deactivate_bonus_food(self) -> None:
        """
        Deactivate the bonus food
        Reset the bonus food state
        """
        self._bonus_food_active = False
        self._bonus_food_pos = None
        self._bonus_food_duration_timer = 0

    def reset(self) -> None:
        """
        Reset the food system
        """
        self._food_pos = [0, 0]
        self._new_food = True
        self._bonus_food_pos = None
        self._bonus_food_spawn_timer = 0
        self._bonus_food_duration_timer = 0
        self._bonus_food_active = False
