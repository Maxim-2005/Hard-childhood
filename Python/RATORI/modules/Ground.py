from modules.Terrain import Terrain

class Ground(object):
    def __init__(self):
        self.terrain = Terrain()

    def update(self):
        """Обновление"""
        pass

    def draw(self, g):
        g.fill('magenta')
        for y in range(10):
            for x in range(25):
                key = self.terrain.map[y][x]
                tile = self.terrain.tile_atlas[key]
                g.blit(tile, (x*48, y*48))