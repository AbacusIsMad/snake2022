import pygame


class Snake:
    def __init__(self, parent):
        self.game = parent
        self.image_up = pygame.image.load('./images/head_up.bmp')

        self.tail_up = pygame.image.load('./images/tail_up.bmp')
        
        self.image_body = pygame.image.load('./images/body.bmp')
        self.image_body_s = pygame.image.load('./images/body_s.bmp')
        self.image_body_c = pygame.image.load('./images/body_c.bmp')
        self.image_space = pygame.image.load('./images/space.bmp')
        
        #self.facing = "right"
        self.initialize()

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

    def blit_head(self, loc, dire, screen, size, x0, y0):
        x, y = (loc[0] + x0)*size, (loc[1] + y0)*size

        if dire == [0, 1]:
            screen.blit(self.image_up, (x, y))
        elif dire == [0, -1]:
            screen.blit(pygame.transform.rotate(self.image_up, 180), (x, y))  
        elif dire == [1, 0]:
            screen.blit(pygame.transform.rotate(self.image_up, 90), (x, y)) 
        else:
            screen.blit(pygame.transform.rotate(self.image_up, 270), (x, y))


    def blit_tail(self, x, y, screen, size, x0, y0):
        #tail_direction = [self.segments[-2][i] - self.segments[-1][i] for i in range(2)]
        tail_direction = self.segments[-1]
        x = (x + x0)*size
        y = (y + y0)*size
        print(tail_direction)
        print(self.segments)
        print(self.segmentd)
        #ls[big iterator][small iterator]
        
        if tail_direction == [0, 1]:
            screen.blit(self.tail_up, (x, y))
        elif tail_direction == [0, -1]:
            screen.blit(pygame.transform.rotate(self.tail_up, 180), (x, y))    
        elif tail_direction == [1, 0]:
            screen.blit(pygame.transform.rotate(self.tail_up, 90), (x, y))
        else:
            screen.blit(pygame.transform.rotate(self.tail_up, 270), (x, y)) 

    def blit(self, rect_len, screen, last=None):
        x0 = int(self.game.config.settings["xOffset"])
        y0 = int(self.game.config.settings["yOffset"])
        for index, position in enumerate(self.segments[1:-1]):
            self.blit_body(self.segmentd[index + 1], position, self.segments[index + 2], screen, rect_len, x0, y0)
        self.blit_tail(self.segmentd[-1][0], self.segmentd[-1][1], screen, rect_len, x0, y0)
        if isinstance(last, list):
            #this only outputs regular spaces, since the features in it get added later than the snake!
            screen.blit(self.image_space, ((last[0] + x0)*rect_len, (last[1] + y0)*rect_len))
        self.blit_head(self.segmentd[0], self.segments[1], screen, rect_len, x0, y0)
        
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
        if self.game.map.tiles[headpos[1]][headpos[0]].type == 'Solid':
            #transforms direction to a power of 2 to compare
            vector = ((not not pos[0])*25 + pos[0]*15 + (not not pos[1])*50 - pos[1]*30)//10
            opposite = ((not not pos[0])*25 - pos[0]*15 + (not not pos[1])*50 + pos[1]*30)//10
            print(vector, opposite)

            #actual comparison, bit mask black magic
            if self.game.map.tiles[headpos[1]][headpos[0]].wrap_plate & vector:
                print("yep")
                #go on that specific direction
                while not self.game.map.tiles[headpos[1]- pos[1]][headpos[0] - pos[0]].wrap_plate & opposite:
                    headpos[0] -= pos[0]
                    headpos[1] -= pos[1]
                #found it!
            elif self.game.map.tiles[headpos[1]][headpos[0]].pad_clone & vector:
                dont_move = True
            else:   
                return -1, []

        #check for body collision, if yes the snake doesnt move forward.
        if headpos in self.segmentd[:-1]:
            return -1, []


        if not dont_move:
            self.segments.insert(0, headpos)
            self.segmentd.insert(0, headpos)

        last_tail = []
        #check for strawberry at head pos now.
        if self.segments[0] == self.game.strawberry.position:
            self.game.strawberry.random_pos()
            reward = 1
            self.score += 1
            last_tail = [-1, -1]
        elif not dont_move:
            self.segments.pop()
            #unblit tail
            last_tail = self.segmentd.pop()
        if not dont_move:
            self.segments[1] = [-pos[0], -pos[1]]
        return 0, last_tail
