import pygame
from pygame.locals import *

import os
import operator
import time

from game import Game
from snake import Snake
from map import Map, Tile
from config import Config

black = pygame.Color(0, 0, 0)
dark_gray = pygame.Color(20, 20, 20)
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



def yes():
    return True

def text_objects(text, font, color=black):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_display(text, screen, x, y, color=black, size=50):
    large_text = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + '/arial.ttf', size)
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = (x, y)
    screen.blit(text_surf, text_rect)
    pygame.display.update()

#def button(msg, x, y, w, h, inactive_color, active_color, action=None, parameter=None):
def button(msg, screen, x, y, w, h, inactive_color, active_color, action, **kwargs):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            if kwargs:
                return action(**kwargs)
            else:
                return action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))

    #placeholder
    pressed = 0
    smallText = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + '/arial.ttf', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = (x + (w / 2), y + (h / 2))
    screen.blit(TextSurf, TextRect)
    return pressed



warning_dict = {'name' : 'name must not already exist',
                'mapX': 'must be integer between 1-30',
                'mapY': 'must be integer between 1-30',
                'xOffset': 'must be integer between 0-10',
                'yOffset': 'must be integer between 4-10',
                'maxS': 'must be integer between 0-60'}



comparison_dict = {'name' : lambda line: line.strip() not in os.listdir(os.path.abspath('.') + '/snakeData/levels')\
                        and len(line) > 0,
                    'mapX' : lambda value: int(value) <= 30 and int(value) >= 1,
                    'mapY' : lambda value: int(value) <= 30 and int(value) >= 1,
                    'xOffset' : lambda value: int(value) <= 10 and int(value) >= 0,
                    'yOffset' : lambda value: int(value) <= 10 and int(value) >= 4,
                    'maxS' : lambda value: int(value) <= 60 and int(value) >= 0,
                    'strawberry': lambda empty : True}


class InputBox:

    def __init__(self, game, x, y, w, h, datatype=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.datatype = datatype
        self.game = game

        self.text = ''
        self.font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + '/arial.ttf', 20)
        self.txt_surface = self.font.render(self.text, True, white)
        self.color = red
        self.active = False

        self.font_warning = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + '/arial.ttf', 15)
        self.text_warning = ''
        self.txt_warning_surface = self.font_warning.render(self.text_warning, True, red)
        self.active_warning = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                #change colour lol
                self.active = True
                self.active_warning = False
                self.text_warning = ''
            else:
                #display warning if necessary. I need to search up this part.
                try:
                    if not comparison_dict[self.datatype](self.text):
                        raise ValueError
                except Exception:
                    if self.text:
                        self.text_warning = warning_dict[self.datatype]
                        self.active_warning = True
                
                self.active = False

            # Change the current color of the input box.
            if self.active:
                self.color = green
            elif self.active_warning:
                self.color = red
            elif self.text:
                self.color = green
            else:
                self.color = red


        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                    try:
                        if not comparison_dict[self.datatype](self.text):
                            raise ValueError
                    except Exception:
                        if self.text:
                            self.text_warning = warning_dict[self.datatype]
                            self.active_warning = True

                    if self.active_warning:
                        self.color = red
                    elif self.text:
                        self.color = green
                    else:
                        self.color = red


                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text) <= 15:
                    self.text += event.unicode
                # Re-render the text.
        self.txt_surface = self.font.render(self.text, True, white)
        self.txt_warning_surface = self.font_warning.render(self.text_warning, True, red)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        screen.blit(self.txt_warning_surface, (self.rect.x + 5, self.rect.y - 30))
        pygame.draw.rect(screen, self.color, self.rect, 2)





def level_maker(game=None):
    screen = game.screen
    screen.fill(white)

    game.custom = True
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if button('New level', screen, 370, 150, 160, 40, red, bright_red, new_level, game=game):
            screen.fill(white)
            break

        if button('Edit existing level', screen, 370, 300, 160, 40, red, bright_red, edit_level, game=game):
            screen.fill(white)
            break

        if button('Back', screen, 410, 600, 80, 40, red, bright_red, yes):
            screen.fill(white)
            break

        pygame.display.update()
        pygame.time.Clock().tick(15)



