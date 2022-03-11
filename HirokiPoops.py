import sys
import pygame
from utils.screen import window
from utils.load_image import load_image

pygame.init()


clock = pygame.time.Clock()
sky_image = load_image("img/sky.png").convert()


# Add user events so that we can add poops on a timer
add_poop = pygame.USEREVENT + 1
pygame.time.set_timer(add_poop, 180)
add_cloud = pygame.USEREVENT + 2
pygame.time.set_timer(add_cloud, 1000)


def main(win):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        win.blit(sky_image, (0, 0))

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main(window)
