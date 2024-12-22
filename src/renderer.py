from src import constants as c
from src.game_state import GameState
from src.graphics import draw_rectangle, draw_start_screen

import pygame


class Renderer:
    """
    Class to render the game state on the screen

    Attributes:
        screen (pygame.Surface): The screen to render on
    """

    def __init__(self, screen):
        self.screen = screen

    def render(self, game_state: GameState) -> None:
        """
        Render the game state on the screen

        Args:
            game_state (GameState): The current game state
        """
        self.screen.fill(c.BACKGROUND)

        if game_state.start_screen:
            draw_start_screen(self.screen)
        else:
            self._render_snake(game_state.snake)

            self._render_food(game_state.food_pos)

            if game_state.bonus_food_active:
                self._render_food(game_state.bonus_food_pos, bonus_food=True)

        pygame.display.flip()

    def _render_snake(self, snake):
        """Render the snake on the screen"""
        snake_head, *snake_body = snake.get_snake_body_positions()
        for segment in snake_body:
            draw_rectangle(
                self.screen,
                c.PASTEL_GREEN,
                segment[0],
                segment[1],
                c.CELL_SIZE,
                c.CELL_SIZE,
            )

        draw_rectangle(
            self.screen,
            c.DARKER_PASTEL_GREEN,
            snake_head[0],
            snake_head[1],
            c.CELL_SIZE,
            c.CELL_SIZE,
        )

        snake_right_eye, snake_left_eye = self._get_eyes_positions(
            snake_head, snake.direction
        )
        pygame.draw.rect(
            self.screen,
            c.TEXT_COLOR,
            (snake_right_eye[0], snake_right_eye[1], c.EYE_SIZE, c.EYE_SIZE),
        )
        pygame.draw.rect(
            self.screen,
            c.TEXT_COLOR,
            (snake_left_eye[0], snake_left_eye[1], c.EYE_SIZE, c.EYE_SIZE),
        )

    def _get_eyes_positions(self, head_pos, direction):
        """
        Calculate eyes positions based on head position and direction
        Returns tuple of (left_eye_pos, right_eye_pos)
        """

        if direction == c.LEFT:
            return (
                (head_pos[0] + c.EYE_DEPTH, head_pos[1] - c.EYE_OFFSET_SIDE_FAR),
                (head_pos[0] + c.EYE_DEPTH, head_pos[1] + c.EYE_OFFSET_SIDE_NEAR),
            )
        elif direction == c.UP:
            return (
                (head_pos[0] + c.EYE_OFFSET_NEAR, head_pos[1] - c.EYE_DEPTH_UP),
                (head_pos[0] + c.EYE_OFFSET_FAR, head_pos[1] - c.EYE_DEPTH_UP),
            )
        elif direction == c.RIGHT:
            return (
                (
                    head_pos[0] + c.CELL_SIZE - c.EYE_DEPTH - c.EYE_SIZE,
                    head_pos[1] - c.EYE_OFFSET_SIDE_FAR,
                ),
                (
                    head_pos[0] + c.CELL_SIZE - c.EYE_DEPTH - c.EYE_SIZE,
                    head_pos[1] + c.EYE_OFFSET_SIDE_NEAR,
                ),
            )
        elif direction == c.DOWN:
            return (
                (head_pos[0] + c.EYE_OFFSET_NEAR, head_pos[1] + c.EYE_DEPTH),
                (head_pos[0] + c.EYE_OFFSET_FAR, head_pos[1] + c.EYE_DEPTH),
            )

    def _render_food(self, food_pos, bonus_food=False):
        """Render the food on the screen"""
        color = c.MINT_GREEN if bonus_food else c.PASTEL_PINK

        draw_rectangle(
            self.screen,
            color,
            food_pos[0] * c.CELL_SIZE,
            food_pos[1] * c.CELL_SIZE,
            c.CELL_SIZE,
            c.CELL_SIZE,
        )
