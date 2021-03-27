import pygame as pg
from modules.ground.Ground import Ground
from modules.unit.Unit import Unit
from modules.unit.Hero import Hero
from modules.interface.Interface import Interface

class Game(object):

    def __init__(self, size):
        """"Конструктор игры"""
        self.size = size
        self.ground = Ground()
        self.unit = Unit()
        self.hero = Hero()
        self.interface = Interface(self.size)
        self.unit.rect.center = self.position(size)
        self.hero.rect.center = self.position(size)

    def update(self, e):
        """Обновление игры"""
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.unit.rect.center = self.position(size)
            self.hero.rect.center = self.position(size)

        if e.type == pg.KEYDOWN and e.key == pg.K_UP:
            self.unit.rect.y -= 10
        if e.type == pg.KEYDOWN and e.key == pg.K_DOWN:
            self.unit.rect.y += 10
        if e.type == pg.KEYDOWN and e.key == pg.K_LEFT:
            self.unit.rect.x -= 10
        if e.type == pg.KEYDOWN and e.key == pg.K_RIGHT:
            self.unit.rect.x += 10

        if e.type == pg.KEYDOWN and e.key == pg.K_UP:
            self.hero.rect.y -= 10
        if e.type == pg.KEYDOWN and e.key == pg.K_DOWN:
            self.hero.rect.y += 10
        if e.type == pg.KEYDOWN and e.key == pg.K_LEFT:
            self.hero.rect.x -= 10
        if e.type == pg.KEYDOWN and e.key == pg.K_RIGHT:
            self.hero.rect.x += 10
        self.interface.update()

    def draw(self, g):
        """Отрисовка игры"""
        self.ground.draw(g)
        #self.unit.draw(g)
        self.hero.draw(g)
        self.interface.draw(g)

    def position(self, size):
        x = size[0] // 2
        y = size[1] // 2
        return x, y
