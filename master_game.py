from enum import Enum
# from GIFImage import GIFImage
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

class PetType(Enum):
    BALA = 0
    MAMAU = 1
    TORA = 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255) # More colours should be added here
ORANGE = (255, 128, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (127, 0, 255)
WIDTH = 800
HEIGHT = 480

pg.init()
pg.font.init()

titleFont = pg.font.SysFont('VT323-Regular.ttf', 180)
textFont = pg.font.SysFont('VT323-Regular.ttf', 100)
screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)

class Pet(pg.sprite.Sprite):
    petType = -1
    name = ""
    food = 100
    water = 100
    sleep = 100
    stress = 0
    picture = "graphicAssets/SpriteBala"
    def __init__ (self, petType, name):
        WHITE = (255, 255, 255)
        super().__init__()
        self.petType = petType
        self.name = name
        if (petType == PetType.BALA):
            picture = "graphicAssets/SpriteBala.png"
        elif (petType == PetType.MAMAU):
            picture = "graphicAssets/SpriteMamau.png"
        elif (petType == PetType.TORA):
            picture = "graphicAssets/SpriteTora.png"
        self.image = pg.image.load(picture)
        self.image.set_colorkey(WHITE)

    def draw(self, x, y):
        screen.blit(self.image, (x, y))
        pg.display.flip()

def drawWithBorder(innerRect, color):
    borderRect = pg.Rect(innerRect.left, innerRect.top, innerRect.width + 10, innerRect.height + 10)
    borderRect.center = innerRect.center
    pg.draw.rect(screen, BLACK, borderRect)
    pg.draw.rect(screen, color, innerRect)

def drawStatBar(rect, color, val):
    drawWithBorder(rect, WHITE)
    pg.draw.rect(screen, color, pg.Rect(rect.left, rect.top, rect.width * (val / 100), rect.height))

def main():


    # titleBG = GIFImage("graphicAssets/BgTitle2.gif")
    # titleBG = pg.transform.scale(titleBG.getImage, (1280, 720))
    
    currGameState = Screen.STARTING
    currPet = Pet(PetType.BALA, "bala")
    while True:
        ev = pg.event.get()
        screen.fill(WHITE)

        if currGameState == Screen.STARTING:

            outerRect = pg.Rect(WIDTH / 2, HEIGHT / 2, 410, 160)
            innerRect = pg.Rect(WIDTH / 2, HEIGHT / 2, 390, 140)
            outerRect.centerx = WIDTH / 2 #draw rectangles at the center of the screen
            outerRect.centery = HEIGHT / 2
            innerRect.center = outerRect.center
            drawWithBorder(innerRect, WHITE)

            title = titleFont.render('JikoAi', True, (0, 0, 0))
            screen.blit(title,(WIDTH / 4 + 13, HEIGHT / 2 - 57))

            # titleBG.render(screen, (0, 0))
            pg.display.update()

            if pg.mouse.get_pressed()[0]:
                currGameState = Screen.HOME

        elif currGameState == Screen.HOME:
            innerFoodBar = pg.Rect(40, 40, 200, 25)
            innerWaterBar = pg.Rect(40, 80, 200, 25)
            innerSleepBar = pg.Rect(40, 120, 200, 25)
            innerStressBar = pg.Rect(40, 160, 200, 25)
            drawStatBar(innerFoodBar, ORANGE, currPet.food)
            drawStatBar(innerWaterBar, BLUE, currPet.water)
            drawStatBar(innerSleepBar, PURPLE, currPet.sleep)
            drawStatBar(innerStressBar, RED, currPet.stress)
            currPet.draw(WIDTH / 2, 3 / 4 * HEIGHT)
            # screen.blit(welcome,(WIDTH / 4 + 13, HEIGHT / 2 - 57))
        
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
