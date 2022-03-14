import pygame

from utils.screen import window
from utils.load_image import load_image

from game.player import Player
from game.poop import Poop

import sys
import os


pygame.init()


clock = pygame.time.Clock()
sky_image = load_image("img/sky.png").convert()


poop_max_speed = 20
poop_minimum_speed = 7


# Add user events so that we can add poops on a timer
add_poop = pygame.USEREVENT + 1
pygame.time.set_timer(add_poop, 180)
add_cloud = pygame.USEREVENT + 2
pygame.time.set_timer(add_cloud, 1000)


# Player code
player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)
mostly_everything = pygame.sprite.Group()
poops = pygame.sprite.Group()


def redraw_window(win):
    win.blit(sky_image, (0, 0))
    player_group.draw(win)
    mostly_everything.draw(win)

    pygame.display.update()


def main(win):
    # Play some music
    pygame.mixer.music.load(os.path.join(os.getcwd(), "sounds/stained_glass.mp3"))
    pygame.mixer.music.play(loops=-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == add_poop:
                new_poop = Poop(poop_max_speed, poop_minimum_speed)

                poops.add(new_poop)
                mostly_everything.add(new_poop)
                print("New poop")

        # Deal with user input
        keys = pygame.key.get_pressed()
        player_group.update(keys)
        mostly_everything.update()
        redraw_window(win)

        clock.tick(30)


if __name__ == '__main__':
    main(window)
