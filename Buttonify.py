import pygame

class Buttonify(object):

    def __init__ (self, Picture, coords, surface):

        self.image = pygame.image.load(Picture)
        self.imagerect = self.image.get_rect()
        self.imagerect.topright = coords
        self.surface = surface

    def getImageRect(self):
        return self.imagerect

    def draw(self): 
        self.surface.blit(self.image, self.imagerect)

    