import pygame
from GIFImage import GIFImage
from RectButton import RectButton
from datetime import datetime

class Meditate(object):

    def __init__(self, screen):
        self.screen = screen
        self.isOn = False
        self.labelArray = [self.drawLabel(100, 100)]
        self.textArray = ["sample"]

    def setOn(self):
        if(self.isOn == False):
            self.isOn = True
            self.initTime = datetime.now()
        self.run()
    
    def setOff(self):
        if(self.isOn == True):
            self.isOff = False

    def run(self):
        timeNow = datetime.now()
        if((timeNow - self.initTime).seconds >= 0 and (timeNow - self.initTime).seconds <= 3):
            self.fadeIn(self.labelArray[0], self.textArray[0])
        elif((timeNow - self.initTime).seconds >= 3 and (timeNow - self.initTime).seconds <= 5):
            self.fadeOut(self.labelArray[0], self.textArray[0])

    def drawLabel(self, x, y, width = 215, height = 50, colour = (0, 0, 0), alpha = 0):
        rect = RectButton(x, y, width, height, self.screen, colour, alpha)
        return rect

    def fadeIn(self, rectLabel, text):
        if(rectLabel.getAlpha() < 120):
            rectLabel.setAlpha(rectLabel.getAlpha() + 1)
        rectLabel.draw()
        rectLabel.draw_text_self(text)
    
    def fadeOut(self, rectLabel, text):
        if(rectLabel.getAlpha() > 0):
            rectLabel.setAlpha(rectLabel.getAlpha() - 1)
        rectLabel.draw()
        rectLabel.draw_text_self(text)
        

        

        


    