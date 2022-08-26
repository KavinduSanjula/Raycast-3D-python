from cmath import sqrt
import math
import pygame as pg
from pygame import Vector2
from config import CELL_SIZE

from player import Player
from map import Map


class Raycaster:

    def __init__(self, player:Player, map:Map, surface):
        self.surface = surface
        self.angle = 0
        self.player = player
        self.map = map

    def plot(self, x, y):
        pg.draw.circle(self.surface, (20,20,255),(x,y),4)

    def cast_a_ray(self):
        
        ray_dir_x = math.cos(math.radians(self.player.heding))
        ray_dir_y = math.sin(math.radians(self.player.heding))

        step_x = 0
        step_y = 0

        map_x = self.player.position[0] // CELL_SIZE
        map_y = self.player.position[1] // CELL_SIZE

        pos_x_in_cell = self.player.position[0] - int(map_x) * CELL_SIZE
        pos_y_in_cell = self.player.position[1] - int(map_y) * CELL_SIZE

        dx = CELL_SIZE - pos_x_in_cell
        dy = CELL_SIZE - pos_y_in_cell

        dof = 5

        if ray_dir_x > 0:
            
            opp1 = math.tan(math.radians(self.player.heding)) * dx
            y1 = (map_y + 1) * CELL_SIZE + (opp1 - dy)
            x1 = (map_x + 1) * CELL_SIZE
            self.plot(x1,y1)

            for i in range(dof):
                opp = math.tan(math.radians(self.player.heding)) * (dx + CELL_SIZE * i)
                x = (map_x + i+1) * CELL_SIZE
                y = (map_y + 1) * CELL_SIZE + (opp - dy)
                self.plot(x,y)

        else:

            opp1 = math.tan(math.radians(self.player.heding)) * pos_x_in_cell
            y1 = (map_y + 1) * CELL_SIZE + (-opp1-dy)
            x1 = (map_x) * CELL_SIZE
            self.plot(x1,y1)

            for i in range(dof):
                opp = math.tan(math.radians(self.player.heding)) * (pos_x_in_cell + CELL_SIZE * i)
                x = (map_x - i) * CELL_SIZE
                y = (map_y + 1) * CELL_SIZE + (-opp-dy)
                self.plot(x,y)



        pos2X = (self.player.position[0] + dx, self.player.position[1])
        pos2Y = (self.player.position[0] , self.player.position[1] + dy)
        pg.draw.line(self.surface,(255,255,20),self.player.position, pos2X) 
        pg.draw.line(self.surface,(20,255,20),self.player.position, pos2Y) 

        
