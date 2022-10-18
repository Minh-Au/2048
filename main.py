from ctypes.wintypes import RGB
import sys
from turtle import Screen, color
import pygame as pg

def main():
    pg.init()
    SIZE = WIDTH, HEIGHT = 550, 800
    SCREEN = pg.display.set_mode(SIZE)
    BGCOLOR = 250,248,239

    GRID_BGCOLOR = 187,173,160
    GRID_SIZE = 500, 500
    GRID_POS = (WIDTH /2, HEIGHT - GRID_SIZE[0]/2 - 30)
    GRID_RECT = pg.Rect((0, 0), GRID_SIZE)
    GRID_RECT.center = GRID_POS

    CELL_SIZE = 106, 106
    CELL_COLOR = 238,228,218,0.35
    PADDING = (GRID_SIZE[0] - CELL_SIZE[0])/5
    CELL_RECTS = [[pg.Rect((x*CELL_SIZE[0] + PADDING, y*CELL_SIZE[0] + PADDING), CELL_SIZE) for y in range(0,4)] for x in range(0,4)]
     
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        
        SCREEN.fill(BGCOLOR) # reset screen
        pg.draw.rect(SCREEN, GRID_BGCOLOR, GRID_RECT)
        drawCells(SCREEN, CELL_COLOR, CELL_RECTS)
        pg.display.flip()

def drawCells(screen:pg.Surface, color:tuple, rects: list[list[pg.Rect]]) -> None:
    for x in rects:
        for y in x:
            pg.draw.rect(screen, color, y)

if __name__ == '__main__':
    main()
