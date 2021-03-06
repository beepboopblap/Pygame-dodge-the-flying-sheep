from pickletools import pyfloat
import pygame, random
from pygame.locals import *
from pygame import mixer
import math

SCREEN_HEIGHT = 900
SCREEN_WIDTH = 690

pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# declare colours, images, sounds, fonts
x = 690
y = 900
player_x = 240
player_y = 680
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (165, 42, 42)
pink = (247, 49, 188)
Calibri60 = pygame.font.SysFont("Calibri", 60)
Calibri40 = pygame.font.SysFont("Calibri", 40)
pixel40 = pygame.font.SysFont("ARCADECLASSIC.TTF", 40)
player_sprite = pygame.image.load("player_sprite.png").convert_alpha()
sheep_sprite = pygame.image.load("sheep_sprite (1).png").convert_alpha()
heart_sprite = pygame.image.load("heart_sprite_new.png").convert_alpha()
sheep_speed = -5
sheep_x = 104
sheep_x1 = 40
sheep_x2 = 13
sheep_x3 = 79
heart_x = 29
sheep_y = -17
sheep_y1 = -10
sheep_y2 = -4
sheep_y3 = -7
heart_y = -5

start_text = Calibri60.render("Press a key to begin!", 1, red)
lives = 3
collision_sfx = mixer.Sound("spacebar_soundfx.mp3")
hurt_sfx = mixer.Sound("hurt_sfx (mp3cut.net).mp3")
healing_sfx = mixer.Sound("healing_sfx.mp3")
game_over_text = Calibri60.render("Game Over", 1, red)


start = True
running = True
game_easy = False
game_normal = False
game_hard = False
game_impossible = False
quit = False
gameover = False
hearts = False
player_x = 240
player_y = 680
pause = False

# transformations

heart_sprite = pygame.transform.scale(heart_sprite, (140, 140))
player_sprite = pygame.transform.scale(player_sprite, (140, 140))
sheep_sprite = pygame.transform.scale(sheep_sprite, (140, 140))
sheep_sprite1 = pygame.transform.scale(sheep_sprite, (140, 140))
sheep_sprite2 = pygame.transform.scale(sheep_sprite, (140, 140))
sheep_sprite3 = pygame.transform.scale(sheep_sprite, (140, 140))
sheep_sprite4 = pygame.transform.scale(sheep_sprite, (140, 140))

all_sprites = [
    player_sprite,
    sheep_sprite,
    sheep_sprite1,
    sheep_sprite2,
    sheep_sprite3,
    sheep_sprite4,
    heart_sprite,
]
# variables for keeping track of my game players etc.

# collision code
def isCollision(sheep_x, sheep_y, player_x, player_y):
    distance = math.sqrt(
        (math.pow(player_x - sheep_x, 2)) + (math.pow(player_y - sheep_y, 2))
    )
    if distance < 114:
        return True
    else:
        return False


def isCollision(sheep_x1, sheep_y1, player_x1, player_y1):
    distance = math.sqrt(
        (math.pow(player_x1 - sheep_x1, 2)) + (math.pow(player_y1 - sheep_y1, 2))
    )
    if distance < 114:
        return True
    else:
        return False

def isCollision(sheep_x2, sheep_y2, player_x2, player_y2):
    distance = math.sqrt(
        (math.pow(player_x2 - sheep_x2, 2)) + (math.pow(player_y2 - sheep_y2, 2))
    )
    if distance < 114:
        return True
    else:
        return False

def isCollision(sheep_x3, sheep_y3, player_x3, player_y3):
    distance = math.sqrt(
        (math.pow(player_x3 - sheep_x3, 2)) + (math.pow(player_y3 - sheep_y3, 2))
    )
    if distance < 114:
        return True
    else:
        return False

point = 0
start = True
game_over = False
score = 0
levels = False


