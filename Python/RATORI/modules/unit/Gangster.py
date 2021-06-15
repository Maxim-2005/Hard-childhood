import pygame as pg
from random import randint as r


class Gangster(object):
    pg.init()
    _atlas_ = pg.image.load('images\\gangster.png')

    def __init__(self):
        """Конструктор"""
        self.rate_x = 160
        self.rate_y = 130
        self.step = 0
        self.row = 7
        self.col = 0
        self.unit_speed = 4
        self.unit_speed_line = 3
        self.time_move = 60
        self.scroll_line = 10
        self.unit_turn = 8
        self.scroll = self.scroll_line / 1.4
        self.tile_atlas = []
        self.tile_atlas = self.filling()
        self.point_x, self.point_y = (r(200, 600), r(200, 400))
        self.image = self.tile_atlas[self.row][self.col]
        self.rect = pg.Rect(self.point_x, self.point_y, self.rate_x, self.rate_y)

    def update(self, turn):
        """Обновление"""
        self.rect.x, self.rect.y = self.pos_unit(turn)
        if self.time_move < 1:
            self.unit_turn = r(0, 8)
            self.time_move = r(30, 150)
        self.time_move -= 1
        if self.unit_turn > 7:
            self.image = self.tile_atlas[6][0]
        else:
            self.col = self.unit_turn
            self.image = self.select()
        self.move_unit()

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
            self.step += 12
        return self.tile_atlas[self.row][self.col]

    # Отрисовка Трраина
    def filling(self):
        """Заполняем атлас тайлами"""
        atlas = self._atlas_
        size = (self.rate_x, self.rate_y)
        for row in range(atlas.get_height() // self.rate_y):
            self.tile_atlas.append([])
            for col in range(atlas.get_width() // self.rate_x):
                rect = (self.rate_x * col, self.rate_y * row)
                image = atlas.subsurface((rect, size))
                self.tile_atlas[row].append(image)
        return self.tile_atlas

    def pos_unit(self, turn):
        """Позиция юнита"""
        if turn == 'right_down':
            self.point_x -= self.scroll
            self.point_y -= self.scroll
        elif turn == 'left_down':
            self.point_x += self.scroll
            self.point_y -= self.scroll
        elif turn == 'left_up':
            self.point_x += self.scroll
            self.point_y += self.scroll
        elif turn == 'right_up':
            self.point_x -= self.scroll
            self.point_y += self.scroll
        elif turn == 'right':
            self.point_x -= self.scroll_line
        elif turn == 'down':
            self.point_y -= self.scroll_line
        elif turn == 'left':
            self.point_x += self.scroll_line
        elif turn == 'up':
            self.point_y += self.scroll_line
        return self.point_x, self.point_y

    def move_unit(self):
        """Движение юнита"""
        if self.unit_turn == 1:
            self.point_x += self.unit_speed_line
            self.point_y += self.unit_speed_line
        elif self.unit_turn == 7:
            self.point_x -= self.unit_speed_line
            self.point_y += self.unit_speed_line
        elif self.unit_turn == 5:
            self.point_x -= self.unit_speed_line
            self.point_y -= self.unit_speed_line
        elif self.unit_turn == 3:
            self.point_x += self.unit_speed_line
            self.point_y -= self.unit_speed_line
        elif self.unit_turn == 2:
            self.point_x += self.unit_speed
        elif self.unit_turn == 0:
            self.point_y += self.unit_speed
        elif self.unit_turn == 6:
            self.point_x -= self.unit_speed
        elif self.unit_turn == 4:
            self.point_y -= self.unit_speed

