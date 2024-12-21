import pygame


def draw_rectangle(screen, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))
