from src.core.game_loop import game_loop
from src.core.game_state import GameState
from src.utils import constants as c

import pygame


def main() -> None:
    """
    Main function to run the game.
    Initializes the game and runs the game loop.
    """
    pygame.init()
    screen = pygame.display.set_mode((c.WINDOW_SIZE, c.WINDOW_SIZE))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    game_state = GameState()
    game_state.particle_system.screen = screen

    game_loop(screen, game_state, clock)

    pygame.quit()


if __name__ == "__main__":
    main()
