import pygame

from src import constants as c


def draw_rectangle(screen, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))

def draw_start_screen(screen: pygame.Surface):
    """
    Draw the start screen on the screen.

    Args:
        screen (pygame.Surface): The screen to draw on
    """
    screen.fill(c.BACKGROUND)

    _draw_title(screen)
    _draw_start_button(screen)


def _draw_title(screen: pygame.Surface):
    title_font = pygame.font.SysFont(c.TITLE_FONT, c.TITLE_FONT_SIZE)
    title_surface = title_font.render(c.TITLE_TEXT, True, c.TITLE_COLOR)
    title_rect = title_surface.get_rect(centerx=c.WINDOW_SIZE // 2, y=c.TITLE_Y_POS)

    screen.blit(title_surface, title_rect)


def get_start_button_rect() -> pygame.Rect:
    """
    Get the rectangle of the start button.

    Returns:
        pygame.Rect: The rectangle of the start button
    """
    return pygame.Rect(
        (c.WINDOW_SIZE - c.START_BUTTON_WIDTH) // 2,
        (c.WINDOW_SIZE - c.START_BUTTON_HEIGHT * 3),
        c.START_BUTTON_WIDTH,
        c.START_BUTTON_HEIGHT,
    )


def _draw_start_button(screen: pygame.Surface | None) -> pygame.Rect:
    """
    Draw the start button on the screen.

    Args:
        screen (pygame.Surface): The screen to draw on

    Returns:
        pygame.Rect: The rectangle of the start button
    """
    button_rect = get_start_button_rect()

    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        button_color = c.START_BUTTON_HOVER_COLOR
        button_text_color = c.START_BUTTON_TITLE_HOVER_COLOR
    else:
        button_color = c.START_BUTTON_COLOR
        button_text_color = c.START_BUTTON_TITLE_COLOR

    pygame.draw.rect(screen, button_color, button_rect)

    button_font = pygame.font.SysFont(None, c.START_BUTTON_FONT_SIZE)
    button_surface = button_font.render(c.START_BUTTON_TEXT, True, button_text_color)
    text_rect = button_surface.get_rect(center=button_rect.center)

    screen.blit(button_surface, text_rect)

    return button_rect

#
# def draw_game_over(screen: pygame.Surface, game_state: GameState) -> None:
#     """
#     Draw the game over screen on the screen.
#
#     Args:
#         screen (pygame.Surface): The screen to draw on
#         game_state (GameState): The current game state
#     """
#     overlay = pygame.Surface((c.WINDOW_SIZE, c.WINDOW_SIZE))
#     overlay.set_alpha(200)
#     overlay.fill(c.BLACK)
#     screen.blit(overlay, (0, 0))
#
#     font = pygame.font.Font(None, c.FONT_SIZE)
#
#     if game_state.winner:
#         text = f"Player {game_state.winner} wins!"
#     else:
#         text = "It's a draw!"
#
#     text_surface = font.render(text, True, c.TEXT_COLOR)
#     text_rect = text_surface.get_rect(
#         center=(c.WINDOW_SIZE // 2, c.WINDOW_SIZE // 2 - 30)
#     )
#     screen.blit(text_surface, text_rect)
#
#     small_font = pygame.font.Font(None, c.FONT_SIZE // 2)
#     instruction_text = 'Press "R" to try again or "Q" to quit'
#     instruction_surface = small_font.render(instruction_text, True, c.TEXT_COLOR)
#     instruction_rect = instruction_surface.get_rect(
#         center=(c.WINDOW_SIZE // 2, c.WINDOW_SIZE // 2 + 20)
#     )
#     screen.blit(instruction_surface, instruction_rect)
#
#
# def draw_score(screen: pygame.Surface, game_state: GameState) -> None:
#     """
#     Draw the score on the screen.
#
#     Args:
#         screen (pygame.Surface): The screen to draw on
#         game_state (GameState): The current game state
#     """
#     font = pygame.font.Font(None, c.SCORE_FONT_SIZE)
#
#     score_text = (
#         f"X: {game_state.scores['X']}      "
#         f"Draws: {game_state.scores['Draws']}      "
#         f"O: {game_state.scores['O']}"
#     )
#
#     score_surface = font.render(score_text, True, c.SCORE_COLOR)
#     score_rect = score_surface.get_rect(midtop=(c.WINDOW_SIZE // 2, c.SCORE_PADDING))
#
#     screen.blit(score_surface, score_rect)