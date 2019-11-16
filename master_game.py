import sys
from enum import Enum
from gifImage import gifImage
from Pet import Pet
from Pet import PetType
from Buttonify import Buttonify
from RectButton import RectButton
import pygame as pg
from RectButton import RectButton
import os
import shutil
import datetime

class Screen(Enum):
    STARTING = 0
    SELECTION = 1
    EGG = 2
    Q_A = 3
    Q_A1 = 4
    Q_A2 = 5
    Q_A3 = 6
    Q_A4 = 7
    HATCH = 8
    HOME = 9
    FOOD = 10
    WATER = 11
    SLEEP = 12
    FUN = 13

    def __lt__(this, other):
        if this.__class__ is other.__class__:
            return this.value < other.value
        return NotImplemented

    def __gt__(this, other):
        if this.__class__ is other.__class__:
            return this.value > other.value
        return NotImplemented


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # More colours should be added here
ORANGE = (255, 128, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (127, 0, 255)
WIDTH = 800
HEIGHT = 480

FOOD_CHANGE_RATE = -1
WATER_CHANGE_RATE = -1
SLEEP_CHANGE_RATE = -1
STRESS_CHANGE_RATE = 1

pg.init()
pg.font.init()
init_time = datetime.datetime.now()
titleFont = pg.font.Font("VT323-Regular.ttf", 180)
textFont = pg.font.Font("VT323-Regular.ttf", 60)
smallFont = pg.font.Font("VT323-Regular.ttf", 40)

screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)


def update_save(currPet):
    savefile = open("save/saveFile.txt", "w+")
    savefile.write(str((currPet.petType)) + "\n")
    savefile.write(currPet.name + "\n")
    savefile.write(str(currPet.food) + "\n")
    savefile.write(str(currPet.water) + "\n")
    savefile.write(str(currPet.sleep) + "\n")
    savefile.write(str(currPet.stress) + "\n")
    savefile.write(str(datetime.datetime.now()) + "\n")
    savefile.close()

