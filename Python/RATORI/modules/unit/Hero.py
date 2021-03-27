import pygame as pg

class Hero(object):
    _atlas_ = pg.image.load('images\\hero.png')
    _rate_ = 64

    def __init__(self):
        """Конструктор"""
        self.rate = self._rate_
        self.rect = pg.Rect(0, 0, self.rate, self.rate)

    def draw(self, g):
        """Отрисовка"""
        rate = self.rate
        size = (rate, rate)
        rect = (0, 0)
        image = self._atlas_.subsurface(rect, size)
        g.blit(image, self.rect)
