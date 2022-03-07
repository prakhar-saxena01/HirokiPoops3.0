from .settings import pygame
import os


def get_font(font_name, size):
    main_dir = os.getcwd()
    return pygame.font.Font(os.path.join(main_dir, "fonts", font_name), size)


def render_font(text: str, font):
    """Returns a text surface and a text rect."""
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect()
