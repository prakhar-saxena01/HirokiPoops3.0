import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("Hiroki's Poops")
icon_img = pygame.image.load("img/game_icon.png").convert_alpha()
pygame.display.set_icon(icon_img)


def placeholder_function(): pass


class DummyJoystick:
    def __init__(self):
        pass

    @staticmethod
    def get_hat(hat):
        return 0, 0
