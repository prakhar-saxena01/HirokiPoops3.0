from .settings import pygame, SCREEN_WIDTH, SCREEN_HEIGHT
import random


class Poop(pygame.sprite.Sprite):
    def __init__(self, poop_speed, poop_minimum_speed):
        super(Poop, self).__init__()
        self.image = pygame.image.load("img/poop.png").convert()
        self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.dead = False
        self.dead_iter = 0
        # The starting position is randomly generated, as is the speed
        self.rect = self.image.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.poop_max_speed = round(poop_speed)
        self.poop_minimum_speed = round(poop_minimum_speed)
        self.speed = random.randint(6, self.poop_max_speed)
        self.poop_explode_sound = pygame.mixer.Sound("sounds/splat.wav")

    # Move the poop based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        if self.dead:
            if self.dead_iter < 1:
                self.image = pygame.image.load("img/explosion.png").convert_alpha()
            elif self.dead_iter > 1 and not self.dead_iter > 6:
                self.image = pygame.transform.scale(self.image, (16 * int(self.dead_iter), int(16 * self.dead_iter)))
            elif self.dead_iter > 6:
                self.image = pygame.transform.scale(self.image, (int(self.image.get_width() / 1.5),
                                                                 int(self.image.get_height() / 1.5)))
            self.dead_iter += 1

    def explode(self):
        self.dead = True
        self.poop_explode_sound.play()
