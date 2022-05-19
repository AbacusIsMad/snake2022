# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:19:25 2018

@author: zou
BingQi Ling
"""
import pygame, random
#import numpy as np
import threading
import time
from map import Map
from snake import Snake
from config import Config


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


class Settings:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.rect_len = 30

        #size of game, and then size of individual grids. 
        # self.width = 52
        # self.height = 52
        # self.rect_len = 15

class Strawberry():
    def __init__(self, settings, parent):
        self.settings = settings
        self.parent = parent

        self.style = str(random.randint(1, 8))
        path = self.parent.src + "/styles/" + self.parent.style + "/images/"

        self.images = [pygame.transform.scale(pygame.image.load(path + 'food' + str(i + 1) + '.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len)) for i in range(8)]

        self.times_called = 0     
        self.initialize()
        
    def random_pos(self):
        self.style = str(random.randint(1, 8))             
        print("called!")

        random.shuffle(self.parent.map.strawberry_valid)
        valid_pos = (loc for loc in self.parent.map.strawberry_valid if not \
                    ((loc in self.parent.snake.segmentd) or (loc in self.parent.snake_clone.segmentd)))

        try:
            pos = next(valid_pos)
        except StopIteration:
            pos = [-100, -100]

        self.position = [pos[0], pos[1]]


    def reset_img_source(self):
        path = self.parent.src + "/styles/" + self.parent.style + "/images/"

        self.images = [pygame.transform.scale(pygame.image.load(path + 'food' + str(i + 1) + '.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len)) for i in range(8)]


    def blit(self, screen, x0, y0):
        x_f = (self.position[0] + x0)*self.settings.rect_len
        y_f = (self.position[1] + y0)*self.settings.rect_len
        screen.blit(self.images[int(self.style) - 1], (x_f, y_f))
        pygame.display.update(pygame.Rect(x_f, y_f, self.settings.rect_len, self.settings.rect_len))
   
    def initialize(self):
        self.position = [15, 10]


class Game:
    def __init__(self, package_data, file_location):
        self.src = package_data
        self.srcreal = file_location
        self.custom = False
        self.won = False

        with open(self.srcreal + '/snakeData/style.txt') as f:
            self.style = f.read()
        #self.style = '0'
        self.settings = Settings()
        self.reset_img_source()
        self.snake = Snake(self)
        self.snake_clone = Snake(self, clone=True)
        self.strawberry = Strawberry(self.settings, self)
        self.move_dict = {0 : 'right',
                          1 : 'up',
                          2 : 'left',
                          3 : 'down',
                          -1: 'none'}

    def reset_img_source(self):

        path = self.src + "/styles/" + self.style + "/images/"


        self.tile_img = pygame.transform.scale(pygame.image.load(path + 'tile.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len))
        self.space_img = pygame.transform.scale(pygame.image.load(path + 'space.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len))
        self.wrap_img = pygame.transform.scale(pygame.image.load(path + 'wrap.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len))
        self.pad_img = pygame.transform.scale(pygame.image.load(path + 'pad.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len))
        self.plate_img = pygame.transform.scale(pygame.image.load(path + 'plate.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len))
        self.platea_img = pygame.transform.scale(pygame.image.load(path + 'platea.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len))
        self.plate_alt_img = pygame.transform.scale(pygame.image.load(path + 'plate_alt.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len))
        self.platea_alt_img = pygame.transform.scale(pygame.image.load(path + 'platea_alt.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len))
        self.clone_img = [pygame.transform.scale(pygame.image.load(path + 'clone' + str(i) + '.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len)) for i in range(4)]
        self.clonea_img = [pygame.transform.scale(pygame.image.load(path + 'clonea' + str(i) + '.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len)) for i in range(4)]

    def restart_game(self, mapdir, custom=False): 
        
        self.custom = custom
        #set config. This has a bunch of options that control stuff.
        self.config = Config(parent=self, mapdir=mapdir)
        #set game size:
        if int(self.config.settings['mapX']) > 30 or int(self.config.settings['mapY']) > 26:
            self.settings.rect_len = 15
        else:
            self.settings.rect_len = 30


        #update visuals at the start of the game
        self.reset_img_source()
        self.snake.reset_img_source()
        self.strawberry.reset_img_source()



        #set map
        self.map = Map(parent=self, mapdir=mapdir)
        self.map.generate_spaces()
        #set snake
        self.snake.initialize('snakeData/'*custom + 'levels/' + mapdir)
        self.snake_clone.init = False
        self.snake_clone.segmentd = []
        self.snake_clone.score = 0
        #set stawberry if it exists.
        self.strawberry.times_called = 0
        if int(self.config.settings['strawberry']) or int(self.config.settings['maxS']) == 0:
            self.strawberry.random_pos()
        else:
            self.strawberry.position = [-100, -100]
        self.snake.won = False
        self.won = False
    
    def direction_to_int(self, direction):
        direction_dict = {value : key for key,value in self.move_dict.items()}
        return direction_dict[direction]
        
    def do_move(self, move):
        move_dict = self.move_dict

        change_direction = move_dict[move]

        #this translates the number back to the string again. Kinda redundant tbh.

        if change_direction == 'right' and not self.snake.segments[1] == [1, 0]:
            self.snake.facing = change_direction
        if change_direction == 'left' and not self.snake.segments[1] == [-1, 0]:
            self.snake.facing = change_direction
        if change_direction == 'up' and not self.snake.segments[1] == [0, -1]:
            self.snake.facing = change_direction
        if change_direction == 'down' and not self.snake.segments[1] == [0, 1]:
            self.snake.facing = change_direction

        if self.snake_clone.init:

            offset = int(self.config.settings['cOffset'])

            clone_change_direction = move_dict[(move + offset) % 4]

            if clone_change_direction == 'right' and not self.snake_clone.segments[1] == [1, 0]:
                self.snake_clone.facing = clone_change_direction
            if clone_change_direction == 'left' and not self.snake_clone.segments[1] == [-1, 0]:
                self.snake_clone.facing = clone_change_direction
            if clone_change_direction == 'up' and not self.snake_clone.segments[1] == [0, -1]:
                self.snake_clone.facing = clone_change_direction
            if clone_change_direction == 'down' and not self.snake_clone.segments[1] == [0, 1]:
                self.snake_clone.facing = clone_change_direction
        
        #state, replace = self.snake.update()
        if self.snake_clone.init:
            state1, replace1 = self.snake_clone.update()
        else:
            state1, replace1 = 0, []
        state, replace = self.snake.update()

        return state, state1, replace, replace1
    
    def game_end(self):
        end = False
        # if the snake hits the edge of the border, the snake dies
        if self.snake.position[0] >= (self.settings.width-2) or self.snake.position[0] < 2:
            end = True
        if self.snake.position[1] >= (self.settings.height-2) or self.snake.position[1] < 2:
            end = True
        if self.snake.segments[0] in self.snake.segments[1:]:
            end = True
        return end
    
    def blit_score(self, color, s_color, screen):
        font = pygame.font.Font(self.src + '/arial.ttf', 25)

        straw = "strawberries: " + str(self.snake.score + self.snake_clone.score) + '/' +\
                    str(self.config.settings['maxS'])

        plate = "plates: " + str(self.plates_pressed) + '/' +\
                    str(self.plates_pressed_goal)

        color2 = color

        if self.config.settings['strawberry'] == '0':
            if self.plates_pressed == self.plates_pressed_goal:
                color = s_color
            text = font.render(plate, True, color)
            screen.blit(text, (0, 0))

        elif self.config.settings['strawberry'] == '1':
            if self.snake.score + self.snake_clone.score >= int(self.config.settings['maxS']):
                color = s_color
            text = font.render(straw, True, color)
            screen.blit(text, (0, 0))

        elif self.config.settings['strawberry'] == '2':
            if self.snake.score + self.snake_clone.score >= int(self.config.settings['maxS']):
                color = s_color

            if self.plates_pressed == self.plates_pressed_goal:
                color2 = s_color

            text = font.render(straw, True, color)
            text2 = font.render(plate, True, color2)
            screen.blit(text, (0, 0))
            screen.blit(text2, (0, 20))

    def blit_map(self, rect_len, screen, developer=False):
        x0 = int(self.config.settings["xOffset"])
        y0 = int(self.config.settings["yOffset"])

        if developer:
            true_empty_img = pygame.transform.scale(pygame.image.load(self.src + '/styles/'\
                             + self.style + '/images/true_empty.bmp'),\
                            (self.settings.rect_len, self.settings.rect_len))

        for i in range(0, int(self.config.settings["mapX"])):
            for k in range(0, int(self.config.settings["mapY"])):
                tile = self.map.tiles[k][i]
                if tile.type == "Other":
                    pass
                elif tile.type == "Solid":
                    screen.blit(self.tile_img, ((i + x0)*rect_len, (k + y0)*rect_len))
                    for j in range(4):
                        if tile.wrap_plate & (1 << j):
                            screen.blit(pygame.transform.rotate(self.wrap_img, j*90), ((i + x0)*rect_len, (k + y0)*rect_len))
                    for j in range(4):
                        if tile.pad_clone & (1 << j):
                            screen.blit(pygame.transform.rotate(self.pad_img, j*90), ((i + x0)*rect_len, (k + y0)*rect_len))
                elif tile.type == "Empty": 
                    if developer and tile.true_empty:
                        screen.blit(true_empty_img, ((i + x0)*rect_len, (k + y0)*rect_len))
                    else:
                        screen.blit(self.space_img, ((i + x0)*rect_len, (k + y0)*rect_len))
                else:
                    pass

    def blit_features(self, rect_len, screen):
        x0 = int(self.config.settings["xOffset"])
        y0 = int(self.config.settings["yOffset"])
        #pressure plates
        for location in self.map.goals:
            x_f, y_f = (location[0] + x0)*rect_len, (location[1] + y0)*rect_len
            if (location in self.snake.segmentd) or (location in self.snake_clone.segmentd):
                screen.blit(self.platea_img, (x_f, y_f))
            else: 
                screen.blit(self.plate_img, (x_f, y_f))
            pygame.display.update(pygame.Rect(x_f, y_f, self.settings.rect_len, self.settings.rect_len))
        for location in self.map.alt_goals:
            x_f, y_f = (location[0] + x0)*rect_len, (location[1] + y0)*rect_len
            if (location in self.snake.segmentd) or (location in self.snake_clone.segmentd):
                screen.blit(self.platea_alt_img, (x_f, y_f))
            else: 
                screen.blit(self.plate_alt_img, (x_f, y_f))
            pygame.display.update(pygame.Rect(x_f, y_f, self.settings.rect_len, self.settings.rect_len))
        offset = int(self.config.settings['cOffset'])
        for location in self.map.clones:
            x_f, y_f = (location[0] + x0)*rect_len, (location[1] + y0)*rect_len
            if self.snake_clone.init:
                screen.blit(self.clonea_img[offset], (x_f, y_f))
            else:
                screen.blit(self.clone_img[offset], (x_f, y_f))
            pygame.display.update(pygame.Rect(x_f, y_f, self.settings.rect_len, self.settings.rect_len))
