import unittest
from unittest.mock import patch

from src.core.snake import Snake
from src.utils import constants as c


class SnakeShould(unittest.TestCase):

    def test_init_initializesSuccessfully(self):
        snake = Snake()
        self.assertIsNotNone(snake)

    def test_init_setsLengthToTwo(self):
        snake = Snake()
        self.assertEqual(2, snake.length)

    def test_init_setsPositions(self):
        snake = Snake()
        self.assertEqual(
            ((10, 10), (11, 10)),
            snake.positions,
        )

    def test_init_setsDirection(self):
        snake = Snake()
        self.assertEqual((-1, 0), snake.direction)

    def test_init_setsHasDirectionChangedToFalse(self):
        snake = Snake()
        self.assertFalse(snake.has_direction_changed)

    def test_getHeadPosition_returnsHeadPosition(self):
        snake = Snake()
        self.assertEqual((10, 10), snake.get_head_position())

    def test_getSnakeBodyPositions_returnsBodyPositions(self):
        snake = Snake()
        self.assertEqual(
            ((200, 200), (220, 200)),
            snake.get_snake_body_positions(),
        )

    def test_move_returnsTail(self):
        snake = Snake()
        with patch.object(snake, "_get_next_head_position", return_value=(9, 10)):
            tail = snake.move()
            self.assertEqual((11, 10), tail)

    def test_move_updatesPositions(self):
        snake = Snake()
        with patch.object(snake, "_get_next_head_position", return_value=(9, 10)):
            snake.move()
            self.assertEqual(
                ((9, 10), (10, 10)),
                snake.positions,
            )

    def test_move_setsHasDirectionChangedToFalse(self):
        snake = Snake()
        with patch.object(snake, "_get_next_head_position", return_value=(9, 10)):
            snake.move()
            self.assertFalse(snake.has_direction_changed)

    def test_grow_addsTailToPositions(self):
        snake = Snake()
        snake.grow((8, 10))
        self.assertEqual(
            ((10, 10), (11, 10), (8, 10)),
            snake.positions,
        )

    def test_getNextHeadPosition_returnsNextHeadPosition(self):
        snake = Snake()
        self.assertEqual((9, 10), snake._get_next_head_position())

    def test_changeDirection_validDirection_returnsTrue(self):
        snake = Snake()
        self.assertTrue(snake.change_direction(c.UP))

    def test_changeDirection_validDirection_updatesDirection(self):
        snake = Snake()
        snake.change_direction(c.UP)
        self.assertEqual(c.UP, snake.direction)

    def test_changeDirection_validDirection_setsHasDirectionChangedTrue(self):
        snake = Snake()
        snake.change_direction(c.UP)
        self.assertTrue(snake.has_direction_changed)

    def test_changeDirection_oppositeDirection_returnsFalse(self):
        snake = Snake()  # LEFT
        self.assertFalse(snake.change_direction(c.RIGHT))

    def test_changeDirection_oppositeDirection_doesNotUpdateDirection(self):
        snake = Snake()  # LEFT
        snake.change_direction(c.RIGHT)
        self.assertEqual(c.LEFT, snake.direction)

    def test_changeDirection_invalidDirection_returnsFalse(self):
        snake = Snake()
        self.assertFalse(snake.change_direction((2, 2)))

    def test_changeDirection_invalidDirection_doesNotUpdateDirection(self):
        snake = Snake()
        snake.change_direction((2, 2))
        self.assertEqual(c.LEFT, snake.direction)

    def test_changeDirection_afterDirectionChanged_returnsFalse(self):
        snake = Snake()
        snake.change_direction(c.UP)
        self.assertFalse(snake.change_direction(c.RIGHT))

    def test_changeDirection_afterDirectionChanged_doesNotUpdateDirection(self):
        snake = Snake()
        snake.change_direction(c.UP)
        snake.change_direction(c.RIGHT)
        self.assertEqual(c.UP, snake.direction)
