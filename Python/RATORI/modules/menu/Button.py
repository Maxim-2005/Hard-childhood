import pygame as pg
import pygame

class Button(object):
    pg.init()
    pg.font.init()
    _font_ = pg.font.SysFont('Agency FB', 40)

    def __init__(self, btn_pos, name):
        """Конструктор кнопки"""
        self.name = name
        self.font_color = 'red'
        self.border_color = 'red'
        self.active = True
        self.focus = False
        self.pressed = False
        self.rect = pg.Rect(btn_pos, (300, 100))

    def update(self):
        """Обновление кнопки"""
        if self.active:
            self.font_color = 'red'
            self.border_color = 'red'
            if self.focus:
                self.font_color = 'white'
                self.border_color = 'white'
                if self.pressed:
                    self.font_color = 'black'
                    self.border_color = 'red'
        else:
            self.font_color = 'grey'
            self.border_color = 'red'

    def draw(self, g):
        """Отрисовка кнопки"""
        radius = 20
        pg.draw.rect(g, 'black', self.rect, border_radius=radius)
        pg.draw.rect(g, self.border_color, self.rect, 3, radius)
        self.text_button = self._font_.render(self.name, True, self.font_color)
        self.text_rect = self.text_button.get_rect()
        self.text_rect.center = self.rect.center
        g.blit(self.text_button, self.text_rect)
