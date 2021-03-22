import pygame as pg

class Unit(object):
    pg.init()
    _image_ = pg.image.load('images\\BG.png')
    sound = pg.mixer.Sound('sounds\\sound.wav')

    # Юнит
    def __init__(self):
        self.image = self._image_
        self.rect = self.image.get_rect()

    # Отрисовка юнмта
    def draw(self, g):
        if self.rect.y == 150:
            pg.mixer.Sound.play(self.sound)
        g.blit(self.image, self.rect)
