#Assets from: https://www.megupets.com/
import pygame 
from GIFImage import GIFImage

# import pygame module in this program 
  
# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 
  
# define the RGB value 
# for white colour 
white = (255, 255, 255) 
  
# assigning values to X and Y variable 
X = 400
Y = 400
  
# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y )) 
  
# set the pygame window name 
pygame.display.set_caption('Image') 
  
# create a surface object, image is drawn on it. 
titleBG = GIFImage("graphicAssets/BgTitle.gif")
#image = pygame.image.load(r'graphicAssets/BgTitle.gif') 

# infinite loop 
while True : 
  
    # completely fill the surface object 
    # with white colour 
    display_surface.fill(white) 
    titleBG.render(display_surface, (0, 0))
    pygame.display.update() 
    # copying the image surface object 
    # to the display surface object at 
    # (0, 0) coordinate. 
    # display_surface.blit(image, (0, 0)) 

    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
  
            # deactivates the pygame library 
            pygame.quit() 
  
            # quit the program. 
            quit() 
  
        # Draws the surface object to the screen.   
        