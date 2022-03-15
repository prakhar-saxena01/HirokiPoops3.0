from game_class import Game
import pygame
from utils.screen import window

pygame.init()


g = Game(window)

while g.running:
    g.current_menu.display_menu()
    if g.playing:
        g.game_loop()

print("Quit")
