import pygame as pg
from modules.ground.Terrain import Terrain

class MiniMap(object):
    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.terrain = Terrain()
        self.count_x = len(self.terrain.map[0])
        self.count_y = len(self.terrain.map)
        self.rate = 5
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
        for y in range(self.count_y):
            for x in range(self.count_x):
                key = self.terrain.map[y][x]
                tile = self.terrain.tile_atlas[key]
                g.blit(tile, (x*self.rate, y*self.rate+self.rect[1], self.rate, self.rate))

        pg.draw.rect(g, 'white', (self.rect, (self.size[0] // 3, self.size[1] // 3)), 3)

    def position(self, size):
        x = 0
        y = size[1] - self.size[1] // 3
        return x, y
