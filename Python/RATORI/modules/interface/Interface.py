from modules.interface.MiniMap import MiniMap

class Interface(object):
    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.minimap = MiniMap(self.size)

    def update(self, hero):
        """Обновление"""
        self.minimap.update(hero)

    def draw(self, g):
        """Отрисовка"""
        self.minimap.draw(g)