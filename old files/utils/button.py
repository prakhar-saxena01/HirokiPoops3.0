from .settings import pygame
from .fonts import get_font


class Button:
    def __init__(self, x, y, width, height, color, active_color, action=None, text=None,
                 text_color=(0, 0, 0), text_size=20, font="comic.ttf"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.action = action
        self.text_size = text_size
        self.font = font
        self.is_clicked = False
        self.active_color = active_color
        self.active = False

    def draw(self, win):
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 0:
            self.is_clicked = False
        mouse_pos = pygame.mouse.get_pos()

        if self.active:
            pygame.draw.rect(win, self.active_color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

        self.active = False

        if self.text:
            button_font = get_font(self.font, self.text_size)
            text_surface = button_font.render(self.text, 1, self.text_color)
            win.blit(text_surface, (self.x + self.width /
                                    2 - text_surface.get_width() / 2,
                                    self.y + self.height / 2 - text_surface.get_height() / 2))

    def clicked(self, pos):
        x, y = pos

        if not (self.x <= x <= self.x + self.width):
            return False
        if not (self.y <= y <= self.y + self.height):
            return False

        if not self.is_clicked:
            self.is_clicked = True
            return True
