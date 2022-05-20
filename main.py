# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:22:20 2018 bruh are you serious

@author: zou
"""
import pygame
import time
import threading
import sys
import os
import math
import datetime
import json
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE
from pygame.locals import QUIT
from snake import Snake
from instructions import display_instructions
from level import level_maker


if __name__ == "__main__":
    #get locally stored config file
    invalid_loc = False
    print(os.path.abspath(sys.executable))
    if getattr(sys, 'frozen', False):
        print("okay we are in executable probably")
        real_path = os.path.join(os.path.abspath(sys.executable), 'snakeData')
    else:
        print("apparently we are not, but perhaps I'm just stupid")
        real_path = os.path.join(os.path.abspath('.'), 'snakeData')

    #temporary location to test like everything
    #real_path = '/home/ruize/Desktop/snakeData'


    package_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snakeData')
    print("real path:", real_path)
    print("unpackaged path:", package_path)
    if real_path == package_path:
        print("inside a python script. No need to do anything more.")
    else:
        print("we are inside the executable.")


    if not os.path.exists(real_path + '/levels'):
        try:
            os.makedirs(real_path + '/levels')
        except Exception:
            print("failed to make directory or file! Returning to normal dir.")
            real_path = package_path
            invalid_loc = True



    #create the files if they don't exist.
    if not os.path.exists(real_path + '/style.txt'):
        with open(real_path + '/style.txt', 'w') as f:
            f.write('0')
            print("style written")
    if not os.path.exists(real_path + '/playerData.txt'):
        with open(real_path + '/playerData.txt', 'w') as f:
            playerData = [0 for i in range(50)] #no levels done yet
            json.dump(playerData, f)
            print("playerData written")

    

    


from game import Game

# loading colours 
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
purple = pygame.Color(135, 7, 255)
bright_purple = pygame.Color(189, 58, 255)



# initialising all features of the game
game = Game(os.path.dirname(package_path), os.path.dirname(real_path))
rect_len = game.settings.rect_len
snake = game.snake
pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((game.settings.width * game.settings.rect_len, game.settings.height * game.settings.rect_len))
game.screen = screen
pygame.display.set_caption('Gluttonous++')
crash_sound = pygame.mixer.Sound(game.src + '/sound/crash.wav')

def yes():
    # arbitrary function to utilise in buttons 
    return True

def text_objects(text, font, color=black):
    # rendering fonts and text
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_display(text, x, y, color=black, size=50):
    # displays messages on the screen
    large_text = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + '/arial.ttf', size)
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = (x, y)
    screen.blit(text_surf, text_rect)
    pygame.display.update()

def button(msg, x, y, w, h, inactive_color, active_color, action, **kwargs):
    # initialising button  
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # checks if button is hovered over, then clicked
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            if kwargs:
                return action(**kwargs)
            else:
                return action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))

    # blits button to screen
    pressed = 0
    smallText = pygame.font.Font(os.path.dirname(package_path) + '/arial.ttf', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = (x + (w / 2), y + (h / 2))
    screen.blit(TextSurf, TextRect)
    return pressed

def quitgame():
    # exits game 
    pygame.quit()
    sys.exit()


def crash():
    # executes the crash of the snake 

    # plays sound and displays message
    pygame.mixer.Sound.play(crash_sound)
    message_display('crashed', game.settings.width / 2 * 30,\
                    game.settings.height / 6 * 30, red)
    
    # fades out screen
    fadeout = pygame.Surface((rect_len*game.settings.width, rect_len*game.settings.height))
    fadeout = fadeout.convert()
    fadeout.fill(black)
    pygame.time.delay(500)
    for i in range(10):
       fadeout.set_alpha(5)
       screen.blit(fadeout, (0, 0))
       pygame.display.update()
       pygame.time.delay(10)
    for i in range(10):
       fadeout.set_alpha(40)
       screen.blit(fadeout, (0, 0))
       pygame.display.update()
       pygame.time.delay(10)
    for i in range(10):
       fadeout.set_alpha(80)
       screen.blit(fadeout, (0, 0))
       pygame.display.update()
       pygame.time.delay(10)
    screen.fill(black)
    pygame.display.update()
    pygame.time.delay(500)


def initial_interface(invalid, directory):
    # displays the landing page 

    restart = False
    screen.fill(white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # displays title 
        message_display('Gluttonous++', game.settings.width / 2 * game.settings.rect_len, game.settings.height / 4 * game.settings.rect_len)
        
        # error messages 
        if invalid_loc:
            message_display('Error', game.settings.width / 4 * game.settings.rect_len, game.settings.height / 2 * game.settings.rect_len)

        # displays go button to take user to level select
        button('Go!', 410, 280, 80, 40, green, bright_green, level_select)

        # displays settings button to take user to visual settings
        if not invalid:
            button('Settings', 410, 340, 80, 40, yellow, bright_yellow, settings, directory=directory)
        else:
            button('settings disabled', 390, 340, 120, 40, yellow, bright_yellow, yes)

        # displays quit button to close game window
        button('Quit', 410, 400, 80, 40, red, bright_red, quitgame)

        # displays level maker button 
        if not invalid:
            button('Level Maker', 390, 460, 120, 40, purple, bright_purple, level_maker, game=game)
        else:
            button('maker disabled', 390, 460, 120, 40, purple, bright_purple, yes)

        # displays instructions button 
        button('Instructions', 390, 520, 120, 40, blue, bright_blue, display_instructions, package_path=package_path, screen=screen, game=game)

        pygame.display.update()
        pygame.time.Clock().tick(15)

def settings(directory):
    # allows users to change the style of the game features 

    # reads in style from the data file  
    with open(directory + "/style.txt", 'r') as f:
        style = f.read()

    screen.fill(black)

    # displays the page continuously until 'back' button is pressed or window is closed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # returns user to landing page 
        if button('Home', 100, 200, 80, 40, red, bright_red, yes):
            screen.fill(white)
            return 0

        # displays the selected style as green and other buttons as yellow
        #  allows style to be changed between retro, goofy and pop
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
        if style == 'pop':
            button('pop', 140, 20, 40, 40, green, green, yes)
        elif button('pop', 140, 20, 40, 40, yellow, bright_yellow, yes):
            with open(directory + "/style.txt", "w") as f:
                f.write('pop')
                style = 'pop'

        pygame.display.update()
        pygame.time.Clock().tick(15)


def level_select():

    # opens the directory containing the level data 
    with open(real_path + '/playerData.txt', "r") as f:
        playerData = json.load(f)

    
    intro = True
    restart = [0, ""]
    screen.fill(black)
    while intro:
        # displays level select page until something is selected
        if restart[0]:
            break
        if restart[1]:
            restart = game_loop(restart[1], game.custom, restart=True)
            continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
       
        with open(real_path + '/playerData.txt', "r") as f:
            playerData = json.load(f)

        if button('Reset finished levels', 130, 800, 200, 40, red, bright_red, yes):
            with open(real_path + '/playerData.txt', "w") as f:
                playerData = [0 for i in range(50)]
                json.dump(playerData, f)


        message_display('Select Level', game.settings.width / 2 * game.settings.rect_len, \
                        game.settings.height / 8 * game.settings.rect_len, color=white)
        message_display('Preset levels', game.settings.width / 4 * game.settings.rect_len, \
                        game.settings.height / 5 * game.settings.rect_len, color=white, size=30)
        message_display('Custom levels', 3*game.settings.width / 4 * game.settings.rect_len, \
                        game.settings.height / 5 * game.settings.rect_len, color=white, size=30)

        if button('Home', 410, 150, 80, 40, red, bright_red, yes):
            screen.fill(white)
            return 0

        dontrender = False
        #generate buttons for preset levels. Sorts them first
        for idx, d in enumerate(sorted(os.listdir(os.path.dirname(package_path) + '/levels'), key=lambda name: int(name.split('-')[0])*11 + int(name.split('-')[1]))):
            if playerData[idx]:
                temp = button(d, 80 + 60*(idx%5), 220 + 50*(idx//5), 50, 40,\
                                blue, bright_blue, game_loop, level=d, custom=False)
            else:
                temp = button(d, 80 + 60*(idx%5), 220 + 50*(idx//5), 50, 40,\
                                green, bright_green, game_loop, level=d, custom=False)
            if isinstance(temp, list):
                restart = temp
                if restart[0] or restart[1]:
                    dontrender = True
                    break

        if dontrender:
            continue
        #generate buttons for customised levels.
        if not os.listdir(real_path + '/levels'):
            message_display('wow, such empty ~', 3*game.settings.width / 4 * game.settings.rect_len, game.settings.height / 4 * game.settings.rect_len, color=bright_blue, size=25)
        for idx, d in enumerate(sorted(os.listdir(real_path + '/levels'))):
            temp = button(d, 520 + 160*(idx%2), 220 + 50*(idx//2), 150, 40, yellow, bright_yellow, game_loop, level=d, custom=True)
            if isinstance(temp, list):
                restart = temp
                if restart[0] or restart[1]:
                    break


        if restart[0]:
            break
        pygame.display.update()
        pygame.time.Clock().tick(15)


def game_loop(level, custom=False, restart=False):
    with open(os.path.join(game.srcreal, "snakeData/style.txt"), 'r') as f:
        game.style = f.read()

    game.restart_game(mapdir=level, custom=custom)

    #give instructions if necesssary:
    msg = game.config.settings.get('intro', None)

    if int(game.config.settings['mapX']) > 30 or int(game.config.settings['mapY']) > 26:
        game.settings.rect_len = 15
    else:
        game.settings.rect_len = 30

    rect_len = game.settings.rect_len



    screen.fill(black)
    game.blit_map(rect_len, screen)
    
    if msg is not None and restart == False:
        #draw box

        pygame.draw.rect(screen, white, pygame.Rect(200, 350, 500, 200))
        #draw message
        msg = msg.split('-')
        for index, line in enumerate(msg):
            message_display(line, 450, 400 + index*30, black, 20)

        pygame.display.update()
        while True:
            pygame.event.pump()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if button('OK', 410, 500, 80, 40, blue, bright_blue, yes):
                break
            pygame.display.update()
            pygame.time.delay(40)

    screen.fill(black)
    game.blit_map(rect_len, screen)


    space_img = game.space_img
    #whether the game is stopped
    stop = False


    #always blit once before doing stuff, and sleep for a little bit! This allows for some time preparation.
    game.snake.blit(rect_len, screen, 1, 0)
    game.strawberry.blit(screen, int(game.config.settings["xOffset"]), int(game.config.settings["yOffset"]))
    game.blit_features(rect_len, screen)

    game.plates_pressed_goal = len(game.map.goals) + len(game.map.alt_goals)
    game.plates_pressed = 0

    game.blit_score(white, yellow, screen)
    pygame.display.update()
    pygame.time.delay(1000)
    score_cover = pygame.Rect(0, 0, 300, 50)
    button_cover = pygame.Rect(300, 0, 200, 50)

    #the phase of the process, split into 5
    phase = 0
    move = game.direction_to_int(snake.facing)

    #information for winning
    maxS = int(game.config.settings['maxS'])
    mode = int(game.config.settings['strawberry'])


    fps = 5
    delay = 1000/(fps*5)

    while True:
        pygame.event.pump()
        move_temp, escape = human_move()

        #measures time between the two to make sure the speed stays the same
        before = datetime.datetime.now()
        
        stop = stop ^ escape
        if move_temp >= 0 and not stop:
            move = move_temp


        restart = [0, "", custom]
        if stop:
            #build restart screen
            #xOffset, yOffset, width, height
            restart[1] = button('Restart', 400, 10, 80, 40, yellow, bright_yellow, yes) * level
            restart[0] += button('Home', 300, 10, 80, 40, green, bright_green, yes)
            if restart[0] or restart[1]:
                if restart[0]: 
                    screen.fill(white)
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

            #update strawberry
            if (game.snake.score + game.snake_clone.score < int(game.config.settings['maxS']))\
                and game.strawberry.position == [-100, -100]:
                game.strawberry.random_pos()

            #blit snake
            game.snake.blit(rect_len, screen, state, phase)
            if game.snake_clone.init:
                game.snake_clone.blit(rect_len, screen, state1, phase)
            #blit the features, which always appear on top of the snake
            game.blit_features(rect_len, screen)
            game.strawberry.blit(screen, int(game.config.settings["xOffset"]), int(game.config.settings["yOffset"]))
            #covers up the score and home, restart buttons.
            pygame.draw.rect(screen, black, button_cover)
            pygame.display.update(button_cover)

            #update everything around the snake
            for coord in game.snake.segmentd + game.snake_clone.segmentd + [result] + [result1]:
                if coord:
                    x_f, y_f = (coord[0] + x0)*rect_len, (coord[1] + y0)*rect_len
                    pygame.display.update(pygame.Rect(x_f, y_f, rect_len, rect_len))

        else:
            game.snake.blit(rect_len, screen, state, phase)
            if game.snake_clone.init:
                game.snake_clone.blit(rect_len, screen, state1, phase)
            if phase == 1: #winning mechanics
                if mode == 0 or mode == 2:
                    game.plates_pressed = len(game.map.alt_goals)
                    for coord in (game.snake.segmentd + game.snake_clone.segmentd):
                        if coord in game.map.goals:
                            game.plates_pressed += 1
                        elif coord in game.map.alt_goals:
                            game.plates_pressed -= 1

                pygame.draw.rect(screen, black, score_cover)

                game.blit_score(white, yellow, screen)
                pygame.display.update(score_cover)


                if mode == 0 and game.plates_pressed == game.plates_pressed_goal:
                    game.won = True
                elif mode == 1 and game.snake.score + game.snake_clone.score >= maxS:
                    game.won = True
                elif mode == 2 and game.plates_pressed == game.plates_pressed_goal and\
                game.snake.score + game.snake_clone.score >= maxS:
                    game.won = True

                if game.won:
                    if not custom:
                        #write progress to file
                        with open(real_path + '/playerData.txt', "r+") as f:
                            compon = level.split('-')
                            playerData = json.load(f)
                            playerData[(int(compon[0]) - 1)*10 + (int(compon[1]) - 1)] = 1
                            f.seek(0, 0)
                            json.dump(playerData, f)
                    message_display('You Won!', 450, 800, green, 60)


            if phase == 4 and game.won:
                fadeout = pygame.Surface((rect_len*game.settings.width, rect_len*game.settings.height))
                fadeout = fadeout.convert()
                fadeout.fill(white)
                pygame.time.delay(100)
                for i in range(20):
                    fadeout.set_alpha(3)
                    screen.blit(fadeout, (0, 0))
                    pygame.display.update()
                    pygame.time.delay(50)
                for i in range(20):
                    fadeout.set_alpha(10)
                    screen.blit(fadeout, (0, 0))
                    pygame.display.update()
                    pygame.time.delay(50)
                for i in range(20):
                    fadeout.set_alpha(30)
                    screen.blit(fadeout, (0, 0))
                    pygame.display.update()
                    pygame.time.delay(40)
                pygame.time.delay(100)
                screen.fill(black)
                pygame.display.update()

                #reset screen size so nothing messes up
                game.settings.rect_len = 30
                return restart
            

        phase = (phase + 1) % 5

        #at the end we measure it:
        diff = (datetime.datetime.now() - before).microseconds


        pygame.time.delay(math.ceil(delay - diff/1000))

    if not (restart[0] or restart[1]):
        crash()
        restart[1] = level
    game.settings.rect_len = 30
    return restart

def options():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            return True
    return False


def human_move():
    # if the user selects something on their keypad, this is tracked
    direction = 'none'
    escape = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        # player can use arrow keys or WASD to move 
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

                escape = True

    # move is translated to an integer as per the function defined in the game class
    move = game.direction_to_int(direction)
    return move, escape


if __name__ == "__main__":
    initial_interface(invalid_loc, real_path)
