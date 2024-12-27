import unittest
from unittest.mock import Mock, patch

from src.ui.ui_components import (
    _draw_start_button,
    create_rectangle,
    create_title,
    draw_instructions,
    draw_start_screen,
    get_start_button_rect,
)


class UiComponentsShould(unittest.TestCase):
    def setUp(self):
        self.screen = Mock()

    def test_createRectangle_drawsRectangleWithCorrectParameters(self):
        test_color = (255, 0, 0)
        test_x = 10
        test_y = 20
        test_width = 30
        test_height = 40

        with patch("pygame.draw.rect") as mock_draw_rect:
            create_rectangle(
                self.screen, test_color, test_x, test_y, test_width, test_height
            )

            mock_draw_rect.assert_called_once_with(
                self.screen, test_color, (test_x, test_y, test_width, test_height)
            )

    def test_drawStartScreen_drawsStartScreen(self):
        with (
            patch.object(self.screen, "fill"),
            patch("src.ui.ui_components.create_title"),
            patch("src.ui.ui_components.draw_instructions"),
            patch("src.ui.ui_components._draw_start_button"),
        ):
            draw_start_screen(self.screen)
            self.screen.fill.assert_called_once()

    def test_createTitle_drawsTitle(self):
        with (
            patch("pygame.font.SysFont") as mock_font_class,
            patch.object(self.screen, "blit") as mock_blit,
        ):
            mock_font = Mock()
            mock_font_class.return_value = mock_font
            mock_title_surface = Mock()
            mock_font.render.return_value = mock_title_surface
            mock_title_surface.get_rect.return_value = "title_rect"

            create_title(self.screen)

            mock_font_class.assert_called_once_with("impact", 50)
            mock_font.render.assert_called_once_with("SNAKE", True, (105, 105, 105))
            mock_title_surface.get_rect.assert_called_once_with(centerx=200, y=80)
            mock_blit.assert_called_once_with(mock_title_surface, "title_rect")

    def test_getStartButtonRect_returnsStartButtonRect(self):
        with patch("pygame.Rect") as mock_rect:
            mock_rect.return_value = "start_button_rect"
            self.assertEqual("start_button_rect", get_start_button_rect())

    def test_drawStartButton_drawsStartButton_whenNotHovering(self):
        with (
            patch(
                "src.ui.ui_components.get_start_button_rect"
            ) as mock_get_start_button_rect,
            patch("pygame.mouse.get_pos", return_value=(0, 0)),
            patch("pygame.draw.rect"),
            patch("pygame.font.SysFont"),
        ):
            mock_button_rect = Mock()
            mock_button_rect.collidepoint.return_value = True
            mock_get_start_button_rect.return_value = mock_button_rect

            _draw_start_button(self.screen)

            mock_button_rect.collidepoint.assert_called_once_with((0, 0))

    def test_drawStartButton_drawsStartButton_whenHovering(self):
        with (
            patch(
                "src.ui.ui_components.get_start_button_rect"
            ) as mock_get_start_button_rect,
            patch("pygame.mouse.get_pos", return_value=(0, 0)),
            patch("pygame.draw.rect"),
            patch("pygame.font.SysFont"),
        ):
            mock_button_rect = Mock()
            mock_button_rect.collidepoint.return_value = False
            mock_get_start_button_rect.return_value = mock_button_rect

            _draw_start_button(self.screen)

            mock_button_rect.collidepoint.assert_called_once_with((0, 0))

    def test_drawInstructions_drawsInstructions(self):
        with (patch("pygame.font.SysFont") as mock_font_class,):
            mock_font = Mock()
            mock_font_class.return_value = mock_font
            mock_text_surface = Mock()
            mock_font.render.return_value = mock_text_surface
            mock_text_surface.get_rect.return_value = "text_rect"

            draw_instructions(self.screen, last=4)

            self.assertEqual(mock_font_class.call_count, 4)
            self.assertEqual(mock_font.render.call_count, 4)
            self.assertEqual(mock_text_surface.get_rect.call_count, 4)
            self.assertEqual(self.screen.blit.call_count, 4)