def main():
    
    currPet = Pet(PetType.BALA, "bala")
    
    savefile = open("save/saveFile.txt", "a+")

    FRAMERATE = 12

    titleBG = gifImage("graphicAssets/BgTitle3")
    homeBG = gifImage("graphicAssets/BgTitle5")
    homeBG.resize(800, 480)
    qaBG = gifImage("graphicAssets/BgTitle4")
    qaBG.resize(800, 480)

    eggUnhatched = gifImage("graphicAssets/EggUnhatched",
                            WIDTH/4 + 80, HEIGHT/2 - 170, 15)
    eggUnhatched.resize(250, 250)

    startButton = Buttonify("graphicAssets/startButton.png", screen)
    startButton.resize(300, 100)
    startButton.setCoords(100, 300)

    newGameButton = Buttonify("graphicAssets/NewGame.png", screen)
    newGameButton.resize(320, 110)
    newGameButton.setCoords(75, 180)

    continueGameButton = Buttonify("graphicAssets/LoadGame.png", screen)
    continueGameButton.resize(300, 100)
    continueGameButton.setCoords(425, 175)

    qa1LeftButton = RectButton(
        WIDTH / 4 - 145, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa1MiddleButton = RectButton(
        WIDTH / 4 + 98, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa1RightButton = RectButton(
        WIDTH / 4 + 340, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)

    qa2LeftButton = RectButton(
        WIDTH / 4 - 145, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa2MiddleButton = RectButton(
        WIDTH / 4 + 98, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa2RightButton = RectButton(
        WIDTH / 4 + 340, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)

    qa3LeftButton = RectButton(
        WIDTH / 4 - 145, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa3MiddleButton = RectButton(
        WIDTH / 4 + 98, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa3RightButton = RectButton(
        WIDTH / 4 + 340, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)

    qa4LeftButton = RectButton(
        WIDTH / 4 - 145, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa4MiddleButton = RectButton(
        WIDTH / 4 + 98, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)
    qa4RightButton = RectButton(
        WIDTH / 4 + 340, HEIGHT / 2 + 55, 215, 50, screen, BLACK, 100)

    HomeFoodButton = RectButton(
        7 * WIDTH / 8, HEIGHT / 16 + 10, 90, 90, screen, BLACK, 180)
    HomeWaterButton = RectButton(
        7 * WIDTH / 8, HEIGHT / 16 + 110, 90, 90, screen, BLACK, 180)
    HomeSleepButton = RectButton(
        7 * WIDTH / 8, HEIGHT / 16 + 210, 90, 90, screen, BLACK, 180)
    HomeStressButton = RectButton(
        7 * WIDTH / 8, HEIGHT / 16 + 310, 90, 90, screen, BLACK, 180)

    currGameState = Screen.STARTING

    petSum = 0
    
    while True:

        clock = pg.time.Clock()

        ev = pg.event.get()
        screen.fill(WHITE)

        if currGameState.value > Screen.HATCH.value:
            currPet.food += FOOD_CHANGE_RATE
            currPet.water += WATER_CHANGE_RATE
            currPet.sleep += SLEEP_CHANGE_RATE
            currPet.stress += STRESS_CHANGE_RATE

            currPet.food = 0 if currPet.food < 0 else 100 if currPet.food > 100 else currPet.food
            currPet.water = 0 if currPet.water < 0 else 100 if currPet.water > 100 else currPet.water
            currPet.sleep = 0 if currPet.sleep < 0 else 100 if currPet.sleep > 100 else currPet.sleep
            currPet.stress = 0 if currPet.stress < 0 else 100 if currPet.stress > 100 else currPet.stress

        if currGameState == Screen.STARTING:

            titleBG.animate(screen)

            title = titleFont.render('JikoAi', True, WHITE)
            screen.blit(title, (WIDTH / 4 - 15, HEIGHT / 2 - 100))

        elif currGameState == Screen.SELECTION:

            titleBG.animate(screen)

            newGameButton.draw()
            continueGameButton.draw()

        elif currGameState == Screen.HOME:

            homeBG.animate(screen)

            innerFoodBar = pg.Rect(40, 40, 200, 25)
            innerWaterBar = pg.Rect(40, 80, 200, 25)
            innerSleepBar = pg.Rect(40, 120, 200, 25)
            innerStressBar = pg.Rect(40, 160, 200, 25)
            currPet.drawStatBar(screen, innerFoodBar, ORANGE, currPet.food)
            currPet.drawStatBar(screen, innerWaterBar, BLUE, currPet.water)
            currPet.drawStatBar(screen, innerSleepBar, PURPLE, currPet.sleep)
            currPet.drawStatBar(screen, innerStressBar, RED, currPet.stress)
            currPet.draw(screen, WIDTH / 2, 3 * HEIGHT / 4)

            HomeFoodButton.draw()
            HomeFoodButton.draw_text("food")
            HomeWaterButton.draw()
            HomeWaterButton.draw_text("water")
            HomeSleepButton.draw()
            HomeSleepButton.draw_text("sleep")
            HomeStressButton.draw()
            HomeStressButton.draw_text("play")

        elif currGameState == Screen.EGG:
            print("FILLER")
        elif currGameState == Screen.FOOD:
            print("FILLER")
        elif currGameState == Screen.HATCH:
            if petSum <= 6:
                currPet = Pet(PetType.BALA, "bala")
            elif petSum <= 9:
                currPet = Pet(PetType.MAMAU, "mamau")
            else:
                currPet = Pet(PetType.TORA, "tora")
            savefile.write(str(currPet.petType.value) + "\n")
            #TODO: make an animation
            currGameState = Screen.HOME
        elif currGameState == Screen.Q_A:

            homeBG.animate(screen)
            eggUnhatched.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 80, HEIGHT / 2 + 70))

            eggSubtitle = textFont.render('Who will your pet be?', True, WHITE)
            screen.blit(eggSubtitle, (WIDTH / 4 - 30, HEIGHT / 2 + 77))

            if pg.mouse.get_pressed()[0] and currGameState == Screen.Q_A:
                currGameState = Screen.Q_A1

        elif currGameState == Screen.Q_A1:

            qaBG.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 90, HEIGHT / 2 - 160))

            qTitle = textFont.render('Some questions first!', True, WHITE)
            screen.blit(qTitle, (WIDTH / 4 - 30, HEIGHT / 2 - 157))

            q1Text = textFont.render(
                'Do you often feel stressed?', True, WHITE)

            bgRect1 = pg.Surface((700, 75))
            bgRect1.set_alpha(100)
            bgRect1.fill(BLACK)

            screen.blit(bgRect1, (WIDTH / 4 - 145, HEIGHT / 2 - 35))
            screen.blit(q1Text, (WIDTH / 4 - 110, HEIGHT / 2 - 30))

            answer1Text = smallFont.render('Not often', True, WHITE)

            bgRect2 = pg.Surface((215, 50))
            bgRect2.set_alpha(100)
            bgRect2.fill(BLACK)

            qa1LeftButton.draw()
            screen.blit(answer1Text, (WIDTH / 4 - 110, HEIGHT / 2 + 60))

            answer2Text = smallFont.render('Sometimes', True, WHITE)

            qa1MiddleButton.draw()
            screen.blit(answer2Text, (WIDTH / 4 + 133, HEIGHT / 2 + 60))

            answer3Text = smallFont.render('Often', True, WHITE)

            qa1RightButton.draw()
            screen.blit(answer3Text, (WIDTH / 4 + 400, HEIGHT / 2 + 60))

        elif currGameState == Screen.Q_A2:

            qaBG.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 90, HEIGHT / 2 - 160))

            qTitle = textFont.render('Some questions first!', True, WHITE)
            screen.blit(qTitle, (WIDTH / 4 - 30, HEIGHT / 2 - 157))

            q1Text = textFont.render('I feel good about myself.', True, WHITE)

            bgRect1 = pg.Surface((700, 75))
            bgRect1.set_alpha(100)
            bgRect1.fill(BLACK)

            screen.blit(bgRect1, (WIDTH / 4 - 145, HEIGHT / 2 - 35))
            screen.blit(q1Text, (WIDTH / 4 - 110, HEIGHT / 2 - 30))

            answer1Text = smallFont.render('Disagree', True, WHITE)

            bgRect2 = pg.Surface((215, 50))
            bgRect2.set_alpha(100)
            bgRect2.fill(BLACK)

            qa2LeftButton.draw()
            screen.blit(answer1Text, (WIDTH / 4 - 110, HEIGHT / 2 + 60))

            answer2Text = smallFont.render('Not sure', True, WHITE)

            qa2MiddleButton.draw()
            screen.blit(answer2Text, (WIDTH / 4 + 133, HEIGHT / 2 + 60))

            answer3Text = smallFont.render('Agree', True, WHITE)

            qa2RightButton.draw()
            screen.blit(answer3Text, (WIDTH / 4 + 400, HEIGHT / 2 + 60))

        elif currGameState == Screen.Q_A3:

            qaBG.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 90, HEIGHT / 2 - 160))

            qTitle = textFont.render('Some questions first!', True, WHITE)
            screen.blit(qTitle, (WIDTH / 4 - 30, HEIGHT / 2 - 157))

            q1Text = textFont.render(
                'I have things under control.', True, WHITE)

            bgRect1 = pg.Surface((700, 75))
            bgRect1.set_alpha(100)
            bgRect1.fill(BLACK)

            screen.blit(bgRect1, (WIDTH / 4 - 145, HEIGHT / 2 - 35))
            screen.blit(q1Text, (WIDTH / 4 - 110, HEIGHT / 2 - 30))

            answer1Text = smallFont.render('Disagree', True, WHITE)

            bgRect2 = pg.Surface((215, 50))
            bgRect2.set_alpha(100)
            bgRect2.fill(BLACK)

            qa3LeftButton.draw()
            screen.blit(answer1Text, (WIDTH / 4 - 110, HEIGHT / 2 + 60))

            answer2Text = smallFont.render('Not sure', True, WHITE)

            qa3MiddleButton.draw()
            screen.blit(answer2Text, (WIDTH / 4 + 133, HEIGHT / 2 + 60))

            answer3Text = smallFont.render('Agree', True, WHITE)

            qa3RightButton.draw()
            screen.blit(answer3Text, (WIDTH / 4 + 400, HEIGHT / 2 + 60))

        elif currGameState == Screen.Q_A4:

            qaBG.animate(screen)

            bgRect = pg.Surface((600, 75))
            bgRect.set_alpha(100)
            bgRect.fill(BLACK)
            screen.blit(bgRect, (WIDTH / 4 - 90, HEIGHT / 2 - 160))

            qTitle = textFont.render('Some questions first!', True, WHITE)
            screen.blit(qTitle, (WIDTH / 4 - 30, HEIGHT / 2 - 157))

            q1Text = textFont.render(
                'I take good care of myself.', True, WHITE)

            bgRect1 = pg.Surface((700, 75))
            bgRect1.set_alpha(100)
            bgRect1.fill(BLACK)

            screen.blit(bgRect1, (WIDTH / 4 - 145, HEIGHT / 2 - 35))
            screen.blit(q1Text, (WIDTH / 4 - 110, HEIGHT / 2 - 30))

            answer1Text = smallFont.render('Disagree', True, WHITE)

            bgRect2 = pg.Surface((215, 50))
            bgRect2.set_alpha(100)
            bgRect2.fill(BLACK)

            qa4LeftButton.draw()
            screen.blit(answer1Text, (WIDTH / 4 - 110, HEIGHT / 2 + 60))

            answer2Text = smallFont.render('Not sure', True, WHITE)

            qa4MiddleButton.draw()
            screen.blit(answer2Text, (WIDTH / 4 + 133, HEIGHT / 2 + 60))

            answer3Text = smallFont.render('Agree', True, WHITE)

            qa4RightButton.draw()
            screen.blit(answer3Text, (WIDTH / 4 + 400, HEIGHT / 2 + 60))

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
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if currGameState.value > Screen.HATCH.value:
                    savefile.close()
                    update_save(currPet) 
                    savefile = open("save/saveFile.txt", 'a+')
                    print ("saving")
                mouse = pg.mouse.get_pos()
                if currGameState == Screen.STARTING:
                    currGameState = Screen.SELECTION
                elif newGameButton.getImageRect().collidepoint(mouse) and currGameState == Screen.SELECTION:
                    open("save/saveFile.txt", 'w').close()
                    currGameState = Screen.Q_A
                elif continueGameButton.getImageRect().collidepoint(mouse) and currGameState == Screen.SELECTION:
                    lines = open("save/saveFile.txt", "r").read().splitlines()
                    if len(lines) > 6:
                        currPet = Pet(lines[0], lines[1])
                        currPet.food = int(lines[2])
                        currPet.water = int(lines[3])
                        currPet.sleep = int(lines[4])
                        currPet.stress = int(lines[5])
                        currGameState = Screen.HOME
                    else:
                        print("Save game not found")
                        open("save/saveFile.txt", 'w').close()
                        currGameState = Screen.Q_A
                elif qa1LeftButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A1:
                    petSum += 1
                    currGameState = Screen.Q_A2
                elif qa1MiddleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A1:
                    petSum += 2
                    currGameState = Screen.Q_A2
                elif qa1RightButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A1:
                    petSum += 3
                    currGameState = Screen.Q_A2
                elif qa2LeftButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A2:
                    petSum += 1
                    currGameState = Screen.Q_A3
                elif qa2MiddleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A2:
                    petSum += 2
                    currGameState = Screen.Q_A3
                elif qa2RightButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A2:
                    petSum += 3
                    currGameState = Screen.Q_A3
                elif qa3LeftButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A3:
                    petSum += 1
                    currGameState = Screen.Q_A4
                elif qa3MiddleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A3:
                    petSum += 2
                    currGameState = Screen.Q_A4
                elif qa3RightButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A3:
                    petSum += 3
                    currGameState = Screen.Q_A4
                elif qa4LeftButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A4:
                    petSum += 1
                    currGameState = Screen.HATCH
                elif qa4MiddleButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A4:
                    petSum += 2
                    currGameState = Screen.HATCH
                elif qa4RightButton.getImageRect().collidepoint(mouse) and currGameState == Screen.Q_A4:
                    petSum += 3
                    currGameState = Screen.HATCH
                elif currGameState == Screen.HATCH:
                    currGameState = Screen.HOME
                elif currGameState == Screen.HOME:
                    if HomeFoodButton.getImageRect().collidepoint(mouse):
                        currGameState = Screen.FOOD
                    elif HomeWaterButton.getImageRect().collidepoint(mouse):
                        currGameState = Screen.WATER
                    elif HomeSleepButton.getImageRect().collidepoint(mouse):
                        currGameState = Screen.SLEEP
                    elif HomeStressButton.getImageRect().collidepoint(mouse):
                        currGameState = Screen.FUN


main()
