import pygame as pg 
from enum import Enum

class PetType(Enum):
    BALA = 0
    MAMAU = 1
    TORA = 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # More colours should be added here
ORANGE = (255, 128, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (127, 0, 255)
WIDTH = 800
HEIGHT = 480


class Pet(pg.sprite.Sprite):

    petType = -1
    name = ""
    food = 100
    water = 100
    sleep = 100
    stress = 0
    picture = "graphicAssets/SpriteBala.png"

    def __init__(self, petType, name):
        WHITE = (255, 255, 255)
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
        self.image = pg.transform.smoothscale(self.image, (105, 135))

    def draw(self, screen, x, y):
        screen.blit(self.image, (x - self.image.get_width() /
            2, y - self.image.get_width() / 2))
        pg.display.flip()

    def drawWithBorder(self, screen, innerRect, color):
        borderRect = pg.Rect(innerRect.left, innerRect.top,
            innerRect.width + 10, innerRect.height + 10)
        borderRect.center = innerRect.center
        pg.draw.rect(screen, BLACK, borderRect)
        pg.draw.rect(screen, color, innerRect)

    def drawStatBar(self, screen, rect, color, val):
        self.drawWithBorder(screen, rect, WHITE)
        pg.draw.rect(screen, color, pg.Rect(rect.left, rect.top, rect.width * (val / 100), rect.height))