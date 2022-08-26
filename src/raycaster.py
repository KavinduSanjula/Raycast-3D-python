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
        dir = Vector2(ray_dir_x,ray_dir_y).normalize()

        step_x = 0
        step_y = 0

        map_x = self.player.position[0] // CELL_SIZE
        map_y = self.player.position[1] // CELL_SIZE

        pos_x_in_cell = self.player.position[0] - int(map_x) * CELL_SIZE
        pos_y_in_cell = self.player.position[1] - int(map_y) * CELL_SIZE

        delta_x = CELL_SIZE - pos_x_in_cell
        delta_y = CELL_SIZE - pos_y_in_cell

        dof = 15
        dist_x = 0
        dist_y = 0

        if ray_dir_x > 0:

            for i in range(dof):
                opp = math.tan(math.radians(self.player.heding)) * (delta_x + CELL_SIZE * i)
                x = (map_x + i+1) * CELL_SIZE
                y = (map_y + 1) * CELL_SIZE + (opp - delta_y)
                # self.plot(x,y)

                if not self.map.get_cell(int(x//CELL_SIZE), int(y//CELL_SIZE)): break

        else:

            for i in range(dof):
                opp = math.tan(math.radians(self.player.heding)) * (pos_x_in_cell + CELL_SIZE * i)
                x = (map_x - i) * CELL_SIZE
                y = (map_y + 1) * CELL_SIZE + (-opp-delta_y)
                # self.plot(x,y)

                if not self.map.get_cell(int(x//CELL_SIZE) -1, int(y//CELL_SIZE)): break

        hit_x = Vector2(x,y)
        distance_x = (self.player.position - hit_x).magnitude()
        


        if ray_dir_x > 0:

            if ray_dir_y < 0:
                for i in range(0, dof):
                    op = math.tan(math.radians(90 - self.player.heding)) * (pos_y_in_cell + (CELL_SIZE * i))
                    x = (map_x * CELL_SIZE) + pos_x_in_cell + -op
                    y = (map_y - i) * CELL_SIZE
                    # self.plot(x,y)
                    
                    if not self.map.get_cell(int(x//CELL_SIZE), int(y//CELL_SIZE)-1): break



            else:
                for i in range(0, dof):
                    op = math.tan(math.radians(90 - self.player.heding)) * (delta_y + (CELL_SIZE * i))
                    x = (map_x * CELL_SIZE) + pos_x_in_cell + op
                    y = (map_y + i+1) * CELL_SIZE
                    # self.plot(x,y)
                    
                    if not self.map.get_cell(int(x//CELL_SIZE), int(y//CELL_SIZE)): break


        else:

            if ray_dir_y < 0:
                angle = self.player.heding - 90

                for i in range(0, dof):
                    op = math.tan(math.radians(angle)) * (pos_y_in_cell + (CELL_SIZE * i))
                    x = (map_x + 1) * CELL_SIZE - delta_x + op
                    y = (map_y - i) * CELL_SIZE
                    # self.plot(x,y)
                    
                    if not self.map.get_cell(int(x//CELL_SIZE), int(y//CELL_SIZE)-1): break

            else:
                angle = 90 - (self.player.heding - 180)

                for i in range(0, dof):
                    op = math.tan(math.radians(angle)) * (delta_y + (CELL_SIZE * i))
                    x = (map_x + 1) * CELL_SIZE - delta_x + op
                    y = (map_y + i+1) * CELL_SIZE
                    # self.plot(x,y)

                    if not self.map.get_cell(int(x//CELL_SIZE), int(y//CELL_SIZE)): break
                
        hit_y = Vector2(x,y)
        distance_y = (self.player.position - hit_y).magnitude()
        
        ray_distance = distance_x if distance_x < distance_y else distance_y

        pg.draw.line(self.surface,(255,255,255),self.player.position, self.player.position + dir*ray_distance)





        # pos2X = (self.player.position[0] + delta_x, self.player.position[1])
        # pos2Y = (self.player.position[0] , self.player.position[1] + delta_y)
        # pg.draw.line(self.surface,(255,255,20),self.player.position, pos2X) 
        # pg.draw.line(self.surface,(20,255,20),self.player.position, pos2Y) 

        
