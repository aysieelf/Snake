from src import constants as c
from src.game_state import GameState

import pygame


class EventHandler:
    """
    Class to handle all the events in the game

    Args:
        game_state (GameState): The current game state

    Attributes:
        game_state (GameState): The current game state
    """

    def __init__(self, game_state: GameState) -> None:
        self.game_state = game_state

    def handle_events(self) -> bool:
        """
        Handle all the events in the game

        Returns:
            bool: True if the game should continue, False if the game should end
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                continue_game = self._handle_keyboard(event)
                if not continue_game:
                    return False
        return True

    def _handle_keyboard(self, event: pygame.event.Event) -> bool:
        """
        Handle the keyboard events

        Args:
            event (pygame.event): The event to handle
                - R key: Resets the game
                - Q key: Exits the game

        Returns:
            bool: True if the game should continue, False if the game should end
        """
        # Restart the game
        if event.key == pygame.K_r:
            self.game_state.reset()

        # Exit the game
        elif event.key == pygame.K_q:
            return False

        # Change the direction of the snake
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            self.game_state.snake.change_direction(c.UP)
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.game_state.snake.change_direction(c.LEFT)
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.game_state.snake.change_direction(c.DOWN)
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.game_state.snake.change_direction(c.RIGHT)

        # Pause the game
        elif event.key == pygame.K_SPACE:
            self.game_state.pause_game() if not self.game_state.paused else self.game_state.continue_game()

        return True