def new_level(game=None):
    screen = game.screen
    

    font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + '/arial.ttf', 30)
    active = False

    name_box = InputBox(game, 350, 100, 200, 32, 'name')
    x_size_box = InputBox(game, 250, 300, 140, 32, 'mapX')
    y_size_box = InputBox(game, 450, 300, 140, 32, 'mapY')
    x_offset_box = InputBox(game, 250, 400, 140, 32, 'xOffset')
    y_offset_box = InputBox(game, 450, 400, 140, 32, 'yOffset')
    max_straw_box = InputBox(game, 350, 500, 140, 32, 'maxS')
    boxes = [name_box, x_size_box, y_size_box, x_offset_box, y_offset_box, max_straw_box]

    mode = 1
    mode_txt = ['Plates', 'Strawberry', 'Hybrid']
    mode_c = [green, yellow, blue]
    mode_ca = [bright_green, bright_yellow, bright_blue]

    cooldown = 4

    while True:
        screen.fill(black)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            for box in boxes:
                box.handle_event(event)

        for box in boxes:
            box.draw(screen)

        if button(mode_txt[mode], screen, 390, 450, 120, 40, mode_c[mode], mode_ca[mode], yes) and cooldown == 4:
            mode = (mode + 1) % 3
            cooldown = 0
        #to prevent multi clicks
        if cooldown < 4:
            cooldown += 1
        

        #progress onto next stage, but before that let's put stuff into an object
        if button('Continue', screen, 410, 600, 80, 40, blue, bright_blue, yes):
            compare = dict((key.datatype, key.text) for key in boxes)
            compare['strawberry'] = mode
            for ty in compare:
                try:
                    if not comparison_dict[ty](compare[ty]):
                        break
                except Exception:
                        break
            else:
                if create_level(config=compare, game=game):
                    #finalise a bunch of stuff
                    return 1
                else:
                    pass


        if button('Back', screen, 410, 700, 80, 40, red, bright_red, yes):
            screen.fill(white)
            break        
        

        pygame.display.update()
        pygame.time.delay(30)


