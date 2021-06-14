import pygame as pg
from modules.ground.Ground import Ground
from modules.unit.Enemy import Enemy
from modules.unit.Gangster import Gangster
from modules.unit.Hero import Hero
from modules.interface.Interface import Interface

class Game(object):

    def __init__(self, size):
        """"Конструктор игры"""
        self.size = size
        self.ground = Ground(self.size)
        self.enemy = Enemy()
        self.gangster = Gangster()
        self.hero = Hero()
        self.interface = Interface(self.size)
        self.hero.rect.center = self.position(self.size)
        self.turn = 'stop'

    def update(self, e):
        """Обновление игры"""
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.hero.rect.center = self.position(size)

        #Список кликов клавиатуры
        keys = pg.key.get_pressed()

        if (keys[pg.K_RIGHT] and keys[pg.K_DOWN]):
            self.turn = 'right_down'
        elif (keys[pg.K_LEFT] and keys[pg.K_DOWN]):
            self.turn = 'left_down'
        elif (keys[pg.K_LEFT] and keys[pg.K_UP]):
            self.turn = 'left_up'
        elif (keys[pg.K_RIGHT] and keys[pg.K_UP]):
            self.turn = 'right_up'
        elif (keys[pg.K_RIGHT]):
            self.turn = 'right'
        elif (keys[pg.K_DOWN]):
            self.turn = 'down'
        elif (keys[pg.K_LEFT]):
            self.turn = 'left'
        elif (keys[pg.K_UP]):
            self.turn = 'up'
        else:
            self.turn = 'stop'

        self.ground.update(self.size, self.turn)
        self.gangster.update(self.turn)
        self.hero.update(self.turn)
        hero = self.ground.point_x, self.ground.point_y
        self.interface.update(hero)

        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.hero.rect.center = self.position(size)

    def draw(self, g):
        """Отрисовка игры"""
        self.ground.draw(g)
        self.enemy.draw(g)
        self.gangster.draw(g)
        self.hero.draw(g)
        self.interface.draw(g)

    def position(self, size):
        """Позиция"""
        x = size[0] // 2
        y = size[1] // 2
        return x, y
