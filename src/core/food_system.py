from src.utils import constants as c
from src.utils.helpers import get_random_position


class FoodSystem:
    def __init__(self, snake):
        self._snake = snake
        self._food_pos = [0, 0]
        self._new_food = True

        self._bonus_food_pos = None
        self._bonus_food_spawn_timer = 0
        self._bonus_food_duration_timer = 0
        self._bonus_food_active = False

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

    def update_bonus_food(self, tail):
        self._bonus_food_spawn_timer += 1 if self._bonus_food_pos is None else 0

        if self._bonus_food_spawn_timer == c.BONUS_FOOD_SPAWN_INTERVAL:
            self._spawn_bonus_food()

        if self._bonus_food_active:
            bonus_food_collected = self._handle_bonus_food(tail)
            if self._bonus_food_duration_timer >= c.BONUS_FOOD_DURATION:
                self.deactivate_bonus_food()
            return bonus_food_collected
        return False

    def _handle_bonus_food(self, tail):
        if self._snake.get_head_position() == tuple(self._bonus_food_pos):
            self._collect_bonus_food(tail)
            return True
        else:
            self._bonus_food_duration_timer += 1
            return False

    def _collect_bonus_food(self, tail):
        self._snake.grow(tail)
        self.deactivate_bonus_food()

    def _spawn_bonus_food(self):
        self._bonus_food_pos = self._validate_food_position(bonus_food=True)
        self._bonus_food_spawn_timer = 0
        self._bonus_food_active = True
        self._bonus_food_duration_timer = 0

    def spawn_food(self):
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
                    or new_pos_tuple in self._snake.positions
                ):
                    attempts += 1
                    continue

            else:
                if (
                    self._bonus_food_active and new_pos_tuple == self._bonus_food_pos
                ) or new_pos_tuple in self._snake.positions:
                    attempts += 1
                    continue

            return new_pos

    def deactivate_bonus_food(self):
        self._bonus_food_active = False
        self._bonus_food_pos = None
        self._bonus_food_duration_timer = 0

    def reset(self):
        self._food_pos = [0, 0]
        self._new_food = True
        self._bonus_food_pos = None
        self._bonus_food_spawn_timer = 0
        self._bonus_food_duration_timer = 0
        self._bonus_food_active = False
