import pygame as pg
from random import randint as r


class Cat(object):
    pg.init()
    image = pg.image.load('images\\cat.png')
    image = pg.transform.scale(image, (50, 60))

    def __init__(self, size):
        """Конструктор"""
        self.rate_x = 160
        self.rate_y = 130
        self.step = 0
        self.row = 6
        self.col = 8
        self.time_move = 60
        self.scroll_line = 10
        self.unit_turn = 8
        self.scroll = self.scroll_line / 1.4
        self.point_x = r(size[0] // 8, size[0] * 3 // 4)
        self.point_y = r(size[1] // 8, size[1] * 3 // 4)
        self.rect = pg.Rect(self.point_x, self.point_y, self.rate_x, self.rate_y)

    def update(self, turn):
        """Обновление"""
        self.rect.x, self.rect.y = self.pos_unit(turn)
        if self.time_move < 1:
            self.unit_turn = r(0, 8)
            self.time_move = r(30, 150)
        self.time_move -= 1

    def draw(self, g):
        """Отрисовка"""
        g.blit(self.image, self.rect)

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
