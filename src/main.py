import pygame as pg
from pygame.math import Vector2
from application import Application
from config import HEIGHT, TITLE, WIDTH
from map import Map
from player import Player
from raycaster import Raycaster
from renderer import Renderer


class Raycast3D(Application):

    def __init__(self):
        super().__init__(TITLE, WIDTH, HEIGHT)

        self.map = Map()
        self.player = Player(pg.math.Vector2((150,150)))
        self.raycaster = Raycaster(self.player,self.map,self.window)
        self.renderer = Renderer()

    def update(self, delta):
        # self.map.heighlight_square(self.player.position, self.window)
        self.player.update()
        dists = self.raycaster.ray_cast()
        self.renderer.render(dists,self.window)

        # self.map.draw(self.window)
        # self.player.draw(se-lf.window)

def main():
    app = Raycast3D()
    app.run()


if __name__ == '__main__':
    main()