from abc import ABC, abstractmethod
import pygame as pg

from config import FPS

class Application(ABC):

    def __init__(self, title:str, width:int, height:int):
        self.title = title
        self.width = width
        self.height = height
        
        self.window = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption(self.title)

        self.clock = pg.time.Clock()
        self.fps = FPS
        self.runnig = False

    @abstractmethod
    def update(self, delta):
        pass


    def run(self):
        self.runnig = True
        previous_time = pg.time.get_ticks()
        while self.runnig:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.runnig = False
                    return

            self.window.fill(0)
            delta = pg.time.get_ticks() - previous_time
            self.update(delta/1000.0)
            previous_time = pg.time.get_ticks()
            pg.display.flip()
            pg.display.update()
            self.clock.tick(self.fps)





