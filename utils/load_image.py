import pygame
import os

pygame.init()


def load_image(rel_path: str):
    """
    You may want to call the .convert() function afterwards on your image.

    @param rel_path: the relative path to your image
    @return: the loaded iamge

    """

    new_path = os.path.join(os.getcwd(), rel_path)
    image = pygame.image.load(new_path)
    return image
