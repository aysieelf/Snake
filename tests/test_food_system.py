import unittest
from unittest.mock import Mock, patch

from src.core.food_system import FoodSystem
from src.utils import constants as c


class FoodSystemShould(unittest.TestCase):
    def setUp(self):
        self.snake = Mock()
        self.particle_system = Mock()
        self.food_system = FoodSystem(self.snake, self.particle_system)

    def test_init_initializesSuccessfully(self):
        self.assertIsNotNone(self.food_system)

    def test_init_setsFoodPos(self):
        self.assertEqual((0, 0), self.food_system.food_pos)

    def test_init_setsNewFood(self):
        self.assertTrue(self.food_system.new_food)

    def test_init_setsBonusFoodPos(self):
        self.assertIsNone(self.food_system.bonus_food_pos)

    def test_init_setsBonusFoodActive(self):
        self.assertFalse(self.food_system.bonus_food_active)

    def test_init_setsBonusFoodDurationTimer(self):
        self.assertEqual(0, self.food_system.bonus_food_duration_timer)

    def test_init_setsBonusFoodSpawnTimer(self):
        self.assertEqual(0, self.food_system.bonus_food_spawn_timer)

    def test_updateBonusFood_returnsBonusFoodCollected_whenBonusFoodActive(self):
        self.food_system._bonus_food_active = True

        with (patch.object(self.food_system, "_handle_bonus_food", return_value=True) as mock_handle_bonus_food):

            result = self.food_system.update_bonus_food(None)
            self.assertTrue(result)
            mock_handle_bonus_food.assert_called_once()

    def test_updateBonusFood_returnsFalse_whenBonusFoodNotActive(self):
        self.food_system._bonus_food_active = False

        result = self.food_system.update_bonus_food(None)
        self.assertFalse(result)

    def test_updateBonusFood_incrementsBonusFoodSpawnTimer_whenBonusFoodPosNone(self):
        self.food_system._bonus_food_pos = None

        self.food_system.update_bonus_food(None)
        self.assertEqual(1, self.food_system.bonus_food_spawn_timer)

    def test_updateBonusFood_spawnsBonusFood_whenBonusFSTEqualBonusFSI(self):
        self.food_system._bonus_food_spawn_timer = c.BONUS_FOOD_SPAWN_INTERVAL - 1

        with patch.object(self.food_system, "_spawn_bonus_food") as mock_spawn_bonus_food:

            self.food_system.update_bonus_food(None)
            mock_spawn_bonus_food.assert_called_once()

    def test_updateBonusFood_deactivatesBonusFood_whenBonusFDTEqualsBonusFD(self):
        self.food_system._bonus_food_active = True
        self.food_system._bonus_food_duration_timer = c.BONUS_FOOD_DURATION

        with (patch.object(self.food_system, "_handle_bonus_food", return_value=True) as mock_handle_bonus_food,
                patch.object(self.food_system, "deactivate_bonus_food") as mock_deactivate_bonus_food,
              ):

            self.food_system.update_bonus_food(None)
            self.assertTrue(self.food_system.bonus_food_active)
            mock_handle_bonus_food.assert_called_once()
            mock_deactivate_bonus_food.assert_called_once()

    def test_handleBonusFood_returnsTrue_whenSnakeHeadPositionEqualsBonusFoodPos(self):
        self.food_system._bonus_food_pos = [10, 10]
        self.snake.get_head_position.return_value = (10, 10)

        with patch.object(self.food_system, "_collect_bonus_food") as mock_collect_bonus_food:
            result = self.food_system._handle_bonus_food(None)
            self.assertTrue(result)
            mock_collect_bonus_food.assert_called_once()

    def test_handleBonusFood_returnsFalse_whenSnakeHeadPositionNotEqualsBonusFoodPos(self):
        self.food_system._bonus_food_pos = [10, 10]
        self.snake.get_head_position.return_value = (10, 11)

        result = self.food_system._handle_bonus_food(None)
        self.assertFalse(result)

    def test_handleBonusFood_incrementsBonusFoodDurationTimer_whenSnakeHeadPosNotEqualsBonusFoodPos(self):
        self.food_system._bonus_food_pos = [10, 10]
        self.snake.get_head_position.return_value = (10, 11)

        self.food_system._handle_bonus_food(None)
        self.assertEqual(1, self.food_system.bonus_food_duration_timer)

    def test_collectBonusFood_callsParticleSystemSpawnParticles(self):
        self.food_system._bonus_food_pos = [10, 10]
        tail = Mock()

        with (patch.object(self.food_system._particle_system, "spawn_particles") as mock_spawn_particles,
              patch.object(self.food_system._snake, "grow"),
              patch.object(self.food_system, "deactivate_bonus_food"),
              ):

            self.food_system._collect_bonus_food(tail)
            mock_spawn_particles.assert_called_once()

    def test_collectBonusFood_callsSnakeGrow(self):
        self.food_system._bonus_food_pos = [10, 10]
        tail = Mock()

        with (patch.object(self.food_system._particle_system, "spawn_particles"),
              patch.object(self.food_system._snake, "grow") as mock_grow,
              patch.object(self.food_system, "deactivate_bonus_food"),
              ):

            self.food_system._collect_bonus_food(tail)
            mock_grow.assert_called_once_with(tail)

    def test_collectBonusFood_deactivatesBonusFood(self):
        self.food_system._bonus_food_pos = [10, 10]
        tail = Mock()

        with (patch.object(self.food_system._particle_system, "spawn_particles"),
              patch.object(self.food_system._snake, "grow"),
              patch.object(self.food_system, "deactivate_bonus_food") as mock_deactivate_bonus_food,
              ):

            self.food_system._collect_bonus_food(tail)
            mock_deactivate_bonus_food.assert_called_once()

    def test_spawnBonusFood_setsBonusFoodPos(self):
        with patch.object(self.food_system, "_validate_food_position", return_value=(10, 10)):
            self.food_system._spawn_bonus_food()
            self.assertEqual((10, 10), self.food_system.bonus_food_pos)

    def test_spawnBonusFood_setsBonusFoodSpawnTimer(self):
        self.food_system._bonus_food_spawn_timer = 10

        with patch.object(self.food_system, "_validate_food_position", return_value=(10, 10)):
            self.food_system._spawn_bonus_food()
            self.assertEqual(0, self.food_system.bonus_food_spawn_timer)

    def test_spawnBonusFood_setsBonusFoodActive(self):
        self.food_system._bonus_food_active = False

        with patch.object(self.food_system, "_validate_food_position", return_value=(10, 10)):
            self.food_system._spawn_bonus_food()
            self.assertTrue(self.food_system.bonus_food_active)

    def test_spawnBonusFood_setsBonusFoodDurationTimer(self):
        self.food_system._bonus_food_duration_timer = 10

        with patch.object(self.food_system, "_validate_food_position", return_value=(10, 10)):
            self.food_system._spawn_bonus_food()
            self.assertEqual(0, self.food_system.bonus_food_duration_timer)

    def test_spawnFood_setsFoodPos(self):
        self.food_system._new_food = True

        with patch.object(self.food_system, "_validate_food_position", return_value=(10, 10)):
            self.food_system.spawn_food()
            self.assertEqual((10, 10), self.food_system.food_pos)

    def test_spawnFood_doesNotSetFoodPos_whenNewFoodFalse(self):
        self.food_system._new_food = False

        with patch.object(self.food_system, "_validate_food_position", return_value=(10, 10)):
            self.food_system.spawn_food()
            self.assertEqual((0, 0), self.food_system.food_pos)

    def test_spawnFood_setsNewFoodFalse(self):
        self.food_system._new_food = True

        with patch.object(self.food_system, "_validate_food_position", return_value=(10, 10)):
            self.food_system.spawn_food()
            self.assertFalse(self.food_system.new_food)

    def test_validateFoodPosition_returnsRandomPosition_whenPositionValid(self):
        self.snake.positions = [(5, 5)]
        random_pos = [3, 3]

        with patch('src.core.food_system.get_random_position', return_value=random_pos):
            result = self.food_system._validate_food_position()
            self.assertEqual(random_pos, result)

    def test_validateFoodPosition_returnsDefaultPosition_whenMaxAttemptsReached(self):
        self.snake.positions = [(1, 1)]

        with patch('src.core.food_system.get_random_position', return_value=[1, 1]):
            result = self.food_system._validate_food_position()
            self.assertEqual([1, 1], result)

    def test_validateFoodPosition_forBonusFood_avoidsSnakeAndFoodPos(self):
        self.snake.positions = [(5, 5)]
        self.food_system._food_pos = (2, 2)
        random_pos = [3, 3]

        with patch('src.core.food_system.get_random_position', return_value=random_pos):
            result = self.food_system._validate_food_position(bonus_food=True)
            self.assertEqual(random_pos, result)

    def test_validateFoodPosition_forRegularFood_avoidsBonusFoodPos(self):
        self.snake.positions = [(5, 5)]
        self.food_system._bonus_food_active = True
        self.food_system._bonus_food_pos = (2, 2)
        random_pos = [3, 3]

        with patch('src.core.food_system.get_random_position', return_value=random_pos):
            result = self.food_system._validate_food_position()
            self.assertEqual(random_pos, result)

    def test_deactivateBonusFood_setsBonusFoodActiveToFalse(self):
        self.food_system._bonus_food_active = True

        self.food_system.deactivate_bonus_food()
        self.assertFalse(self.food_system.bonus_food_active)

    def test_deactivateBonusFood_setsBonusFoodPosToNone(self):
        self.food_system._bonus_food_pos = [10, 10]

        self.food_system.deactivate_bonus_food()
        self.assertIsNone(self.food_system.bonus_food_pos)

    def test_deactivateBonusFood_setsBonusFoodDurationTimerToZero(self):
        self.food_system._bonus_food_duration_timer = 10

        self.food_system.deactivate_bonus_food()
        self.assertEqual(0, self.food_system.bonus_food_duration_timer)

    def test_reset_setsFoodPosToZeros(self):
        self.food_system._food_pos = [10, 10]

        self.food_system.reset()
        self.assertEqual((0, 0), self.food_system.food_pos)

    def test_reset_setsNewFoodToTrue(self):
        self.food_system._new_food = False

        self.food_system.reset()
        self.assertTrue(self.food_system.new_food)

    def test_reset_setsBonusFoodPosToNone(self):
        self.food_system._bonus_food_pos = [10, 10]

        self.food_system.reset()
        self.assertIsNone(self.food_system.bonus_food_pos)

    def test_reset_setsBonusFoodSpawnTimerToZero(self):
        self.food_system._bonus_food_spawn_timer = 10

        self.food_system.reset()
        self.assertEqual(0, self.food_system.bonus_food_spawn_timer)

    def test_reset_setsBonusFoodDurationTimerToZero(self):
        self.food_system._bonus_food_duration_timer = 10

        self.food_system.reset()
        self.assertEqual(0, self.food_system.bonus_food_duration_timer)

    def test_reset_setsBonusFoodActiveToFalse(self):
        self.food_system._bonus_food_active = True

        self.food_system.reset()
        self.assertFalse(self.food_system.bonus_food_active)







