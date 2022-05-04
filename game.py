# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:19:25 2018

@author: zou
BingQi Ling
"""
import pygame, random
import numpy as np

class Settings:
    def __init__(self):
        self.width = 28
        self.height = 28
        self.rect_len = 15
        #size of game, and then size of individual grids. 
        # self.width = 52
        # self.height = 52
        # self.rect_len = 15

class Snake:
    def __init__(self):
        
        self.image_up = pygame.image.load('images/head_up.bmp')
        self.image_down = pygame.image.load('images/head_down.bmp')
        self.image_left = pygame.image.load('images/head_left.bmp')
        self.image_right = pygame.image.load('images/head_right.bmp')

        self.tail_up = pygame.image.load('images/tail_up.bmp')
        self.tail_down = pygame.image.load('images/tail_down.bmp')
        self.tail_left = pygame.image.load('images/tail_left.bmp')
        self.tail_right = pygame.image.load('images/tail_right.bmp')
            
        self.image_body = pygame.image.load('images/body.bmp')

        self.facing = "right"
        self.initialize()

    def initialize(self):
        #self.position = [6, 6]
        #self.segments = [[6 - i, 6] for i in range(3)]
        self.position = [6, 6]
        self.segments = [self.position, [-1, 0], [-1, 0]]
        #this is so wacky
        self.score = 0

    def blit_body(self, loc, cur, next, screen, size):
        x, y = loc[0]*size, loc[1]*size
        screen.blit(self.image_body, (x, y))
    '''
    def blit_head(self, x, y, screen):
        if self.facing == "up":
            screen.blit(self.image_up, (x, y))
        elif self.facing == "down":
            screen.blit(self.image_down, (x, y))  
        elif self.facing == "left":
            screen.blit(self.image_left, (x, y))  
        else:
            screen.blit(self.image_right, (x, y))  
    '''
    def blit_head(self, loc, dire, screen, size):
        x, y = loc[0]*size, loc[1]*size
        if dire == [0, 1]:
            screen.blit(self.image_up, (x, y))
        elif dire == [0, -1]:
            screen.blit(self.image_down, (x, y))  
        elif dire == [1, 0]:
            screen.blit(self.image_left, (x, y))  
        else:
            screen.blit(self.image_right, (x, y))     
    def blit_tail(self, x, y, screen, size):
        #tail_direction = [self.segments[-2][i] - self.segments[-1][i] for i in range(2)]
        tail_direction = self.segments[-1]
        x *= size
        y *= size
        print(tail_direction)
        print(self.segments)
        #ls[big iterator][small iterator]
        
        if tail_direction == [0, 1]:
            screen.blit(self.tail_up, (x, y))
        elif tail_direction == [0, -1]:
            screen.blit(self.tail_down, (x, y))  
        elif tail_direction == [1, 0]:
            screen.blit(self.tail_left, (x, y))  
        else:
            screen.blit(self.tail_right, (x, y))  
    '''
    def blit(self, rect_len, screen):
        self.blit_head(self.segments[0][0]*rect_len, self.segments[0][1]*rect_len, screen)                
        for index, position in enumerate(self.segments[1:-1]):
            #body_direction = []
            self.blit_body(position[0]*rect_len, position[1]*rect_len, screen)
        self.blit_tail(self.segments[-1][0]*rect_len, self.segments[-1][1]*rect_len, screen)  
    '''
    def blit(self, rect_len, screen):
        self.blit_head(self.segments[0], self.segments[1], screen, rect_len)
        location = self.segments[0]
        for index, position in enumerate(self.segments[1:-1]):
            #add wrapping logic later here
            location = [location[0] + position[0], location[1] + position[1]]
            self.blit_body(location, position, self.segments[index + 1], screen, rect_len)
        location = [location[0] + self.segments[-1][0], location[1] + self.segments[-1][1]]
        self.blit_tail(location[0], location[1], screen, rect_len)
          
    '''
    def update(self):
        if self.facing == 'right':
            self.position[0] += 1
        if self.facing == 'left':
            self.position[0] -= 1
        if self.facing == 'up':
            self.position[1] -= 1
        if self.facing == 'down':
            self.position[1] += 1
        self.segments.insert(0, list(self.position))
        #called by moving. ill look at it later.
    '''
    def update(self, straw):
        pos = [0, 0]
        if self.facing == 'right':
            pos[0] += 1
        if self.facing == 'left':
            pos[0] -= 1
        if self.facing == 'up':
            pos[1] -= 1
        if self.facing == 'down':
            pos[1] += 1
        #add wrap checking here later
        #wrap_check()
        #add collision check too
        #collision_check()
        self.segments.insert(0, [self.segments[0][0] + pos[0], self.segments[0][1] + pos[1]])
        #check for strawberry at head pos now.
        print("pos: ", straw)
        if self.segments[0] == straw.position:
            straw.random_pos(self)
            reward = 1
            self.score += 1
        else:
            self.segments.pop()
        self.segments[1] = [-pos[0], -pos[1]]

class Strawberry():
    def __init__(self, settings):
        self.settings = settings
        
        self.style = str(random.randint(1, 8))
        self.image = pygame.image.load('images/food' + str(self.style) + '.bmp')        
        self.initialize()
        
    def random_pos(self, snake):
        self.style = str(random.randint(1, 8))
        self.image = pygame.image.load('images/food' + str(self.style) + '.bmp')                
        
        self.position[0] = random.randint(0, self.settings.width-1)
        self.position[1] = random.randint(0, self.settings.height-1)

        self.position[0] = random.randint(9, 19)
        self.position[1] = random.randint(9, 19)
        #yo recursion?
        if self.position in snake.segments:
            self.random_pos(snake)

    def blit(self, screen):
        screen.blit(self.image, [p * self.settings.rect_len for p in self.position])
   
    def initialize(self):
        self.position = [15, 10]
      
        
class Game:
    """
    """
    def __init__(self):
        self.settings = Settings()
        self.snake = Snake()
        self.strawberry = Strawberry(self.settings)
        self.move_dict = {0 : 'up',
                          1 : 'down',
                          2 : 'left',
                          3 : 'right'}       
        
    def restart_game(self):
        self.snake.initialize()
        self.strawberry.initialize()

    def current_state(self):         
        state = np.zeros((self.settings.width+2, self.settings.height+2, 2))
        expand = [[0, 1], [0, -1], [-1, 0], [1, 0], [0, 2], [0, -2], [-2, 0], [2, 0]]
        
        for position in self.snake.segments:
            state[position[1], position[0], 0] = 1
        
        state[:, :, 1] = -0.5        

        state[self.strawberry.position[1], self.strawberry.position[0], 1] = 0.5
        for d in expand:
            state[self.strawberry.position[1]+d[0], self.strawberry.position[0]+d[1], 1] = 0.5
        return state
    
    def direction_to_int(self, direction):
        direction_dict = {value : key for key,value in self.move_dict.items()}
        return direction_dict[direction]
        
    def do_move(self, move, pos):
        move_dict = self.move_dict

        change_direction = move_dict[move]
        #this translates the number back to the string again. Kinda redundant tbh.
        
        if change_direction == 'right' and not self.snake.facing == 'left':
            self.snake.facing = change_direction
        if change_direction == 'left' and not self.snake.facing == 'right':
            self.snake.facing = change_direction
        if change_direction == 'up' and not self.snake.facing == 'down':
            self.snake.facing = change_direction
        if change_direction == 'down' and not self.snake.facing == 'up':
            self.snake.facing = change_direction

        self.snake.update(pos)
        #moves maybe? Yes.
        
        if self.snake.position == self.strawberry.position:
            self.strawberry.random_pos(self.snake)
            reward = 1
            self.snake.score += 1
        else:
            #self.snake.segments.pop()
            reward = 0
        #point and eating        
        
        if self.game_end():
            return -1
                    
        return reward
    
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
    
    def blit_score(self, color, screen):
        font = pygame.font.SysFont(None, 25)
        text = font.render('Score: ' + str(self.snake.score), True, color)
        screen.blit(text, (0, 0))

    def blit_border(self, screen):
        # using one of the food tiles as a wall for the time being 
        # no changes yet to make it so that the player dies when it hits the walls- 
        # this would be better implemented with the use of a map class
        for i in range(1, 28): 
            screen.blit(pygame.image.load('images/food8.bmp'), (0, 15*i))
            screen.blit(pygame.image.load('images/food8.bmp'), (15*i, 15))
            screen.blit(pygame.image.load('images/food8.bmp'), (405, 15*i))
            screen.blit(pygame.image.load('images/food8.bmp'), (15*i, 405))

# class Map() :
#     def __init__(self):
#         
# ideally, this map oculd be loaded in from like a text file or something...., so that players could make their own levels? 


        
