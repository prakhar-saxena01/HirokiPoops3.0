from game import Game
import pygame

pygame.init()

width, height = 480, 500

window = pygame.display.set_mode((width, height), pygame.SCALED)

g = Game(window)

while g.running:
    g.current_menu.display_menu()
    g.game_loop()

print("Quit")