def edit_level(game=None):
    screen = game.screen
    screen.fill(black)


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        for idx, d in enumerate(sorted(os.listdir(game.srcreal + '/snakeData/levels'))):
            if button(d, screen, 520 + 160*(idx%2), 220 + 50*(idx//2), 150, 40, yellow, bright_yellow, \
                    create_level, game=game, edit=True, mapdir=d):
                screen.fill(white)
                return 1

        if button('Back', screen, 410, 800, 80, 40, red, bright_red, yes):
            screen.fill(white)
            break

        pygame.display.update()
        pygame.time.delay(30)





def blit_cursor(image, pointer, game):
    screen = game.screen
    x0 = int(game.config.settings["xOffset"])
    y0 = int(game.config.settings["yOffset"])
    x_f, y_f = (pointer[0] + x0)*game.settings.rect_len, (pointer[1] + y0)*game.settings.rect_len
    screen.blit(image, (x_f, y_f))


def magic(game, start_pos, direction):
    vector = ((not not direction[0])*25 + direction[0]*15 + (not not direction[1])*50 - direction[1]*30)//10
    opposite = ((not not direction[0])*25 - direction[0]*15 + (not not direction[1])*50 + direction[1]*30)//10
    x_max = int(game.config.settings['mapX'])
    y_max = int(game.config.settings['mapX'])

    analysis = start_pos.copy()
    analysis = [analysis[0] + direction[0], analysis[1] + direction[1]]

    #illegal movement
    if analysis[0] < 0 or analysis[0] > x_max - 1\
        or analysis[1] < 0 or analysis[1] > y_max - 1:
        return None

    if game.map.tiles[analysis[1]][analysis[0]].type == "Solid":
        if not game.map.tiles[analysis[1]][analysis[0]].wrap_plate & vector:
            return None
        while not ((game.map.tiles[analysis[1] - direction[1]][analysis[0] - direction[0]].wrap_plate & opposite)\
        and game.map.tiles[analysis[1] - direction[1]][analysis[0] - direction[0]].type == "Solid"):
            #needs to be a small buffer or illegal index happens
            if analysis[0] - direction[0] < 1 or analysis[0] - direction[0] > x_max - 2\
            or analysis[1] - direction[1] < 1 or analysis[1] - direction[1] > y_max - 2:
                return None

            analysis[0] -= direction[0]
            analysis[1] -= direction[1]

    #still a solid block somehow
    if game.map.tiles[analysis[1]][analysis[0]].type == "Solid"\
    or game.map.tiles[analysis[1]][analysis[0]].type == "Other":
        return None

    #cannot crash onto itself
    if analysis in game.snake.segmentd:
        return None

    #cannot be on clone plate
    if game.map.tiles[analysis[1]][analysis[0]].pad_clone:
        return None

    return analysis





def create_level(config=None, game=None, edit=False, mapdir=None):

    #setup config:
    if edit:
        game.config = Config(parent=game, mapdir=mapdir)
    else:
        game.config = Config(parent=game)
        game.config.settings = config
    print(game.config.settings)
   
    #setup blank map (of course this will remove past progress)
    if edit:
        game.map = Map(parent=game, mapdir=mapdir)

    else:
        game.map = Map(parent=game)
        game.map.tiles = [[Tile(game.map, "Other", i, j, 0, 0) for i in range(int(config['mapX']))]\
                     for j in range(int(config['mapY']))]


 
    screen = game.screen
    #where to move stuff
    pointer = [0, 0]
    x_max = int(game.config.settings['mapX'])
    y_max = int(game.config.settings['mapY'])
    x_offset = int(game.config.settings['xOffset'])
    y_offset = int(game.config.settings['yOffset'])

    #visualising the borsers of the map
    rect_len = game.settings.rect_len
    working_rect = pygame.Rect(x_offset*rect_len, y_offset*rect_len,\
                                x_max*rect_len, y_max*rect_len)

    #extra images
    pointer_img = pygame.transform.scale(pygame.image.load(game.src + '/styles/' + game.style \
                        + '/images/pointer.bmp'), (game.settings.rect_len, game.settings.rect_len))
    pointer_img2 = pygame.transform.scale(pygame.image.load(game.src + '/styles/' + game.style \
                        + '/images/pointer2.bmp'), (game.settings.rect_len, game.settings.rect_len))
    potential_img = pygame.transform.scale(pygame.image.load(game.src + '/styles/' + game.style \
                        + '/images/potential.bmp'), (game.settings.rect_len, game.settings.rect_len))
    
    #theres an option to switch between drawing map and drawing snake
    snake_mode = False
    #indicators to show where the snake can be placed: 0 means not potential
    potential_pos = [0, 0, 0, 0]

    #setup snake
    if edit:
        game.snake.initialize(mapdir=("snakeData/levels/" + mapdir))
    else:
        game.snake.segments, game.snake.segmentd = [], []


    #blit initial state
    screen.fill(black)
    pygame.draw.rect(screen, dark_gray, working_rect)
    game.blit_map(game.settings.rect_len, screen, developer=True)
    if len(game.snake.segments):
        game.snake.blit(rect_len, screen, 1, 0)
    game.blit_features(rect_len, screen)

    blit_cursor(pointer_img, pointer, game)

    message_display("Position (0, 0), tile type Other", screen, 200, 30, white, 20)

    pygame.display.update()

    something_changed = 0
    #start loop. This is very much like game_loop
    while True:
        #switch between big types
        pygame.event.pump()
        something_changed = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            elif event.type == KEYDOWN:
                #moving the cursor around
                if event.key == K_RIGHT or event.key == ord('d'):
                    pointer[0] += 1
                    if pointer[0] > x_max - 1: 
                        pointer[0] = x_max - 1
                    something_changed = 1
                if event.key == K_LEFT or event.key == ord('a'):
                    pointer[0] -= 1
                    if pointer[0] < 0: 
                        pointer[0] = 0
                    something_changed = 1
                if event.key == K_UP or event.key == ord('w'):
                    pointer[1] -= 1
                    if pointer[1] < 0: 
                        pointer[1] = 0
                    something_changed = 1
                if event.key == K_DOWN or event.key == ord('s'):
                    pointer[1] += 1
                    if pointer[1] > y_max - 1: 
                        pointer[1] = y_max - 1
                    something_changed = 1

                #F: toggle between map and snake mode
                if event.key == ord('f'):
                    snake_mode = not snake_mode
                    something_changed = 1

                #Z: change tile type OR add/remove snake segment
                if event.key == ord('z'):
                    tile = game.map.tiles[pointer[1]][pointer[0]]
                    if snake_mode:
                        #first segment, anywhere except clone plate
                        if len(game.snake.segmentd) == 0 and tile.type == "Empty" and not tile.pad_clone:
                            game.snake.segments.append([pointer[0], pointer[1]])
                            game.snake.segmentd.append([pointer[0], pointer[1]])
                        elif len(game.snake.segmentd):
                            #look at potentials
                            if pointer in game.snake.segmentd: #truncates snake
                                index = game.snake.segmentd.index(pointer)
                                game.snake.segments = game.snake.segments[:index]
                                game.snake.segmentd = game.snake.segmentd[:index]
                            elif pointer in potential_pos: #add snake
                                game.snake.segmentd.append([pointer[0], pointer[1]])
                                index = potential_pos.index(pointer)
                                print("index:", index)
                                if index == 0:
                                    add = [1, 0]
                                elif index == 1:
                                    add = [0, -1]
                                elif index == 2:
                                    add = [-1, 0]
                                else:
                                    add = [0, 1]
                                game.snake.segments.append([add[0], add[1]])

                        print(game.snake.segments)
                        print(game.snake.segmentd)

                    #extra protection. You can only change tile type if no snake on top
                    elif pointer not in game.snake.segmentd:
                        if tile.type == "Other":
                            tile.type = "Empty"
                            tile.true_empty = False
                        elif tile.type == "Empty":
                            if pointer in game.map.clones:
                                game.map.clones.remove(pointer)
                            if pointer in game.map.goals:
                                game.map.goals.remove(pointer)
                            if pointer in game.map.alt_goals:
                                game.map.alt_goals.remove(pointer)
                            tile.type = "Solid"
                            tile.wrap_plate = 0
                            tile.pad_clone = 0
                            tile.true_empty = False
                        elif tile.type == "Solid":
                            tile.type = "Other"
                            tile.wrap_plate = 0
                            tile.pad_clone = 0

                    something_changed = 1

                #X: change tile subtype, behaviour maintained in snake mode, make sure to remove snake if bad
                #Solid: None, wrap, pad
                #empty: None, true_empty, plate, alt_plate, clone (limit number)
                if event.key == ord('x'):
                    tile = game.map.tiles[pointer[1]][pointer[0]]
                    if tile.type == "Solid":
                        if tile.wrap_plate % 2:
                            tile.wrap_plate -= tile.wrap_plate & 1
                            tile.pad_clone = tile.pad_clone | 1
                        elif tile.pad_clone % 2:
                            tile.wrap_plate -= tile.wrap_plate & 1
                            tile.pad_clone -= tile.pad_clone & 1
                        else: #nothing
                            tile.pad_clone -= tile.pad_clone & 1
                            tile.wrap_plate = tile.wrap_plate | 1

                    elif tile.type == "Empty":
                        if tile.wrap_plate == 1:
                            print("alt_plate!")
                            game.map.goals.remove(pointer)
                            game.map.alt_goals.append([pointer[0], pointer[1]])
                            tile.wrap_plate = 2
                        elif tile.wrap_plate == 2:
                            print("clone/space!")
                            game.map.alt_goals.remove(pointer)
                            if pointer not in game.snake.segmentd\
                            and len(game.map.clones) < 2:
                                tile.wrap_plate = 0
                                tile.pad_clone = 1
                                game.map.clones.append([pointer[0], pointer[1]])
                            else:
                                tile.wrap_plate = 0
                                tile.pad_clone = 0
                        elif tile.pad_clone:
                            print("empty!")
                            tile.wrap_plate = 0
                            tile.pad_clone = 0
                            game.map.clones.remove(pointer)
                        elif not (tile.wrap_plate or tile.pad_clone or tile.true_empty):
                            print("true empty!")
                            tile.true_empty = True
                        elif tile.true_empty:
                            print("plate!")
                            tile.true_empty = False
                            game.map.goals.append([pointer[0], pointer[1]])
                            tile.wrap_plate = 1                 

                    something_changed = 1
                #C: rotate, behaviour maintained in snake mode
                if event.key == ord('c'):
                    tile = game.map.tiles[pointer[1]][pointer[0]]
                    if tile.type == "Solid":
                        tile.wrap_plate <<= 1
                        tile.wrap_plate = tile.wrap_plate % 16 + tile.wrap_plate // 16
                        tile.pad_clone <<= 1
                        tile.pad_clone = tile.pad_clone % 16 + tile.pad_clone // 16
                    something_changed = 1

        



        if something_changed:
            
            if game.snake.segmentd: #recalculate snake
                length = len(game.snake.segmentd) - 1
                game.snake.segmentd = game.snake.segmentd[:1]
                for i in range(length):
                    sus = magic(game, game.snake.segmentd[i], game.snake.segments[i + 1])
                    if sus is None:
                        game.snake.segments = game.snake.segments[:i+1]
                        game.snake.segmentd = game.snake.segmentd[:i+1]
                        break
                    #rearrange snake if necessary
                    game.snake.segmentd.append([sus[0], sus[1]])


                propagate = game.snake.segmentd[-1]
                start = [0, 1]
                for i in range(4): #to the right, anticlockwise
                    start = [start[1], -start[0]] #90 deg rotation like a matrix
                    new = magic(game, propagate, start)
                    if new:
                        potential_pos[i] = new.copy()
                    else:
                        potential_pos[i] = 0

                print(potential_pos)

            #screen.fill(black)
            #draw descriptive text
            pygame.draw.rect(screen, black, pygame.Rect(0, 0, 400, 100))
            tile = game.map.tiles[pointer[1]][pointer[0]]

            msg = "Position ({}, {}), tile type {}".format(tile.x, tile.y, tile.type)
            if tile.type == "Solid":
                extra_information = "wrap value: {}, pad value: {}".format(tile.wrap_plate, tile.pad_clone)
            if tile.type == "Empty":
                extra_information = "plate value: {}, true empty: {}".format(tile.wrap_plate + tile.pad_clone*3,\
                                                                        tile.true_empty)
            else:
                extra_information = ""
            message_display(msg, screen, 200, 30, white, 20)
            message_display(extra_information, screen, 200, 60, white, 20)


            pygame.draw.rect(screen, dark_gray, working_rect)
            game.blit_map(rect_len, screen, developer=True)
            #snake blitting has more restrictions now. be careful!
            if len(game.snake.segments):
                game.snake.blit(rect_len, screen, 1, 0)

            if snake_mode:
                blit_cursor(pointer_img2, pointer, game)
            else:
                blit_cursor(pointer_img, pointer, game)

            game.blit_features(rect_len, screen)

            #blit potential spots
            if snake_mode:
                if not game.snake.segmentd:
                    potential_pos = [0, 0, 0, 0]
                for i in range(4):
                    if potential_pos[i]:
                        screen.blit(potential_img, ((potential_pos[i][0] + x_offset)*rect_len,\
                            (potential_pos[i][1] + y_offset)*rect_len))

            pygame.display.update()
            pygame.time.delay(30)

        #yeets progress and just doesn't do anything
        if button('Back', screen, 400, 20, 80, 40, red, bright_red, yes):
            screen.fill(black)
            pygame.display.update()
            return 0



        if button('Save', screen, 500, 20, 80, 40, blue, bright_blue, yes):
            pygame.draw.rect(screen, black, pygame.Rect(500, 0, 400, 100))
            invalid = False
            #scan for snake
            if len(game.snake.segments) < 3:
                message_display('Snake too short!', screen, 650, 20, white, 15)
                invalid = True
            #scan for true empty space
            breaker = False

            mode = int(game.config.settings['strawberry'])

            if mode:
                for line in game.map.tiles:
                    for tile in line:
                        if tile.true_empty:
                            breaker = True
                            break
                    if breaker:
                        break
                else:
                    message_display('No true empty space for strawberry!', screen, 750, 35, white, 15)
                    invalid = True

            if mode == 0 or mode == 2:
                if not (game.map.goals or game.map.alt_goals):
                    message_display('No plates!', screen, 620, 50, white, 15)
                    invalid = True

            if len(game.map.clones) == 1:
                message_display('Invalid clone configuration!', screen, 680, 65, white, 15)
                invalid = True

            #save map gaming
            if not invalid:
                game.map.writeMap(game.srcreal + '/snakeData/levels/' + game.config.settings['name'])
                if edit: 
                    message_display('Level Saved!', screen, 450, 800, green, 60)
                else: 
                    message_display('Level Created!', screen, 450, 800, green, 60)
                pygame.display.update()
                pygame.time.delay(2000)
                return 1
                    


        pygame.display.update(pygame.Rect(0, 0, 900, 100))
        pygame.time.delay(30)
        














