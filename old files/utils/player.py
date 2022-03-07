from .settings import pygame, SCREEN_WIDTH, SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self, character="Hiroki"):
        super(Player, self).__init__()
        if character == "Hiroki":
            self.image = pygame.image.load("img/Hiroki.png").convert()
            self.collision_sound = pygame.mixer.Sound("sounds/Hiroki_crash.wav")
        elif character == "Edward":
            self.image = pygame.image.load("img/Edward.png").convert()
            self.collision_sound = pygame.mixer.Sound("sounds/Edward_crash.wav")
        else:
            self.image = pygame.image.load("img/Hiroki.png").convert()
            self.collision_sound = pygame.mixer.Sound("sounds/Hiroki_crash.wav")

        self.image.set_colorkey((255, 185, 216), pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.bullets = []
        self.missile_cool_down = 0
        self.mass_missile_cool_down = 0
        self.bullet_sound = pygame.mixer.Sound("sounds/shoot_sound.wav")
        self.amount_of_bullets = 10

    def update(self, pressed_keys=None, clock=None, joystick=None):
        if joystick is not None:
            hat_pos = joystick.get_hat(0)
            if hat_pos[0] == 1:
                # It was moved right
                self.rect.move_ip(5, 0)
            if hat_pos[0] == -1:
                # left
                self.rect.move_ip(-5, 0)
            if hat_pos[1] == 1:
                # up
                self.rect.move_ip(0, -5)
            if hat_pos[1] == -1:
                # down
                self.rect.move_ip(0, 5)

            if joystick.get_button(0) or joystick.get_button(2):
                self.missile_cool_down += clock.get_time()
                self.mass_missile_cool_down += clock.get_time()
                if self.mass_missile_cool_down > 1000:
                    self.mass_missile_cool_down = 0
                if self.missile_cool_down > 200:
                    self.missile_cool_down = 0

                # Limit the bullet shooting to only when the bullets spent is < self.bullet_max
                # and all of the cooldowns are right.
                if self.missile_cool_down == 0 and self.mass_missile_cool_down < 500 and \
                        self.amount_of_bullets != 0:
                    self.bullet_sound.play()
                    self.amount_of_bullets -= 1
                    return "add_bullet"

        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)

        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)

        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)

        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        if pressed_keys[pygame.K_s]:
            self.missile_cool_down += clock.get_time()
            self.mass_missile_cool_down += clock.get_time()
            if self.mass_missile_cool_down > 1000:
                self.mass_missile_cool_down = 0
            if self.missile_cool_down > 200:
                self.missile_cool_down = 0

            # Limit the bullet shooting to only when the bullets spent is < self.bullet_max
            # and all of the cooldowns are right.
            self.missile_cool_down += clock.get_time()
            self.mass_missile_cool_down += clock.get_time()
            if self.mass_missile_cool_down > 1000:
                self.mass_missile_cool_down = 0
            if self.missile_cool_down > 200:
                self.missile_cool_down = 0

            # Limit the bullet shooting to only when the bullets spent is < self.bullet_max
            # and all of the cooldowns are right.
            if self.missile_cool_down == 0 and self.mass_missile_cool_down < 500 and\
                    self.amount_of_bullets != 0:
                self.bullet_sound.play()
                self.amount_of_bullets -= 1
                return "add_bullet"

    def die(self):
        self.collision_sound.play()
        self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.image = pygame.image.load("img/missile.png").convert_alpha()
        self.speed = 10
        self.rect = self.image.get_rect(
            center=(
                x+48, y+12
            )
        )

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def draw(self, win):
        win.blit(self.image, self.rect)
