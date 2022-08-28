import math
from typing import List
import pygame as pg

from config import FOV, HEIGHT, RAY_COUNT, WIDTH


class Renderer:

    def __init__(self):

        self.max_wall_height = HEIGHT / 2
        self.wall_width = WIDTH / RAY_COUNT
        self.screen_dist = (WIDTH/2) * math.tan(math.radians(FOV/2))

    def render(self, distance_list, surface):
        pg.draw.rect(surface, (200,200,255),[0, 0, WIDTH, HEIGHT/2])
        pg.draw.rect(surface, (50,50,50),[0, HEIGHT/2, WIDTH, HEIGHT])

        for i, dist in enumerate(distance_list):
            self.draw_rect(dist,i,surface)


    def draw_rect(self, dist, id, surface):
 
        proj_height = self.screen_dist / (dist + 0.00001)

        wall_height = proj_height * self.max_wall_height
        color = [255 / (1 + dist * 0.005)] * 3

        x_pos = id * self.wall_width
        y_pos = HEIGHT / 2 + -wall_height / 2

        pg.draw.rect(surface,color,[x_pos, y_pos, self.wall_width+1, wall_height])
