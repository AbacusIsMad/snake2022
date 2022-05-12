# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:22:20 2018 

@author: zou
"""
import pygame
import time
import threading
import sys
import os
import math
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE
from pygame.locals import QUIT
from snake import Snake

'''
def base_path(path):
    try:
        basedir = sys._MEIPASS
    except Exception:
        basedir = os.path.abspath(".")
    print(os.path.join(basedir, path))
    return os.path.join(basedir, path)
'''

if __name__ == "__main__":
    #get locally stored config file
    invalid_loc = False
    real_path = os.path.join(os.path.abspath('.'), 'snakeData')
    package_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snakeData')
    print("real path:", real_path)
    print("unpackaged path:", package_path)
    if real_path == package_path:
        print("inside a python script. No need to do anything more.")
    else:
        print("we are inside the executable.")
    if not os.path.exists(real_path):
        try:
            os.makedirs(real_path)
        except Exception:
            print("failed to make directory or file! Returning to normal dir.")
            real_path = package_path
            invalid_loc = True


    '''
    if getattr(sys, 'frozen', None):
        print("frozen executable!")
        game_data = os.path.join(os.path.dirname(sys.executable), 'snakeData')
    else:
        print("normal")
        game_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snakeData')
    print("current directory:", game_data)
    

    #check for permissions, or else resort to internal directory.
    print("coming here now")
    if not os.path.exists(game_data):
        try:
            os.makedirs(game_data)
        except Exception:
            print("failed to make directory or file! Returning to normal dir.")
            #game_data = './snakeData'
            game_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snakeData')
            #invalid_loc = True
    elif not os.access(game_data, os.W_OK):
        print("directory is not writable! Returning to normal dir.")
        #game_data = './snakeData'
        game_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snakeData')
        #invalid_loc = True
    print('storage directory:', game_data)

    #os.chdir(base_path(''))
    '''

    #create the files if they don't exist.
    if not os.path.exists(real_path + '/style.txt'):
        with open(real_path + '/style.txt', 'w') as f:
            f.write('0')
            print("style written")
    if not os.path.exists(real_path + '/playerData.txt'):
        with open(real_path + '/playerData.txt', 'w') as f:
            f.write('')
            print("playerData written")

    #change to _MEIxxxx if needed, to get src
    #os.chdir(base_path(''))
    


from game import Game

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

green = pygame.Color(0, 200, 0)
bright_green = pygame.Color(0, 255, 0)
red = pygame.Color(200, 0, 0)
bright_red = pygame.Color(255, 0, 0)
blue = pygame.Color(32, 178, 170)
bright_blue = pygame.Color(32, 200, 200)
yellow = pygame.Color(255, 205, 0)
bright_yellow = pygame.Color(255, 255, 0)

'''The Strat:
Load default from folder
Load into temp location
copy level to playing zone
pass any pass-death features to intermediate
when level quit, unload on both levels
ALWAYS PICKLE IT!
'''

game = Game(os.path.dirname(package_path), os.path.dirname(real_path))
rect_len = game.settings.rect_len
snake = game.snake
pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((game.settings.width * game.settings.rect_len, game.settings.height * game.settings.rect_len))
pygame.display.set_caption('Gluttonous')

#osx problem?
#pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
crash_sound = pygame.mixer.Sound(os.path.dirname(package_path) + '/sound/crash.wav')

def yes():
    return True

def text_objects(text, font, color=black):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_display(text, x, y, color=black, size=50):
    large_text = pygame.font.Font(os.path.dirname(package_path) + '/arial.ttf', size)
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = (x, y)
    screen.blit(text_surf, text_rect)
    pygame.display.update()

def button(msg, x, y, w, h, inactive_color, active_color, action=None, parameter=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            if parameter != None:
                return action(parameter)
            else:
                return action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))

    #placeholder
    pressed = 0
    smallText = pygame.font.Font(os.path.dirname(package_path) + '/arial.ttf', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = (x + (w / 2), y + (h / 2))
    screen.blit(TextSurf, TextRect)
    return pressed

def quitgame():
    pygame.quit()
    #quit()
    sys.exit()


def crash():
    pygame.mixer.Sound.play(crash_sound)
    message_display('crashed', game.settings.width / 2 * 15, game.settings.height / 3 * 15, white)
    time.sleep(1)


def initial_interface(invalid, directory):
    intro = True
    restart = False

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(white)
        message_display('Gluttonous', game.settings.width / 2 * 15, game.settings.height / 4 * 15)
        if invalid_loc:
            message_display('Error', game.settings.width / 4 * 15, game.settings.height / 2 * 15)

        button('Go!', 80, 240, 80, 40, green, bright_green, level_select)

        if not invalid:
            button('Settings', 175, 240, 80, 40, yellow, bright_yellow, settings, directory)
        else:
            button('Nope lol', 175, 240, 80, 40, yellow, bright_yellow, yes)

        button('Quit', 270, 240, 80, 40, red, bright_red, quitgame)

        pygame.display.update()
        pygame.time.Clock().tick(15)

def settings(directory):
    with open(directory + "/style.txt", 'r') as f:
        style = f.read()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(black)

        if button('Home', 100, 200, 80, 40, red, bright_red, yes):
            break

        if style == '0':
            button('retro', 20, 20, 40, 40, green, green, yes)
        elif button('retro', 20, 20, 40, 40, yellow, bright_yellow, yes):
            with open(directory + "/style.txt", 'w') as f:
                f.write('0')
                style = '0'

        if style == 'cringe':
            button('goofy', 80, 20, 40, 40, green, green, yes)
        elif button('goofy', 80, 20, 40, 40, yellow, bright_yellow, yes):
            with open(directory + "/style.txt", "w") as f:
                f.write('cringe')
                style = 'cringe'


        button('Instructions', 155, 300, 120, 40, blue, bright_blue, display_instructions)

        pygame.display.update()
        pygame.time.Clock().tick(15)


def level_select():
    intro = True
    restart = [0, ""]
    while intro:
        if restart[0]:
            break
        if restart[1]:
            restart = game_loop(restart[1])
            continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(black)
        message_display('Select Level', game.settings.width / 2 * 15, game.settings.height / 4 * 15, color=white)

        if button('Home', 100, 200, 80, 40, red, bright_red, yes):
            return 0

        temp = button('1-1', 20, 20, 40, 40, green, bright_green, game_loop, "1-1")
        if isinstance(temp, list):
            restart = temp
        temp = button('1-2', 80, 20, 40, 40, green, bright_green, game_loop, "1-2")
        if isinstance(temp, list):
            restart = temp
        temp = button('1-3', 140, 20, 40, 40, green, bright_green, game_loop, "1-3")
        if isinstance(temp, list):
            restart = temp
        temp = button('1-4', 200, 20, 40, 40, green, bright_green, game_loop, "1-4")
        if isinstance(temp, list):
            restart = temp
        if restart[0]:
            break
        pygame.display.update()
        pygame.time.Clock().tick(15)

def display_instructions():
    #  this instruction page explains how to move the snake
    intro = True
    restart = [0, ""]

    # The page will display until the button is pressed or quit 
    while intro:
        if restart[0]:
            break
        if restart[1]:
            restart = game_loop(restart[1])
            continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(black)

        #  Text is displayed on the screen
        message_display("How to Play Gluttonous!", 200, 50, color=white, size=30)

        # Buttons to go back to the home screen or to the next page
        home = button('Home', 100, 350, 80, 40, red, bright_red, yes)
        nextbutton = button('Next', 250, 350, 80, 40, red, bright_red, yes)

        # A .bmp of arrow keys as well as a 'sample' snake is blitted to screen 
        arrows = pygame.image.load("images/arrowkeys.bmp")
        arrows = pygame.transform.scale(arrows, (140, 140))            
        screen.blit(arrows, (110, 88))
        screen.blit(pygame.image.load("styles/0/images/head_up1.bmp"), (280, 125))
        screen.blit(pygame.image.load("styles/0/images/body_s.bmp"), (280, 140))
        screen.blit(pygame.image.load("styles/0/images/body_s.bmp"), (280, 155))            
        screen.blit(pygame.image.load("styles/0/images/body_s.bmp"), (280, 170))
        screen.blit(pygame.image.load("styles/0/images/tail_up.bmp"), (280, 185))
        message_display("Use the arrow keys to move the snake", 200, 90, color=white, size=20)   

        message_display("Eat the food to grow the snake", 200, 220, color=white, size=20)

        # blit the food onto the screen to show users 
        for i in range(1, 9):
            food = pygame.image.load("styles/0/images/food" + str(i) + ".bmp")
            food = pygame.transform.scale(food, (30, 30))
            if i in range(1, 5): 
                screen.blit(food, (150+(i-1)*31, 250))
            else: 
                screen.blit(food, (150+(i-5)*31, 281))
        
        if home: 
            return 0
        if nextbutton: 
            instructions_pagetwo()
        if restart[0]:
            break
        pygame.display.update()
        pygame.time.Clock().tick(15)

def instructions_pagetwo(): 
    #  this instructions page explains how the food items work with growing the snake
    intro = True
    restart = [0, ""]
    while intro:
        if restart[0]:
            break
        if restart[1]:
            restart = game_loop(restart[1])
            continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(black)

        #  instructions set telling players not to crash into the walls, with a demonstration
        message_display("Don't crash into the walls!", 200, 40, color=white, size=20)

        screen.blit(pygame.image.load("styles/0/images/tile.bmp"), (200, 60))
        snakehead = pygame.transform.rotate(pygame.image.load("styles/0/images/head_up1.bmp"), 270)
        snakebody = pygame.transform.rotate(pygame.image.load('styles/0/images/body_s.bmp'), 270)
        snaketail = pygame.transform.rotate(pygame.image.load('styles/0/images/tail_up.bmp'), 270)
        screen.blit(snakehead,(185,60))
        screen.blit(snakebody, (170, 60))
        screen.blit(snakebody, (155, 60))
        screen.blit(snaketail, (140, 60))

        cross = pygame.transform.scale(pygame.image.load("images/cross.bmp"), (40, 40))
        screen.blit(cross, (240, 40))

        #  Instructions set telling players not to crash into themselves, with a demonstration
        message_display("Don't crash into yourself!", 200, 100, color=white, size=20)

        screen.blit(snaketail, (140, 120))
        screen.blit(snakebody, (155, 120))
        screen.blit(snakebody, (170, 120))
        screen.blit(snakebody, (185, 120))
        screen.blit(pygame.transform.rotate(snakebody, 90), (185, 133))
        screen.blit(pygame.transform.rotate(snakebody, 90), (185, 148))
        screen.blit(pygame.transform.rotate(snakebody, 180), (172, 148))
        screen.blit(pygame.transform.rotate(snakebody, 180), (157, 148))
        screen.blit(pygame.transform.rotate(snakehead, 90), (155, 135))

        screen.blit(cross, (240, 120))
        
        # Instructions demonstrating the wrap walls
        message_display("You teleport through wrap walls", 200, 170, color=white, size=20)

        screen.blit(snaketail, (170, 190))
        screen.blit(snakebody, (185, 190))
        screen.blit(pygame.image.load("styles/0/images/tile.bmp"), (200, 190))
        screen.blit(pygame.transform.rotate(pygame.image.load("styles/0/images/wrap.bmp"), 180), (200, 190))

        screen.blit(pygame.image.load("styles/0/images/tile.bmp"), (240, 190))
        screen.blit(pygame.image.load("styles/0/images/wrap.bmp"), (240, 190))
        screen.blit(snakebody, (255, 190))
        screen.blit(snakehead, (270, 190))

        #  Instructions for padded walls
        message_display("You can survive impact with padded walls", 200, 230, color=white, size=20)
        screen.blit(pygame.image.load("styles/0/images/tile.bmp"), (200, 240))
        screen.blit(pygame.image.load("styles/0/images/pad.bmp"), (200,240))

        message_display("Once the snake is big enough, activate the pressure plates to win the level", 200, 300, color=white, size=10)

        back = button('Back', 150, 350, 80, 40, red, bright_red, yes)
       
    
        if back: 
            return 0
        # if nextbutton: 
        #     i
        if restart[0]:
            break
        pygame.display.update()
        pygame.time.Clock().tick(15)

def game_loop(level):
    with open(os.path.join(game.src, "snakeData/style.txt"), 'r') as f:
        game.style = f.read()

    game.restart_game(level)
    screen.fill(black)
    game.blit_map(rect_len, screen)
    
    space_img = game.space_img
    #whether the game is stopped
    stop = False
    #if the snake has crashed or lost
    #cont = 1

    #always blit once before doing stuff, and sleep for a little bit! This allows for some time preparation.
    game.snake.blit(rect_len, screen, 1, 0)
    game.strawberry.blit(screen, int(game.config.settings["xOffset"]), int(game.config.settings["yOffset"]))
    game.blit_features(rect_len, screen)
    game.blit_score(white, screen)
    pygame.display.update()
    pygame.time.delay(1000)
    score_cover = pygame.Rect(0, 0, 400, 80)

    #the phase of the process, split into 5
    phase = 0
    move = game.direction_to_int(snake.facing)
    while True:
        pygame.event.pump()
        move_temp, escape = human_move()
        
        stop = stop ^ escape
        if move_temp >= 0 and not stop:
            move = move_temp

        fps = 5

        restart = [0, ""]
        if stop:
            #build restart screen
            #xOffset, yOffset, width, height
            restart[1] = button('Restart', 270, 20, 80, 40, yellow, bright_yellow, yes) * level
            restart[0] += button('Home', 20, 20, 80, 40, green, bright_green, yes)
            if restart[0] or restart[1]:
                break
            pygame.display.update()
            fpsClock.tick(30)
            continue
        if phase == 0:
            #the first section and basically decides the next 4 frames.
            state, state1, result, result1 = game.do_move(move)
            print(state, state1, result, result1)
            if state < 0 or state1 < 0:
                break

            #blit everything with spaces where the snake is so clones don't affect each other.
            x0 = int(game.config.settings["xOffset"])
            y0 = int(game.config.settings["yOffset"])
            for coord in game.snake.segmentd:
                x_f, y_f = (coord[0] + x0)*rect_len, (coord[1] + y0)*rect_len
                screen.blit(space_img, (x_f, y_f))
                #pygame.display.update(pygame.Rect(x_f, y_f, rect_len, rect_len))
            if game.snake_clone.init:
                for coord in game.snake_clone.segmentd:
                    x_f, y_f = (coord[0] + x0)*rect_len, (coord[1] + y0)*rect_len
                    screen.blit(space_img, (x_f, y_f))
                    #pygame.display.update(pygame.Rect(x_f, y_f, rect_len, rect_len))
            if result:
                x_f, y_f = (result[0] + x0)*rect_len, (result[1] + y0)*rect_len
                screen.blit(space_img, (x_f, y_f))
                #pygame.display.update(pygame.Rect(x_f, y_f, rect_len, rect_len))
            if result1:
                x_f, y_f = (result1[0] + x0)*rect_len, (result1[1] + y0)*rect_len
                screen.blit(space_img, (x_f, y_f))
                #pygame.display.update(pygame.Rect(x_f, y_f, rect_len, rect_len))

            #blit snake
            game.snake.blit(rect_len, screen, state, phase)
            if game.snake_clone.init:
                game.snake_clone.blit(rect_len, screen, state1, phase)
            #blit the features, which always appear on top of the snake
            game.blit_features(rect_len, screen)
            game.strawberry.blit(screen, int(game.config.settings["xOffset"]), int(game.config.settings["yOffset"]))
            #covers up the score and home, restart buttons.
            pygame.draw.rect(screen, black, score_cover)
            game.blit_score(white, screen)
            pygame.display.update(score_cover)

            #update everything around the snake
            for coord in game.snake.segmentd + game.snake_clone.segmentd + [result] + [result1]:
                if coord:
                    x_f, y_f = (coord[0] + x0)*rect_len, (coord[1] + y0)*rect_len
                    pygame.display.update(pygame.Rect(x_f, y_f, rect_len, rect_len))

            #pygame.display.update()
        else:
            game.snake.blit(rect_len, screen, state, phase)
            if game.snake_clone.init:
                game.snake_clone.blit(rect_len, screen, state1, phase)

        phase = (phase + 1) % 5
        pygame.time.delay(math.ceil(1000//(fps*5)))

    if not (restart[0] or restart[1]):
        crash()
        restart[1] = level
    return restart

def options():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            return True
    return False


def human_move():
    # When the user presses 
    direction = 'none'
    escape = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                direction = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                direction = 'left'
            if event.key == K_UP or event.key == ord('w'):
                direction = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                direction = 'down'
            if event.key == K_ESCAPE:
                #pygame.event.post(pygame.event.Event(QUIT))
                escape = True

    move = game.direction_to_int(direction)
    #0 - 3 here
    return move, escape


if __name__ == "__main__":
    #os.chdir(base_path(''))
    initial_interface(invalid_loc, real_path)
