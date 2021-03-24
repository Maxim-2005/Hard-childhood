import pygame as pg

class Terrain(object):
    pg.init()
    _atlas_ = pg.image.load('images\\sprite.bmp')
    _atlas_.set_colorkey((255, 255, 255))
    _rate_ = 48

    # Трраин
    def __init__(self):
        self.atlas = self._atlas_
        self.rect = (self._rate_, self._rate_)
        self.image = self.atlas.subsurface((0, 0), (self._rate_, self._rate_))

    # Отрисовка Трраина
    def draw(self, g):
        g.blit(self.image, self.rect)