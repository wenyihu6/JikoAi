import os
import pygame
from PIL import Image

class gifImage(object):

    def __init__(self, folderPath, x ,y):
        self.folderPath = folderPath
        self.imgNames = []
        self.images = []
        self.x = 0
        self.y = 0
        self.frameNum = 0
        self.getFrames()

    def setCoords(x, y):
        self.x = x  
        self.y = y

    def getFrames(self):
        self.imgNames = os.listdir(self.folderPath)
        print(self.imgNames)
        for i in range(len(self.imgNames)):
            print(i)
            self.images.append(pygame.image.load(self.folderPath + "/" + self.imgNames[i]))

    def animate(self, screen):
        screen.blit(self.images[self.frameNum], (self.x, self.y))
        self.frameNum = self.frameNum + 1
        if self.frameNum >= len(self.images):
            self.frameNum = 0

