import pygame

from utils.load_image import load_image

from game.player import Player
from game.poop import Poop
from game.cloud import Cloud

import sys
import os

pygame.init()

clock = pygame.time.Clock()
sky_image = load_image("img/sky.png").convert()
score_font = pygame.font.Font("fonts/Loma.ttf", 40)

poop_max_speed = 20
poop_minimum_speed = 7

# Add user events so that we can add poops on a timer
add_poop = pygame.USEREVENT + 1
pygame.time.set_timer(add_poop, 180)
add_cloud = pygame.USEREVENT + 2
pygame.time.set_timer(add_cloud, 1000)


def redraw_window(win, player_group, mostly_everything, score):
    win.blit(sky_image, (0, 0))
    player_group.draw(win)
    mostly_everything.draw(win)

    score_image = score_font.render(str(score), True, "red")
    win.blit(score_image, (690, 10))

    pygame.display.update()


def handle_collisions(win, player_group1: pygame.sprite.GroupSingle, poop_group: pygame.sprite.Group, player):
    if pygame.sprite.spritecollideany(player_group1.sprite, poop_group):
        pygame.mixer.music.stop()
        player.die()
        # Return false for running
        pygame.image.save(win, f"{os.getcwd()}/img/tmp/screenshot.png")
        return False
    else:
        return True


def handle_events(poops, mostly_everything):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == add_poop:
            new_poop = Poop(poop_max_speed, poop_minimum_speed)

            poops.add(new_poop)
            mostly_everything.add(new_poop)

        if event.type == add_cloud:
            new_cloud = Cloud()
            mostly_everything.add(new_cloud)


def main(win, game_class):
    # Player code
    player = Player()
    player_group = pygame.sprite.GroupSingle()
    player_group.add(player)
    mostly_everything = pygame.sprite.Group()
    poops = pygame.sprite.Group()

    score = 0

    # Play some music
    pygame.mixer.music.load(f"{os.getcwd()}/sounds/stained_glass.mp3")
    pygame.mixer.music.play(loops=-1)
    run = True

    while run:
        score += 1

        handle_events(poops, mostly_everything)

        keys = pygame.key.get_pressed()

        print("FPS:", clock.get_fps())

        player_group.update(keys)

        mostly_everything.update()
        redraw_window(win, player_group, mostly_everything, score)
        # handle_collisions updates the run variable
        # If the player hit a poop, set run to false
        run = handle_collisions(win, player_group, poops, player_group.sprite)

        clock.tick(30)

    game_class.playing = False
    game_class.current_menu = game_class.crash_menu
