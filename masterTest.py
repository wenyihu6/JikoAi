import sys
import pygame as pg

WIDTH = 800
HEIGHT = 480

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)

def main():

    while True:

        clock = pg.time.Clock()

        ev = pg.event.get()
        screen.fill((0, 0, 0))

        for event in ev:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()


main()
