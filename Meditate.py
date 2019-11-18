import pygame
import GIFImage
import RectButton

class Meditate(object):

    def __init__(self, screen):
        self.screen = screen
    
    def drawLabel(x, y, width = 215, height = 50, colour = (0, 0, 0), alpha = 100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.alpha = alpha

        rectButton = new RectButton(self.x, self.y, self.width, self.height, self.screen, self.colour, self.alpha)
        rectButton