import pygame as pg
from modules.unit.Abstract import Abstract


class Shot(Abstract):
    """Пуля"""
    def __init__(self, size):
        self.size = size
        self.point_x = self.size[0] // 2
        self.point_y = self.size[1] // 2

    def update(self, turn):
        self.point_x, self.point_y = self.pos_unit(turn)
        self.point_x += 1
        self.point_y += 1

    def draw(self, g):
        pg.draw.circle(g, "yellow", (self.point_x, self.point_y), 3)
