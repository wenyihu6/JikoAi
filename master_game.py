import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode([100,100])
    screen.fill([25, 226, 230])
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
