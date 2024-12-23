import unittest
from unittest.mock import Mock, patch

from src.core.food_system import FoodSystem
from src.utils import constants as c


class FoodSystemShould(unittest.TestCase):
    def setUp(self):
        self.snake = Mock()
        self.particle_system = Mock()

    def test_init_initializesSuccessfully(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        self.assertIsNotNone(food_system)

    def test_init_setsFoodPos(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        self.assertEqual((0, 0), food_system.food_pos)

    def test_init_setsNewFood(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        self.assertTrue(food_system.new_food)

    def test_init_setsBonusFoodPos(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        self.assertIsNone(food_system.bonus_food_pos)

    def test_init_setsBonusFoodActive(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        self.assertFalse(food_system.bonus_food_active)

    def test_init_setsBonusFoodDurationTimer(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        self.assertEqual(0, food_system.bonus_food_duration_timer)

    def test_init_setsBonusFoodSpawnTimer(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        self.assertEqual(0, food_system.bonus_food_spawn_timer)

    def test_updateBonusFood_returnsBonusFoodCollected_whenBonusFoodActive(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_active = True

        with (patch.object(food_system, "_handle_bonus_food", return_value=True) as mock_handle_bonus_food):

            result = food_system.update_bonus_food(None)
            self.assertTrue(result)
            mock_handle_bonus_food.assert_called_once()

    def test_updateBonusFood_returnsFalse_whenBonusFoodNotActive(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_active = False

        result = food_system.update_bonus_food(None)
        self.assertFalse(result)

    def test_updateBonusFood_incrementsBonusFoodSpawnTimer_whenBonusFoodPosNone(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_pos = None

        food_system.update_bonus_food(None)
        self.assertEqual(1, food_system.bonus_food_spawn_timer)

    def test_updateBonusFood_spawnsBonusFood_whenBonusFoodSpawnTimerEqualsBonusFoodSpawnInterval(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_spawn_timer = c.BONUS_FOOD_SPAWN_INTERVAL - 1

        with patch.object(food_system, "_spawn_bonus_food") as mock_spawn_bonus_food:

            food_system.update_bonus_food(None)
            mock_spawn_bonus_food.assert_called_once()

    def test_updateBonusFood_deactivatesBonusFood_whenBonusFoodDurationTimerEqualsBonusFoodDuration(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_active = True
        food_system._bonus_food_duration_timer = c.BONUS_FOOD_DURATION

        with (patch.object(food_system, "_handle_bonus_food", return_value=True) as mock_handle_bonus_food,
                patch.object(food_system, "deactivate_bonus_food") as mock_deactivate_bonus_food,
              ):

            food_system.update_bonus_food(None)
            self.assertTrue(food_system.bonus_food_active)
            mock_handle_bonus_food.assert_called_once()
            mock_deactivate_bonus_food.assert_called_once()

    def test_handleBonusFood_returnsTrue_whenSnakeHeadPositionEqualsBonusFoodPos(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_pos = [10, 10]
        self.snake.get_head_position.return_value = (10, 10)

        with patch.object(food_system, "_collect_bonus_food") as mock_collect_bonus_food:
            result = food_system._handle_bonus_food(None)
            self.assertTrue(result)
            mock_collect_bonus_food.assert_called_once()

    def test_handleBonusFood_returnsFalse_whenSnakeHeadPositionNotEqualsBonusFoodPos(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_pos = [10, 10]
        self.snake.get_head_position.return_value = (10, 11)

        result = food_system._handle_bonus_food(None)
        self.assertFalse(result)

    def test_handleBonusFood_incrementsBonusFoodDurationTimer_whenSnakeHeadPositionNotEqualsBonusFoodPos(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_pos = [10, 10]
        self.snake.get_head_position.return_value = (10, 11)

        food_system._handle_bonus_food(None)
        self.assertEqual(1, food_system.bonus_food_duration_timer)

    def test_collectBonusFood_callsParticleSystemSpawnParticles(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_pos = [10, 10]
        tail = Mock()

        with (patch.object(food_system._particle_system, "spawn_particles") as mock_spawn_particles,
              patch.object(food_system._snake, "grow") as mock_grow,
              patch.object(food_system, "deactivate_bonus_food") as mock_deactivate_bonus_food,
              ):

            food_system._collect_bonus_food(tail)
            mock_spawn_particles.assert_called_once()

    def test_collectBonusFood_callsSnakeGrow(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_pos = [10, 10]
        tail = Mock()

        with (patch.object(food_system._particle_system, "spawn_particles") as mock_spawn_particles,
              patch.object(food_system._snake, "grow") as mock_grow,
              patch.object(food_system, "deactivate_bonus_food") as mock_deactivate_bonus_food,
              ):

            food_system._collect_bonus_food(tail)
            mock_grow.assert_called_once_with(tail)

    def test_collectBonusFood_deactivatesBonusFood(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_pos = [10, 10]
        tail = Mock()

        with (patch.object(food_system._particle_system, "spawn_particles") as mock_spawn_particles,
              patch.object(food_system._snake, "grow") as mock_grow,
              patch.object(food_system, "deactivate_bonus_food") as mock_deactivate_bonus_food,
              ):

            food_system._collect_bonus_food(tail)
            mock_deactivate_bonus_food.assert_called_once()

    def test_spawnBonusFood_setsBonusFoodPos(self):
        food_system = FoodSystem(self.snake, self.particle_system)

        with patch.object(food_system, "_validate_food_position", return_value=(10, 10)):
            food_system._spawn_bonus_food()
            self.assertEqual((10, 10), food_system.bonus_food_pos)

    def test_spawnBonusFood_setsBonusFoodSpawnTimer(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_spawn_timer = 10

        with patch.object(food_system, "_validate_food_position", return_value=(10, 10)):
            food_system._spawn_bonus_food()
            self.assertEqual(0, food_system.bonus_food_spawn_timer)

    def test_spawnBonusFood_setsBonusFoodActive(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_active = False

        with patch.object(food_system, "_validate_food_position", return_value=(10, 10)):
            food_system._spawn_bonus_food()
            self.assertTrue(food_system.bonus_food_active)

    def test_spawnBonusFood_setsBonusFoodDurationTimer(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_duration_timer = 10

        with patch.object(food_system, "_validate_food_position", return_value=(10, 10)):
            food_system._spawn_bonus_food()
            self.assertEqual(0, food_system.bonus_food_duration_timer)

    def test_spawnFood_setsFoodPos(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._new_food = True

        with patch.object(food_system, "_validate_food_position", return_value=(10, 10)):
            food_system.spawn_food()
            self.assertEqual((10, 10), food_system.food_pos)

    def test_spawnFood_doesNotSetFoodPos_whenNewFoodFalse(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._new_food = False

        with patch.object(food_system, "_validate_food_position", return_value=(10, 10)):
            food_system.spawn_food()
            self.assertEqual((0, 0), food_system.food_pos)

    def test_spawnFood_setsNewFoodFalse(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._new_food = True

        with patch.object(food_system, "_validate_food_position", return_value=(10, 10)):
            food_system.spawn_food()
            self.assertFalse(food_system.new_food)

    # TODO: Implement tests for _validate_food_position
    def test_validateFoodPosition_returnsValidPosition(self):
        pass

    def test_deactivateBonusFood_setsBonusFoodActiveToFalse(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_active = True

        food_system.deactivate_bonus_food()
        self.assertFalse(food_system.bonus_food_active)

    def test_deactivateBonusFood_setsBonusFoodPosToNone(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_pos = [10, 10]

        food_system.deactivate_bonus_food()
        self.assertIsNone(food_system.bonus_food_pos)

    def test_deactivateBonusFood_setsBonusFoodDurationTimerToZero(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_duration_timer = 10

        food_system.deactivate_bonus_food()
        self.assertEqual(0, food_system.bonus_food_duration_timer)

    def test_reset_setsFoodPosToZeros(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._food_pos = [10, 10]

        food_system.reset()
        self.assertEqual((0, 0), food_system.food_pos)

    def test_reset_setsNewFoodToTrue(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._new_food = False

        food_system.reset()
        self.assertTrue(food_system.new_food)

    def test_reset_setsBonusFoodPosToNone(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_pos = [10, 10]

        food_system.reset()
        self.assertIsNone(food_system.bonus_food_pos)

    def test_reset_setsBonusFoodSpawnTimerToZero(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_spawn_timer = 10

        food_system.reset()
        self.assertEqual(0, food_system.bonus_food_spawn_timer)

    def test_reset_setsBonusFoodDurationTimerToZero(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_duration_timer = 10

        food_system.reset()
        self.assertEqual(0, food_system.bonus_food_duration_timer)

    def test_reset_setsBonusFoodActiveToFalse(self):
        food_system = FoodSystem(self.snake, self.particle_system)
        food_system._bonus_food_active = True

        food_system.reset()
        self.assertFalse(food_system.bonus_food_active)







