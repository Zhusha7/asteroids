import pygame as pg
from constants import *

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill(color="black")
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

if __name__ == "__main__":
    main()