import pygame

import pygame_textinput
#https://github.com/Nearoo/pygame-text-input

import os
import operator

from game import Game
from snake import Snake
from map import Map
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



warning_dict = {'name' : 'name must be printable',
                'mapX': 'must be integer between 0-30',
                'mapY': 'must be integer between 0-30',
                'xOffset': 'must be integer between 0-10',
                'yOffset': 'must be integer between 0-10'}

comparison_dict = {'name' : lambda line: line.isprintable() and len(line) > 0,
                    'mapX' : lambda value: int(value) <= 30 and int(value) >= 0,
                    'mapY' : lambda value: int(value) <= 30 and int(value) >= 0,
                    'xOffset' : lambda value: int(value) <= 10 and int(value) >= 0,
                    'yOffset' : lambda value: int(value) <= 10 and int(value) >= 0}


class InputBox:

    def __init__(self, x, y, w, h, datatype=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.datatype = datatype

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
                    self.text_warning = warning_dict[self.datatype]
                    self.active_warning = True
                
                self.active = False

            # Change the current color of the input box.
            self.color = green if (self.active or not self.active_warning) else red


        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                    
                    try:
                        if not comparison_dict[self.datatype](self.text):
                            raise ValueError
                    except Exception:
                        self.text_warning = warning_dict[self.datatype]
                        self.active_warning = True

                    self.color = red if self.active_warning else green

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
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        button('New level', screen, 370, 150, 160, 40, red, bright_red, new_level, game=game)
        button('Edit existing level', screen, 370, 300, 160, 40, red, bright_red, yes)

        if button('Back', screen, 410, 600, 80, 40, red, bright_red, yes):
            screen.fill(white)
            break

        pygame.display.update()
        pygame.time.Clock().tick(15)



def new_level(game=None):
    screen = game.screen
    

    font = pygame.font.Font(os.path.dirname(os.path.abspath(__file__)) + '/arial.ttf', 30)
    active = False

    name_box = InputBox(350, 100, 200, 32, 'name')
    x_size_box = InputBox(250, 300, 140, 32, 'mapX')
    y_size_box = InputBox(450, 300, 140, 32, 'mapY')
    x_offset_box = InputBox(250, 400, 140, 32, 'xOffset')
    y_offset_box = InputBox(450, 400, 140, 32, 'yOffset')
    boxes = [name_box, x_size_box, y_size_box, x_offset_box, y_offset_box]

    while True:
        screen.fill(black)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            for box in boxes:
                box.handle_event(event)

        for box in boxes:
            box.draw(screen)

        #progress onto next stage, but before that let's put stuff into an object
        if button('Continue', screen, 410, 450, 80, 40, blue, bright_blue, yes):
            

            dict((key.datatype, key.text) for key in boxes[1:])

        if button('Back', screen, 410, 700, 80, 40, red, bright_red, yes):
            screen.fill(white)
            break        
        

        pygame.display.update()
        pygame.time.delay(30)







