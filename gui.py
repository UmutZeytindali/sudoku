import pygame as pg
import numpy as np
import sys
from sudoku import check_nums, solution


pg.init()

# misc. vars
screen = pg.display.set_mode((750, 750))
pg.display.set_caption("Sudoku")
WINDOW_ICON = pg.image.load("sudoku/sudoku.svg")
pg.display.set_icon(WINDOW_ICON)
clock = pg.time.Clock()
font = pg.font.SysFont(None, 80)


def draw_background():
    screen.fill(pg.Color("gray"))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 720, 720), 10)
    i = 1
    while (i * 80) < 720:
        line_width = 5 if i % 3 > 0 else 10
        pg.draw.line(
            screen,
            pg.Color("Black"),
            pg.Vector2((i * 80) + 15, 15),
            pg.Vector2((i * 80) + 15, 735),
            line_width,
        )
        pg.draw.line(
            screen,
            pg.Color("Black"),
            pg.Vector2(15, (i * 80) + 15),
            pg.Vector2(735, (i * 80) + 15),
            line_width,
        )
        i += 1


def draw_numbers():
    global grid
    row = 0
    offset = 40
    while row < 9:
        col = 0
        while col < 9:
            output = grid[row][col]
            n_text = font.render(str(output), True, pg.Color("Black"))
            screen.blit(
                n_text, pg.Vector2((col * 80) + offset + 5, (row * 80) + offset - 2)
            )
            col += 1
        row += 1


def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit("")
    pg.display.update()
    clock.tick(60)
    draw_background()
    draw_numbers()


while True:
    game_loop()
