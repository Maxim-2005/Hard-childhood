import pygame as pg

class Unit(object):
    pg.init()
    _image_ = pg.image.load('images\\BG.png')
    sound = pg.mixer.Sound('sounds\\sound.wav')

    def __init__(self):
        """Юнит"""
        self.image = self._image_
        self.rect = self.image.get_rect()

    def draw(self, g):
        """Отрисовка юнита"""
        if self.rect.y == 150:
            pg.mixer.Sound.play(self.sound)
        g.blit(self.image, self.rect)
