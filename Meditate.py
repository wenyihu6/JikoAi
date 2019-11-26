import pygame
from GIFImage import GIFImage
from RectButton import RectButton
from datetime import datetime

class Meditate(object):

    def __init__(self, screen):
        self.screen = screen
        self.isOn = False
        self.labelArray = [self.drawLabel(100, 100, 610, 325), self.drawLabel(10, 75, 780, 375)]
        self.textArray = ["Sit in a comfortable position.", "Now, start breathing naturally.",
            "Make no effort to control the breath.", "Simply let it be.",
            "Focus your attention on the breath.", "Focus on how the body moves with each breath.",
            "When ready, close your eyes and breathe for as long as you need.",
            "Thanks for being mindful! Your pet's stats will update. :D"]

    def setOn(self):
        if(self.isOn == False):
            self.isOn = True
            self.initTime = datetime.now()
        self.run()
    
    def setOff(self):
        if(self.isOn == True):
            self.isOn = False

    def run(self):
        timeNow = datetime.now()
        if((timeNow - self.initTime).seconds >= 0 and (timeNow - self.initTime).seconds <= 3):
            self.fadeIn(self.labelArray[0], self.textArray[0])
        elif((timeNow - self.initTime).seconds > 3 and (timeNow - self.initTime).seconds <= 6):
            self.fadeOut(self.labelArray[0], self.textArray[0])
        elif((timeNow - self.initTime).seconds > 6 and (timeNow - self.initTime).seconds <= 9):
            self.fadeIn(self.labelArray[0], self.textArray[1])
        elif((timeNow - self.initTime).seconds > 9 and (timeNow - self.initTime).seconds <= 12):
            self.fadeOut(self.labelArray[0], self.textArray[1])
        elif((timeNow - self.initTime).seconds > 12 and (timeNow - self.initTime).seconds <= 15):
            self.fadeIn(self.labelArray[0], self.textArray[2])
        elif((timeNow - self.initTime).seconds > 15 and (timeNow - self.initTime).seconds <= 18):
            self.fadeOut(self.labelArray[0], self.textArray[2])
        elif((timeNow - self.initTime).seconds > 18 and (timeNow - self.initTime).seconds <= 21):
            self.fadeIn(self.labelArray[0], self.textArray[3])
        elif((timeNow - self.initTime).seconds > 21 and (timeNow - self.initTime).seconds <= 24):
            self.fadeOut(self.labelArray[0], self.textArray[3]) 
        elif((timeNow - self.initTime).seconds > 24 and (timeNow - self.initTime).seconds <= 27):
            self.fadeIn(self.labelArray[0], self.textArray[4])
        elif((timeNow - self.initTime).seconds > 27 and (timeNow - self.initTime).seconds <= 30):
            self.fadeOut(self.labelArray[0], self.textArray[4])
        elif((timeNow - self.initTime).seconds > 30 and (timeNow - self.initTime).seconds <= 33):
            self.fadeIn(self.labelArray[0], self.textArray[5], 30)
        elif((timeNow - self.initTime).seconds > 33 and (timeNow - self.initTime).seconds <= 36):
            self.fadeOut(self.labelArray[0], self.textArray[5], 30)
        elif((timeNow - self.initTime).seconds > 36 and (timeNow - self.initTime).seconds <= 41):
            self.fadeIn(self.labelArray[1], self.textArray[6], 30)
        elif((timeNow - self.initTime).seconds > 41 and (timeNow - self.initTime).seconds <= 45):
            self.fadeOut(self.labelArray[1], self.textArray[6], 30)
        elif((timeNow - self.initTime).seconds > 45 and (timeNow - self.initTime).seconds <= 50):
            self.fadeIn(self.labelArray[1], self.textArray[7], 30)
        elif((timeNow - self.initTime).seconds > 50 and (timeNow - self.initTime).seconds <= 53):
            self.fadeOut(self.labelArray[1], self.textArray[7], 30)


    def drawLabel(self, x, y, width = 215, height = 50, colour = (0, 0, 0), alpha = 0):
        rect = RectButton(x, y, width, height, self.screen, colour, alpha)
        return rect

    def fadeIn(self, rectLabel, text, size = 40):
        if(rectLabel.getAlpha() < 250):
            rectLabel.setAlpha(rectLabel.getAlpha() + 4)
        rectLabel.draw()
        rectLabel.draw_text_self(text, size)
    
    def fadeOut(self, rectLabel, text, size = 40):
        if(rectLabel.getAlpha() > 0):
            rectLabel.setAlpha(rectLabel.getAlpha() - 4)

        rectLabel.draw()
        rectLabel.draw_text_self(text, size)

        if(rectLabel.getAlpha() <= 60):
            rectLabel.emptySelf()

        

        

        


    