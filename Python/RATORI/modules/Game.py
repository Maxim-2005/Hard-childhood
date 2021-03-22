import pygame as pg
from modules.Ground import Ground
from modules.Unit import Unit
from modules.Interface import Interface

class Game(object):

    def __init__(self, size):
        """"Конструктор игры"""
        self.size = size
        self.Ground = Ground()
        self.unit = Unit()
        self.Interface = Interface()
        self.unit.rect.center = self.position(size)

    def update(self, e):
        """Обновление игры"""
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.unit.rect.center = self.position(size)

        if e.type == pg.KEYDOWN and e.key == pg.K_UP:
            self.unit.rect.y -= 100
        if e.type == pg.KEYDOWN and e.key == pg.K_DOWN:
            self.unit.rect.y += 100
        if e.type == pg.KEYDOWN and e.key == pg.K_LEFT:
            self.unit.rect.x -= 100
        if e.type == pg.KEYDOWN and e.key == pg.K_RIGHT:
            self.unit.rect.x += 100

    def draw(self, g):
        """Отрисовка игры"""
        g.fill('grey')
        self.unit.draw(g)

    def position(self, size):
        x = size[0] // 2
        y = size[1] // 2
        return x, y
