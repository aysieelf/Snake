from src.utils import constants as c

import pygame


def create_rectangle(screen, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))


def draw_start_screen(screen: pygame.Surface):
    """
    Draw the start screen on the screen.

    Args:
        screen (pygame.Surface): The screen to draw on
    """
    screen.fill(c.BACKGROUND)

    create_title(screen)
    draw_instructions(screen, last=4)
    _draw_start_button(screen)


def create_title(screen: pygame.Surface):
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


def draw_instructions(screen: pygame.Surface, first=0, last=len(c.INSTRUCTIONS)):
    """
    Draw the instructions on the screen.

    Args:
        screen (pygame.Surface): The screen to draw on
    """
    curr_y_pos = c.INSTRUCTIONS_POS
    for instruction in c.INSTRUCTIONS[first:last]:
        font = pygame.font.SysFont(c.INSTRUCTIONS_FONT, c.INSTRUCTIONS_FONT_SIZE)
        instruction_surface = font.render(instruction, True, c.TEXT_COLOR)
        instruction_rect = instruction_surface.get_rect(
            center=(c.WINDOW_SIZE // 2, curr_y_pos)
        )
        curr_y_pos += 20
        screen.blit(instruction_surface, instruction_rect)
