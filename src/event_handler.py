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
        if event.key == pygame.K_r:
            self.game_state.reset()
        elif event.key == pygame.K_q:
            return False
        return True