# main game loop
while running:

    if start == True:
        window.fill(yellow)

        if point == 0:
            start_text = Calibri60.render("Start", 1, red)
            exit_text = Calibri40.render("Exit", 1, black)
            main_menu = Calibri60.render("Main Menu", 1, blue)
            credits_text = Calibri40.render("Made by", 1, black)
            credits_name = Calibri60.render("beepboopblap", 1, red)
            window.blit(credits_text, (140, 730))
            window.blit(credits_name, (140, 780))
            window.blit(player_sprite, (80, 200))
            window.blit(start_text, (270, 400))
            window.blit(exit_text, (270, 490))
            window.blit(main_menu, (170, 100))
            window.blit(sheep_sprite, (450, 200))

        elif point == 1:
            start_text = Calibri40.render("Start", 1, black)
            exit_text = Calibri60.render("Exit", 1, red)
            window.blit(start_text, (270, 400))
            window.blit(exit_text, (270, 490))
            window.blit(main_menu, (170, 100))
            window.blit(player_sprite, (80, 200))
            credits_text = Calibri40.render("Made by", 1, black)
            credits_name = Calibri60.render("beepboopblap", 1, red)
            window.blit(credits_text, (140, 730))
            window.blit(credits_name, (140, 780))
            window.blit(sheep_sprite, (450, 200))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYUP:
                if event.key == K_DOWN:
                    point += 1
                    collision_sfx.play()
                elif event.key == K_UP:
                    point -= 1
                    collision_sfx.play()
                elif event.key == K_RETURN:
                    if point == 0:
                        collision_sfx.play()
                        start = False
                        levels = True

                    elif point == 1:
                        pygame.quit()

        point = point % 2
        pygame.display.update()

    elif levels == True:
        point = 0
        while levels == True:
            window.fill(yellow)

            if point == 0:
                game_easy_text = Calibri60.render("Easy", 1, green)
                game_normal_text = Calibri40.render("Normal", 1, black)
                game_hard_text = Calibri40.render("Hard", 1, black)
                game_impossible_text = Calibri40.render("Insane", 1, black)
                difficulty_label = Calibri60.render("Select Difficulty", 1, blue)
                game_random_text = Calibri40.render("??Random??", 1, black)

                window.blit(game_easy_text, (270, 300))
                window.blit(game_normal_text, (270, 370))
                window.blit(game_hard_text, (270, 440))
                window.blit(game_impossible_text, (270, 510))
                window.blit(difficulty_label, (130, 100))
                window.blit(game_random_text, (270, 580))
            elif point == 1:
                game_easy_text = Calibri40.render("Easy", 1, black)
                game_normal_text = Calibri60.render("Normal", 1, blue)
                game_hard_text = Calibri40.render("Hard", 1, black)
                game_impossible_text = Calibri40.render("Insane", 1, black)
                difficulty_label = Calibri60.render("Select Difficulty", 1, blue)
                game_random_text = Calibri40.render("??Random??", 1, black)

                window.blit(game_easy_text, (270, 300))
                window.blit(game_normal_text, (270, 370))
                window.blit(game_hard_text, (270, 440))
                window.blit(game_impossible_text, (270, 510))
                window.blit(difficulty_label, (130, 100))
                window.blit(game_random_text, (270, 580))

            elif point == 2:
                game_easy_text = Calibri40.render("Easy", 1, black)
                game_normal_text = Calibri40.render("Normal", 1, black)
                game_hard_text = Calibri60.render("Hard", 1, red)
                game_impossible_text = Calibri40.render("Insane", 1, black)
                difficulty_label = Calibri60.render("Select Difficulty", 1, blue)
                game_random_text = Calibri40.render("??Random??", 1, black)

                window.blit(game_easy_text, (270, 300))
                window.blit(game_normal_text, (270, 370))
                window.blit(game_hard_text, (270, 440))
                window.blit(game_impossible_text, (270, 510))
                window.blit(difficulty_label, (130, 100))
                window.blit(game_random_text, (270, 580))

            elif point == 3:
                game_easy_text = Calibri40.render("Easy", 1, black)
                game_normal_text = Calibri40.render("Normal", 1, black)
                game_hard_text = Calibri40.render("Hard", 1, black)
                game_impossible_text = Calibri60.render("Insane", 1, brown)
                difficulty_label = Calibri60.render("Select Difficulty", 1, blue)
                game_random_text = Calibri40.render("??Random??", 1, black)

                window.blit(game_easy_text, (270, 300))
                window.blit(game_normal_text, (270, 370))
                window.blit(game_hard_text, (270, 440))
                window.blit(game_impossible_text, (270, 510))
                window.blit(difficulty_label, (130, 100))
                window.blit(game_random_text, (270, 580))

            elif point == 4:

                game_easy_text = Calibri40.render("Easy", 1, black)
                game_normal_text = Calibri40.render("Normal", 1, black)
                game_hard_text = Calibri40.render("Hard", 1, black)
                game_impossible_text = Calibri40.render("Insane", 1, black)
                difficulty_label = Calibri60.render("Select Difficulty", 1, blue)
                game_random_text = Calibri60.render("??Random??", 1, pink)

                window.blit(game_easy_text, (270, 300))
                window.blit(game_normal_text, (270, 370))
                window.blit(game_hard_text, (270, 440))
                window.blit(game_impossible_text, (270, 510))
                window.blit(difficulty_label, (130, 100))
                window.blit(game_random_text, (270, 580))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == KEYUP:
                    if event.key == K_DOWN:
                        point += 1
                        collision_sfx.play()
                    elif event.key == K_UP:
                        point -= 1
                        collision_sfx.play()
                    elif event.key == K_RETURN:
                        if point == 0:
                            collision_sfx.play()
                            levels = False
                            game_easy = True
                        elif point == 1:
                            levels = False
                            game_normal = True
                            collision_sfx.play()
                        elif point == 2:
                            levels = False
                            game_hard = True
                        elif point == 3:
                            levels = False
                            game_impossible = True
                        elif point == 4:
                            random_difficulty_chooser = random.randint(1, 4)
                            print(random_difficulty_chooser)
                            if random_difficulty_chooser == 1:
                                levels = False
                                game_easy = True
                            elif random_difficulty_chooser == 2:
                                levels = False
                                game_normal = True
                            elif random_difficulty_chooser == 3:
                                levels = False
                                game_hard = True
                            elif random_difficulty_chooser == 4:
                                levels = False
                                game_impossible = True

            point = point % 5
            pygame.display.update()

    elif game_over == True:

        window.fill(yellow)
        window.blit(game_over_text, (190, 400))
        score_text = Calibri40.render("Score:" + str(score), 1, red)
        window.blit(score_text, (280, 180))
        main_menu_label = Calibri40.render("Press 'm' For Main Menu", 1, blue)

        for event in pygame.event.get():
            if event.type == QUIT:

                pygame.quit()

        pygame.display.update()

    elif game_easy == True:

        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == ord("w"):
                    player_y = player_y - 40
                if event.key == ord("s"):
                    player_y = player_y + 40
                if event.key == ord("a"):
                    player_x = player_x - 40
                if event.key == ord("d"):
                    player_x = player_x + 40
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()

        # perform calculations

        # code for borders
        if player_x >= 599:
            player_x = 599
        if player_x <= -35:
            player_x = -35
        if player_y >= 760:
            player_y = 760
        if player_y <= 0:
            player_y = 0

        # draw graphics
        window.fill(yellow)

        window.blit(player_sprite, (player_x, player_y))
        pygame.draw.rect(window, black, (3, 3, 683, 890), 4)
        watch_out_label = Calibri40.render("Watch out for flying sheep!", 1, blue)
        controls = Calibri40.render("Use WASD to move", 1, blue)
        window.blit(controls, (150, 300))
        window.blit(watch_out_label, (70, 200))
        lives_counter = Calibri40.render("Lives left:" + str(lives), 1, red)
        window.blit(lives_counter, (10, 60))
        score_text = Calibri40.render("Score:" + str(score), 1, red)
        window.blit(score_text, (10, 140))
        difficulty_text = Calibri40.render("Difficulty: Easy", 1, green)
        window.blit(difficulty_text, (300, 50))

        if lives <= 0:
            game = False
            game_over = True

        # sheep falling from the sky code

        if sheep_y < y:

            window.blit(sheep_sprite, (sheep_x, sheep_y))
            sheep_y = sheep_y + 15
            if sheep_y > 830:
                sheep_x = random.randrange(0, x)
                sheep_y = 0
                score = score + 1

            # Collision for sheep
            collision = isCollision(sheep_x, sheep_y, player_x, player_y)

            if collision:
                sheep_y = 0
                sheep_x = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()

        if sheep_y1 < y:

            window.blit(sheep_sprite1, (sheep_x1, sheep_y1))
            sheep_y1 = sheep_y1 + 25
            if sheep_y1 > 830:
                sheep_x1 = random.randrange(0, 100)
                sheep_y1 = 0
                score = score + 1

            collision = isCollision(sheep_x1, sheep_y1, player_x, player_y)

            if collision:
                sheep_y1 = 0
                sheep_x1 = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()

        if sheep_y2 < y:

            window.blit(sheep_sprite2, (sheep_x2, sheep_y2))
            sheep_y2 = sheep_y2 + random.randint(20, 45)
            if sheep_y2 > 830:
                sheep_x2 = random.randrange(0, SCREEN_WIDTH)
                sheep_y2 = 0
                score = score + 1

            collision = isCollision(sheep_x2, sheep_y2, player_x, player_y)

            if collision:
                sheep_y2 = 0
                sheep_x2 = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()

        if score == 35:
            hearts = True
        elif score == 70:
            hearts = True
        elif score == 105:
            hearts = True
        elif score == 140:
            hearts = True
        elif score == 175:
            hearts = True

        elif hearts == True:
            window.blit(heart_sprite, (heart_x, heart_y))
            heart_y = heart_y + 10
            if heart_y > 830:
                heart_x = random.randrange(0, SCREEN_WIDTH)
                heart_y = 0

            collision = isCollision(heart_x, heart_y, player_x, player_y)

            if collision:
                heart_y = 0
                heart_x = 0
                lives = lives + 1
                healing_sfx.play()

                hearts = False

    elif game_normal == True:

        # process events
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == ord("w"):
                    player_y = player_y - 40
                if event.key == ord("s"):
                    player_y = player_y + 40
                if event.key == ord("a"):
                    player_x = player_x - 40
                if event.key == ord("d"):
                    player_x = player_x + 40
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()

        # perform calculations

        # code for borders
        if player_x >= 599:
            player_x = 599
        if player_x <= -35:
            player_x = -35
        if player_y >= 760:
            player_y = 760
        if player_y <= 0:
            player_y = 0

        # draw graphics
        window.fill(yellow)

        window.blit(player_sprite, (player_x, player_y))
        pygame.draw.rect(window, black, (3, 3, 683, 890), 4)
        watch_out_label = Calibri40.render("Watch out for flying sheep!", 1, blue)
        controls = Calibri40.render("Use WASD to move", 1, blue)
        window.blit(controls, (150, 300))
        window.blit(watch_out_label, (70, 200))
        lives_counter = Calibri40.render("Lives left:" + str(lives), 1, red)
        window.blit(lives_counter, (10, 60))
        score_text = Calibri40.render("Score:" + str(score), 1, red)
        window.blit(score_text, (10, 140))
        difficulty_text = Calibri40.render("Difficulty: Normal", 1, blue)
        window.blit(difficulty_text, (285, 50))

        if lives <= 0:
            game = False
            game_over = True

        # sheep falling from the sky code

        if sheep_y < y:

            window.blit(sheep_sprite, (sheep_x, sheep_y))
            sheep_y = sheep_y + 20
            if sheep_y > 830:
                sheep_x = random.randrange(0, x)
                sheep_y = 0
                score = score + 1

            # Collision for sheep
            collision = isCollision(sheep_x, sheep_y, player_x, player_y)

            if collision:
                sheep_y = 0
                sheep_x = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()

        if sheep_y1 < y:

            window.blit(sheep_sprite1, (sheep_x1, sheep_y1))
            sheep_y1 = sheep_y1 + 30
            if sheep_y1 > 830:
                sheep_x1 = random.randrange(0, 100)
                sheep_y1 = 0
                score = score + 1

            collision = isCollision(sheep_x1, sheep_y1, player_x, player_y)

            if collision:
                sheep_y1 = 0
                sheep_x1 = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()

        if sheep_y2 < y:

            window.blit(sheep_sprite2, (sheep_x2, sheep_y2))
            sheep_y2 = sheep_y2 + random.randint(20, 60)
            if sheep_y2 > 830:
                sheep_x2 = random.randrange(0, SCREEN_WIDTH)
                sheep_y2 = 0
                score = score + 1

            collision = isCollision(sheep_x2, sheep_y2, player_x, player_y)

            if collision:
                sheep_y2 = 0
                sheep_x2 = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()

        if score == 50:
            hearts = True
        elif score == 100:
            hearts = True
        elif score == 150:
            hearts = True
        elif score == 200:
            hearts = True
        elif score == 250:
            hearts = True
        elif score == 300:
            hearts = True

        elif hearts == True:
            window.blit(heart_sprite, (heart_x, heart_y))
            heart_y = heart_y + 10
            if heart_y > 830:
                heart_x = random.randrange(0, SCREEN_WIDTH)
                heart_y = 0

            collision = isCollision(heart_x, heart_y, player_x, player_y)

            if collision:
                heart_y = 0
                heart_x = 0
                lives = lives + 1
                healing_sfx.play()

                hearts = False

    elif game_hard == True:

        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == ord("w"):
                    player_y = player_y - 40
                if event.key == ord("s"):
                    player_y = player_y + 40
                if event.key == ord("a"):
                    player_x = player_x - 40
                if event.key == ord("d"):
                    player_x = player_x + 40
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                elif event.key == K_SPACE:
                    pause = True
                    if pause == True:
                        pause_label = Calibri40.render("Paused", 1, black)
                        press_space = Calibri40.render("Press Space To Continue", 1, red)
                        pygame.time.delay(30000000000)
                        window.blit(pause_label, (290,650))
                        window.blit(press_space, (290, 750))
                        if event.key == K_SPACE:
                            pause = False
                    elif pause == False:
                        pygame.time.delay(0)
                       

        # perform calculations

        # code for borders
        if player_x >= 599:
            player_x = 599
        if player_x <= -35:
            player_x = -35
        if player_y >= 760:
            player_y = 760
        if player_y <= 0:
            player_y = 0

        # draw graphics
        window.fill(yellow)

        window.blit(player_sprite, (player_x, player_y))
        pygame.draw.rect(window, black, (3, 3, 683, 890), 4)
        watch_out_label = Calibri40.render("Watch out for flying sheep!", 1, blue)
        controls = Calibri40.render("Use WASD to move", 1, blue)
        window.blit(controls, (150, 300))
        window.blit(watch_out_label, (70, 200))
        lives_counter = Calibri40.render("Lives left:" + str(lives), 1, red)
        window.blit(lives_counter, (10, 60))
        score_text = Calibri40.render("Score:" + str(score), 1, red)
        window.blit(score_text, (10, 140))
        difficulty_text = Calibri40.render("Difficulty: Hard", 1, red)
        window.blit(difficulty_text, (300, 50))

        if lives <= 0:
            game = False
            game_over = True

        # sheep falling from the sky code

        if sheep_y < y:

            window.blit(sheep_sprite, (sheep_x, sheep_y))
            sheep_y = sheep_y + 25
            if sheep_y > 830:
                sheep_x = random.randrange(0, x)
                sheep_y = 0
                score = score + 1

            # Collision for sheep
            collision = isCollision(sheep_x, sheep_y, player_x, player_y)

            if collision:
                sheep_y = 0
                sheep_x = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()

        if sheep_y1 < y:

            window.blit(sheep_sprite1, (sheep_x1, sheep_y1))
            sheep_y1 = sheep_y1 + 30
            if sheep_y1 > 830:
                sheep_x1 = random.randrange(0, 100)
                sheep_y1 = 0
                score = score + 1

            collision = isCollision(sheep_x1, sheep_y1, player_x, player_y)

            if collision:
                sheep_y1 = 0
                sheep_x1 = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()

        if sheep_y2 < y:

            window.blit(sheep_sprite2, (sheep_x2, sheep_y2))
            sheep_y2 = sheep_y2 + random.randint(20, 60)
            if sheep_y2 > 830:
                sheep_x2 = random.randrange(0, SCREEN_WIDTH)
                sheep_y2 = 0
                score = score + 1

            collision = isCollision(sheep_x2, sheep_y2, player_x, player_y)

            if collision:
                sheep_y2 = 0
                sheep_x2 = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()

        if sheep_y3 < y:

            window.blit(sheep_sprite3, (sheep_x3, sheep_y3))
            sheep_y3 = sheep_y3 + random.randint(20, 60)
            if sheep_y3 > 830:
                sheep_x3 = random.randrange(0, SCREEN_WIDTH)
                sheep_y3 = 0
                score = score + 1

            collision = isCollision(sheep_x3, sheep_y3, player_x, player_y)

            if collision:
                sheep_y3 = 0
                sheep_x3 = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()

        if score == 100:
            hearts = True
        elif score == 200:
            hearts = True
        elif score == 300:
            hearts = True
        elif score == 400:
            hearts = True
        elif score == 500:
            hearts = True

        elif hearts == True:
            window.blit(heart_sprite, (heart_x, heart_y))
            heart_y = heart_y + 10
            if heart_y > 830:
                heart_x = random.randrange(0, SCREEN_WIDTH)
                heart_y = 0

            collision = isCollision(heart_x, heart_y, player_x, player_y)

            if collision:
                heart_y = 0
                heart_x = 0
                lives = lives + 1
                healing_sfx.play()

                hearts = False

    elif game_impossible == True:

        mode_text = Calibri60.render("Mode: Impossible", 1, brown)
        window.blit(mode_text, (0, 0))

        lives = 1

        for event in pygame.event.get():

            print(event)

            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == ord("w"):
                    player_y = player_y - 40
                if event.key == ord("s"):
                    player_y = player_y + 40
                if event.key == ord("a"):
                    player_x = player_x - 40
                if event.key == ord("d"):
                    player_x = player_x + 40
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()

        # perform calculations

        # code for borders
        if player_x >= 599:
            player_x = 599
        if player_x <= -35:
            player_x = -35
        if player_y >= 760:
            player_y = 760
        if player_y <= 0:
            player_y = 0

        # draw graphics
        window.fill(yellow)

        window.blit(player_sprite, (player_x, player_y))
        pygame.draw.rect(window, black, (3, 3, 683, 890), 4)
        watch_out_label = Calibri40.render("Watch out for flying sheep!", 1, blue)
        controls = Calibri40.render("Use WASD to move", 1, blue)
        window.blit(controls, (150, 300))
        window.blit(watch_out_label, (70, 200))
        lives_counter = Calibri40.render("Lives left:" + str(lives), 1, red)
        window.blit(lives_counter, (10, 60))
        score_text = Calibri40.render("Score:" + str(score), 1, red)
        window.blit(score_text, (10, 140))
        difficulty_text = Calibri40.render("Difficulty: Insane", 1, brown)
        window.blit(difficulty_text, (280, 50))

        # sheep falling from the sky code

        if sheep_y < y:

            window.blit(sheep_sprite, (sheep_x, sheep_y))
            sheep_y = sheep_y + 31
            if sheep_y > 830:
                sheep_x = random.randrange(0, x)
                sheep_y = 0
                score = score + 1

            # Collision for sheep
            collision = isCollision(sheep_x, sheep_y, player_x, player_y)

            if collision:
                sheep_y = 0
                sheep_x = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()
                game_over = True
                game_impossible = False

        if sheep_y1 < y:

            window.blit(sheep_sprite1, (sheep_x1, sheep_y1))
            sheep_y1 = sheep_y1 + 47
            if sheep_y1 > 830:
                sheep_x1 = random.randrange(0, 100)
                sheep_y1 = 0
                score = score + 1

            collision = isCollision(sheep_x1, sheep_y1, player_x, player_y)

            if collision:
                sheep_y1 = 0
                sheep_x1 = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()
                game_over = True
                game_impossible = False

        if sheep_y2 < y:

            window.blit(sheep_sprite2, (sheep_x2, sheep_y2))
            sheep_y2 = sheep_y2 + random.randint(30, 50)
            if sheep_y2 > 830:
                sheep_x2 = random.randrange(0, SCREEN_WIDTH)
                sheep_y2 = 0
                score = score + 1

            collision = isCollision(sheep_x2, sheep_y2, player_x, player_y)

            if collision:
                sheep_y2 = 0
                sheep_x2 = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()
                game_over = True
                game_impossible = False

        if sheep_y3 < y:

            window.blit(sheep_sprite3, (sheep_x3, sheep_y3))
            sheep_y3 = sheep_y3 + random.randint(30, 65)
            if sheep_y3 > 830:
                sheep_x3 = random.randrange(0, SCREEN_WIDTH)
                sheep_y3 = 0
                score = score + 1

            collision = isCollision(sheep_x3, sheep_y3, player_x, player_y)

            if collision:
                sheep_y3 = 0
                sheep_x3 = random.randrange(0, x)
                lives = lives - 1
                collision_sfx.play()
                hurt_sfx.play()
                game_over = True
                game_impossible = False

    # update
    pygame.display.update()
    fps.tick(11)


# loop over, game over
pygame.quit()
