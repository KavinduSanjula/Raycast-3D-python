from re import M
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
        currnt_point = self.player.position
        while True:
            currnt_point = currnt_point + self.player.heding_vector * self.step

            x = int(currnt_point[0]//self.map.cell_size)
            y = int(currnt_point[1]//self.map.cell_size)

            if not self.map.get_cell(x,y):
                break

        pg.draw.line(self.surface,(255,255,0),self.player.position,currnt_point)
