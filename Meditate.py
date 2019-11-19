import pygame
import datetime
import GIFImage
import RectButton

class Meditate(object):

    def __init__(self, screen):
        self.screen = screen
        self.isOn = False
        self.labels = []

    def setOn(self):
        if(self.isOn == False):
            self.isOn = True
            self.initTime = datetime.datetime.now()
        self.run()
    
    def setOff(self):
        if(self.isOn == True):
            self.isOff = False

    def run(self):


    def drawLabel(self, x, y, text, width = 215, height = 50, colour = (0, 0, 0), alpha = 0):
        self.text = text
        self.rectButton = RectButton(self.x, self.y, self.width, self.height, self.screen, self.colour, self.alpha)
    
    def fadeIn(self, rectLabel):
        if(rectLabel.getAlpha() < 100)
            rectLabel.setAlpha(rectLabel.getAlpha() + 1)
        rectLabel.draw()
        rectLabel.draw_text(self.text)
    
    def fadeOut(self, rectLabel)
        if(rectLabel.getAlpha() > 0)
            rectLabel.setAlpha(rectLabel.getAlpha() - 1)
        rectLabel.draw()
        rectLabel.draw_text()
        

        

        


    