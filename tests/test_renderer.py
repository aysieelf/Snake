import unittest
from unittest.mock import Mock, patch

from src.ui.renderer import Renderer
from src.utils import constants as c


class RendererShould(unittest.TestCase):
    def setUp(self):
        self.screen = Mock()
        self.renderer = Renderer(self.screen)
        self.game_state = Mock()

    def test_init_initializesSuccessfully(self):
        self.assertIsNotNone(self.renderer)

    def test_init_setsScreen(self):
        self.assertEqual(self.screen, self.renderer.screen)

    def test_renderer_rendersStartScreen_whenGameStateInStartScreen(self):
        self.game_state.start_screen = True

        with (
            patch("src.ui.renderer.draw_start_screen") as mock_draw_start_screen,
            patch("pygame.display.flip"),
        ):
            self.renderer.render(self.game_state)
            mock_draw_start_screen.assert_called_once_with(self.screen)

    def test_renderer_rendersGameScreen_whenGameStateNotInStartScreen(self):
        self.game_state.start_screen = False

        with (
            patch("src.ui.renderer.draw_start_screen") as mock_draw_start_screen,
            patch.object(self.renderer, "_draw_snake"),
            patch.object(self.renderer, "_draw_food"),
            patch.object(self.renderer, "_draw_score"),
            patch.object(self.game_state.particle_system, "update"),
            patch.object(self.game_state.particle_system, "draw"),
            patch.object(self.renderer, "_draw_game_over"),
            patch("pygame.display.flip"),
        ):
            self.renderer.render(self.game_state)
            mock_draw_start_screen.assert_not_called()

    def test_renderer_drawsBonusFood_whenBonusFoodActive(self):
        # Setup
        self.game_state.start_screen = False
        self.game_state.food_system.bonus_food_active = True

        with (
            patch("src.ui.renderer.draw_start_screen"),
            patch.object(self.renderer, "_draw_snake"),
            patch.object(self.renderer, "_draw_food") as mock_draw_food,
            patch.object(self.renderer, "_draw_score"),
            patch.object(self.game_state.particle_system, "update"),
            patch.object(self.game_state.particle_system, "draw"),
            patch.object(self.renderer, "_draw_game_over"),
            patch("pygame.display.flip"),
        ):
            self.renderer.render(self.game_state)
            self.assertEqual(mock_draw_food.call_count, 2)

    def test_renderer_drawsGameOver_whenGameOver(self):
        # Setup
        self.game_state.start_screen = False
        self.game_state.game_over = True

        with (
            patch("src.ui.renderer.draw_start_screen"),
            patch.object(self.renderer, "_draw_snake"),
            patch.object(self.renderer, "_draw_food"),
            patch.object(self.renderer, "_draw_score"),
            patch.object(self.game_state.particle_system, "update"),
            patch.object(self.game_state.particle_system, "draw"),
            patch.object(self.renderer, "_draw_game_over") as mock_draw_game_over,
            patch("pygame.display.flip"),
        ):
            self.renderer.render(self.game_state)
            mock_draw_game_over.assert_called_once()

    def test_drawSnake_drawsSnakeBody(self):
        self.game_state.snake.get_snake_body_positions.return_value = [
            (0, 0),
            (1, 1),
            (2, 2),
        ]

        with (
            patch("src.ui.renderer.create_rectangle") as mock_create_rectangle,
            patch.object(
                self.renderer, "_get_eyes_positions", return_value=((0, 0), (1, 1))
            ),
            patch("pygame.draw.rect"),
        ):
            self.renderer._draw_snake(self.game_state.snake)
            # 2 calls to create_rectangle for the body segments, 1 for the head
            self.assertEqual(mock_create_rectangle.call_count, 3)

    def test_getEyesPositions_returnsCorrectPositions_whenFacingLeft(self):
        head = (100, 100)
        direction = c.LEFT

        expected_left_eye = (head[0] + c.EYE_DEPTH, head[1] - c.EYE_OFFSET_SIDE_FAR)
        expected_right_eye = (head[0] + c.EYE_DEPTH, head[1] + c.EYE_OFFSET_SIDE_NEAR)

        eyes = self.renderer._get_eyes_positions(head, direction)
        self.assertEqual((expected_left_eye, expected_right_eye), eyes)

    def test_getEyesPositions_returnsCorrectPositions_whenFacingRight(self):
        head = (100, 100)
        direction = c.RIGHT

        expected_left_eye = (
            head[0] + c.CELL_SIZE - c.EYE_DEPTH - c.EYE_SIZE,
            head[1] - c.EYE_OFFSET_SIDE_FAR,
        )
        expected_right_eye = (
            head[0] + c.CELL_SIZE - c.EYE_DEPTH - c.EYE_SIZE,
            head[1] + c.EYE_OFFSET_SIDE_NEAR,
        )

        eyes = self.renderer._get_eyes_positions(head, direction)
        self.assertEqual((expected_left_eye, expected_right_eye), eyes)

    def test_getEyesPositions_returnsCorrectPositions_whenFacingUp(self):
        head = (100, 100)
        direction = c.UP

        expected_left_eye = (head[0] + c.EYE_OFFSET_NEAR, head[1] - c.EYE_DEPTH_UP)
        expected_right_eye = (head[0] + c.EYE_OFFSET_FAR, head[1] - c.EYE_DEPTH_UP)

        eyes = self.renderer._get_eyes_positions(head, direction)
        self.assertEqual((expected_left_eye, expected_right_eye), eyes)

    def test_getEyesPositions_returnsCorrectPositions_whenFacingDown(self):
        head = (100, 100)
        direction = c.DOWN

        expected_left_eye = (head[0] + c.EYE_OFFSET_NEAR, head[1] + c.EYE_DEPTH)
        expected_right_eye = (head[0] + c.EYE_OFFSET_FAR, head[1] + c.EYE_DEPTH)

        eyes = self.renderer._get_eyes_positions(head, direction)
        self.assertEqual((expected_left_eye, expected_right_eye), eyes)

    def test_drawFood_drawsFood(self):
        food_pos = (0, 0)

        with patch("src.ui.renderer.create_rectangle") as mock_create_rectangle:
            self.renderer._draw_food(food_pos)
            mock_create_rectangle.assert_called_once_with(
                self.screen, (255, 198, 214), 0, 0, 20, 20
            )

    def test_drawGameOver_drawsGameOverScreen(self):
        with (
            patch.object(
                self.renderer, "_draw_game_over_overlay"
            ) as mock_draw_game_over_overlay,
            patch.object(
                self.renderer, "_draw_game_over_text"
            ) as mock_draw_game_over_text,
            patch("src.ui.renderer.draw_instructions"),
        ):
            self.renderer._draw_game_over()
            mock_draw_game_over_overlay.assert_called_once()
            mock_draw_game_over_text.assert_called_once()

    def test_drawGameOverOverlay_createsAndDrawsOverlay(self):
        with (
            patch("pygame.Surface") as mock_surface,
            patch.object(self.screen, "blit") as mock_blit,
        ):
            mock_overlay = Mock()
            mock_surface.return_value = mock_overlay

            self.renderer._draw_game_over_overlay()

            mock_surface.assert_called_once_with((c.WINDOW_SIZE, c.WINDOW_SIZE))
            mock_overlay.set_alpha.assert_called_once_with(c.OVERLAY_ALPHA)
            mock_overlay.fill.assert_called_once_with(c.GAME_OVER_COLOR)
            mock_blit.assert_called_once_with(mock_overlay, (0, 0))

    def test_drawGameOverText_createsAndDrawsText(self):
        with (
            patch("pygame.font.SysFont") as mock_font_class,
            patch.object(self.screen, "blit") as mock_blit,
        ):
            mock_font = Mock()
            mock_font_class.return_value = mock_font
            mock_text_surface = Mock()
            mock_font.render.return_value = mock_text_surface
            mock_text_surface.get_rect.return_value = "text_rect"

            self.renderer._draw_game_over_text()

            mock_font_class.assert_called_once_with(
                c.GAME_OVER_FONT, c.GAME_OVER_FONT_SIZE
            )
            mock_font.render.assert_called_once_with(
                c.GAME_OVER_TEXT, True, c.GAME_OVER_TEXT_COLOR
            )
            mock_text_surface.get_rect.assert_called_once_with(
                center=(c.WINDOW_SIZE // 2, c.GAME_OVER_TEXT_POS)
            )
            mock_blit.assert_called_once_with(mock_text_surface, "text_rect")

    def test_drawScore_createsAndDrawsScore(self):
        test_score = 42
        with (
            patch("pygame.font.SysFont") as mock_font_class,
            patch.object(self.screen, "blit") as mock_blit,
        ):
            mock_font = Mock()
            mock_font_class.return_value = mock_font
            mock_score_surface = Mock()
            mock_font.render.return_value = mock_score_surface
            mock_score_surface.get_rect.return_value = "score_rect"

            self.renderer._draw_score(test_score)

            mock_font_class.assert_called_once_with(c.SCORE_FONT, c.SCORE_FONT_SIZE)
            expected_score_text = f"{c.SCORE_TEXT} {test_score}"
            mock_font.render.assert_called_once_with(
                expected_score_text, True, c.SCORE_COLOR
            )
            mock_score_surface.get_rect.assert_called_once_with(
                midtop=(c.WINDOW_SIZE // 2, c.SCORE_PADDING)
            )
            mock_blit.assert_called_once_with(mock_score_surface, "score_rect")
