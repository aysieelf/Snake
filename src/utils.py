import random

from src import constants as c


def get_random_position():
    """
    Get a random position on the grid
    """
    return [random.randint(1, c.GRID_SIZE - 1), random.randint(1, c.GRID_SIZE - 1)]
