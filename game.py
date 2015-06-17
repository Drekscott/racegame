import pygame, os

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

def car(x,y):
    gameDisplay.blit(car_img, (x,y))
    
def game_loop():
    x=(display_width * 0.45)
    y=(display_height * .6)
    x_change = 0

    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
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
        car(x,y)
        
        if x > display_width - car_width or x<0:
            gameExit = True
            
        
        pygame.display.update()
        clock.tick(60)
        
game_loop()        
pygame.quit()
quit()