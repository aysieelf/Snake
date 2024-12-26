import unittest
from unittest.mock import patch, Mock
from src.utils import constants as c
from src.utils.helpers import get_random_position

class GetRandomPositionShould(unittest.TestCase):
    def test_init_returnsListWithTwoElements(self):
        result = get_random_position()
        self.assertIsInstance(result, list)
        self.assertEqual(2, len(result))

    def test_init_returnsNumbersInValidRange(self):
        result = get_random_position()
        self.assertTrue(1 <= result[0] <= c.GRID_SIZE - 2)
        self.assertTrue(1 <= result[1] <= c.GRID_SIZE - 2)

    def test_init_usesCorrectRange(self):
        mock_randint = Mock()
        mock_randint.return_value = 5

        with patch("random.randint", mock_randint):
            get_random_position()
            mock_randint.assert_called_with(1, c.GRID_SIZE - 2)