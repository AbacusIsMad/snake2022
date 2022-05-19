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

#change this to 1 to make it big
correction_factor = 2

class Settings:
    def __init__(self):
        #size of game, and then size of individual grids. 
        self.width = 30
        self.height = 30
        self.rect_len = 30


class Strawberry():
    def __init__(self, settings, parent):
        #  strawberry is initialised with a parent game, and the settings/size of the game
        self.settings = settings
        self.parent = parent

        # the type of strawberry is chosen randomly, along with its associated sprite 
        self.style = str(random.randint(1, 8))
        path = self.parent.src + "/styles/" + self.parent.style + "/images/"
        self.images = [pygame.transform.scale(pygame.image.load(path + 'food' + str(i + 1) + '.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len)) for i in range(8)]

        self.times_called = 0     
        self.initialize()
        
    def random_pos(self):
        # randomly generates the strawberry's new random position

        self.style = str(random.randint(1, 8))             
        
        # confirms if the position of the strawberry is valid 
        random.shuffle(self.parent.map.strawberry_valid)
        valid_pos = (loc for loc in self.parent.map.strawberry_valid if not \
                    ((loc in self.parent.snake.segmentd) or (loc in self.parent.snake_clone.segmentd)))

        try:
            pos = next(valid_pos)
        except StopIteration:
            pos = [-100, -100]

        #  sets position of the strawberry to new pos 
        self.position = [pos[0], pos[1]]


    def reset_img_source(self):
        # calls the correct sprite and makes sure that strawberry is in the correct style 
        path = self.parent.src + "/styles/" + self.parent.style + "/images/"

        self.images = [pygame.transform.scale(pygame.image.load(path + 'food' + str(i + 1) + '.bmp'),\
                        (self.settings.rect_len, self.settings.rect_len)) for i in range(8)]


    def blit(self, screen, x0, y0):
        # blits the strawberry on the screen based on its position
        x_f = (self.position[0] + x0)*self.settings.rect_len
        y_f = (self.position[1] + y0)*self.settings.rect_len
        screen.blit(self.images[int(self.style) - 1], (x_f, y_f))
        pygame.display.update(pygame.Rect(x_f, y_f, self.settings.rect_len, self.settings.rect_len))
   
    def initialize(self):
        # strawberry is initialised with an arbitrary position
        self.position = [15, 10]


class Game:
    def __init__(self, package_data, file_location):
        # games are initialised with the correct data which defines where all information
        #  particularly levels, player, and style, are kept 
        self.src = package_data
        self.srcreal = file_location

        self.custom = False
        self.won = False

        # the style/visuals of game are stored in a textfile
        with open(self.srcreal + '/snakeData/style.txt') as f:
            self.style = f.read()
        
        # all aspects of the game are initialised 
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

        #  all aspects of the map are sourced here (in the correct style )
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

        #setting the config file 
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

        #  game is returned to initial state 
        self.snake.won = False
        self.won = False
    
    def direction_to_int(self, direction):
        # transforms string direction to number based on pre-dictionary defined in the game class
        direction_dict = {value : key for key,value in self.move_dict.items()}
        return direction_dict[direction]
        
    def do_move(self, move):

        move_dict = self.move_dict

        #this translates the number back to the string again. 
        change_direction = move_dict[move]

        #  checks to make sure that snake is not travelling in the exact opposite direction
        if change_direction == 'right' and not self.snake.segments[1] == [1, 0]:
            self.snake.facing = change_direction
        if change_direction == 'left' and not self.snake.segments[1] == [-1, 0]:
            self.snake.facing = change_direction
        if change_direction == 'up' and not self.snake.segments[1] == [0, -1]:
            self.snake.facing = change_direction
        if change_direction == 'down' and not self.snake.segments[1] == [0, 1]:
            self.snake.facing = change_direction


        # if the snake has a clone, replicate this behaviour 
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
        
        # returns the state of the snake
        if self.snake_clone.init:
            state1, replace1 = self.snake_clone.update()
        else:
            state1, replace1 = 0, []
        state, replace = self.snake.update()

        return state, state1, replace, replace1
    
    def game_end(self):
        end = False

        # if the snake hits the edge of any border, the snake crashes and game ends
        if self.snake.position[0] >= (self.settings.width-2) or self.snake.position[0] < 2:
            end = True
        if self.snake.position[1] >= (self.settings.height-2) or self.snake.position[1] < 2:
            end = True
        if self.snake.segments[0] in self.snake.segments[1:]:
            end = True
        return end
    
    def blit_score(self, color, screen):
        # score is blitted onto screen in the top left corner
        font = pygame.font.Font(self.src + '/arial.ttf', 25)
        text = font.render('Score: ' + str(self.snake.score + self.snake_clone.score), True, color)
        screen.blit(text, (0, 0))

    def blit_map(self, rect_len, screen, developer=False):
        # blits the map to the screen
        x0 = int(self.config.settings["xOffset"])
        y0 = int(self.config.settings["yOffset"])

        # checks to see if used by level maker
        if developer:
            true_empty_img = pygame.transform.scale(pygame.image.load(self.src + '/styles/'\
                             + self.style + '/images/true_empty.bmp'),\
                            (self.settings.rect_len, self.settings.rect_len))

        # parses through the list of the map and blits each tile
        #  based on their x and y coordiantes 
        for i in range(0, int(self.config.settings["mapX"])):
            for k in range(0, int(self.config.settings["mapY"])):
                tile = self.map.tiles[k][i]
                if tile.type == "Other":
                    pass

                # the tile features of any solid tiles are blitted, including wrap or pads
                elif tile.type == "Solid":
                    screen.blit(self.tile_img, ((i + x0)*rect_len, (k + y0)*rect_len))
                    for j in range(4):
                        if tile.wrap_plate & (1 << j):
                            screen.blit(pygame.transform.rotate(self.wrap_img, j*90), ((i + x0)*rect_len, (k + y0)*rect_len))
                    for j in range(4):
                        if tile.pad_clone & (1 << j):
                            screen.blit(pygame.transform.rotate(self.pad_img, j*90), ((i + x0)*rect_len, (k + y0)*rect_len))
                
                #  empty tiles are blitted
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

        # Blitting pressure plates (on top of empty tiles)
        for location in self.map.goals:
            x_f, y_f = (location[0] + x0)*rect_len, (location[1] + y0)*rect_len

            # if plate is initialised within snake or clone, it must already be blittted in activated state
            if (location in self.snake.segmentd) or (location in self.snake_clone.segmentd):
                screen.blit(self.platea_img, (x_f, y_f))
            # otherwise, plate is not yet activated
            else: 
                screen.blit(self.plate_img, (x_f, y_f))
            pygame.display.update(pygame.Rect(x_f, y_f, self.settings.rect_len, self.settings.rect_len))
        for location in self.map.alt_goals:
            x_f, y_f = (location[0] + x0)*rect_len, (location[1] + y0)*rect_len

            # same as above- if reverse plate is within snake or clone, it must be blitted in active state
            if (location in self.snake.segmentd) or (location in self.snake_clone.segmentd):
                screen.blit(self.platea_alt_img, (x_f, y_f))

            # otherwise, not yet activated
            else: 
                screen.blit(self.plate_alt_img, (x_f, y_f))
            pygame.display.update(pygame.Rect(x_f, y_f, self.settings.rect_len, self.settings.rect_len))
        offset = int(self.config.settings['cOffset'])

        # Blitting clone plates 
        for location in self.map.clones:
            x_f, y_f = (location[0] + x0)*rect_len, (location[1] + y0)*rect_len

            # if there is already a clone, the clone plate must be blitted in active state
            if self.snake_clone.init:
                screen.blit(self.clonea_img[offset], (x_f, y_f))

            #  otherwise, inactive state
            else:
                screen.blit(self.clone_img[offset], (x_f, y_f))
            pygame.display.update(pygame.Rect(x_f, y_f, self.settings.rect_len, self.settings.rect_len))
