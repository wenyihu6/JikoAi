import pygame
from GIFImage import GIFImage
from RectButton import RectButton
from datetime import datetime

class Affirmations(object):

    def __init__(self, screen):
        self.screen = screen
        self.speechParsed = False
        self.initTime = datetime.now()
        self.subtitle = RectButton(50, 70, 700, 50, self.screen, (0, 0, 0), 100)
        self.subtitleText = "Say something positive into the mic!"
        self.afterSpeechText = "Thanks for being positive! Your pet's stats will be updated! <3"
        self.displayText = "lorem ipsum"
        self.labelArray = [self.drawLabel(100, 150, 610, 290), self.drawLabel(10, 135, 780, 325)]

    def setSpeechParsed(self, isParsed):
        self.speechParsed = isParsed
        if(isParsed == True):
            self.initTime = datetime.now()

    def setDisplayText(self, text):
        self.displayText = text

    def run(self):
        
        timeNow = datetime.now()
        self.subtitle.draw()
        self.subtitle.draw_text(self.subtitleText)
        
        if(self.speechParsed == True) :
            if((timeNow - self.initTime).seconds >= 0 and (timeNow - self.initTime).seconds <= 4):
                if(len(self.displayText) > 30): 
                    self.fadeIn(self.labelArray[1], self.displayText, 30)
                else:
                    self.fadeIn(self.labelArray[0], self.displayText)
            elif((timeNow - self.initTime).seconds > 4 and (timeNow - self.initTime).seconds <= 7):
                if(len(self.displayText) > 30): 
                    self.fadeOut(self.labelArray[1], self.displayText, 30)
                else:
                    self.fadeOut(self.labelArray[0], self.displayText)
            elif((timeNow - self.initTime).seconds > 7 and (timeNow - self.initTime).seconds <= 10):
                self.fadeIn(self.labelArray[1], self.afterSpeechText, 30)
            elif((timeNow - self.initTime).seconds > 10 and (timeNow - self.initTime).seconds <= 13):
                self.fadeOut(self.labelArray[1], self.afterSpeechText, 30)
            elif((timeNow - self.initTime).seconds >= 13):
                self.labelArray[0].emptySelf()
                self.labelArray[1].emptySelf()
                self.setSpeechParsed(False)

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

        

        

        


    