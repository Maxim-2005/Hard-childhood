from modules.unit.Gangster import Gangster
from modules.unit.Cat import Cat
from modules.unit.Civil import Civil
from modules.unit.Adapter import Adapter
from modules.unit.Shot import Shot

class Units(object):
    def __init__(self, size):
        """Конструктор"""
        tile_atlas = Gangster.filling()
        atlas_cat = Cat.filling()
        atlas_civil = Civil.filling()
        atlas_dog = Adapter.filling()
        self.list_unit = []
        self.list_shot = []
        self.count = 10
        for i in range(self.count):
            unit = Gangster(size, tile_atlas)
            self.list_unit.append(unit)
        for i in range(self.count):
            unit = Cat(size, atlas_cat)
            self.list_unit.append(unit)
        for i in range(self.count):
            unit = Civil(size, atlas_civil)
            self.list_unit.append(unit)
        for i in range(self.count):
            unit = Adapter(size, atlas_dog)
            #self.list_unit.append(unit)
        self.unit_speed = 4
        self.unit_speed_line = 3
        self.size = size

    def update(self, turn):
        """Обновление"""
        for unit in self.list_unit:
            unit.rect.x, unit.rect.y = self.move_unit(unit)
            if unit.rect.collidepoint(self.size[0] // 2, self.size[1] // 2):
                unit.arrest = True
                unit.unit_turn = 8
            unit.update(turn)

        for shot in self.list_shot:
            shot.update(turn)

    def draw(self, g):
        """Отрисовка"""
        for unit in self.list_unit:
            unit.draw(g)
        for shot in self.list_shot:
            shot.draw(g)

    def add_shot(self, turn):
        """Создание выстрела"""
        shot = Shot(self.size, turn)
        self.list_shot.append(shot)

    def move_unit(self, unit):
        """Движение юнита"""
        if unit.unit_turn == 1:
            unit.point_x += self.unit_speed_line
            unit.point_y += self.unit_speed_line
        elif unit.unit_turn == 7:
            unit.point_x -= self.unit_speed_line
            unit.point_y += self.unit_speed_line
        elif unit.unit_turn == 5:
            unit.point_x -= self.unit_speed_line
            unit.point_y -= self.unit_speed_line
        elif unit.unit_turn == 3:
            unit.point_x += self.unit_speed_line
            unit.point_y -= self.unit_speed_line
        elif unit.unit_turn == 2:
            unit.point_x += self.unit_speed
        elif unit.unit_turn == 0:
            unit.point_y += self.unit_speed
        elif unit.unit_turn == 6:
            unit.point_x -= self.unit_speed
        elif unit.unit_turn == 4:
            unit.point_y -= self.unit_speed

        return unit.point_x, unit.point_y
