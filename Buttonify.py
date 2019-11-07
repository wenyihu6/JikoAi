import pygame

class Buttonify(object):

    def __init__ (self, Picture, x, y, surface):

        self.image = pygame.image.load(Picture)
        self.imagerect = self.image.get_rect()
        self.imagerect.topright = (x, y)
        self.surface = surface

    def getImageRect(self):
        return self.imagerect

    def draw(self): 
        self.surface.blit(self.image, self.imagerect)
    
    def resize(self, width, height): 
        self.image = pygame.transform.scale(self.image, (width, height))
        self.imagerect = self.image.get_rect()
    
    def setCoords(self, x, y): #Set coordinates
        self.imagerect.topright = (x, y)

    