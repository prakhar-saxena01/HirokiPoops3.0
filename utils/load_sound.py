import pygame
import os


def load_sound(path):
    new_path = os.path.join(os.getcwd(), path)
    sound = pygame.mixer.Sound(new_path)
    return sound
