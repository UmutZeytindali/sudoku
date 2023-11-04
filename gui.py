import pygame as pg
from sys import exit

pg.init()

# misc. vars
screen = pg.display.set_mode((600, 700))
pg.display.set_caption("Sudoku Çözücü")
WINDOW_ICON = pg.image.load("sudoku/sudoku.svg")
pg.display.set_icon(WINDOW_ICON)
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    pg.display.update()
    clock.tick(60)
