import pygame as pg
from pygame import Vector2

from player import Player
from map import Map


class Raycaster:

    def __init__(self, player:Player, map:Map, surface):
        self.surface = surface
        self.angle = 0
        self.player = player
        self.map = map
        self.step = 10

    def cast_a_ray(self):
        x1,y1 = 0,0
        x2,y2 = 10,0
        dx,dy = (x2-x1), (y2-y1)
        x,y = 0,0

        if abs(dx) > abs(dy):
            step = abs(dx)
        else:
            step = abs(dy)

        x_inc = dx/step
        y_inc = dy/step

        x = x1
        y = y1

        pg.draw.rect(self.surface,(255,255,200),
        [round(x) * self.map.cell_size, round(y) * self.map.cell_size, self.map.cell_size,self.map.cell_size])

        while True:
            x += x_inc
            y += y_inc

            pg.draw.rect(self.surface,(255,255,200),
            [round(x) * self.map.cell_size, round(y) * self.map.cell_size, self.map.cell_size,self.map.cell_size])
            pg.draw.circle(self.surface, (20,20,255),(x* self.map.cell_size,y* self.map.cell_size),5)

            if x>= x2: break
            
