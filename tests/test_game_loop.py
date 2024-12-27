import unittest
from unittest.mock import Mock, call, patch

from src.core.game_loop import game_loop


class GameLoopShould(unittest.TestCase):
    def setUp(self):
        self.screen = Mock()
        self.game_state = Mock()
        self.clock = Mock()

        self.food_system = Mock()
        self.game_state.food_system = self.food_system

    def test_init_createsEventHandlerAndRenderer(self):
        mock_event_handler = Mock()
        mock_event_handler.handle_events.return_value = False

        with (
            patch(
                "src.core.game_loop.EventHandler", return_value=mock_event_handler
            ) as mock_eh_class,
            patch("src.core.game_loop.Renderer") as mock_renderer_class,
        ):
            game_loop(self.screen, self.game_state, self.clock)

            mock_eh_class.assert_called_once_with(self.game_state)
            mock_renderer_class.assert_called_once_with(self.screen)

    def test_gameLoop_callsRequiredMethodsInOrder(self):
        mock_event_handler = Mock()
        mock_event_handler.handle_events.side_effect = [True, False]

        mock_renderer = Mock()

        with (
            patch("src.core.game_loop.EventHandler", return_value=mock_event_handler),
            patch("src.core.game_loop.Renderer", return_value=mock_renderer),
        ):
            game_loop(self.screen, self.game_state, self.clock)

            expected_calls = [
                call.tick(60),
                call.update(),
                call.food_system.spawn_food(),
                call.spawn_food(),
            ]

            self.assertEqual(
                self.clock.method_calls, [expected_calls[0], expected_calls[0]]
            )
            self.assertEqual(
                self.game_state.method_calls,
                [
                    expected_calls[1],
                    expected_calls[2],
                    expected_calls[1],
                    expected_calls[2],
                ],
            )
            self.assertEqual(
                self.food_system.method_calls, [expected_calls[3], expected_calls[3]]
            )
            self.assertEqual(mock_event_handler.handle_events.call_count, 2)
            mock_renderer.render.assert_called_once_with(self.game_state)

    def test_gameLoop_stopsWhenHandleEventsReturnsFalse(self):
        mock_event_handler = Mock()
        mock_event_handler.handle_events.side_effect = [True, True, False]

        with (
            patch("src.core.game_loop.EventHandler", return_value=mock_event_handler),
            patch("src.core.game_loop.Renderer"),
        ):
            game_loop(self.screen, self.game_state, self.clock)

            self.assertEqual(mock_event_handler.handle_events.call_count, 3)
            self.assertEqual(self.clock.tick.call_count, 3)
