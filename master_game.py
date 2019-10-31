from enum import Enum
import pygame as pg

class Screen(Enum):
    STARTING = 0
    HOME = 1


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
            if pg.mouse.get_pressed()[0]:
                currGameState = Screen.HOME

        elif currGameState == Screen.HOME:
            welcome = textFont.render('h', True, (0, 0, 0))
            screen.blit(welcome,(WIDTH / 4 + 13, HEIGHT / 2 - 57))
        
        for event in ev:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()


main()
