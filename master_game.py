import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    screen.display.set_caption('jiko-ai')
    screen.display.fill([255, 255, 255])
    #running state of the game variable
    run = True
    while run:
        #event handling and visuals go in here
        for event in pygame.event.get():
            #can do other stuff in here for listeners
            if event.type == pygame.QUIT:
                run = False

if __name__ == "__main__":
    main()
