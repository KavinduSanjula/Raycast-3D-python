import pygame as pg
from pygame.math import Vector2

from config import CELL_SIZE

class Map:

    def __init__(self):    
        self.cell_size = CELL_SIZE
        _ = False
        self.map = [
        [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,],
        [_,1,1,1,1,1,1,1,1,1,1,_,1,1,1,1,1,1,1,_,],
        [_,1,1,1,1,1,1,1,1,1,1,_,1,1,1,1,1,1,1,_,],
        [_,1,1,1,1,1,1,1,1,1,1,_,1,1,1,1,1,1,1,_,],
        [_,1,1,1,_,1,1,1,1,1,1,_,1,1,1,1,1,1,1,_,],
        [_,1,1,1,_,1,1,_,_,_,_,_,_,_,_,_,_,1,1,_,],
        [_,1,1,1,_,1,1,1,1,1,1,1,1,1,1,1,1,1,1,_,],
        [_,1,1,1,_,1,1,1,1,1,1,1,1,1,1,1,1,1,1,_,],
        [_,1,1,1,_,1,1,1,1,1,1,1,1,1,1,1,1,1,1,_,],
        [_,1,1,1,_,1,1,1,1,1,1,1,1,1,1,1,1,1,1,_,],
        [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,],
    ]

    def draw(self, surface):
        for y,row in enumerate(self.map):
            for x,cell in enumerate(row):
                if not cell:
                    pos_x = x*self.cell_size
                    pos_y = y*self.cell_size
                    pg.draw.rect(surface,(255,255,255),[pos_x, pos_y, self.cell_size, self.cell_size],1)

    def get_cell(self, x,y):
        return self.map[y][x]

    def heighlight_square(self, pos:Vector2, surface):
        pos_x = (pos[0]//self.cell_size) * self.cell_size
        pos_y = (pos[1]//self.cell_size) * self.cell_size
        pg.draw.rect(surface,(0,255,25),[pos_x,pos_y,self.cell_size,self.cell_size])
        


    