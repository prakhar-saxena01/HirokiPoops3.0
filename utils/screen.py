import pygame
import os

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height), pygame.SCALED)
pygame.display.set_icon(pygame.image.load(os.path.join(os.getcwd(), "img/game_icon.png")).convert_alpha())
