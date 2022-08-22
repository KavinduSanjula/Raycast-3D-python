import pygame as pg
from pygame.math import Vector2
import math


class Player:

    def __init__(self, position:Vector2):
        self.position = position

        self.heding = 0
        self.heding_vector = Vector2((math.cos(self.heding), math.sin(self.heding))).normalize()
        self.size = 10
        self.speed = 5

    def update(self, surface):
        self.controls()
        self.draw(surface)

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
            self.rotate(-.05)

        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.rotate(.05)

    def draw(self,surface):
        pg.draw.circle(surface,(255,20,10),self.position,self.size)
        pg.draw.line(surface,(150,150,255),self.position,self.position + self.heding_vector * 50)


    def move_forward(self, dir = 1):
        self.position += self.heding_vector * dir * self.speed

    def move_right(self, dir = 1):
        self.position += self.get_right_vector() * dir * self.speed

    def rotate(self, angle):
        self.heding += angle
        self.heding_vector = Vector2((math.cos(self.heding), math.sin(self.heding))).normalize()



    def get_right_vector(self):
        a = self.heding + 90
        right_vector = Vector2((math.cos(a), math.sin(a))).normalize()
        return right_vector