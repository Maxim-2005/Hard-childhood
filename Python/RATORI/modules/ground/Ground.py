from modules.ground.Terrain import Terrain
import pygame as pg

class Ground(object):
    def __init__(self, size):
        self.size = size
        self.terrain = Terrain()
        self.surface = pg.Surface(self.size)
        self.rect =self.surface.get_rect()
        self.point_x, self.point_y = self.terrain.start_point

        #Шрифт для кода
        pg.font.init()
        self.font = pg.font.SysFont('arial', 12, True)

    def update(self, size, turn):
        """Обновление"""
        self.select()
        scroll = 5

        if turn == 'right_down':
            self.point_x += scroll
            self.point_y += scroll
        elif turn == 'left_down':
            self.point_x -= scroll
            self.point_y += scroll
        elif turn == 'left_up':
            self.point_x -= scroll
            self.point_y -= scroll
        elif turn == 'right_up':
            self.point_x += scroll
            self.point_y -= scroll
        elif turn == 'right':
            self.point_x += scroll
        elif turn == 'down':
            self.point_y += scroll
        elif turn == 'left':
            self.point_x -= scroll
        elif turn == 'up':
            self.point_y -= scroll

    def draw(self, g):
        g.fill('grey')
        g.blit(self.surface, self.rect)

    def select(self):
        """Отрисовка поверхности"""
        rate = self.terrain.rate
        #Границы окна
        x_left = self.point_x - self.size[0] // 2
        x_right = self.point_x + self.size[0]
        y_top = self.point_y - self.size[1] // 2
        y_bottom = self.point_y + self.size[1]
        for y in range(y_top // rate, y_bottom // rate):
            for x in range(x_left // rate, x_right // rate):
                key = self.terrain.map[y][x]
                tile = self.terrain.tile_atlas[key]
                self.surface.blit(tile, (x*rate-x_left, y*rate-y_top, rate, rate))

                #Коды тайлов
                text = self.font.render((str(y) + "-" + str(x)), True, "red")
                text_rect = text.get_rect()
                self.surface.blit(text, (x * rate - x_left + 4, y * rate - y_top + 16), text_rect)