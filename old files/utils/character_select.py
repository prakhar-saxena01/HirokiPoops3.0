import pygame

from .button import Button
from .settings import placeholder_function, DummyJoystick
import sys


def character_select(win: pygame.Surface, joystick=DummyJoystick()):
    buttons = [
        Button(55, 350, 150, 100, "blue", "cornflowerblue", action=placeholder_function, text="Hiroki", text_size=40),
        Button(win.get_width()-210, 350, 150, 100, "blue", "cornflowerblue", action=placeholder_function, text="Edward",
               text_size=40)
    ]

    current_button_index = 0

    hiroki = pygame.image.load("img/portraits/hiroki-portrait.png").convert_alpha()
    portrait_rect = hiroki.get_rect()
    portrait_rect.centerx = win.get_width()/2
    portrait_rect.centery = win.get_height()/2 - 100

    edward = pygame.image.load("img/portraits/edward-portrait.png").convert_alpha()

    character = "Hiroki"
    cool_down = 0
    clock = pygame.time.Clock()

    while 1:
        for event in pygame.event.get():
            # Handle quit events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == 13:
                    # The user pressed enter
                    if character == "Hiroki":
                        return "Hiroki"
                    elif character == "Edward":
                        return "Edward"
                    else:
                        return "Hiroki"

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0 or event.button == 2:
                    if character == "Hiroki":
                        return "Hiroki"
                    elif character == "Edward":
                        return "Edward"
                    else:
                        return "Hiroki"

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        win.fill("grey")
        keys = pygame.key.get_pressed()

        if joystick.get_hat(0)[0] == 1 or keys[pygame.K_RIGHT]:
            # joystick was pressed right
            cool_down += clock.get_time()
            if cool_down > 100:
                cool_down = 0
            if cool_down == 0:
                current_button_index -= 1
        elif joystick.get_hat(0)[0] == -1 or keys[pygame.K_LEFT]:
            # joystick was pressed left
            cool_down += clock.get_time()
            if cool_down > 100:
                cool_down = 0
            if cool_down == 0:
                current_button_index += 1

        if current_button_index > len(buttons)-1:
            current_button_index = 0
        if current_button_index < 0:
            current_button_index = len(buttons)-1

        buttons[current_button_index].active = True
        if buttons[current_button_index].text == "Hiroki":
            character = "Hiroki"
        elif buttons[current_button_index].text == "Edward":
            character = "Edward"

        for button in buttons:
            button.draw(win)
            if button.active:
                if button.text == "Hiroki":
                    character = "Hiroki"
                elif button.text == "Edward":
                    character = "Edward"

        if character == "Hiroki":
            win.blit(hiroki, portrait_rect)
        elif character == "Edward":
            win.blit(edward, portrait_rect)

        pygame.draw.rect(win, "blue", portrait_rect, 5)

        pygame.display.update()
        clock.tick(30)
