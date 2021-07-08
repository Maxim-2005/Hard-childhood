from modules.interface.Life import Life
from modules.interface.Bullet import Bullet
from modules.interface.Score import Score
from modules.interface.MiniMap import MiniMap

class Interface(object):
    """Пример паттерна Фасад"""
    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.minimap = MiniMap(self.size)
        self.life = Life()
        self.bullet = Bullet(size)
        self.score = Score(size)

    def update(self, hero):
        """Обновление"""
        self.minimap.update(hero)
        self.life.update()
        self.bullet.update(self.size)
        self.score.update(self.size)

    def draw(self, g):
        """Отрисовка"""
        self.minimap.draw(g)
        self.life.draw(g)
        self.bullet.draw(g)
        self.score.draw(g)