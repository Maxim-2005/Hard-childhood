import pygame as pg

class Score(object):
    """ Очки игры """

    def __init__(self, size):
        """ Очки """
        self.size = size
        self.score = 0
        self.font = pg.font.Font(None, 36)
        self.text = self.font.render(str(self.score), True, 'White')

    def update(self, size):
        """ Обновление """
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size

    def draw(self, g):
        """ Отрисовка """
        g.blit(self.text, (self.size[0]-50, 0))