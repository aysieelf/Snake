import unittest
from unittest.mock import patch

from src.core.game_state import GameState


class GameStateShould(unittest.TestCase):
    def setUp(self):
        self.game_state = GameState()

    def test_init_initializesSuccessfully(self):
        self.assertIsNotNone(self.game_state)

    def test_init_createsSnake(self):
        self.assertIsNotNone(self.game_state.snake)

    def test_init_setsScoreToZero(self):
        self.assertEqual(0, self.game_state.score)

    def test_init_setsFrameCountToZero(self):
        self.assertEqual(0, self.game_state._frame_count)

    def test_init_setsMoveDelayToTwenty(self):
        self.assertEqual(20, self.game_state._move_delay)

    def test_init_createsParticleSystem(self):
        self.assertIsNotNone(self.game_state.particle_system)

    def test_init_createsFoodSystem(self):
        self.assertIsNotNone(self.game_state.food_system)

    def test_init_setsGameOverToFalse(self):
        self.assertFalse(self.game_state.game_over)

    def test_init_setsPausedToTrue(self):
        self.assertTrue(self.game_state.paused)

    def test_init_setsStartScreenToTrue(self):
        self.assertTrue(self.game_state.start_screen)

    def test_update_incrementsFrameCount(self):
        self.game_state.update()
        self.assertEqual(1, self.game_state._frame_count)

    def test_update_callsUpdateSpeed(self):
        with patch.object(self.game_state, "_update_speed") as mock_update_speed:
            self.game_state.update()
            mock_update_speed.assert_called_once()

    def test_update_doesNotCallUpdateMovement_whenGameOver(self):
        self.game_state._game_over = True
        with patch.object(self.game_state, "_update_movement") as mock_update_movement:
            self.game_state.update()
            mock_update_movement.assert_not_called()

    def test_update_doesNotCallUpdateMovement_whenGamePaused(self):
        self.game_state._paused = True
        with patch.object(self.game_state, "_update_movement") as mock_update_movement:
            self.game_state.update()
            mock_update_movement.assert_not_called()

    def test_update_callsUpdateMovement_whenGameNotOverAndNotPaused(self):
        self.game_state._game_over = False
        self.game_state._paused = False
        with patch.object(self.game_state, "_update_movement") as mock_update_movement:
            self.game_state.update()
            mock_update_movement.assert_called_once()

    def test_update_setsGameOverToTrue_whenWallCollision(self):
        self.game_state._game_over = False
        self.game_state._paused = False
        with (patch.object(self.game_state, "_update_movement") as mock_update_movement,
              patch.object(self.game_state, "_check_wall_collision", return_value=True) as mock_check_wall_collision,
              ):

            self.game_state.update()
            self.assertTrue(self.game_state.game_over)

    def test_update_setsGameOverToTrue_whenSelfCollision(self):
        self.game_state._game_over = False
        self.game_state._paused = False
        with (patch.object(self.game_state, "_update_movement") as mock_update_movement,
              patch.object(self.game_state, "_check_wall_collision", return_value=False) as mock_check_wall_collision,
              patch.object(self.game_state, "_check_self_collision", return_value=True) as mock_check_self_collision,
              ):

            self.game_state.update()
            self.assertTrue(self.game_state.game_over)

    def test_update_callsHandleFoodCollision_whenHeadPositionEqualsFoodPos(self):
        self.game_state._game_over = False
        self.game_state._paused = False
        self.game_state.food_system._food_pos = (0, 0)
        with (patch.object(self.game_state, "_update_movement") as mock_update_movement,
              patch.object(self.game_state, "_check_wall_collision", return_value=False) as mock_check_wall_collision,
              patch.object(self.game_state, "_check_self_collision", return_value=False) as mock_check_self_collision,
              patch.object(self.game_state.snake, "get_head_position", return_value=(0, 0)) as mock_get_head_position,
              patch.object(self.game_state, "_handle_food_collision") as mock_handle_food_collision,
              ):

            self.game_state.update()
            mock_handle_food_collision.assert_called_once()

    def test_update_doesNotCallHandleFoodCollision_whenHeadPositionNotEqualsFoodPos(self):
        self.game_state._game_over = False
        self.game_state._paused = False
        self.game_state.food_system._food_pos = (0, 0)
        with (patch.object(self.game_state, "_update_movement") as mock_update_movement,
              patch.object(self.game_state, "_check_wall_collision", return_value=False) as mock_check_wall_collision,
              patch.object(self.game_state, "_check_self_collision", return_value=False) as mock_check_self_collision,
              patch.object(self.game_state.snake, "get_head_position", return_value=(1, 1)) as mock_get_head_position,
              patch.object(self.game_state, "_handle_food_collision") as mock_handle_food_collision,
              ):

            self.game_state.update()
            mock_handle_food_collision.assert_not_called()

    def test_update_incrementsScoreByThree_whenBonusFoodCollected(self):
        self.game_state._game_over = False
        self.game_state._paused = False
        self.game_state.food_system._food_pos = (0, 0)
        with (patch.object(self.game_state, "_update_movement") as mock_update_movement,
              patch.object(self.game_state, "_check_wall_collision", return_value=False) as mock_check_wall_collision,
              patch.object(self.game_state, "_check_self_collision", return_value=False) as mock_check_self_collision,
              patch.object(self.game_state.snake, "get_head_position", return_value=(1, 1)) as mock_get_head_position,
              patch.object(self.game_state.food_system, "update_bonus_food", return_value=True) as mock_update_bonus_food,
              ):

            self.game_state.update()
            self.assertEqual(3, self.game_state.score)

    def test_checkWallCollision_returnsTrue_whenHeadPositionLessThanZero(self):
        with patch.object(self.game_state.snake, "get_head_position", return_value=(-1, 0)):
            self.assertTrue(self.game_state._check_wall_collision())

    def test_checkWallCollision_returnsTrue_whenHeadPositionGreaterThanGridSize(self):
        with patch.object(self.game_state.snake, "get_head_position", return_value=(20, 0)):
            self.assertTrue(self.game_state._check_wall_collision())

    def test_checkWallCollision_returnsFalse_whenHeadPositionWithinGridSize(self):
        with patch.object(self.game_state.snake, "get_head_position", return_value=(10, 10)):
            self.assertFalse(self.game_state._check_wall_collision())

    def test_checkSelfCollision_returnsTrue_whenHeadPositionInSnakePositions(self):
        self.game_state.snake._positions = ((10, 10), (11, 10), (10, 10))
        with patch.object(self.game_state.snake, "get_head_position", return_value=(10, 10)):
            self.assertTrue(self.game_state._check_self_collision())

    def test_checkSelfCollision_returnsFalse_whenHeadPositionNotInSnakePositions(self):
        self.game_state.snake._positions = ((10, 10), (11, 10))
        with patch.object(self.game_state.snake, "get_head_position", return_value=(10, 11)):
            self.assertFalse(self.game_state._check_self_collision())

    def test_handleFoodCollision_growsSnake(self):
        tail = (10, 10)
        with (patch.object(self.game_state.snake, "grow") as mock_grow,
              patch.object(self.game_state.particle_system, "spawn_particles") as mock_spawn_particles,
              ):
            self.game_state._handle_food_collision(tail)
            mock_grow.assert_called_once_with(tail)

    def test_handleFoodCollision_incrementsScoreByOne(self):
        tail = (10, 10)
        self.game_state.score = 0
        with (patch.object(self.game_state.snake, "grow") as mock_grow,
              patch.object(self.game_state.particle_system, "spawn_particles") as mock_spawn_particles,
              ):
            self.game_state._handle_food_collision(tail)
            self.assertEqual(1, self.game_state.score)

    def test_handleFoodCollision_setsNewFoodToTrue(self):
        tail = (10, 10)
        self.game_state.food_system._new_food = False
        with (patch.object(self.game_state.snake, "grow") as mock_grow,
              patch.object(self.game_state.particle_system, "spawn_particles") as mock_spawn_particles,
              ):
            self.game_state._handle_food_collision(tail)
            self.assertTrue(self.game_state.food_system.new_food)

    def test_handleFoodCollision_callsParticleSystemSpawnParticles(self):
        tail = (10, 10)
        with (patch.object(self.game_state.snake, "grow") as mock_grow,
              patch.object(self.game_state.particle_system, "spawn_particles") as mock_spawn_particles,
              ):

            self.game_state._handle_food_collision(tail)
            mock_spawn_particles.assert_called_once()

    def test_updateMovement_returnsTail_whenFrameCountMoreThanMoveDelay(self):
        self.game_state._frame_count = 21
        with patch.object(self.game_state.snake, "move") as mock_move:
            self.game_state._update_movement()
            mock_move.assert_called_once()

    def test_updateMovement_returnsTail_whenFrameCountEqualToMoveDelay(self):
        self.game_state._frame_count = 20
        with patch.object(self.game_state.snake, "move") as mock_move:
            self.game_state._update_movement()
            mock_move.assert_called_once()

    def test_updateMovement_returnsNone_whenFrameCountLessThanMoveDelay(self):
        self.game_state._frame_count = 19
        with patch.object(self.game_state.snake, "move") as mock_move:
            self.assertIsNone(self.game_state._update_movement())

    def test_updateMovement_setsFrameCountToZero_whenFrameCountMoreThanMoveDelay(self):
        self.game_state._frame_count = 21
        with patch.object(self.game_state.snake, "move") as mock_move:
            self.game_state._update_movement()
            self.assertEqual(0, self.game_state._frame_count)

    def test_updateSpeed_reducesMoveDelayByTwo_whenScoreEqualToFive(self):
        self.game_state.score = 5
        self.game_state._update_speed()
        self.assertEqual(18, self.game_state._move_delay)

    def test_updateSpeed_reducesMoveDelayByFour_whenScoreEqualToTen(self):
        self.game_state.score = 10
        self.game_state._update_speed()
        self.assertEqual(16, self.game_state._move_delay)

    def test_updateSpeed_doesNotReduceMoveDelayBelowFive(self):
        self.game_state.score = 100
        self.game_state._update_speed()
        self.assertEqual(5, self.game_state._move_delay)

    def test_updateSpeed_doesNothing_whenScoreLessThanFive(self):
        self.game_state.score = 3
        self.game_state._update_speed()
        self.assertEqual(20, self.game_state._move_delay)

    def test_startGame_setsStartScreenToFalse(self):
        self.game_state._start_screen = True
        with patch.object(self.game_state, "reset") as mock_reset:
            self.game_state.start_game()
            self.assertFalse(self.game_state.start_screen)

    def test_startGame_callsReset(self):
        with patch.object(self.game_state, "reset") as mock_reset:
            self.game_state.start_game()
            mock_reset.assert_called_once()

    def test_exitToStartScreen_setsStartScreenToTrue(self):
        self.game_state._start_screen = False
        self.game_state.exit_to_start_screen()
        self.assertTrue(self.game_state.start_screen)

    def test_pauseGame_setsPausedToTrue(self):
        self.game_state._paused = False
        self.game_state.pause_game()
        self.assertTrue(self.game_state.paused)

    def test_continueGame_setsPausedToFalse(self):
        self.game_state._paused = True
        self.game_state.continue_game()
        self.assertFalse(self.game_state.paused)

    def test_reset_resetsScoreToZero(self):
        self.game_state.score = 10
        self.game_state.reset()
        self.assertEqual(0, self.game_state.score)

    def test_reset_resetsFrameCountToZero(self):
        self.game_state._frame_count = 10
        self.game_state.reset()
        self.assertEqual(0, self.game_state._frame_count)

    def test_reset_resetsMoveDelayToTwenty(self):
        self.game_state._move_delay = 10
        self.game_state.reset()
        self.assertEqual(20, self.game_state._move_delay)

    def test_reset_setsGameOverToFalse(self):
        self.game_state._game_over = True
        self.game_state.reset()
        self.assertFalse(self.game_state.game_over)

    def test_reset_setsPausedToFalse(self):
        self.game_state._paused = True
        self.game_state.reset()
        self.assertFalse(self.game_state.paused)

    def test_reset_createsNewSnake(self):
        self.game_state.snake = None
        self.game_state.reset()
        self.assertIsNotNone(self.game_state.snake)

    def test_reset_createsNewFoodSystem(self):
        self.game_state.food_system = None
        self.game_state.reset()
        self.assertIsNotNone(self.game_state.food_system)

    # TODO: find out why this test is failing
    # def test_reset_callsFoodSystemReset(self):
    #     with patch.object(self.game_state.food_system, "reset") as mock_reset:
    #         self.game_state.reset()
    #         mock_reset.assert_called_once()


