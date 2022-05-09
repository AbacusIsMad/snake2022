import pygame
import copy
import threading
import time
import datetime


class Snake:
    def __init__(self, parent, clone=False):
        self.parent = parent
        self.clone = clone
        self.init = False
        
        #self.facing = "right"
        self.segments = []
        self.segmentd = []
        self.score = 0
        if self.clone == False:
            self.initialize()
        self.reset_img_source()

    def reset_img_source(self):
        clone = self.clone
        path = "./styles/" + self.parent.style + "/images/"
        self.image_up = pygame.transform.scale(pygame.image.load(path + 'clone'*clone + 'head_up.bmp'), (self.parent.settings.rect_len, self.parent.settings.rect_len))
        self.tail_up = pygame.transform.scale(pygame.image.load(path + 'clone'*clone + 'tail_up.bmp'), (self.parent.settings.rect_len, self.parent.settings.rect_len))
        self.image_body_s = pygame.transform.scale(pygame.image.load(path + 'clone'*clone + 'body_s.bmp'), (self.parent.settings.rect_len, self.parent.settings.rect_len))
        self.image_body_c = pygame.transform.scale(pygame.image.load(path + 'clone'*clone + 'body_c.bmp'), (self.parent.settings.rect_len, self.parent.settings.rect_len))
        self.image_ups = [pygame.transform.scale(pygame.image.load(path + 'clone'*clone + 'head_up' + str(i) + '.bmp'), (self.parent.settings.rect_len, self.parent.settings.rect_len)) for i in range(5)]
        self.tail_ups = [pygame.transform.scale(pygame.image.load(path + 'clone'*clone + 'tail_up' + str(i) + '.bmp'), (self.parent.settings.rect_len, self.parent.settings.rect_len)) for i in range(5)]

        self.image_space = self.parent.space_img


    def initialize(self, mapdir=None):
        if mapdir is not None:
            with open("./levels/" + mapdir + "/snake.txt", "r") as f:
                t = f.readlines()
            self.segments = []
            self.segmentd = []
            for pair in t:
                mid = pair[:-1].split(",")
                self.segments.append([int(mid[0]), int(mid[1])])
                self.segmentd.append([int(mid[2]), int(mid[3])])
            dire = self.segments[1]
            if dire == [-1, 0]:
                self.facing = "right"
            if dire == [0, 1]:
                self.facing = "up"
            if dire == [1, 0]:
                self.facing = "left"
            if dire == [0, -1]:
                self.facing = "down"
        else: #default to fallback to
            self.segments = [[6, 6], [-1, 0], [-1, 0], [-1, 0]]
            self.segmentd = [[6, 6], [5, 6], [4, 6], [3, 6]]
            self.facing = "right"
        self.score = 0
        self.init = True

    def dir_to_pos(self):
        #lets start
        buf = []
        buf.append([self.segments[0][0], self.segments[0][1]])
        bufpos = [self.segments[0][0], self.segments[0][1]]
        
        print("starting clone")
        print(self.segments)
        print(self.segments[1:])
        #going thru the direction form one by one now, logic copied from below
        for direction in self.segments[1:]:
            print(direction)
            bufpos[0] += direction[0]
            bufpos[1] += direction[1]
            if self.parent.map.tiles[bufpos[1]][bufpos[0]].type == 'Solid':
                vector = ((not not direction[0])*25 + direction[0]*15 + (not not direction[1])*50 - direction[1]*30)//10
                opposite = ((not not direction[0])*25 - direction[0]*15 + (not not direction[1])*50 + direction[1]*30)//10
            
                if self.parent.map.tiles[bufpos[1]][bufpos[0]].wrap_plate & vector:
                    while not self.parent.map.tiles[bufpos[1]- direction[1]][bufpos[0] - direction[0]].wrap_plate & opposite:
                        bufpos[0] -= direction[0]
                        bufpos[1] -= direction[1]
                else:
                    #solid block somehow
                    return False
            buf.append([bufpos[0], bufpos[1]])
        print(buf)
        self.segmentd = copy.deepcopy(buf)
        print("ending clone")
        return True

    def blit_body(self, loc, cur, next, screen, size, x0, y0):
        x, y = (loc[0] + x0)*size, (loc[1] + y0)*size
        direction = [2*cur[0] + next[0], 2*cur[1] + next[1]]
        if direction[0] == 0:
            screen.blit(self.image_body_s, (x, y))
        elif direction[1] == 0:
            screen.blit(pygame.transform.rotate(self.image_body_s, 90), (x, y))
        elif direction == [2, 1] or direction == [-1, -2]:
            screen.blit(self.image_body_c, (x, y))
        elif direction == [-2, 1] or direction == [1, -2]:
            screen.blit(pygame.transform.rotate(self.image_body_c, 90), (x, y))
        elif direction == [-2, -1] or direction == [1, 2]:
            screen.blit(pygame.transform.rotate(self.image_body_c, 180), (x, y))
        elif direction == [2, -1] or direction == [-1, 2]:
            screen.blit(pygame.transform.rotate(self.image_body_c, 270), (x, y))
        else:
            screen.blit(self.image_right, (x, y))  

    def blit_head(self, loc, dire, screen, size, x0, y0, pad):
        x, y = (loc[0] + x0)*size, (loc[1] + y0)*size
        #plates only have one varient, due to them being stepped on.
        overlap = None
        tile = self.parent.map.tiles[loc[1]][loc[0]]
        if tile.wrap_plate == 1:
            overlap = self.parent.platea_img
        elif tile.wrap_plate == 2:
            overlap = self.parent.platea_alt_img
        elif tile.pad_clone:
            overlap = self.parent.clonea_img

        if dire == [0, 1]:
            rotation = 0
        elif dire == [0, -1]:
            rotation = 180  
        elif dire == [1, 0]:
            rotation = 90
        else:
            rotation = 270
        if pad == 1:
            screen.blit(pygame.transform.rotate(self.image_ups[4], rotation), (x, y))
        else:
            threading.Timer(0, self.animate, args=(screen, self.image_ups, x, y, rotation, overlap)).start()

    def blit_tail(self, x, y, screen, size, x0, y0, pad):
        tail_direction = self.segments[-1]
        x1 = (x + x0)*size
        y1 = (y + y0)*size
        overlap = None
        tile = self.parent.map.tiles[y][x]
        if tile.wrap_plate == 1:
            overlap = self.parent.platea_img
        elif tile.wrap_plate == 2:
            overlap = self.parent.platea_alt_img
        elif tile.pad_clone:
            overlap = self.parent.clonea_img

        if tail_direction == [0, 1]:
            rotation = 0
        elif tail_direction == [0, -1]:
            rotation = 180    
        elif tail_direction == [1, 0]:
            rotation = 90
        else:
            rotation = 270
        if pad:
            screen.blit(pygame.transform.rotate(self.tail_ups[4], rotation), (x1, y1))
        else:
            threading.Timer(0, self.animate, args=(screen, self.tail_ups, x1, y1, rotation, overlap)).start()
        '''
        if tail_direction == [0, 1]:
            screen.blit(self.tail_up, (x, y))
        elif tail_direction == [0, -1]:
            screen.blit(pygame.transform.rotate(self.tail_up, 180), (x, y))    
        elif tail_direction == [1, 0]:
            screen.blit(pygame.transform.rotate(self.tail_up, 90), (x, y))
        else:
            screen.blit(pygame.transform.rotate(self.tail_up, 270), (x, y)) 
        '''

    def blit(self, rect_len, screen, pad,last=None):
        x0 = int(self.parent.config.settings["xOffset"])
        y0 = int(self.parent.config.settings["yOffset"])
        for index, position in enumerate(self.segments[1:-1]):
            self.blit_body(self.segmentd[index + 1], position, self.segments[index + 2], screen, rect_len, x0, y0)
        self.blit_tail(self.segmentd[-1][0], self.segmentd[-1][1], screen, rect_len, x0, y0, pad)
        if isinstance(last, list) and last:
            #this only outputs regular spaces, since the features in it get added later than the snake!
            screen.blit(self.image_space, ((last[0] + x0)*rect_len, (last[1] + y0)*rect_len))
        self.blit_head(self.segmentd[0], self.segments[1], screen, rect_len, x0, y0, pad)
    
    def animate(self, screen, images, x, y, rotation, overlap):
        #not connected with fps but i couldn't care less
        prev = datetime.datetime.now()
        for i in range(5):
            curr = datetime.datetime.now()
            diff = curr - prev
            screen.blit(self.image_space, (x, y))
            screen.blit(pygame.transform.rotate(images[i], rotation), (x, y))
            if overlap:
                screen.blit(overlap, (x, y))
            pygame.display.update(pygame.Rect(x, y, 30, 30))
            prev = datetime.datetime.now()
            #if it still doesnt work then reduce the time lol
            if diff.microseconds > 48000:
                #print("too long")
                pygame.time.delay(48 - ((diff.microseconds - 48000)*2)//1000)
            else:
                pygame.time.delay(48)



    def update(self):
        pos = [0, 0]
        if self.facing == 'right':
            pos[0] += 1
        if self.facing == 'left':
            pos[0] -= 1
        if self.facing == 'up':
            pos[1] -= 1
        if self.facing == 'down':
            pos[1] += 1
        headpos = [self.segments[0][0] + pos[0], self.segments[0][1] + pos[1]]
        #convert headpos for wrap or solid tile collision

        
        dont_move = False
        if self.parent.map.tiles[headpos[1]][headpos[0]].type == 'Solid':
            #transforms direction to a power of 2 to compare
            vector = ((not not pos[0])*25 + pos[0]*15 + (not not pos[1])*50 - pos[1]*30)//10
            opposite = ((not not pos[0])*25 - pos[0]*15 + (not not pos[1])*50 + pos[1]*30)//10

            #actual comparison, bit mask black magic
            if self.parent.map.tiles[headpos[1]][headpos[0]].wrap_plate & vector:
                #go on that specific direction
                while not self.parent.map.tiles[headpos[1]- pos[1]][headpos[0] - pos[0]].wrap_plate & opposite:
                    headpos[0] -= pos[0]
                    headpos[1] -= pos[1]
                #found it!
            elif self.parent.map.tiles[headpos[1]][headpos[0]].pad_clone & vector:
                dont_move = True
            else:   
                return -1, []
        
        print(self.segments)
        print(self.segmentd, "\n")


        #check for body collision, if yes the snake doesnt move forward.
        if headpos in self.segmentd[:-1]:
            return -1, []


        if not dont_move:
            self.segments.insert(0, headpos)
            self.segmentd.insert(0, headpos)

        last_tail = []
        #check for strawberry at head pos now.
        longer = False
        if self.segments[0] == self.parent.strawberry.position:
            self.parent.strawberry.random_pos()
            reward = 1
            longer = True
            self.score += 1

        #padded mechanics
        elif not dont_move:
            self.segments.pop()
            #unblit tail
            last_tail = self.segmentd.pop()
            print(last_tail)
        if not dont_move:
            self.segments[1] = [-pos[0], -pos[1]]

        #clone mechanics
        if (not self.parent.snake_clone.init) and (headpos in self.parent.map.clones):
            #setup clone
            clone_pos = self.parent.map.clones[(self.parent.map.clones.index(headpos) + 1) % 2]
            self.parent.snake_clone.facing = self.facing
            self.parent.snake_clone.segments = copy.deepcopy(self.segments)
            self.parent.snake_clone.segments[0] = [clone_pos[0], clone_pos[1]]
            if not self.parent.snake_clone.dir_to_pos():
                return -2, []
            self.parent.snake_clone.init = True
        return 0 + int(dont_move) + 2*int(longer), last_tail
