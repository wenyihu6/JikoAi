#Assets from: https://www.megupets.com/
import pygame 
from GIFImage import GIFImage
vec = pygame.math.Vector2


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
titleBG = GIFImage("graphicAssets/BgTitle2.gif")
#image = pygame.image.load(r'graphicAssets/BgTitle.gif') 

class Button:

    def __init__(self, surface, x, y, width, height, state = '', function = 0, color = (255, 255, 255), 
    hover_color = (255, 255, 255), border= True, border_width = 2, border_colour = (0, 0, 0), txt= False,
    text ='', font_name = 'arial', text_size = 20, text_color = (0, 0, 0), check_bold= False):

        #information of the button
        self.x = x
        self.y = y
        self.pos = vec(x, y)
        self.width = width
        self.height = height

        #draw on the image
        self.surface = surface
        self.image = pygame.Surface((width, height))
        self.fill = self.image.fill(color)
        self.rect = self.image.get_rect() 

        #call this function when button is clicked 
        self.function = function 
        #background color of the button
        self.color = color 
        #change color if button is hovered
        self.mouse_hover_color = hover_color 
        #check if border is needed for the button
        self.border = border 
        #information of the border
        self.border_width = border_width 
        self.border_colour = border_colour 
        #text to put inside the button (give font, text, size, color, and whether bold text is wanted)
        self.txt = txt
        self.text = text 
        self.font_name = font_name
        self.text_size = text_size
        self.text_color = text_color
        self.check_bold = check_bold
        #initialize mouse hover as false
        self.hovered = False 

        #call function by Button.mouse_hovering(arguments)
    def mouse_hovering(self, pos):
        #check if mouse is in the x axis of the button 
        if pos[0] > self.pos[0] and pos[0]<self.pos[0] + self.width:
        #check if mouse is in the y axis of the button 
            if pos[1] > self.pos[1] and pos[1] < self.pos[1] + self.height:
                return True
        return False

    #call function by Button.update(arguments)
    def update (self, pos):
        #call function to check if mouse is hovered and update the position 
        if self.mouse_hovering(pos): 
            self.hovered = True
        else: 
            self.hovered = False 
        
        #call function by Button.draw(arguments)
    def draw (self):
        #if we want border for button
        if self.border: 
            self.fill(self.border.color)
            if self.hovered:
                #if it is hovered, draw the rectangle with other mouse hover color otherwise with original color 
                pygame.draw.rect(self.image, self.mouse_hover_color, (self.border_width, self.border_width, self.width-(self.border_width*2), self.height-(self.border_width*2))) 
            else:
                pygame.draw.rect(self.image, self.color, (self.border_width, self.border_width, self.width-(self.border_width*2), self.height-(self.border_width*2))) 
   
            #if we do not want border for button   
        else:
            self.fill(self.color)

            #if we want text on button           
        if self.txt:
            self.show_text()

        #draw image on top of the surface
        #overlap the surface and can present the image from a loaded library at the given position
        self.surface.blit(self.image, self.pos)

        #call function by Button.show_text(arguments)
    def show_text(self):
        font = pygame.font.SysFont(self.font_name, self.text_size, bold = self.check_bold)
        text = font.render(self.text, False, self.text_color)
        size = text.get_size() 
        pos = vec(self.width//2-(size[0]//2), self.height//2-(size[1]//2))
        #draw text on top of the surface 
        self.surface.blit(text, pos)
            
    #call function by clicking the function (arguments)
    def click(self): 
        if self.function != 0:
            self.function()

# infinite loop 
while True : 
    # completely fill the surface object 
    # with white colour 
    display_surface.fill(white) 
    titleBG.render(display_surface, (0, 0))
    pygame.display.update()
    
    homeButton = Button(display_surface, 50, 50, 100, 100, state = '', function = 0, color = (233, 255, 255), hover_color = (454, 255, 255), border= True, border_width = 2, border_colour = (0, 0, 0), txt= True, text ='dfdf', font_name = 'arial', text_size = 20, text_color = (0, 0, 0), check_bold= True)

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
        
