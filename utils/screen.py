import pygame
from utils.load_image import load_image

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height), pygame.SCALED)
pygame.display.set_icon(load_image("img/game_icon.png").convert_alpha())
pygame.display.set_caption("Hiroki's Poops")
