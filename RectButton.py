import pygame

class RectButton(object):
    pygame.font.init()

    def __init__ (self, x, y, width, height, surface, colour = (0, 0, 0), alpha = 128):
        self.width = width
        self.height = height
        self.colour = colour
        self.alpha = alpha
        self.surface = surface
        self.x = x
        self.y = y

        self.button = pygame.Surface((width, height))
        self.button.set_alpha(alpha)
        self.button.fill(colour)
        
        self.imagerect = self.button.get_rect()
        self.imagerect.topleft = (x, y)

    def getImageRect(self): 
        return self.imagerect

    def draw(self): 
        self.surface.blit(self.button, self.imagerect)

    def draw_text(self, text = "", font = pygame.font.Font("VT323-Regular.ttf", 40)):
        self.text = font.render(text, True, (255, 255, 255))
        text_rect = self.text.get_rect(center=self.imagerect.center)
        self.surface.blit(self.text, text_rect)

    def draw_text_self(self, text = "", font = pygame.font.Font("VT323-Regular.ttf", 40)):
        self.text = font.render(text, True, (255, 255, 255))
        text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.button.blit(self.text, text_rect)

    def resize(self, width, height): 
        self.width = width
        self.height = height
        self.button = pygame.transform.scale(self.button, (self.width, self.height))
        self.imagerect = self.button.get_rect()
    
    def setCoords(self, x, y): 
        self.x = x
        self.y = y
        self.imagerect.topleft = (x, y)

    def setAlpha(self, alpha):
        self.alpha = alpha
        self.button.set_alpha(alpha)

    def getAlpha(self):
        return self.alpha


