import pygame
from utils.screen import window
from utils.load_image import load_image
from game.player import Player
import sys
import os

pygame.init()


clock = pygame.time.Clock()
sky_image = load_image("img/sky.png").convert()


# Add user events so that we can add poops on a timer
add_poop = pygame.USEREVENT + 1
pygame.time.set_timer(add_poop, 180)
add_cloud = pygame.USEREVENT + 2
pygame.time.set_timer(add_cloud, 1000)

# Player code
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)


def main(win):

    # Play some music
    pygame.mixer.music.load(os.path.join(os.getcwd(), "sounds/stained_glass.mp3"))
    pygame.mixer.music.play(loops=-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        win.blit(sky_image, (0, 0))
        keys = pygame.key.get_pressed()
        player_group.update(keys)
        player_group.draw(win)

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main(window)
