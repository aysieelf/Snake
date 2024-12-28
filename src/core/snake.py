from src.utils import constants as c


class Snake:
    """
    Snake class that represents the snake in the game.
    """
    def __init__(self):
        self._length: int = c.SNAKE_SIZE
        self._positions: list[tuple[int, ...]] = [
            (c.GRID_SIZE // 2, c.GRID_SIZE // 2),  # middle of the grid
            (c.GRID_SIZE // 2 + 1, c.GRID_SIZE // 2),  # one cell to the left
        ]
        self._direction: tuple[int] = c.LEFT
        self._has_direction_changed: bool = False

    @property
    def length(self) -> int:
        return self._length

    @property
    def positions(self) -> tuple[tuple[int, ...], ...]:
        return tuple(self._positions)

    @property
    def direction(self) -> tuple[int]:
        return self._direction

    @property
    def has_direction_changed(self) -> bool:
        return self._has_direction_changed

    def get_head_position(self) -> tuple[int, ...]:
        """
        Get the current position of the snake's head.
        """
        return self.positions[0]

    def get_snake_body_positions(self) -> tuple[tuple[int, ...], ...]:
        """
        Get the current positions of the snake's body.
        """
        display_positions = []
        for grid_x, grid_y in self._positions:
            pixel_x = grid_x * c.CELL_SIZE
            pixel_y = grid_y * c.CELL_SIZE
            display_positions.append((pixel_x, pixel_y))

        return tuple(display_positions)

    def move(self) -> tuple[int, ...]:
        """
        Move the snake by one cell.

        Returns:
            tuple[int, int]: the tail of the snake
        """
        tail = self._positions.pop()
        new_head = self._get_next_head_position()
        self._positions.insert(0, new_head)
        self._has_direction_changed = False
        return tail

    def grow(self, tail: tuple[int, ...]) -> None:
        """
        Grow the snake by one cell, adding the tail to the end of the snake.
        """
        self._positions.append(tail)

    def _get_next_head_position(self) -> tuple[int, ...]:
        """
        Get the next position of the snake's head.

        Returns:
            tuple[int, int]: the next position of the snake's head
        """
        curr_head_x, curr_head_y = self._positions[0]
        return (
            curr_head_x + self._direction[0],
            curr_head_y + self._direction[1],
        )

    def change_direction(self, new_dir: tuple[int]) -> bool:
        """
        Change the direction of the snake.

        Args:
            new_dir (tuple[int]): the new direction

        Returns:
            bool: True if the direction has changed, False otherwise
        """
        if self._has_direction_changed:
            return False

        if (
            new_dir[0] + self._direction[0] == 0
            and new_dir[1] + self._direction[1] == 0
        ):
            return False

        if new_dir not in [c.UP, c.LEFT, c.RIGHT, c.DOWN]:
            return False

        self._direction = new_dir
        self._has_direction_changed = True
        return True
