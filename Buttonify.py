import pygame

def Buttonify(Picture, coords, surface):

    image = pygame.image.load(Picture)
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image,imagerect)
    
    return (image,imagerect)