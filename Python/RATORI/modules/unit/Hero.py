import pygame as pg

class Hero(object):
    _atlas_ = pg.image.load('images\\hero.png')
    _rate_ = 64

    def __init__(self):
        """Конструктор"""
        self.rate = self._rate_
        self.rect = pg.Rect(0, 0, self.rate, self.rate)
        self.tile_atlas = []
        self.tile_atlas = self.filling()

    def draw(self, g):
        """Отрисовка"""
        image = self.tile_atlas[4][7]
        g.blit(image, self.rect)

    # Отрисовка Трраина
    def filling(self):
        """Заполняем атлас тайлами"""
        atlas = self._atlas_
        rate = self.rate
        size = (rate, rate)
        for row in range(atlas.get_height() // rate):
            self.tile_atlas.append([])
            for col in range(atlas.get_width() // rate):
                rect = (col * rate, row * rate)
                image = atlas.subsurface((rect, size))
                image = pg.transform.scale(image, (rate*2, rate*2))
                self.tile_atlas[row].append(image)
        return self.tile_atlas
