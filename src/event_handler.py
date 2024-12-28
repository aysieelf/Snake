from src.core.game_state import GameState
from src.ui.ui_components import get_start_button_rect
from src.utils import constants as c

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_start_screen_click()
        return True

    def _handle_keyboard(self, event: pygame.event.Event) -> bool:
        """
        Handle the keyboard events

        Args:
            event (pygame.event): The event to handle
                - R key: Resets the game
                - Q key: Exits the game to start screen or closes the game
                - W key or UP arrow key: Move the snake up
                - A key or LEFT arrow key: Move the snake left
                - S key or DOWN arrow key: Move the snake down
                - D key or RIGHT arrow key: Move the snake right
                - SPACE key: Pause or start the game


        Returns:
            bool: True if the game should continue, False if the game should end
        """
        # Restart the game
        if event.key == pygame.K_r:
            self.game_state.reset()

        # Exit the game
        elif event.key == pygame.K_q:
            return self._handle_exit_game()

        # Change the direction of the snake
        elif event.key in [
            pygame.K_w,
            pygame.K_UP,
            pygame.K_a,
            pygame.K_LEFT,
            pygame.K_s,
            pygame.K_DOWN,
            pygame.K_d,
            pygame.K_RIGHT,
        ]:
            self._handle_direction_change(event.key)

        # Pause or start the game
        elif event.key == pygame.K_SPACE:
            self._handle_space_key()

        return True

    def _handle_exit_game(self) -> bool:
        """
        Handle the exit game event

        Returns:
            bool: True if the game should continue, False if the game should end
        """
        if not self.game_state.start_screen:
            self.game_state.pause_game()
            self.game_state.exit_to_start_screen()
            return True
        else:
            return False

    def _handle_direction_change(self, key: int) -> None:
        """
        Handle the direction change of the snake

        Args:
            key (int): The key pressed by the user
        """
        if key == pygame.K_w or key == pygame.K_UP:
            self.game_state.snake.change_direction(c.UP)
        elif key == pygame.K_a or key == pygame.K_LEFT:
            self.game_state.snake.change_direction(c.LEFT)
        elif key == pygame.K_s or key == pygame.K_DOWN:
            self.game_state.snake.change_direction(c.DOWN)
        elif key == pygame.K_d or key == pygame.K_RIGHT:
            self.game_state.snake.change_direction(c.RIGHT)

    def _handle_space_key(self) -> None:
        """
        Handle the space key press event
        If the game is not paused, pause the game
        If the game is paused, continue the game
        If the game is in the start screen, start the game
        """
        if not self.game_state.paused:
            self.game_state.pause_game()
            return
        if self.game_state.start_screen:
            self.game_state.start_game()
        self.game_state.continue_game()

    def _handle_start_screen_click(self) -> None:
        """
        Handle the click event in the start screen
        """
        button_rect = get_start_button_rect()
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            self.game_state.start_game()
