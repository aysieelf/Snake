import os
import sys
import pygame

from src.core.game_loop import game_loop
from src.core.game_state import GameState
from src.utils import constants as c

# To create a standalone executable:
# pyinstaller --windowed --onedir --name "Snake" --icon=assets/images/icon-macos.icns --add-data "assets:assets" main.py

def get_resource_path() -> str:
    """
    Return the path to the resource directory.

    Returns:
        str: The path to the resource directory
    """
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    """
    Main function to run the game.
    Creates a game state, initializes pygame, and runs the game loop.
    """
    os.chdir(get_resource_path())

    pygame.init()
    pygame.display.set_icon(pygame.image.load('assets/images/icon.png'))
    screen = pygame.display.set_mode((c.WINDOW_SIZE, c.WINDOW_SIZE))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    try:
        game_state = GameState()
        game_state.particle_system.screen = screen
        game_loop(screen, game_state, clock)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()