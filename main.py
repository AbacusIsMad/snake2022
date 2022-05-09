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
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE
from pygame.locals import QUIT

def base_path(path):
    try:
        basedir = sys._MEIPASS
    except Exception:
        basedir = os.path.abspath(".")
    return os.path.join(basedir, path)

if __name__ == "__main__":
    #get locally stored config file
    invalid_loc = False
    if getattr(sys, 'frozen', None):
        game_data = os.path.join(os.path.dirname(sys.executable), 'snakeData')
    else:
        game_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snakeData')

    #check for permissions, or else resort to internal directory.
    if not os.path.exists(game_data):
        try:
            os.makedirs(game_data)
        except Exception:
            print("failed to make directory or file! Returning to normal dir.")
            game_data = './snakeData'
            invalid_loc = True
    elif not os.access(game_data, os.W_OK):
        print("directory is not writable! Returning to normal dir.")
        game_data = './snakeData'
        invalid_loc = True
    print('storage directory:', game_data)

    #create the files if they don't exist.
    if not os.path.exists(game_data + '/style.txt'):
        with open(game_data + '/style.txt', 'w') as f:
            f.write('0')
            print("style written")
    if not os.path.exists(game_data + '/playerData.txt'):
        with open(game_data + '/playerData.txt', 'w') as f:
            f.write('')
            print("playerData written")

    #change to _MEIxxxx if needed, to get src
    os.chdir(base_path(''))
    

    


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

game = Game(game_data)
rect_len = game.settings.rect_len
snake = game.snake
pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((game.settings.width * game.settings.rect_len, game.settings.height * game.settings.rect_len))
pygame.display.set_caption('Gluttonous')

#osx problem?
#pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
crash_sound = pygame.mixer.Sound('./sound/crash.wav')

def yes():
    return True

def text_objects(text, font, color=black):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_display(text, x, y, color=black):
    large_text = pygame.font.SysFont('comicsansms', 50)
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
    smallText = pygame.font.SysFont('comicsansms', 20)
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

        home = button('Home', 100, 200, 80, 40, red, bright_red, yes)
        if home:
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


#def game_loop(player, fps=10):
def game_loop(level):
    with open(os.path.join(game.src, "style.txt"), 'r') as f:
        game.style = f.read()

    game.restart_game(level)
    screen.fill(black)
    game.blit_map(rect_len, screen)
    
    space_img = game.space_img
    #whether the game is stopped
    stop = False
    #if the snake has crashed or lost
    cont = 1
    #I might not use this
    convert = False
    #always blit once before doing stuff, and sleep for a little bit! This allows for some time preparation.
    game.snake.blit(rect_len, screen)
    #game.features.blit
    game.strawberry.blit(screen, int(game.config.settings["xOffset"]), int(game.config.settings["yOffset"]))
    game.blit_features(rect_len, screen)
    game.blit_score(white, screen)
    pygame.display.update()
    pygame.time.delay(1000)
    while cont:

        pygame.event.pump()
        
        
        move, escape = human_move()
        
        stop = stop ^ escape
        #control speed here!
        fps = 5
        # fps = 10
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
        else:
            state, state1, result, result1 = game.do_move(move)
            print(state, state1, result, result1)
            if state < 0 or state1 < 0:
                break


            #blit everything with spaces where the snake is so clones don't affect each other.
            x0 = int(game.config.settings["xOffset"])
            y0 = int(game.config.settings["yOffset"])
            for coord in game.snake.segmentd:
                screen.blit(space_img, ((coord[0] + x0)*rect_len, (coord[1] + y0)*rect_len))
            if game.snake_clone.init:
                for coord in game.snake_clone.segmentd:
                    screen.blit(space_img, ((coord[0] + x0)*rect_len, (coord[1] + y0)*rect_len))
            if result:
                screen.blit(space_img, ((result[0] + x0)*rect_len, (result[1] + y0)*rect_len))
            if result1:
                screen.blit(space_img, ((result1[0] + x0)*rect_len, (result1[1] + y0)*rect_len))

            game.snake.blit(rect_len, screen)
            if game.snake_clone.init:
                game.snake_clone.blit(rect_len, screen)
            game.blit_features(rect_len, screen)
            game.strawberry.blit(screen, int(game.config.settings["xOffset"]), int(game.config.settings["yOffset"]))
            #covers up the score and buttons.
            pygame.draw.rect(screen, black, pygame.Rect(0, 0, 400, 80))
            game.blit_score(white, screen)

            pygame.display.update()
            
            pygame.time.delay(1000//fps)
            #fpsClock.tick(fps)
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
    direction = snake.facing
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
    initial_interface(invalid_loc, game_data)
