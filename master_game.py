import sys
from enum import Enum
from gifImage import gifImage 
import pygame as pg

class Screen(Enum):
    STARTING = 0
    HOME = 1
    EGG = 2
    Q_A = 3
    Q_A1 = 4
    Q_A2 = 5
    Q_A3 = 6
    HATCH = 7
    FOOD = 8
    WATER = 9
    FUN = 10


def main():

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255) # More colours should be added here
    WIDTH = 800
    HEIGHT = 480
    FRAMERATE = 60

    pg.init()
    pg.font.init()
    titleFont = pg.font.Font("VT323-Regular.ttf", 180)
    textFont = pg.font.Font("VT323-Regular.ttf", 60)
    smallFont = pg.font.Font("VT323-Regular.ttf", 40)
    
    screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)

    titleBG = gifImage("graphicAssets/BgTitle3")
    homeBG = gifImage("graphicAssets/BgTitle5")
    homeBG.resize(800, 480)
    qaBG = gifImage("graphicAssets/BgTitle4")
    qaBG.resize(800, 480)

    eggUnhatched = gifImage("graphicAssets/EggUnhatched", WIDTH/4 + 80, HEIGHT/2 - 170, 15)
    eggUnhatched.resize(250, 250)
    
    currGameState = Screen.STARTING

    while True:

        clock = pg.time.Clock()

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

            titleBG.animate(screen)

            title = titleFont.render('JikoAi', True, WHITE)
            screen.blit(title,(WIDTH / 4 - 15, HEIGHT / 2 - 100))

            subtitle = textFont.render('Click to begin!', True, WHITE)
            screen.blit(subtitle, (WIDTH/ 4 + 25, HEIGHT / 2 + 57))

            if pg.mouse.get_pressed()[0]:
                currGameState = Screen.HOME

        elif currGameState == Screen.HOME:

            homeBG.animate(screen)
            eggUnhatched.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 80, HEIGHT /2 + 70))

            eggSubtitle = textFont.render('Who will your pet be?', True, WHITE)
            screen.blit(eggSubtitle, (WIDTH / 4 - 30, HEIGHT / 2 + 77))

            if pg.mouse.get_pressed()[0]:
                currGameState = Screen.Q_A
        
        elif currGameState == Screen.EGG:
            print("FILLER")
        elif currGameState == Screen.FOOD:
            print("FILLER")
        elif currGameState == Screen.HATCH:
            print("FILLER")
        elif currGameState == Screen.Q_A:

            qaBG.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 90, HEIGHT /2 - 160))
            
            qTitle = textFont.render('Some questions first!', True, WHITE)
            screen.blit(qTitle, (WIDTH / 4 - 30, HEIGHT / 2 - 157))


            q1Text = textFont.render('Do you often feel stressed?', True, WHITE)

            bgRect1 = pg.Surface((700, 75))
            bgRect1.set_alpha(100)
            bgRect1.fill(BLACK)

            screen.blit(bgRect1, (WIDTH / 4 - 145, HEIGHT /2 - 35))
            screen.blit(q1Text, (WIDTH / 4 - 110, HEIGHT / 2 - 30))

            answer1Text = smallFont.render('Not often', True, WHITE)

            bgRect2 = pg.Surface((215, 50))
            bgRect2.set_alpha(100)
            bgRect2.fill(BLACK)

            screen.blit(bgRect2, (WIDTH / 4 - 145, HEIGHT /2 + 55))
            screen.blit(answer1Text, (WIDTH / 4 - 110, HEIGHT / 2 + 60))

            answer2Text = smallFont.render('Sometimes', True, WHITE)

            screen.blit(bgRect2, (WIDTH / 4 + 98, HEIGHT /2 + 55))
            screen.blit(answer2Text, (WIDTH / 4 + 133, HEIGHT / 2 + 60))

            answer3Text = smallFont.render('Often', True, WHITE)

            screen.blit(bgRect2, (WIDTH / 4 + 340, HEIGHT /2 + 55))
            screen.blit(answer3Text, (WIDTH / 4 + 400, HEIGHT / 2 + 60))

            if pg.mouse.get_pressed()[0]:
                currGameState = Screen.Q_A1

        elif currGameState == Screen.Q_A1:

            qaBG.animate(screen)

        elif currGameState == Screen.Q_A2:
            qaBG.animate(screen)
        elif currGameState == Screen.Q_A3:
            qaBG.animate(screen)
        elif currGameState == Screen.WATER:
            print("FILLER")
        elif currGameState == Screen.FUN:
            print("FILLER")

        pg.display.update()

        clock.tick(FRAMERATE)

        for event in ev:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

main()
