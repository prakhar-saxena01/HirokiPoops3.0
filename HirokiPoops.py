import pygame
from game_class import Game
from utils.screen import window

import os


if os.path.exists(f"{os.getcwd()}/img/temporary/screenshot.png"):
    os.remove(f"{os.getcwd()}/img/temporary/screenshot.png")

pygame.init()
pygame.mouse.set_visible(False)


g = Game(window)
pygame.mixer.music.load(f"{os.getcwd()}/sounds/he'll_take_care_of_the_rest.mp3")
pygame.mixer.music.play(loops=-1)

while g.running:
    g.current_menu.display_menu()

    if g.playing:
        g.game_loop()
