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
        self.position()

    def update(self, e):
        """Обновление игры"""
        if e.type == pg.KEYDOWN and e.key == pg.K_UP:
            self.unit.rect.y -= 10
        if e.type == pg.KEYDOWN and e.key == pg.K_DOWN:
            self.unit.rect.y += 10
        if e.type == pg.KEYDOWN and e.key == pg.K_LEFT:
            self.unit.rect.x -= 10
        if e.type == pg.KEYDOWN and e.key == pg.K_RIGHT:
            self.unit.rect.x += 10

    def draw(self, g):
        """Отрисовка игры"""
        g.fill('grey')
        self.unit.draw(g)

    def position(self):
        self.unit.rect.x = self.size[0] // 2 - self.unit.rect.width // 2
        self.unit.rect.y = self.size[1] // 2 - self.unit.rect.height // 2
