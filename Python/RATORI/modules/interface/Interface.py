from modules.interface.Life import Life
from modules.interface.MiniMap import MiniMap

class Interface(object):
    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.minimap = MiniMap(self.size)
        self.life = Life()

    def update(self, hero):
        """Обновление"""
        self.minimap.update(hero)
        self.life.update()

    def draw(self, g):
        """Отрисовка"""
        self.minimap.draw(g)
        self.life.draw(g)