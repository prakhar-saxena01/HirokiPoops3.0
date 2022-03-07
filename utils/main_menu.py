from .settings import pygame, SCREEN_WIDTH, SCREEN_HEIGHT, placeholder_function, DummyJoystick
from .fonts import get_font, render_font
from .button import Button
import sys

clock = pygame.time.Clock()


def main_menu(win, joystick=DummyJoystick()):
    pygame.mixer.music.load("sounds/he'll_take_care_of_the_rest.mp3")
    pygame.mixer.music.play(loops=-1)

    title_image = pygame.image.load("img/title.png").convert()
    current_button_index = 0
    cool_down = 0
    button_list = [
        Button(150, 450, 100, 50, (0, 170, 0), "green", placeholder_function, "Play"),
        Button(550, 450, 100, 50, (170, 0, 0), "red", placeholder_function, "Quit")
    ]

    intro = True
    while intro:
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == pygame.KEYDOWN:
                # Was it the Escape key? If so, stop the loop
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == 13:
                    if button_list[current_button_index].text == "Play":
                        return "character_select"
                    elif button_list[current_button_index].text == "Quit":
                        pygame.quit()
                        sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0 or event.button == 2:
                    if button_list[current_button_index].text == "Play":
                        return "character_select"
                    elif button_list[current_button_index].text == "Quit":
                        pygame.quit()
                        sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 11 or event.button == 7:
                    # the start button was pressed so we will start the game
                    return "character_select"

        win.blit(title_image, (0, 0))
        large_text = get_font("comic.ttf", 115)
        text_surf, text_rect = render_font("Hiroki's Poops", large_text)
        text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 10)
        win.blit(text_surf, text_rect)

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

        if current_button_index > len(button_list) - 1:
            current_button_index = 0
        if current_button_index < 0:
            current_button_index = len(button_list) - 1

        button_list[current_button_index].active = True

        for button in button_list:
            button.draw(win)

        pygame.display.update()
        clock.tick(15)
