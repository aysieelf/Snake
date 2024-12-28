import random

from src.utils import constants as c


def get_random_position() -> list[int]:
    """
    Get a random position on the grid

    Returns:
        list[int]: A list with two integers representing the x and y coordinates
    """
    return [random.randint(1, c.GRID_SIZE - 2), random.randint(1, c.GRID_SIZE - 2)]
