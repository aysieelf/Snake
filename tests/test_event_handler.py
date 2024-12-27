import unittest
from unittest.mock import Mock, patch

from src.event_handler import EventHandler
from src.utils import constants as c

import pygame


class EventHandlerShould(unittest.TestCase):
    def setUp(self):
        self.game_state = Mock()
        self.event_handler = EventHandler(self.game_state)

    def test_init_initializesSuccessfully(self):
        self.assertIsNotNone(self.event_handler)

    def test_handleEvents_returnsFalse_whenQuitEvent(self):
        mock_event = Mock()
        mock_event.type = pygame.QUIT

        with patch("pygame.event.get", return_value=[mock_event]):
            result = self.event_handler.handle_events()

            self.assertFalse(result)

    def test_handleEvents_returnsFalse_whenKeyboardEventFalse(self):
        mock_event = Mock()
        mock_event.type = pygame.KEYDOWN
        mock_event.key = pygame.K_q

        with (
            patch("pygame.event.get", return_value=[mock_event]),
            patch.object(self.event_handler, "_handle_keyboard", return_value=False),
        ):
            result = self.event_handler.handle_events()

            self.assertFalse(result)

    def test_handleEvents_returnsTrue_whenKeyboardEventTrue(self):
        mock_event = Mock()
        mock_event.type = pygame.KEYDOWN
        mock_event.key = pygame.K_q

        with (
            patch("pygame.event.get", return_value=[mock_event]),
            patch.object(self.event_handler, "_handle_keyboard", return_value=True),
        ):
            result = self.event_handler.handle_events()

            self.assertTrue(result)

    def test_handleEvents_returnsTrue_whenMouseButtonDownEvent(self):
        mock_event = Mock()
        mock_event.type = pygame.MOUSEBUTTONDOWN

        with (
            patch("pygame.event.get", return_value=[mock_event]),
            patch.object(self.event_handler, "_handle_start_screen_click"),
        ):
            result = self.event_handler.handle_events()

            self.assertTrue(result)

    def test_handleEvents_callsHandleStartScreenClick_whenMouseButtonDownEvent(self):
        mock_event = Mock()
        mock_event.type = pygame.MOUSEBUTTONDOWN

        with (
            patch("pygame.event.get", return_value=[mock_event]),
            patch.object(
                self.event_handler, "_handle_start_screen_click"
            ) as mock_handle_start_screen_click,
        ):
            self.event_handler.handle_events()

            mock_handle_start_screen_click.assert_called_once()

    def test_handleKeyboard_resetsGameState_whenRKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_r

        with patch.object(self.game_state, "reset") as mock_reset:
            self.event_handler._handle_keyboard(mock_event)

            mock_reset.assert_called_once()

    def test_handleKeyboard_returnsTrue_whenRKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_r

        result = self.event_handler._handle_keyboard(mock_event)

        self.assertTrue(result)

    def test_handleKeyboard_callsHandleExitGame_whenQKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_q

        with patch.object(
            self.event_handler, "_handle_exit_game"
        ) as mock_handle_exit_game:
            self.event_handler._handle_keyboard(mock_event)

            mock_handle_exit_game.assert_called_once()

    def test_handleKeyboard_returnsFalse_whenQKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_q

        result = self.event_handler._handle_keyboard(mock_event)

        self.assertFalse(result)

    def test_handleKeyboard_callsHandleDirectionChange_whenWKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_w

        with patch.object(
            self.event_handler, "_handle_direction_change"
        ) as mock_handle_direction_change:
            self.event_handler._handle_keyboard(mock_event)

            mock_handle_direction_change.assert_called_once_with(pygame.K_w)

    def test_handleKeyboard_callsHandleDirectionChange_whenUPKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_UP

        with patch.object(
            self.event_handler, "_handle_direction_change"
        ) as mock_handle_direction_change:
            self.event_handler._handle_keyboard(mock_event)

            mock_handle_direction_change.assert_called_once_with(pygame.K_UP)

    def test_handleKeyboard_callsHandleDirectionChange_whenAKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_a

        with patch.object(
            self.event_handler, "_handle_direction_change"
        ) as mock_handle_direction_change:
            self.event_handler._handle_keyboard(mock_event)

            mock_handle_direction_change.assert_called_once_with(pygame.K_a)

    def test_handleKeyboard_callsHandleDirectionChange_whenLEFTKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_LEFT

        with patch.object(
            self.event_handler, "_handle_direction_change"
        ) as mock_handle_direction_change:
            self.event_handler._handle_keyboard(mock_event)

            mock_handle_direction_change.assert_called_once_with(pygame.K_LEFT)

    def test_handleKeyboard_callsHandleDirectionChange_whenSKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_s

        with patch.object(
            self.event_handler, "_handle_direction_change"
        ) as mock_handle_direction_change:
            self.event_handler._handle_keyboard(mock_event)

            mock_handle_direction_change.assert_called_once_with(pygame.K_s)

    def test_handleKeyboard_callsHandleDirectionChange_whenDOWNKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_DOWN

        with patch.object(
            self.event_handler, "_handle_direction_change"
        ) as mock_handle_direction_change:
            self.event_handler._handle_keyboard(mock_event)

            mock_handle_direction_change.assert_called_once_with(pygame.K_DOWN)

    def test_handleKeyboard_callsHandleDirectionChange_whenDKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_d

        with patch.object(
            self.event_handler, "_handle_direction_change"
        ) as mock_handle_direction_change:
            self.event_handler._handle_keyboard(mock_event)

            mock_handle_direction_change.assert_called_once_with(pygame.K_d)

    def test_handleKeyboard_callsHandleDirectionChange_whenRIGHTKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_RIGHT

        with patch.object(
            self.event_handler, "_handle_direction_change"
        ) as mock_handle_direction_change:
            self.event_handler._handle_keyboard(mock_event)

            mock_handle_direction_change.assert_called_once_with(pygame.K_RIGHT)

    def test_handleKeyboard_callsHandleSpaceKey_whenSPACEKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_SPACE

        with patch.object(
            self.event_handler, "_handle_space_key"
        ) as mock_handle_space_key:
            self.event_handler._handle_keyboard(mock_event)

            mock_handle_space_key.assert_called_once()

    def test_handleKeyboard_returnsTrue_whenSpaceKey(self):
        mock_event = Mock()
        mock_event.key = pygame.K_SPACE

        result = self.event_handler._handle_keyboard(mock_event)

        self.assertTrue(result)

    def test_handleExitGame_pausesGame_whenNotStartScreen(self):
        self.game_state.start_screen = False

        with (patch.object(self.game_state, "pause_game") as mock_pause_game,):
            self.event_handler._handle_exit_game()

            mock_pause_game.assert_called_once()

    def test_handleExitGame_callsExitToStartScreen_whenNotStartScreen(self):
        self.game_state.start_screen = False

        with (
            patch.object(
                self.game_state, "exit_to_start_screen"
            ) as mock_exit_to_start_screen,
        ):
            self.event_handler._handle_exit_game()

            mock_exit_to_start_screen.assert_called_once()

    def test_handleExitGame_returnsTrue_whenNotStartScreen(self):
        self.game_state.start_screen = False

        result = self.event_handler._handle_exit_game()

        self.assertTrue(result)

    def test_handleExitGame_returnsFalse_whenStartScreen(self):
        self.game_state.start_screen = True

        result = self.event_handler._handle_exit_game()

        self.assertFalse(result)

    def test_handleDirectionChange_callsChangeDirectionWithUp_whenWKey(self):
        self.event_handler._handle_direction_change(pygame.K_w)

        self.game_state.snake.change_direction.assert_called_once_with(c.UP)

    def test_handleDirectionChange_callsChangeDirectionWithLeft_whenAKey(self):
        self.event_handler._handle_direction_change(pygame.K_a)

        self.game_state.snake.change_direction.assert_called_once_with(c.LEFT)

    def test_handleDirectionChange_callsChangeDirectionWithDown_whenSKey(self):
        self.event_handler._handle_direction_change(pygame.K_s)

        self.game_state.snake.change_direction.assert_called_once_with(c.DOWN)

    def test_handleDirectionChange_callsChangeDirectionWithRight_whenDKey(self):
        self.event_handler._handle_direction_change(pygame.K_d)

        self.game_state.snake.change_direction.assert_called_once_with(c.RIGHT)

    def test_handleSpaceKey_pausesGame_whenNotPaused(self):
        self.game_state.paused = False

        self.event_handler._handle_space_key()

        self.game_state.pause_game.assert_called_once()

    def test_handleSpaceKey_startsGame_whenStartScreen(self):
        self.game_state.start_screen = True

        self.event_handler._handle_space_key()

        self.game_state.start_game.assert_called_once()
        self.game_state.continue_game.assert_called_once()

    def test_handleSpaceKey_continuesGame_whenNotStartScreen(self):
        self.game_state.start_screen = False

        self.event_handler._handle_space_key()

        self.game_state.continue_game.assert_called_once()

    def test_handleSpaceKey_doesNotStartGame_whenNotStartScreen(self):
        self.game_state.start_screen = False

        self.event_handler._handle_space_key()

        self.game_state.start_game.assert_not_called()

    def test_handleStartScreenClick_startsGame_whenCollidePoint(self):
        mock_rect = Mock()
        mock_rect.collidepoint.return_value = True

        with (
            patch("src.event_handler.get_start_button_rect", return_value=mock_rect),
            patch.object(self.game_state, "start_game") as mock_start_game,
            patch("pygame.mouse.get_pos", return_value=(0, 0)),
        ):
            self.event_handler._handle_start_screen_click()
            mock_start_game.assert_called_once()

    def test_handleStartScreenClick_doesNotStartGame_whenNotCollidePoint(self):
        mock_rect = Mock()
        mock_rect.collidepoint.return_value = False

        with (
            patch("src.event_handler.get_start_button_rect", return_value=mock_rect),
            patch.object(self.game_state, "start_game") as mock_start_game,
            patch("pygame.mouse.get_pos", return_value=(0, 0)),
        ):
            self.event_handler._handle_start_screen_click()
            mock_start_game.assert_not_called()
