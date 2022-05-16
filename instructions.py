import pygame
import os

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
    #pygame.display.update(pygame.Rect(x, y, w, h))
    return pressed

def display_instructions(package_path=None, screen=None, game=None):
    #  this instruction page explains how to move the snake
    intro = True
    restart = [0, ""]
    while intro:
        if restart[0]:
            break
        if restart[1]:
            restart = game_loop(restart[1])
            continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(black)

        path = os.path.dirname(package_path) + '/styles/0/'
        x = game.settings.width * game.settings.rect_len
        print(x)
        y = game.settings.height * game.settings.rect_len
        print(y)
        message_display("How to Play Gluttonous!", screen, 428, 108, color=white, size=60)
        # message_display("How to Play Gluttonous!", screen, 50, color=white, size=30)
        home = button('Home', screen, 214, 700, 80, 40, red, bright_red, yes)
        nextbutton = button('Next', screen, 535, 700, 80, 40, red, bright_red, yes)
        arrows = pygame.image.load(path + "images/arrowkeys.bmp")
        arrows = pygame.transform.scale(arrows, (300, 300))            
        screen.blit(arrows, (235, 188))
        message_display("Use the arrow keys to move the snake", screen, 430, 190, color=white, size=40)  
        screen.blit(pygame.transform.scale(pygame.image.load(path + "images/head_up1.bmp"), (45,45)), (556, 220))
        screen.blit(pygame.transform.scale(pygame.image.load(path + "images/body_s.bmp"), (45, 45)), (556, 265))
        screen.blit(pygame.transform.scale(pygame.image.load(path + "images/body_s.bmp"), (45, 45)), (556, 310))
        screen.blit(pygame.transform.scale(pygame.image.load(path + "images/body_s.bmp"), (45, 45)), (556, 355))            
        screen.blit(pygame.transform.scale(pygame.image.load(path + "images/tail_up.bmp"), (45, 45)), (556, 400))
         
        message_display("Eat the food to grow the snake", screen, 428, 470, color=white, size=40)

        # blit the food onto the screen to show users 
        for i in range(1, 9):
            food = pygame.image.load(path + "images/food" + str(i) + ".bmp")
            food = pygame.transform.scale(food, (70, 70))
            if i in range(1, 5): 
                screen.blit(food, (300+(i-1)*71, 535))
            else: 
                screen.blit(food, (300+(i-5)*71, 606))
        
        if home: 
            screen.fill(white)
            return 0
        if nextbutton: 
            instructions_pagetwo(package_path, screen)
        if restart[0]:
            break
        pygame.display.update()
        pygame.time.Clock().tick(15)

def instructions_pagetwo(package_path=None, screen=None): 
    #  this instructions page explains how the food items work with growing the snake
    intro = True
    restart = [0, ""]
    while intro:
        if restart[0]:
            break
        if restart[1]:
            restart = game_loop(restart[1], custom=restart[2])
            continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(black)

        path = os.path.dirname(package_path) + '/styles/0/'

        message_display("Don't crash into the walls!", screen, 430, 85, color=white, size=40)

        
        snakehead = pygame.transform.scale(pygame.transform.rotate(pygame.image.load(path + "images/head_up4.bmp"), 90), (45, 45))
        snakebody = pygame.transform.scale(pygame.transform.rotate(pygame.image.load(path + 'images/body_s.bmp'), 270), (45, 45))
        snaketail = pygame.transform.scale(pygame.transform.rotate(pygame.image.load(path + 'images/tail_up0.bmp'), 90), (45, 45))
        tile = pygame.transform.scale(pygame.image.load(path + "images/tile.bmp"), (45, 45))
        wrap = pygame.transform.scale(pygame.image.load(path + "images/wrap.bmp"), (45, 45))
        pad = pygame.transform.scale(pygame.image.load(path + "images/pad.bmp"), (45, 45))

        cross = pygame.transform.scale(pygame.image.load("images/cross.bmp"), (90, 90))
        tick = pygame.transform.scale(pygame.image.load("images/tick.bmp"), (45, 45))
        
        screen.blit(snakehead, (400,130))
        screen.blit(snakebody, (445, 130))
        screen.blit(snakebody, (490, 130))
        screen.blit(snaketail, (535, 130))
        screen.blit(tile, (355, 130))

        
        screen.blit(cross, (200, 85))

        message_display("Don't crash into yourself!", screen, 430, 215, color=white, size=40)
        screen.blit(pygame.transform.rotate(snaketail, 180), (300, 255))
        screen.blit(snakebody, (345, 255))
        screen.blit(snakebody, (390, 255))
        screen.blit(snakebody, (435, 255))
        screen.blit(pygame.transform.rotate(snakebody, 90), (435, 297))
        screen.blit(pygame.transform.rotate(snakebody, 90), (435, 341))
        screen.blit(pygame.transform.rotate(snakebody, 180), (393, 342))
        screen.blit(pygame.transform.rotate(snakebody, 180), (348, 342))
        screen.blit(pygame.transform.rotate(snakehead,270), (345, 300))

        screen.blit(cross, (500, 290))


        #  Wrap walls instructions

        message_display("You teleport through wrap walls", screen, 430, 400, color=white, size=40)
    
        screen.blit(snaketail, (280, 435))
        screen.blit(pygame.transform.rotate(snakebody, 180), (235, 435))
        screen.blit(tile, (190, 435))
        screen.blit(wrap, (190, 435))

        screen.blit(tile, (430, 435))
        screen.blit(pygame.transform.rotate(wrap, 180), (430, 435))
        screen.blit(pygame.transform.rotate(snakebody, 180), (385, 435))
        screen.blit(snakehead, (340, 435))
        screen.blit(tick, (580, 435))

        # padded walls instructions
        message_display("You can survive impact with padded walls", screen, 430, 520, color=white, size=40)
        screen.blit(tile, (300,565))
        screen.blit(pad, (300,565))

        screen.blit(pygame.transform.rotate(snakehead, 180), (345, 565))
        screen.blit(pygame.transform.rotate(snakebody,180), (390, 565))
        screen.blit(pygame.transform.rotate(snakebody, 180), (435, 565))
        screen.blit(pygame.transform.rotate(snaketail, 180), (480, 565))

        screen.blit(tick, (560, 565))

        # describing the win mechanisms and features 
        message_display("There are a few different ways to win levels", screen, 430, 620, color=white, size=30)
        message_display("Look for pressure plates or clones to help", screen, 350, 660, color=white, size=30)
        screen.blit(pygame.transform.scale(pygame.image.load(path + "images/plate.bmp"), (45, 45)), (650, 640))
        screen.blit(pygame.transform.scale(pygame.image.load(path + "images/clone.bmp"), (45, 45)), (700, 640))
        back = button('Back', screen, 410, 700, 80, 40, red, bright_red, yes)
    
        if back: 
            return 0
        # if nextbutton: 
        #     i
        if restart[0]:
            break
        pygame.display.update()
        pygame.time.Clock().tick(15)
