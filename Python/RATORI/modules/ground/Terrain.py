import pygame as pg
from modules.ground.map import map as _map_

class Terrain(object):
    pg.init()
    _atlas_ = pg.image.load('images\\sprite.bmp')
    _atlas_.set_colorkey((255, 255, 255))
    _rate_ = 48

    def __init__(self):
        """"Терраин"""
        self.map = _map_
        self.rate = self._rate_
        self.tile_atlas = {}
        self.tile_atlas = self.filling()
        self.start_point = 3072, 1896
        self.start_point_enemy = 3072, 1896

    # Отрисовка Трраина
    def filling(self):
        """Заполняем атлас тайлами"""
        atlas = self._atlas_
        rate = self.rate
        size = (rate, rate)
        for row in range(atlas.get_height() // rate):
            for col in range(atlas.get_width() // rate):
                rect = (col * rate, row * rate)
                image = atlas.subsurface((rect, size))
                key = str(f'{row:0{2}}') + str(f'{col:0{2}}')
                self.tile_atlas[key] = image
        return self.tile_atlas
