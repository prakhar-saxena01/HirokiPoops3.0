import pygame
import os


def load_sound(path):
    new_path = f"{os.getcwd()}/{path}"
    sound = pygame.mixer.Sound(new_path)
    return sound
