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

def display_instructions(package_path=None, screen=None):
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

        message_display("How to Play Gluttonous!", screen, 200, 50, color=white, size=30)
        home = button('Home', screen, 100, 350, 80, 40, red, bright_red, yes)
        nextbutton = button('Next', screen, 250, 350, 80, 40, red, bright_red, yes)
        arrows = pygame.image.load(path + "images/arrowkeys.bmp")
        arrows = pygame.transform.scale(arrows, (140, 140))            
        screen.blit(arrows, (110, 88))
        screen.blit(pygame.image.load(path + "images/head_up1.bmp"), (280, 125))
        screen.blit(pygame.image.load(path + "images/body_s.bmp"), (280, 140))
        screen.blit(pygame.image.load(path + "images/body_s.bmp"), (280, 155))            
        screen.blit(pygame.image.load(path + "images/body_s.bmp"), (280, 170))
        screen.blit(pygame.image.load(path + "images/tail_up.bmp"), (280, 185))
        message_display("Use the arrow keys to move the snake", screen, 200, 90, color=white, size=20)   

        message_display("Eat the food to grow the snake", screen, 200, 220, color=white, size=20)

        # blit the food onto the screen to show users 
        for i in range(1, 9):
            food = pygame.image.load(path + "images/food" + str(i) + ".bmp")
            food = pygame.transform.scale(food, (30, 30))
            if i in range(1, 5): 
                screen.blit(food, (150+(i-1)*31, 250))
            else: 
                screen.blit(food, (150+(i-5)*31, 281))
        
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

        message_display("Don't crash into the walls!", screen, 200, 40, color=white, size=20)

        screen.blit(pygame.image.load(path + "images/tile.bmp"), (200, 60))
        snakehead = pygame.transform.rotate(pygame.image.load(path + "images/head_up1.bmp"), 270)
        snakebody = pygame.transform.rotate(pygame.image.load(path + 'images/body_s.bmp'), 270)
        snaketail = pygame.transform.rotate(pygame.image.load(path + 'images/tail_up.bmp'), 270)
        screen.blit(snakehead, (185,60))
        screen.blit(snakebody, (170, 60))
        screen.blit(snakebody, (155, 60))
        screen.blit(snaketail, (140, 60))

        cross = pygame.transform.scale(pygame.image.load(path + "images/cross.bmp"), (40, 40))
        screen.blit(cross, (240, 40))

        message_display("Don't crash into yourself!", screen, 200, 100, color=white, size=20)

        screen.blit(snaketail, (140, 120))
        screen.blit(snakebody, (155, 120))
        screen.blit(snakebody, (170, 120))
        screen.blit(snakebody, (185, 120))
        screen.blit(pygame.transform.rotate(snakebody, 90), (185, 133))
        screen.blit(pygame.transform.rotate(snakebody, 90), (185, 148))
        screen.blit(pygame.transform.rotate(snakebody, 180), (172, 148))
        screen.blit(pygame.transform.rotate(snakebody, 180), (157, 148))
        screen.blit(pygame.transform.rotate(snakehead, 90), (155, 135))

        screen.blit(cross, (240, 120))


        #  Wrap walls instructions

        message_display("You teleport through wrap walls", screen, 200, 170, color=white, size=20)
    
        screen.blit(pygame.transform.rotate(snaketail, 180), (130, 190))
        screen.blit(pygame.transform.rotate(snakebody, 180), (115, 190))
        screen.blit(pygame.image.load("styles/0/images/tile.bmp"), (100, 190))
        screen.blit(pygame.image.load("styles/0/images/wrap.bmp"), (100, 190))

        screen.blit(pygame.image.load("styles/0/images/tile.bmp"), (200, 190))
        screen.blit(pygame.transform.rotate(pygame.image.load("styles/0/images/wrap.bmp"), 180), (200, 190))
        screen.blit(pygame.transform.rotate(snakebody, 180), (185, 190))
        screen.blit(pygame.transform.rotate(snakehead, 180), (170, 190))
        screen.blit(pygame.transform.scale(pygame.image.load("images/tick.bmp"), (30, 30)), (240, 190))

        # padded walls instructions
        message_display("You can survive impact with padded walls", screen, 200, 230, color=white, size=20)
        screen.blit(pygame.image.load(path + "images/tile.bmp"), (140,255))
        screen.blit(pygame.image.load(path + "images/pad.bmp"), (140,255))

        screen.blit(pygame.transform.rotate(snakehead, 180), (155, 255))
        screen.blit(pygame.transform.rotate(snakebody,180), (170, 255))
        screen.blit(pygame.transform.rotate(snakebody, 180), (185, 255))
        screen.blit(pygame.transform.rotate(snaketail, 180), (200, 255))

        screen.blit(pygame.transform.scale(pygame.image.load("images/tick.bmp"), (30, 30)), (240, 245))

        # pressure plates
        message_display("Activate the pressure plates to win the level", screen, 200, 300, color=white, size=20)

        screen.blit(pygame.image.load(path + "images/plate.bmp"), (180, 320))
        screen.blit(pygame.image.load(path + "images/platea.bmp"), (220, 320))
        back = button('Back', screen, 150, 350, 80, 40, red, bright_red, yes)
       
    
        if back: 
            return 0
        # if nextbutton: 
        #     i
        if restart[0]:
            break
        pygame.display.update()
        pygame.time.Clock().tick(15)
