import pygame as pg

class Interface(object):
    def __init__(self):
        """Конструктор"""
        pass

    def update(self):
        """Обновление"""
        pass

    def draw(self, g):
        """Отрисовка"""
        pg.draw.rect(g, 'white', (0, 450, 500, 300))
