from modules.Terrain import Terrain

class Ground(object):
    def __init__(self):
        self.terrain = Terrain()

    def update(self):
        """Обновление"""
        pass

    def draw(self, g):
        self.terrain.draw(g)
        pass
