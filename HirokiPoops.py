from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from utils.settings import pygame, SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH
from utils import Player, Poop, Cloud, get_font
from utils.player import Bullet
from utils.crash import crash
from utils.main_menu import main_menu
from utils.pause_menu import paused
from utils.character_select import character_select
import sys

clock = pygame.time.Clock()

# Create custom events for adding a new enemy and cloud
add_enemy = pygame.USEREVENT + 1
# pygame.time.set_timer(add_enemy, 200)
pygame.time.set_timer(add_enemy, 180)
add_cloud = pygame.USEREVENT + 2
pygame.time.set_timer(add_cloud, 1000)

# Get the joysticks and set them up
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

if len(joysticks) < 1:
    use_joystick = False
else:
    use_joystick = True


def excellent(player, increment_bullets=False):
    if increment_bullets:
        player.amount_of_bullets += 10
    font = get_font("comic.ttf", 60)
    text = font.render("Excellent!!", True, "black")
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    SCREEN.blit(text, text_rect)


def game_loop(character="Hiroki"):
    pygame.mixer.music.load("sounds/stained_glass.mp3")
    pygame.mixer.music.play(loops=-1)
    sky_image = pygame.image.load("img/sky.png").convert()

    if character == "Hiroki":
        player = Player()
    elif character == "Edward":
        player = Player(character=character)
    else:
        player = Player()

    # Create groups to hold poop sprites, cloud sprites, and all sprites
    # - poops is used for collision detection and position updates
    # - clouds is used for position updates
    # - all_sprites is used for rendering
    poops = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    dead_poops = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    bullets = pygame.sprite.Group()

    score = 0
    poop_max_speed = 20
    poop_minimum_speed = 7
    score_font = get_font("tahoma.ttf", 40)
    excellent_iteration = 0

    def multiples(m, count):
        return_dict = []
        for i in range(count):
            return_dict.append(i * m)
        return return_dict

    multiples_of_1000 = multiples(1000, 1000)
    score_for_loop_broken = False
    found_score = None

    # Main loop
    while 1:
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:
                    if use_joystick:
                        pause_info = paused(SCREEN, joysticks[0])
                    else:
                        pause_info = paused(SCREEN)

                    if pause_info == "main_menu":
                        if use_joystick:
                            menu_info_2 = main_menu(SCREEN, joysticks[0])
                        else:
                            menu_info_2 = main_menu(SCREEN)

                        if menu_info_2 == "character_select":
                            if use_joystick:
                                character_select_info2 = character_select(SCREEN, joysticks[0])
                            else:
                                character_select_info2 = character_select(SCREEN)
                            # Check which character the user picked. Then start the game accordingly.
                            if character_select_info2 == "Hiroki":
                                game_loop()
                            elif character_select_info2 == "Edward":
                                game_loop(character="Edward")
                            else:
                                game_loop()
                        if menu_info_2 == "game_loop":
                            game_loop()

                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    # Set the cool downs to a big number, so that they reset. (The player class states that if the
                    # cool down is greater than a certain number, reset it.)
                    player.mass_missile_cool_down, player.mass_missile_cool_down = 100000000000, 100000000000

            # Check if a JoyStick button was pressed
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 11 or event.button == 7:
                    # the start button was pressed so we will pause
                    if use_joystick:
                        pause_info = paused(SCREEN, joysticks[0])
                    else:
                        pause_info = paused(SCREEN)

                    if pause_info == "main_menu":
                        if use_joystick:
                            menu_info_2 = main_menu(SCREEN, joysticks[0])
                        else:
                            menu_info_2 = main_menu(SCREEN)

                        if menu_info_2 == "character_select":
                            if use_joystick:
                                character_select_info2 = character_select(SCREEN, joysticks[0])
                            else:
                                character_select_info2 = character_select(SCREEN)
                            # Check which character the user picked. Then start the game accordingly.
                            if character_select_info2 == "Hiroki":
                                game_loop()
                            elif character_select_info2 == "Edward":
                                game_loop(character="Edward")
                            else:
                                game_loop()
                        if menu_info_2 == "game_loop":
                            game_loop()

            if event.type == pygame.JOYBUTTONUP:
                if event.button == 0 or event.button == 2:
                    # Set the cool downs to a big number, so that they reset. (The player class states that if the
                    # cool down is greater than a certain number, reset it.)
                    player.mass_missile_cool_down, player.mass_missile_cool_down = 100000, 100000

            # Did the user click the window close button? If so, stop the loop
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Should we add a new enemy?
            elif event.type == add_enemy:
                # Create the new enemy, and add it to our sprite groups
                new_enemy = Poop(poop_max_speed, poop_minimum_speed)

                poops.add(new_enemy)
                all_sprites.add(new_enemy)

            # Should we add a new cloud?
            elif event.type == add_cloud:
                # Create the new cloud, and add it to our sprite groups
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)

        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()

        if use_joystick:
            player_return_info = player.update(pressed_keys=pressed_keys, joystick=joysticks[0], clock=clock)
            if player_return_info == "add_bullet":
                bullet = Bullet(player.rect.x, player.rect.y)

                bullets.add(bullet)
                all_sprites.add(bullet)
        # If no input, just use keyboard input.
        else:
            player_return_info = player.update(pressed_keys=pressed_keys, clock=clock)
            if player_return_info == "add_bullet":
                bullet = Bullet(player.rect.x, player.rect.y)

                bullets.add(bullet)
                all_sprites.add(bullet)

        # Update the position of our enemies and clouds
        poops.update()
        clouds.update()
        bullets.update()
        dead_poops.update()
        score += 1

        # Put on the screen the sky image.
        SCREEN.blit(sky_image, (0, 0))

        # Draw all our sprites
        all_sprites.draw(SCREEN)

        # print(joysticks[0].get_hat(0))

        score_img = score_font.render(str(score), True, (225, 0, 0))
        SCREEN.blit(score_img, (690, 10))

        bullets_left_image = score_font.render("Bullets: " + str(player.amount_of_bullets), True,
                                               (225, 0, 0))
        SCREEN.blit(bullets_left_image, (450, 10))

        for item in multiples_of_1000:
            if item - 20 <= score <= item:
                # print(item - 80, score, item + 80)
                score_for_loop_broken = True
                found_score = item
                break

        if score_for_loop_broken:
            if found_score <= score < found_score + 50:
                if excellent_iteration == 0:
                    excellent(player, True)
                    excellent_iteration += 1
                else:
                    excellent(player)
            else:
                score_for_loop_broken = False
                found_score = None
                excellent_iteration = 0

        for poop in poops:
            if pygame.sprite.spritecollideany(poop, bullets):
                for bullet in bullets:
                    if bullet.rect.colliderect(poop.rect):
                        bullet.kill()
                if use_joystick:
                    joysticks[0].rumble(0, 0.3, 200)
                poop.explode()
                score += 20
                dead_poops.add(poop)
                all_sprites.add(poop)
            if poop.dead:
                poop.remove(poops)
        for poop in dead_poops:
            if poop.dead_iter > 10:
                poop.kill()

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(player, poops):
            player.die()
            if use_joystick:
                joysticks[0].rumble(0, 1, 500)
            # Stop the music
            pygame.mixer.music.stop()
            # Enter the crash screen
            if use_joystick:
                crash_info = crash(SCREEN, score, joysticks[0])
            else:
                crash_info = crash(SCREEN, score)

            if crash_info == "game_loop":
                game_loop(character=character)
            elif crash_info == "main_menu":
                if use_joystick:
                    main_menu_info = main_menu(SCREEN, joysticks[0])
                else:
                    main_menu_info = main_menu(SCREEN)
                if main_menu_info == "character_select":
                    if use_joystick:
                        character_select_info2 = character_select(SCREEN, joysticks[0])
                    else:
                        character_select_info2 = character_select(SCREEN)
                    # Check which character the user picked. Then start the game accordingly.
                    if character_select_info2 == "Hiroki":
                        game_loop()
                    elif character_select_info2 == "Edward":
                        game_loop(character="Edward")
                    else:
                        game_loop()
            # Stop the loop
            break

        # Flip everything to the display
        pygame.display.flip()

        # Limit frame rate to 30 frames per second
        clock.tick(30)

    # At this point, we're done, so we can stop and quit the mixer
    pygame.mixer.music.stop()
    pygame.mixer.quit()


if __name__ == '__main__':
    if use_joystick:
        menu_info = main_menu(SCREEN, joysticks[0])
    else:
        menu_info = main_menu(SCREEN)
    if menu_info == "character_select":
        # Get a character from the user to play with
        if use_joystick:
            character_select_info = character_select(SCREEN, joysticks[0])
        else:
            character_select_info = character_select(SCREEN)
        # Check which character the user picked. Then start the game accordingly.
        if character_select_info == "Hiroki":
            game_loop()
        elif character_select_info == "Edward":
            game_loop(character="Edward")
    # game_loop()
