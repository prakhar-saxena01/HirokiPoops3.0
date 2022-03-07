from .settings import SCREEN_HEIGHT, SCREEN_WIDTH, placeholder_function, DummyJoystick
from .fonts import get_font, render_font, pygame
from .button import Button
from .score import check_and_save_score
import sys


def crash(win, score, joystick=DummyJoystick()):
    button_list = [
        Button(150, 450, 100, 50, (0, 170, 0), "green", action=placeholder_function, text="Play Again"),
        Button(550, 450, 100, 50, (170, 0, 0), "red", action=placeholder_function, text="Quit"),
        Button(320, 450, 150, 50, (0, 0, 150), "blue", action=placeholder_function, text="Main Menu")
    ]
    cool_down = 0
    current_button_index = 0
    clock = pygame.time.Clock()
    large_text = get_font("comic.ttf", 115)
    text_surf, text_rect = render_font("You Crashed", large_text)
    text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 60)
    win.blit(text_surf, text_rect)

    with open("saves/highscore.txt") as f:
        high_score = f.read()

    small_text = get_font("comic.ttf", 40)
    text_surf2, text_rect2 = render_font("High score: " + high_score, small_text)
    text_rect2.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 40)
    win.blit(text_surf2, text_rect2)

    check_and_save_score(score)

    text_surf2, text_rect2 = render_font("Your score: " + str(score), small_text)
    text_rect2.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 95)
    win.blit(text_surf2, text_rect2)

    while True:
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == pygame.KEYDOWN:
                # Was it the Escape key? If so, stop the loop
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    if button_list[current_button_index].text == "Play Again":
                        return "game_loop"
                    if button_list[current_button_index].text == "Main Menu":
                        return "main_menu"
                    if button_list[current_button_index].text == "Quit":
                        pygame.quit()
                        sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 11 or event.button == 7:
                    # the start button was pressed so we will start the game
                    return "game_loop"
                if event.button == 0 or event.button == 2:
                    if button_list[current_button_index].text == "Play Again":
                        return "game_loop"
                    if button_list[current_button_index].text == "Main Menu":
                        return "main_menu"
                    if button_list[current_button_index].text == "Quit":
                        pygame.quit()
                        sys.exit()

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
