import pygame as pg
from modules.MiniMap import MiniMap

class Interface(object):
    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.minimap = MiniMap(self.size)

    def update(self):
        """Обновление"""
        self.minimap.update()

    def draw(self, g):
        """Отрисовка"""
        self.minimap.draw(g)