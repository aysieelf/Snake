import unittest
from unittest.mock import patch

from src.core.snake import Snake
from src.utils import constants as c


class SnakeShould(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_init_initializesSuccessfully(self):
        self.assertIsNotNone(self.snake)

    def test_init_setsLengthToTwo(self):
        self.assertEqual(2, self.snake.length)

    def test_init_setsPositions(self):
        self.assertEqual(
            ((10, 10), (11, 10)),
            self.snake.positions,
        )

    def test_init_setsDirection(self):
        self.assertEqual((-1, 0), self.snake.direction)

    def test_init_setsHasDirectionChangedToFalse(self):
        self.assertFalse(self.snake.has_direction_changed)

    def test_getHeadPosition_returnsHeadPosition(self):
        self.assertEqual((10, 10), self.snake.get_head_position())

    def test_getSnakeBodyPositions_returnsBodyPositions(self):
        self.assertEqual(
            ((200, 200), (220, 200)),
            self.snake.get_snake_body_positions(),
        )

    def test_move_returnsTail(self):
        with patch.object(self.snake, "_get_next_head_position", return_value=(9, 10)):
            tail = self.snake.move()
            self.assertEqual((11, 10), tail)

    def test_move_updatesPositions(self):
        with patch.object(self.snake, "_get_next_head_position", return_value=(9, 10)):
            self.snake.move()
            self.assertEqual(
                ((9, 10), (10, 10)),
                self.snake.positions,
            )

    def test_move_setsHasDirectionChangedToFalse(self):
        with patch.object(self.snake, "_get_next_head_position", return_value=(9, 10)):
            self.snake.move()
            self.assertFalse(self.snake.has_direction_changed)

    def test_grow_addsTailToPositions(self):
        self.snake.grow((8, 10))
        self.assertEqual(
            ((10, 10), (11, 10), (8, 10)),
            self.snake.positions,
        )

    def test_getNextHeadPosition_returnsNextHeadPosition(self):
        self.assertEqual((9, 10), self.snake._get_next_head_position())

    def test_changeDirection_validDirection_returnsTrue(self):
        self.assertTrue(self.snake.change_direction(c.UP))

    def test_changeDirection_validDirection_updatesDirection(self):
        self.snake.change_direction(c.UP)
        self.assertEqual(c.UP, self.snake.direction)

    def test_changeDirection_validDirection_setsHasDirectionChangedTrue(self):
        self.snake.change_direction(c.UP)
        self.assertTrue(self.snake.has_direction_changed)

    def test_changeDirection_oppositeDirection_returnsFalse(self):
        self.assertFalse(self.snake.change_direction(c.RIGHT))

    def test_changeDirection_oppositeDirection_doesNotUpdateDirection(self):
        self.snake.change_direction(c.RIGHT)
        self.assertEqual(c.LEFT, self.snake.direction)

    def test_changeDirection_invalidDirection_returnsFalse(self):
        self.assertFalse(self.snake.change_direction((2, 2)))

    def test_changeDirection_invalidDirection_doesNotUpdateDirection(self):
        self.snake.change_direction((2, 2))
        self.assertEqual(c.LEFT, self.snake.direction)

    def test_changeDirection_afterDirectionChanged_returnsFalse(self):
        self.snake.change_direction(c.UP)
        self.assertFalse(self.snake.change_direction(c.RIGHT))

    def test_changeDirection_afterDirectionChanged_doesNotUpdateDirection(self):
        self.snake.change_direction(c.UP)
        self.snake.change_direction(c.RIGHT)
        self.assertEqual(c.UP, self.snake.direction)
