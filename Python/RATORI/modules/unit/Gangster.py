import pygame as pg
from random import randint as r
from modules.unit.Abstract import Abstract


class Gangster(Abstract):

    # Отрисовка Трраина
    @staticmethod
    def filling():
        """Заполняем атлас тайлами"""
        pg.init()
        rate_x = 80
        rate_y = 65
        atlas = pg.image.load('images\\gangster.png')
        atlas = pg.transform.scale(atlas, (8*rate_x, 9*rate_y))
        tile_atlas = []
        for row in range(atlas.get_height() // rate_y):
            tile_atlas.append([])
            for col in range(atlas.get_width() // rate_x):
                rect = (rate_x * col, rate_y * row)
                image = atlas.subsurface((rect, (rate_x, rate_y)))
                tile_atlas[row].append(image)
        return tile_atlas

    def __init__(self, size, tile_atlas):
        """Конструктор"""
        self.size = size
        self.rate_x = 80
        self.rate_y = 65
        self.step = 0
        self.row = 7
        self.col = 0
        self.time_move = 20
        self.unit_turn = 8
        self.tile_atlas = tile_atlas
        self.point_x = r(size[0] // 8, size[0] * 3 // 4)
        self.point_y = r(size[1] // 8, size[1] * 3 // 4)
        self.image = self.tile_atlas[self.row][self.col]
        self.rect = pg.Rect(self.point_x, self.point_y, self.rate_x, self.rate_y)
        self.arrest = False

    def update(self, turn):
        """Обновление"""
        self.rect.x, self.rect.y = self.pos_unit(turn)

        if not self.arrest:
            if self.time_move < 1:
                self.unit_turn = r(0, 10)
                self.time_move = r(30, 150)
            self.time_move -= 1
            if self.unit_turn > 7:
                self.image = self.tile_atlas[6][0]
            else:
                self.col = self.unit_turn
                self.image = self.select()
        else:
            self.image = self.tile_atlas[8][self.col]

    def draw(self, g):
        """Отрисовка"""
        g.blit(self.image, self.rect)

    def select(self):
        """Выбор картинки шага"""
        if self.step > 10:
            if self.row > 4:
                self.row = 0
            else:
                self.row += 1
                self.step = 0
        else:
            self.step += 20
        return self.tile_atlas[self.row][self.col]