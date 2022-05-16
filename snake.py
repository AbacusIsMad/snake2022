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
        
        #the direction and coordinate form of the snake
        self.segments = []
        self.segmentd = []
        #score
        self.score = 0
        self.won = False
        #flags to control the animations
        self.animation = None
        self.animation_offset = 0
        self.tanimation = None
        self.tanimation_offset = 0

        #get data from map
        if self.clone == False:
            self.initialize()

        self.reset_img_source()


    def reset_img_source(self):
        clone = self.clone
        path = self.parent.src + "/styles/" + self.parent.style + "/images/"

        self.image_up = pygame.transform.scale(pygame.image.load(path + 'clone'*clone + 'head_up.bmp'), (self.parent.settings.rect_len, self.parent.settings.rect_len))
        self.tail_up = pygame.transform.scale(pygame.image.load(path + 'clone'*clone + 'tail_up.bmp'), (self.parent.settings.rect_len, self.parent.settings.rect_len))
        self.image_body_s = pygame.transform.scale(pygame.image.load(path + 'clone'*clone + 'body_s.bmp'), (self.parent.settings.rect_len, self.parent.settings.rect_len))
        self.image_body_c = pygame.transform.scale(pygame.image.load(path + 'clone'*clone + 'body_c.bmp'), (self.parent.settings.rect_len, self.parent.settings.rect_len))
        self.image_ups = [pygame.transform.scale(pygame.image.load(path + 'clone'*clone + 'head_up' + str(i) + '.bmp'), (self.parent.settings.rect_len, self.parent.settings.rect_len)) for i in range(5)]
        self.tail_ups = [pygame.transform.scale(pygame.image.load(path + 'clone'*clone + 'tail_up' + str(i) + '.bmp'), (self.parent.settings.rect_len, self.parent.settings.rect_len)) for i in range(5)]

        self.image_space = self.parent.space_img


    def initialize(self, mapdir=None):
        if mapdir is not None:
            if not self.parent.custom:
                with open(self.parent.src + "/" + mapdir + "/snake.txt", "r") as f:
                    t = f.readlines()
            else:
                with open(self.parent.srcreal + "/" + mapdir + "/snake.txt", "r") as f:
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
        self.reset_img_source()
        #lets start
        buf = []
        buf.append([self.segments[0][0], self.segments[0][1]])
        bufpos = [self.segments[0][0], self.segments[0][1]]
        
        print("starting clone")
        print(self.segments)
        print(self.segments[1:])
        x_max = int(self.parent.config.settings['mapX'])
        y_max = int(self.parent.config.settings['mapY'])
        #going thru the direction form one by one now, logic copied from below
        for direction in self.segments[1:]:
            print(direction)
            bufpos[0] += direction[0]
            bufpos[1] += direction[1]
            if self.parent.map.tiles[bufpos[1]][bufpos[0]].type == 'Solid':
                vector = ((not not direction[0])*25 + direction[0]*15 + (not not direction[1])*50\
                         - direction[1]*30)//10
                opposite = ((not not direction[0])*25 - direction[0]*15 + (not not direction[1])*50\
                         + direction[1]*30)//10
            
                if self.parent.map.tiles[bufpos[1]][bufpos[0]].wrap_plate & vector:
                    while not ((self.parent.map.tiles[bufpos[1]- direction[1]][bufpos[0] - direction[0]].wrap_plate\
                    & opposite) and \
                    self.parent.map.tiles[bufpos[1]- direction[1]][bufpos[0] - direction[0]].type == "Solid"):
                        if bufpos[0] - direction[0] < 1 or bufpos[0] - direction[0] > x_max - 2\
                        or bufpos[1] - direction[1] < 1 or bufpos[1] - direction[1] > y_max - 2:
                            return False
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
        pygame.display.update(pygame.Rect(x, y, size, size))


    def blit_head(self, loc, dire, screen, size, x0, y0, pad, phase):
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
            if phase == 0:
                screen.blit(pygame.transform.rotate(self.image_ups[4], rotation), (x, y))
        else:
            screen.blit(self.image_space, (x, y))
            screen.blit(pygame.transform.rotate(self.image_ups[phase], rotation), (x, y))
            if overlap is not None:
                screen.blit(overlap, (x, y))
        pygame.display.update(pygame.Rect(x, y, 30, 30))



    def blit_tail(self, x, y, screen, size, x0, y0, pad, phase):
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
            if phase == 0:
                screen.blit(pygame.transform.rotate(self.tail_ups[4], rotation), (x1, y1))
        else:
            screen.blit(self.image_space, (x1, y1))
            screen.blit(pygame.transform.rotate(self.tail_ups[phase], rotation), (x1, y1))
            if overlap is not None:
                screen.blit(overlap, (x1, y1))
        pygame.display.update(pygame.Rect(x1, y1, 30, 30))


    def blit(self, rect_len, screen, pad, phase):
        x0 = int(self.parent.config.settings["xOffset"])
        y0 = int(self.parent.config.settings["yOffset"])
        if phase == 0 and len(self.segments) > 2:
            for index, position in enumerate(self.segments[1:-1]):
                self.blit_body(self.segmentd[index + 1], position, self.segments[index + 2], screen, rect_len, x0, y0)

        if len(self.segments) > 1:
            self.blit_tail(self.segmentd[-1][0], self.segmentd[-1][1], screen, rect_len, x0, y0, pad, phase)
            self.blit_head(self.segmentd[0], self.segments[1], screen, rect_len, x0, y0, pad, phase)
        else:
            self.blit_head(self.segmentd[0], [1, 0], screen, rect_len, x0, y0, pad, phase)

    def animate(self, screen, images, x, y, rotation, overlap):
        #not connected with fps but i couldn't care less
        prev = datetime.datetime.now()
        attr = (images == self.tail_ups)*'t' + 'animation_offset'
        #for i in range(5):
        for i in range (getattr(self, attr), 5):
            i = getattr(self, attr)
            setattr(self, attr, i + 1)
            curr = datetime.datetime.now()
            diff = curr - prev
            screen.blit(self.image_space, (x, y))
            screen.blit(pygame.transform.rotate(images[i], rotation), (x, y))
            if overlap:
                screen.blit(overlap, (x, y))
            pygame.display.update(pygame.Rect(x, y, 30, 30))
            prev = datetime.datetime.now()
            #if it still doesnt work then reduce the time lol
            if diff.microseconds > 47000:
                pygame.time.delay(47 - max((diff.microseconds - 46000)*2, 5000)//1000)
            else:
                pygame.time.delay(47)


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

        x_max = int(self.parent.config.settings['mapX'])
        y_max = int(self.parent.config.settings['mapY'])

        #Pressure plates
        platesPressed = 0
        for location in self.parent.map.goals:
            if location in self.segmentd or location == headpos:
                platesPressed += 1
        if platesPressed == len(self.parent.map.goals) and len(self.parent.map.goals) != 0:
            self.parent.map.goalsMet = True
        altPlatesPressed = 0
        for location in self.parent.map.alt_goals:
            if location in self.segmentd or location == headpos:
                altPlatesPressed += 1
        if altPlatesPressed == len(self.parent.map.alt_goals) and len(self.parent.map.alt_goals) != 0:
            self.parent.map.alt_goalsMet = True
        
        dont_move = False
        if self.parent.map.tiles[headpos[1]][headpos[0]].type == 'Solid':
            #transforms direction to a power of 2 to compare
            vector = ((not not pos[0])*25 + pos[0]*15 + (not not pos[1])*50 - pos[1]*30)//10
            opposite = ((not not pos[0])*25 - pos[0]*15 + (not not pos[1])*50 + pos[1]*30)//10

            #actual comparison, bit mask black magic
            if self.parent.map.tiles[headpos[1]][headpos[0]].wrap_plate & vector:
                #go on that specific direction
                while not ((self.parent.map.tiles[headpos[1]- pos[1]][headpos[0] - pos[0]].wrap_plate & opposite)\
                and self.parent.map.tiles[headpos[1]- pos[1]][headpos[0] - pos[0]].type == "Solid"):
                    if headpos[0] - pos[0] < 1 or headpos[0] - pos[0] > x_max - 2\
                    or headpos[1]- pos[1] < 1 or headpos[1]- pos[1] > y_max - 2:
                        return -1, []

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

        
        #  If the snake is able to move, the headposition is re-inserted
        if not dont_move:
            self.segments.insert(0, headpos)
            self.segmentd.insert(0, headpos)

        last_tail = []
        #check for strawberry at head pos now.
        longer = False
        if self.segments[0] == self.parent.strawberry.position:
            if (self.parent.strawberry.times_called < int(self.parent.config.settings['maxS']) - 1)\
                or not int(self.parent.config.settings['maxS']):
                self.parent.strawberry.times_called += 1
                self.parent.strawberry.random_pos()
            else:
                self.parent.strawberry.position = [-100, -100]
            reward = 1
            longer = True
            self.score += 1
            self.eatSound()

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
        
        #Winning mechanics
        if (int(self.parent.config.settings['strawberry']) == 1) and (self.parent.snake_clone.score + self.parent.snake.score == 3):
            self.won = True
        if (int(self.parent.config.settings['strawberry']) == 0) and (self.parent.map.goalsMet):
            self.won = True
        if (int(self.parent.config.settings['strawberry']) == 2) and (self.parent.snake_clone.score + self.parent.snake.score == 10) and (self.parent.map.goalsMet):
            self.won = True
        
        
        return 0 + int(dont_move) + 2*int(longer), last_tail

    def eatSound(self):
            eat_sound = pygame.mixer.Sound('./sound/eat.wav')
            pygame.mixer.Sound.play(eat_sound)
