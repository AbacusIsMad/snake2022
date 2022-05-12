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


class Settings:
    def __init__(self):
        #size of game, and then size of individual grids. 
        self.width = 28
        self.height = 28
        self.rect_len = 30
        


class Strawberry():
    def __init__(self, settings, parent):
        #  Strawberry is initialised associated with the settings, as well as a 'parent' game that it is loaded into 
        self.settings = settings
        self.parent = parent

        #  The type of strawberry is randomly allocated, and its associated image is fetched
        self.style = str(random.randint(1, 8))
        path = self.parent.src + "/styles/" + self.parent.style + "/images/"
        self.image = pygame.image.load(path + 'food' + str(self.style) + '.bmp')        
        self.initialize()
        
    def random_pos(self):
        self.style = str(random.randint(1, 8))
        path = self.parent.src + "/styles/" + self.parent.style + "/images/"
        self.image = pygame.image.load(path + 'food' + str(self.style) + '.bmp')                
        print("called!")

        # The strawberry can spawn in randomly at any location in the map 
        self.position[0] = random.randint(0, int(self.parent.config.settings["mapX"])-1)
        self.position[1] = random.randint(0, int(self.parent.config.settings["mapY"])-1)

        # If the strawberry accidentally spawns inside the snake, the function is re-called
        if (self.position in self.parent.snake.segmentd[:-1]) or not self.parent.map.tiles[self.position[1]][self.position[0]].true_empty:
            self.random_pos()

    def blit(self, screen, x0, y0):
        #  The strawberry is blitted onto the screen in it's random position 
        x_f = (self.position[0] + x0)*self.settings.rect_len
        y_f = (self.position[1] + y0)*self.settings.rect_len
        screen.blit(self.image, (x_f, y_f))
        pygame.display.update(pygame.Rect(x_f, y_f, self.settings.rect_len, self.settings.rect_len))
   
    def initialize(self):
        # The initial position for the strawberry is default
        self.position = [15, 10]
    
    def playSound(self):
        # When astrawberry is eaten, the game plays a sound
        eat_sound = pygame.mixer.Sound('./sound/eat.wav')
        pygame.mixer.Sound.play(eat_sound)
 
