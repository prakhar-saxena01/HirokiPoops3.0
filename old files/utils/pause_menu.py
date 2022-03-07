from .fonts import get_font, render_font
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT, pygame, placeholder_function, DummyJoystick
from .button import Button
import sys

clock = pygame.time.Clock()


def paused(win, joystick=DummyJoystick()):

    current_button_index = 0
    cool_down = 0
    button_list = [
        Button(150, 450, 100, 50, (0, 170, 0), "green", placeholder_function, "Continue"),
        Button(550, 450, 100, 50, (170, 0, 0), "red", placeholder_function, "Quit"),
        Button(320, 450, 150, 50, (0, 0, 150), "blue", placeholder_function, "Main Menu")
    ]

    pause = True
    large_text = get_font("comic.ttf", 115)
    text_surf, text_rect = render_font("Paused", large_text)
    text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    win.blit(text_surf, text_rect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:
                    pause = False
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == 13:
                    if button_list[current_button_index].text == "Continue":
                        pause = False
                    elif button_list[current_button_index].text == "Quit":
                        pygame.quit()
                        sys.exit()
                    elif button_list[current_button_index].text == "Main Menu":
                        return "main_menu"

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 11 or event.button == 7:
                    # the start button was pressed so we will un pause
                    pause = False
                if event.button == 0 or event.button == 2:
                    if button_list[current_button_index].text == "Continue":
                        pause = False
                    elif button_list[current_button_index].text == "Quit":
                        pygame.quit()
                        sys.exit()
                    elif button_list[current_button_index].text == "Main Menu":
                        return "main_menu"

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
        clock.tick(30)
