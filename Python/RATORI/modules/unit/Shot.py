import pygame as pg
from modules.unit.Abstract import Abstract


class Shot(Abstract):
    """Пуля"""
    def __init__(self, size, turn):
        self.size = size
        self.shot_turn = turn
        self.point_x = self.size[0] // 2
        self.point_y = self.size[1] // 2
        self.timedel = 600

    def update(self, turn):
        self.point_x, self.point_y = self.pos_unit(turn)
        self.pos_shot()

    def draw(self, g):
        pg.draw.circle(g, "yellow", (self.point_x, self.point_y), 3)

    def pos_shot(self):
        """Позиция юнита"""
        if self.shot_turn == 'right_down':
            self.point_x += self.scroll
            self.point_y += self.scroll
        elif self.shot_turn == 'left_down':
            self.point_x -= self.scroll
            self.point_y += self.scroll
        elif self.shot_turn == 'left_up':
            self.point_x -= self.scroll
            self.point_y -= self.scroll
        elif self.shot_turn == 'right_up':
            self.point_x += self.scroll
            self.point_y -= self.scroll
        elif self.shot_turn == 'right' or self.shot_turn == 'stop':
            self.point_x += self.scroll_line
        elif self.shot_turn == 'left':
            self.point_x -= self.scroll_line
        elif self.shot_turn == 'down':
            self.point_y += self.scroll_line
        elif self.shot_turn == 'up':
            self.point_y -= self.scroll_line

        return self.point_x, self.point_y

    def _del_(self):
        pass
