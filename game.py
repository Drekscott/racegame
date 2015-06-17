import pygame, os
import time
import random

pygame.init()

display_width=800
display_height=600


black=(0,0,0)
white=(255,255,255)
red = (255,0,0)
green = (0, 255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

car_img=pygame.image.load('racecar.png')
car_width = 255

def blocks(blockx, blocky, blockh, blockw, color):
    pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])

def car(x,y):
    gameDisplay.blit(car_img, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    
    time.sleep(2)
    
    game_loop()
    
def crash():
    message_display('You Crashed')
    
def game_loop():
    x=(display_width * 0.25)
    y=(display_height * .6)
    x_change = 0
    
    block_startx = random.randrange(0, display_width) 
    #block_startx = (display_width/2) 
    block_starty = -500
    blocks_speed = 7
    block_width = 100
    block_height = 100
    
    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
        x += x_change
        
        gameDisplay.fill(green)       
        
        #blocks(blockx, blocky, blockh, blockw, color)
        blocks(block_startx, block_starty, block_width, block_height, black)
        block_starty += blocks_speed
        
        car(x,y)
        
        if x > display_width - car_width or x<0:
            crash()
        
        if block_starty > display_height:
            block_starty = 0 - block_height
            block_startx = random.randrange(0, display_width)
            
        if x < block_startx + block_width and x+car_width > block_startx:
            print('x crossover')
            
            if y <= block_starty+block_height:
                print('y crossover')
                crash()
        
            
        
        pygame.display.update()
        clock.tick(30)
        
game_loop()        
pygame.quit()
quit()