import pygame as pg 
from random import randint
from GIFImage import GIFImage
from enum import Enum
from enum import IntEnum
import os

class PetType(Enum):
    BALA = 0
    MAMAU = 1
    TORA = 2
    BALAGIF = 3
    MAMAUGIF = 4
    TORAGIF = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # More colours should be added here
ORANGE = (255, 128, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (127, 0, 255)
WIDTH = 800
HEIGHT = 480
PETFRAMECYCLE = 15

class Pet():

    petType = -1
    name = ""
    food = 100
    water = 100
    sleep = 100
    stress = 0
    picture = os.getcwd() + "/graphicAssets/SpriteBala.png"
    isImage = True

    def __init__(self, petType, name, isImage, moveCycleLen = 30):

        WHITE = (255, 255, 255)
        picture = os.getcwd() + "/graphicAssets/SpriteBala.png"
        self.petType = petType
        self.name = name
        self.isImage = isImage
        self.moveCycleLen = moveCycleLen
        self.frameCycleCount = 1
        self.currX = 0
        self.currY = 0


        if (str(petType) == str(PetType.BALA)):
            picture = os.getcwd() + "/graphicAssets/SpriteBala.png"
        elif (str(petType) == str(PetType.MAMAU)):
            picture = os.getcwd() + "/graphicAssets/SpriteMamau.png"
        elif (str(petType) == str(PetType.TORA)):
            picture = os.getcwd() + "/graphicAssets/SpriteTora.png"
        elif (str(petType) == str(PetType.BALAGIF)):
            picture = os.getcwd() + "/graphicAssets/SpriteBalaGif"
        elif (str(petType) == str(PetType.MAMAUGIF)):
            picture = os.getcwd() + "/graphicAssets/SpriteMamauGif"
        elif (str(petType) == str(PetType.TORAGIF)):
            picture = os.getcwd() + "/graphicAssets/SpriteToraGif"

        if (self.isImage):
            self.image = pg.image.load(picture)
            self.image.set_colorkey(WHITE)
            self.image = pg.transform.smoothscale(self.image, (105, 135))
        else:
            self.image = GIFImage(picture, 0, 0, PETFRAMECYCLE)
            self.image.resize(105, 135)

    @classmethod
    def init_image(cls, petType, name):
        return cls(petType, name, True)

    @classmethod
    def init_gifImage(cls, petType, name):
        return cls(petType, name, False)

    def resize(self, width, height):
        if(self.isImage):
            self.image = pg.transform.scale(self.image, (width, height))
        else:
            self.image.resize(width, height)

    def setCoords(self, x, y):
        self.currX = x - self.image.get_width() / 2
        self.currY = y - self.image.get_width() / 2

    def setMoveCycleCount(self, count):
        self.moveCycleLen = count

    def draw(self, screen):

        if(self.isImage):
            screen.blit(self.image, (self.currX, self.currY))
            pg.display.flip()
        else:
            self.image.setCoords(self.currX, self.currY)
            self.image.animate(screen)

        if(self.frameCycleCount >= self.moveCycleLen):

            randomx = randint(-40, 40)
            randomy = randint(-40, 40)

            if(self.currX + randomx >= WIDTH - 80 or self.currY + randomy >= HEIGHT - 120
            or self.currX + randomx <= 50 or self.currY + randomy <= 50):
                randomx = randint(-40, 40)
                randomy = randint(-40, 40)
            
            self.currX = self.currX + randomx
            self.currY = self.currY + randomy

            self.frameCycleCount = 0

        self.frameCycleCount = self.frameCycleCount + 1

    def drawWithBorder(self, screen, innerRect, color):
        borderRect = pg.Rect(innerRect.left, innerRect.top,
            innerRect.width + 10, innerRect.height + 10)
        borderRect.center = innerRect.center
        pg.draw.rect(screen, BLACK, borderRect)
        pg.draw.rect(screen, color, innerRect)

    def drawStatBar(self, screen, rect, color, val):
        self.drawWithBorder(screen, rect, WHITE)
        pg.draw.rect(screen, color, pg.Rect(rect.left, rect.top, rect.width * (val / 100), rect.height))