import random

from src.utils import constants as c


def get_random_position():
    """
    Get a random position on the grid
    """
    return [random.randint(1, c.GRID_SIZE - 2), random.randint(1, c.GRID_SIZE - 2)]