class Game:
    def __init__(self, game_data, real_location):
        # Each game is initialised with game data, location, settings, a snake, a snake clone, and strawberries
        self.src = game_data
        self.srcreal = real_location
        self.style = '0'
        self.settings = Settings()
        self.reset_img_source()
        self.snake = Snake(self)
        self.snake_clone = Snake(self, clone=True)
        self.strawberry = Strawberry(self.settings, self)
    
        # This dictionary helps in transforming integers to directions
        self.move_dict = {0 : 'up',
                          1 : 'down',
                          2 : 'left',
                          3 : 'right',
                          -1: 'none'}

    def reset_img_source(self): 
        #  Fetching the images for the map - all of the tiles and visuals are sourced here
        path = self.src + "/styles/" + self.style + "/images/"
        self.tile_img = pygame.transform.scale(pygame.image.load(path + 'tile.bmp'), (self.settings.rect_len, self.settings.rect_len))
        self.space_img = pygame.transform.scale(pygame.image.load(path + 'space.bmp'), (self.settings.rect_len, self.settings.rect_len))
        self.wrap_img = pygame.transform.scale(pygame.image.load(path + 'wrap.bmp'), (self.settings.rect_len, self.settings.rect_len))
        self.pad_img = pygame.transform.scale(pygame.image.load(path + 'pad.bmp'), (self.settings.rect_len, self.settings.rect_len))
        self.plate_img = pygame.transform.scale(pygame.image.load(path + 'plate.bmp'), (self.settings.rect_len, self.settings.rect_len))
        self.platea_img = pygame.transform.scale(pygame.image.load(path + 'platea.bmp'), (self.settings.rect_len, self.settings.rect_len))
        self.plate_alt_img = pygame.transform.scale(pygame.image.load(path + 'plate_alt.bmp'), (self.settings.rect_len, self.settings.rect_len))
        self.platea_alt_img = pygame.transform.scale(pygame.image.load(path + 'platea_alt.bmp'), (self.settings.rect_len, self.settings.rect_len))
        self.clone_img = pygame.transform.scale(pygame.image.load(path + 'clone.bmp'), (self.settings.rect_len, self.settings.rect_len))
        self.clonea_img = pygame.transform.scale(pygame.image.load(path + 'clonea.bmp'), (self.settings.rect_len, self.settings.rect_len))

    def restart_game(self, mapdir): 
        #update visuals at the start of the game
        self.reset_img_source()
        self.snake.reset_img_source()

        #set config. This ultimately controls a lot of the functions of the game
        self.config = Config(parent=self, mapdir=mapdir)

        #set map
        self.map = Map(parent=self, mapdir=mapdir)

        #set snake
        self.snake.initialize(mapdir)
        self.snake_clone.init = False
        self.snake_clone.segmentd = []
        self.snake_clone.score = 0

        #set stawberry if it exists.
        self.strawberry.random_pos()
    
    def direction_to_int(self, direction):
        # Parses through the move_dict dictionary, transforming a direction (string) to an integer 
        direction_dict = {value : key for key,value in self.move_dict.items()}
        return direction_dict[direction]
        
    def do_move(self, move):
        move_dict = self.move_dict

        change_direction = move_dict[move]
        #translates the number back to the string again

        #  Direction is changed based off of move - and checks whether the snake is already moving in this direction
        if change_direction == 'right' and not self.snake.segments[1] == [1, 0]:
            self.snake.facing = change_direction
        if change_direction == 'left' and not self.snake.segments[1] == [-1, 0]:
            self.snake.facing = change_direction
        if change_direction == 'up' and not self.snake.segments[1] == [0, -1]:
            self.snake.facing = change_direction
        if change_direction == 'down' and not self.snake.segments[1] == [0, 1]:
            self.snake.facing = change_direction

        # Clone mechanics- if the snake moves, so does the clone
        if self.snake_clone.init:
            if change_direction == 'right' and not self.snake_clone.segments[1] == [1, 0]:
                self.snake_clone.facing = change_direction
            if change_direction == 'left' and not self.snake_clone.segments[1] == [-1, 0]:
                self.snake_clone.facing = change_direction
            if change_direction == 'up' and not self.snake_clone.segments[1] == [0, -1]:
                self.snake_clone.facing = change_direction
            if change_direction == 'down' and not self.snake_clone.segments[1] == [0, 1]:
                self.snake_clone.facing = change_direction
        
        #  The new states (the last tail segment and the changes to the body) of the snake (and its clone ) are returned  
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
        
        # If the snake hits itself, it dies 
        if self.snake.segments[0] in self.snake.segments[1:]:
            end = True
        return end
    
    def blit_score(self, color, screen):
        #  The score is blitted onto the screen
        font = pygame.font.Font(self.src + '/arial.ttf', 25)
        text = font.render('Score: ' + str(self.snake.score + self.snake_clone.score), True, color)
        screen.blit(text, (0, 0))

    def blit_map(self, rect_len, screen): 
        #  Blits the map onto the screen 
        x0 = int(self.config.settings["xOffset"])
        y0 = int(self.config.settings["yOffset"])

        # Parses through the multidimensional list of tiles stored in the map object(multidimensional due to row-column)
        for i in range(0, int(self.config.settings["mapX"])):
            for k in range(0, int(self.config.settings["mapY"])):
                
                tile = self.map.tiles[k][i]
                if tile.type == "Other":
                    pass

                # If the tile type is solid, this is blitted to the screen
                elif tile.type == "Solid":
                    screen.blit(self.tile_img, ((i + x0)*rect_len, (k + y0)*rect_len))
                    for j in range(4):
                        if tile.wrap_plate & (1 << j):
                            # If the tile has a wrap plate, this is blitted too
                            screen.blit(pygame.transform.rotate(self.wrap_img, j*90), ((i + x0)*rect_len, (k + y0)*rect_len))
                    for j in range(4):
                        if tile.pad_clone & (1 << j):
                            # If the tile has a pad plate, this is blitted 
                            screen.blit(pygame.transform.rotate(self.pad_img, j*90), ((i + x0)*rect_len, (k + y0)*rect_len))
                
                # An empty space tile is generated in the map if the tile is of type empty
                elif tile.type == "Empty": 
                    screen.blit(self.space_img, ((i + x0)*rect_len, (k + y0)*rect_len))
                else:
                    pass

    def blit_features(self, rect_len, screen):
        x0 = int(self.config.settings["xOffset"])
        y0 = int(self.config.settings["yOffset"])
        #Pressure plates
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
        for location in self.map.clones:
            x_f, y_f = (location[0] + x0)*rect_len, (location[1] + y0)*rect_len
            if self.snake_clone.init:
                screen.blit(self.clonea_img, (x_f, y_f))
            else:
                screen.blit(self.clone_img, (x_f, y_f))
            pygame.display.update(pygame.Rect(x_f, y_f, self.settings.rect_len, self.settings.rect_len))
