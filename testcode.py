import pygame
import time 
import random 

def main():
    pygame.init()
    screen = pygame.display.set_mode([500,500])
    screen.fill([25, 226, 230])
    
    #running state of the game variable
    run = True
    while run:
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)

        button_color_New = (255, 204, 153)
        button_color_Con = (255, 204, 204)
        button_color_Cre = (204, 255, 204)

        mouse = pygame.mouse.get_pos() 

        if 150+100 > mouse[0] > 150 and 550 + 50 > mouse[1] > 550: 
            pygame.draw.rect(gameDisplay, button_color_New, (150, 550, 100, 50))
        else :
            pygame.draw.rect(gameDisplay, black, (150, 550, 100, 50))


        if 200+100 > mouse[0] > 200 and 550 + 50 > mouse[1] > 550: 
            pygame.draw.rect(gameDisplay, button_color_Con, (200, 550, 100, 50))
        else : 
            pygame.draw.rect(gameDisplay, white, (150, 550, 100, 50))


        if 250+100 > mouse[0] > 250 and 550 + 50 > mouse[1] > 550: 
            pygame.draw.rect(gameDisplay, button_color_Cre, (200, 550, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, (150, 550, 100, 50))


        #event handling and visuals go in here
        for event in pygame.event.get():
            #can do other stuff in here for listeners
            if event.type == pygame.QUIT:
                run = False

if __name__ == "__main__":
    main()
