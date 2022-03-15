import pygame

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


def redraw_window(win, player_group, mostly_everything):
    win.blit(sky_image, (0, 0))
    player_group.draw(win)
    mostly_everything.draw(win)

    pygame.display.update()


def handle_collisions(player_group1: pygame.sprite.GroupSingle, poop_group: pygame.sprite.Group, player):
    if pygame.sprite.spritecollideany(player_group1.sprite, poop_group):
        pygame.mixer.music.stop()
        player.die()
        # show game over screen, with highscore and other stuff
        # Return false for running
        return False
    else:
        return True


def main(win, game_class):
    # Player code
    player = Player()
    player_group = pygame.sprite.GroupSingle()
    player_group.add(player)
    mostly_everything = pygame.sprite.Group()
    poops = pygame.sprite.Group()

    # Play some music
    pygame.mixer.music.load(os.path.join(os.getcwd(), "sounds/stained_glass.mp3"))
    pygame.mixer.music.play(loops=-1)
    run = True
    freeze_keys = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == add_poop:
                new_poop = Poop(poop_max_speed, poop_minimum_speed)

                poops.add(new_poop)
                mostly_everything.add(new_poop)

        keys = pygame.key.get_pressed()

        print("fps:", clock.get_fps())

        player_group.update(keys)

        mostly_everything.update()
        redraw_window(win, player_group, mostly_everything)
        # handle_collisions updates the run variable
        # If the player hit a poop, set run to false
        run = handle_collisions(player_group, poops, player_group.sprite)

        clock.tick(30)

    game_class.playing = False

# if __name__ == '__main__':
#     main(window)
