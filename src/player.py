import pygame as pg
from pygame.math import Vector2
import math


class Player:

    def __init__(self, position:Vector2):
        self.position = position

        self.heding = -30
        self.heding_vector = Vector2((math.cos(math.radians(self.heding)), math.sin(math.radians(self.heding)))).normalize()
        self.size = 10
        self.speed = 5
        self.rotation_speed = 2.5

    def update(self):
        self.controls()

    def controls(self):
        if pg.key.get_pressed()[pg.K_a]:
            self.move_right(-1)

        if pg.key.get_pressed()[pg.K_d]:
            self.move_right()

        if pg.key.get_pressed()[pg.K_w]:
            self.move_forward()

        if pg.key.get_pressed()[pg.K_s]:
            self.move_forward(-1)

        if pg.key.get_pressed()[pg.K_LEFT]:
            self.rotate(-1)

        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.rotate(1)

    def draw(self,surface):
        pass
        pg.draw.circle(surface,(255,20,10),self.position,self.size)
        pg.draw.line(surface,(150,150,255),self.position,self.position + self.heding_vector * 50)


    def move_forward(self, dir = 1):
        self.position += self.heding_vector * dir * self.speed

    def move_right(self, dir = 1):
        self.position += self.get_right_vector() * dir * self.speed

    def rotate(self, angle):
        self.heding += angle * self.rotation_speed
        self.heding_vector = Vector2((math.cos(math.radians(self.heding)), math.sin(math.radians(self.heding)))).normalize()



    def get_right_vector(self):
        a = self.heding + 90
        right_vector = Vector2((math.cos(math.radians(a)), math.sin(math.radians(a)))).normalize()
        return right_vector