import pygame

class RectButton(object):

    def __init__ (self, x, y, width, height, surface, colour = (0, 0, 0), alpha = 128):
        self.width = width
        self.height = height
        self.colour = colour
        self.alpha = alpha
        self.surface = surface

        self.button = pygame.Surface((width, height))
        self.button.set_alpha(alpha)
        self.button.fill(colour)
        
        self.imagerect = self.button.get_rect()
        self.imagerect.topleft = (x, y)

    def getImageRect(self):
        return self.imagerect

    def draw(self): 
        self.surface.blit(self.button, self.imagerect)

    def resize(self, width, height): 
        self.width = width
        self.height = height
        self.button = pygame.transform.scale(self.button, (self.width, self.height))
        self.imagerect = self.button.get_rect()
    
    def setCoords(self, x, y): 
        self.imagerect.topleft = (x, y)

    def setAlpha(self, alpha):
        self.alpha = alpha
        self.button.set_alpha(alpha)


