import pygame as pg

class Shot(object):
    """Пуля"""
    def __init__(self):
        self.point_x = 100
        self.point_y = 100

    def update(self):
        self.point_x += 1
        self.point_y += 1

    def draw(self, g):
        pg.draw.circle(g, "yellow", (self.point_x, self.point_y), 3)
