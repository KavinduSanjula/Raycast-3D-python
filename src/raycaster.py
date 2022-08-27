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

    

    def cast_a_ray(self, angle):
        
        ray_dir_x = math.cos(math.radians(self.player.heding))
        ray_dir_y = math.sin(math.radians(self.player.heding))
        ray_dir = Vector2(ray_dir_x,ray_dir_y).normalize()

        map_x = self.player.position[0] // CELL_SIZE
        map_y = self.player.position[1] // CELL_SIZE

        pos_x_in_cell = self.player.position[0] - int(map_x) * CELL_SIZE
        pos_y_in_cell = self.player.position[1] - int(map_y) * CELL_SIZE

        delta_x = CELL_SIZE - pos_x_in_cell
        delta_y = CELL_SIZE - pos_y_in_cell

        dof = 15
        dist_vert = 0 # distance to wall from vertical lines
        dist_hori = 0 # distance to wall from horizontal lines

        # Vertical line check
        if ray_dir_x > 0: 
            # cos plus side
            for i in range(dof):
                op = math.tan(math.radians(angle)) * (delta_x + i*CELL_SIZE)
                x_coord = (map_x + i + 1) * CELL_SIZE
                y_coord = (map_y * CELL_SIZE) + pos_y_in_cell + op
                # self.plot(x_coord,y_coord)
                if not self.map.get_cell(int(x_coord//CELL_SIZE), int(y_coord//CELL_SIZE)): break

        else:
            # cos minus side
            for i in range(dof):
                op = math.tan(math.radians(180 - angle)) * (pos_x_in_cell + i*CELL_SIZE)
                x_coord = (map_x - i) * CELL_SIZE
                y_coord = (map_y * CELL_SIZE) + pos_y_in_cell + op
                # self.plot(x_coord,y_coord)
                if not self.map.get_cell(int(x_coord//CELL_SIZE - 1), int(y_coord//CELL_SIZE)): break

        hit_vert = Vector2(x_coord,y_coord)
        dist_vert = (self.player.position - hit_vert).magnitude()

        
        # Horizontal line check
        if ray_dir_y > 0:
            #sin plus side
            for i in range(dof):
                op = math.tan(math.radians(90 - angle)) * (delta_y + i*CELL_SIZE)
                x_coord = (map_x * CELL_SIZE) + pos_x_in_cell + op
                y_coord = (map_y + i + 1) * CELL_SIZE
                # self.plot(x_coord,y_coord)
                if not self.map.get_cell(int(x_coord//CELL_SIZE), int(y_coord//CELL_SIZE)): break

        else:
            # sin minus side
            for i in range(dof):
                op = math.tan(math.radians(90 - angle)) * (pos_y_in_cell + i*CELL_SIZE)
                x_coord = (map_x * CELL_SIZE) + pos_x_in_cell - op
                y_coord = (map_y - i) * CELL_SIZE
                # self.plot(x_coord,y_coord)
                if not self.map.get_cell(int(x_coord//CELL_SIZE), int(y_coord//CELL_SIZE - 1)): break

        hit_hori = Vector2(x_coord,y_coord)
        dist_hori = (self.player.position - hit_hori).magnitude()

        ray_distance = dist_vert if dist_vert < dist_hori else dist_hori
        pg.draw.line(self.surface,(255,255,255),self.player.position, self.player.position + ray_dir*ray_distance)