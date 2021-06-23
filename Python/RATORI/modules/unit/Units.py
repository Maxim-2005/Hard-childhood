from modules.unit.Gangster import Gangster
from modules.unit.Enemy import Enemy

class Units(object):
    def __init__(self, size):
        """Конструктор"""
        self.list_unit = []
        self.count = 50
        for i in range(self.count):
            unit = Gangster(size)
            self.list_unit.append(unit)
        self.enemy = Enemy()
        self.unit_speed = 4
        self.unit_speed_line = 3

    def update(self, turn):
        """Обновление"""
        for unit in self.list_unit:
            unit.rect.x, unit.rect.y = self.move_unit(unit)
            unit.update(turn)
        self.enemy.update(turn)

    def draw(self, g):
        """Отрисовка"""
        for unit in self.list_unit:
            unit.draw(g)
        self.enemy.draw(g)

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
