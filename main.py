# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:22:20 2018 bruh are you serious

@author: zou
"""

import pygame
import time
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE
from pygame.locals import QUIT
import threading

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

game = Game()
rect_len = game.settings.rect_len
snake = game.snake
pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((game.settings.width * 15, game.settings.height * 15))
pygame.display.set_caption('Gluttonous')

#osx problem?
#pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
crash_sound = pygame.mixer.Sound('./sound/crash.wav')


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
                action(parameter)
            else:
                action()
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
    quit()


def crash():
    pygame.mixer.Sound.play(crash_sound)
    message_display('crashed', game.settings.width / 2 * 15, game.settings.height / 3 * 15, white)
    time.sleep(1)


def initial_interface():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(white)
        message_display('Gluttonous', game.settings.width / 2 * 15, game.settings.height / 4 * 15)

        button('Go!', 80, 240, 80, 40, green, bright_green, game_loop, 'human')
        button('Quit', 270, 240, 80, 40, red, bright_red, quitgame)

        pygame.display.update()
        pygame.time.Clock().tick(15)


#def game_loop(player, fps=10):
def game_loop(player, fps=10):
    game.restart_game("1-1")
    screen.fill(black)
    game.blit_map(rect_len, screen)
    
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
    pygame.display.update()
    pygame.time.delay(1000)
    print("done")
    while cont:

        pygame.event.pump()
        
        
        move, escape = human_move()
        
        stop = stop ^ escape
        #control speed here!
        fps = 5
        # fps = 10
        if stop:
            #build restart screen
            button('Quit', 270, 240, 80, 40, red, bright_red, quitgame)
            button('Restart', 80, 240, 80, 40, green, bright_green, quitgame)
            pygame.display.update()
            fpsClock.tick(30)
        else:
            #result = game.do_move(move, game.strawberry)
            result = game.do_move(move)
            if result == -1:
                break


            #game.blit_map(screen, "map.txt")
            #the result carries the last  place thte 
            game.snake.blit(rect_len, screen, result)
            #game.features.blit()
            game.strawberry.blit(screen, int(game.config.settings["xOffset"]), int(game.config.settings["yOffset"]))
            game.blit_score(white, screen)

            pygame.display.update()
            
            pygame.time.delay(1000//fps)
            #fpsClock.tick(fps)

    crash()

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
    #print("move: ", move)
    # print(game.snake.segments)
    return move, escape


if __name__ == "__main__":
    initial_interface()
