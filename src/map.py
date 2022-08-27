import pygame as pg
from pygame.math import Vector2

from config import CELL_SIZE

class Map:

    def __init__(self):
        _ = False
        self.map = [
        [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,],
        [_,1,1,1,1,1,1,1,1,1,1,_,1,1,1,1,1,1,1,_,],
        [_,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,_,],
        [_,1,1,1,1,1,1,1,1,1,1,_,1,1,1,1,1,1,1,_,],
        [_,1,1,1,_,1,1,1,1,1,1,_,1,1,1,1,1,1,1,_,],
        [_,1,1,1,_,1,1,_,_,_,_,_,_,_,_,_,_,1,1,_,],
        [_,1,1,1,_,1,1,1,1,1,1,_,1,1,1,1,1,1,1,_,],
        [_,1,1,1,_,1,1,1,1,1,1,_,1,1,1,1,1,1,1,_,],
        [_,1,1,1,_,1,1,1,1,1,1,1,1,1,1,1,1,1,1,_,],
        [_,1,1,1,_,1,1,1,1,1,1,_,1,1,1,1,1,1,1,_,],
        [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,],
    ]

    def draw(self, surface):
        for y,row in enumerate(self.map):
            for x,cell in enumerate(row):
                if not cell:
                    pos_x = x* CELL_SIZE
                    pos_y = y* CELL_SIZE
                    pg.draw.rect(surface,(255,255,255),[pos_x, pos_y, CELL_SIZE, CELL_SIZE],1)

    def get_cell(self, x,y):
        try:
            return self.map[y][x]
        except:
            return False

    def heighlight_square(self, pos:Vector2, surface):
        pos_x = (pos[0]// CELL_SIZE) *  CELL_SIZE
        pos_y = (pos[1]// CELL_SIZE) *  CELL_SIZE
        pg.draw.rect(surface,(0,255,25),[pos_x,pos_y, CELL_SIZE, CELL_SIZE])
        


    