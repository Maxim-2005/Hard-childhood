import pygame as pg
from modules.Button import Button

class Menu(object):

    button_name = ['start', 'create', 'load', 'save', 'options', 'about the game', 'return', 'exit']

    def __init__(self, size):
        """Отрисовка меню"""
        self.menu_state = True
        self.size = size
        self.list_button = []
        for i in range(8):
            btn_pos = self.position(i)
            button = Button(btn_pos, self.button_name[i])
            self.list_button.append(button)
        self.button_action = None
        self.list_button[6].active = False

    def update(self, e):
        """Отрисовка меню"""
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            for i in range(8):
                btn_pos = self.position(i)
                self.list_button[i].rect.x = btn_pos[0]
                self.list_button[i].rect.y = btn_pos[1]

        pos = pg.mouse.get_pos()
        click = pg.mouse.get_pressed(3)
        for button in self.list_button:
            if button.active and button.rect.collidepoint(pos):
                button.focus = True
                if click[0]:
                    button.pressed = True
                    self.function(button.name)
                else:
                    button.pressed = False
                    self.button_action = None
            else:
                button.focus = False
            button.update()

    # Отрисовка меню
    def draw(self, g):
        """Отрисовка меню"""
        g.fill('black')
        for button in self.list_button:
            button.draw(g)

    def function(self, button_name):
        if button_name != self.button_action:
            self.button_action = button_name
            if button_name == self.button_name[0]:
                self.menu_state = False
            if button_name == self.button_name[1]:
                print('нажатак кнопка:', button_name)
            if button_name == self.button_name[2]:
                print('нажатак кнопка:', button_name)
            if button_name == self.button_name[3]:
                print('нажатак кнопка:', button_name)
            if button_name == self.button_name[4]:
                print('нажатак кнопка:', button_name)
            if button_name == self.button_name[5]:
                print('нажатак кнопка:', button_name)
            if button_name == self.button_name[6]:
                print('нажатак кнопка:', button_name)
            if button_name == self.button_name[7]:
                pg.quit()
                quit()

    def position(self, i):
        """"Позиция"""
        if i < 4:
            pos_x = self.size[0] // 2 - 320
            pos_y = self.size[1] // 2 + i * 110 - 240
        else:
            pos_x = self.size[0] // 2 + 20
            pos_y = self.size[1] // 2 + i * 110 - 680
        return pos_x, pos_y