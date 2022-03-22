import pygame
from utils.screen import width, height
import random


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load("img/cloud.png").convert()
        self.image.set_colorkey((0, 0, 0), pygame.RLEACCEL)

        self.rect = self.image.get_rect(
            center=(
                random.randint(width + 20, width + 100),
                random.randint(0, height),
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
