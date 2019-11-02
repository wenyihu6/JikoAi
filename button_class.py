from enum import Enum
from GIFImage import GIFImage
import pygame 
import platform

vec = pygame.math.Vector2
#done by following a youtube tutorial (A Plus Coding)
class Screen(Enum):
    STARTING = 0
    HOME = 1
    EGG = 2
    Q_A = 3
    HATCH = 4
    FOOD = 5
    WATER = 6
    FUN = 7


class Button:

    def _init_(self, surface, x, y, width, height, state = '', function = 0, color = (255, 255, 255), 
    hover_color = (255, 255, 255), border= True, border_width = 2, border_colour = (0, 0, 0), txt= False,
    text ='', font_name = 'arial', text_size = 20, text_color = (0, 0, 0), check_bold= False):

        #information of the button
        self.x = x
        self.y = y
        self.pos = vec(x, y)
        self.width = width
        self.height = height

        #present an image
        self.surface = surface
        self.image = pygame.Surface((width, height))
        self.fill = pygame.Surface.fill(color)
        self.rect = self.image.get_rect() 
        #reference top center as the position of the rectangle 
        self.rect.topCenter = self.pos

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
            self.image.blit(text, pos)
            
        #call function by clicking the function (arguments)
        def click(self): 
            if self.function != 0:
                self.function()
# class Button:

#     def _init_(self, surface, x, y, width, height, state = '', function = 0, color = (255, 255, 255), hover_color = (255, 255, 255), border= True, border_width = 2, border_colour = (0, 0, 0), text ='', font_name = 'arial', text_size = 20, text_color = (0, 0, 0), bold_text= False);

class State():
    #def_init_ 

def main():

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255) # More colours should be added here
    WIDTH = 800
    HEIGHT = 480

    pygame.font.init()
    titleFont = pygame.font.SysFont('VT323-Regular.ttf', 180)
    textFont = pygame.font.SysFont('VT323-Regular.ttf', 100)
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    titleBG = GIFImage("graphicAssets/BgTitle2.gif")
    # titleBG = pg.transform.scale(titleBG.getImage, (1280, 720))
    
    currGameState = Screen.STARTING

    while True:
        ev = pygame.event.get()
        screen.fill(WHITE)

        if currGameState == Screen.STARTING:

            outerRect = pygame.Rect(WIDTH / 2, HEIGHT / 2, 410, 160)
            innerRect = pygame.Rect(WIDTH / 2, HEIGHT / 2, 390, 140)
            outerRect.centerx = WIDTH / 2 #draw rectangles at the center of the screen
            outerRect.centery = HEIGHT / 2
            innerRect.center = outerRect.center
            pygame.draw.rect(screen, BLACK, outerRect)
            pygame.draw.rect(screen, WHITE, innerRect)
                    
            title = titleFont.render('JikoAi', True, (0, 0, 0))
            screen.blit(title,(WIDTH / 4 + 13, HEIGHT / 2 - 57))

            titleBG.render(screen, (0, 0))
            pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                currGameState = Screen.HOME
                mouse = pygame.mouse.get_pos()
                
        elif currGameState == Screen.HOME:
            welcome = textFont.render('h', True, (0, 0, 0))
            screen.blit(welcome,(WIDTH / 4 + 13, HEIGHT / 2 - 57))
        
        elif currGameState == Screen.EGG:
            print("FILLER")
        elif currGameState == Screen.FOOD:
            print("FILLER")
        elif currGameState == Screen.HATCH:
            print("FILLER")
        elif currGameState == Screen.Q_A:
            print("FILLER")
        elif currGameState == Screen.WATER:
            print("FILLER")
        elif currGameState == Screen.FUN:
            print("FILLER")
            
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
                system.exit()


main()