import pygame as pg

class MiniMap(object):
    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.rect = self.position(self.size)

    def update(self):
        """Обновление"""
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.rect = self.position(self.size)
            print(self.rect)

    def draw(self, g):
        """Отрисовка"""
        pg.draw.rect(g, 'white', (self.rect, (self.size[0] // 3, self.size[1] // 3)), 3)

    def position(self, size):
        x = 0
        y = size[1] - self.size[1] // 3
        return x, y
