from enum import Enum
from GIFImage import GIFImage
import pygame as pg

class Screen(Enum):
    STARTING = 0
    HOME = 1
    EGG = 2
    Q_A = 3
    HATCH = 4
    FOOD = 5
    WATER = 6
    FUN = 7


def main():

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255) # More colours should be added here
    WIDTH = 800
    HEIGHT = 480

    pg.init()
    pg.font.init()
    titleFont = pg.font.SysFont('VT323-Regular.ttf', 180)
    textFont = pg.font.SysFont('VT323-Regular.ttf', 100)
    
    screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)

    titleBG = GIFImage("graphicAssets/BgTitle2.gif")
    # titleBG = pg.transform.scale(titleBG.getImage, (1280, 720))
    
    currGameState = Screen.STARTING

    while True:
        ev = pg.event.get()
        screen.fill(WHITE)

        if currGameState == Screen.STARTING:

            outerRect = pg.Rect(WIDTH / 2, HEIGHT / 2, 410, 160)
            innerRect = pg.Rect(WIDTH / 2, HEIGHT / 2, 390, 140)
            outerRect.centerx = WIDTH / 2 #draw rectangles at the center of the screen
            outerRect.centery = HEIGHT / 2
            innerRect.center = outerRect.center
            pg.draw.rect(screen, BLACK, outerRect)
            pg.draw.rect(screen, WHITE, innerRect)
                    
            title = titleFont.render('JikoAi', True, (0, 0, 0))
            screen.blit(title,(WIDTH / 4 + 13, HEIGHT / 2 - 57))

            titleBG.render(screen, (0, 0))
            pg.display.update()

            if pg.mouse.get_pressed()[0]:
                currGameState = Screen.HOME
                mouse = pg.mouse.get_pos()
                        # button_color_New = (255, 204, 153)
                        # button_color_Con = (255, 204, 204)
                        # button_color_Cre = (204, 255, 204)
                        # button_color_ifClicked = (0, 0, 0)

                if 150+100 > mouse[0] > 150 and 550 + 50 > mouse[1] > 550: 
                    pg.draw.rect(screen, (255, 204, 153), (150, 550, 100, 50))
                else :
                    pg.draw.rect(screen, (0, 0, 0), (150, 550, 100, 50))


                if 200+100 > mouse[0] > 200 and 550 + 50 > mouse[1] > 550: 
                    pg.draw.rect(screen, (255, 204, 204), (200, 550, 100, 50))
                else : 
                    pg.draw.rect(screen, (0, 0, 0), (150, 550, 100, 50))


                if 250+100 > mouse[0] > 250 and 550 + 50 > mouse[1] > 550: 
                    pg.draw.rect(screen, (204, 255, 204), (200, 550, 100, 50))
                else:
                    pg.draw.rect(screen, (0, 0, 0), (150, 550, 100, 50))

        elif currGameState == Screen.HOME:
            welcome = textFont.render('h', True, (0, 0, 0))
            screen.blit(welcome,(WIDTH / 4 + 13, HEIGHT / 2 - 57))
        
        elif currGameState == Screen.EGG:
            print("FILLER")
        elif currGameState == Screen.FOOD:
            print("FILLER")
        elif currGameState == Screen.HATCH:
            print("FILLER")
        elif currGameState == Screen.Q_A:
            print("FILLER")
        elif currGameState == Screen.WATER:
            print("FILLER")
        elif currGameState == Screen.FUN:
            print("FILLER")
            
        for event in ev:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()


main()
