import pygame as pg

class Terrain(object):
    pg.init()
    _atlas_ = pg.image.load('images\\sprite.bmp')
    _atlas_.set_colorkey((255, 255, 255))

    # Трраин
    def __init__(self):
        self.atlas = self._atlas_
        self.rect = self.atlas.get_rect()

    # Отрисовка Трраина
    def draw(self, g):
        g.blit(self.atlas, self.rect)