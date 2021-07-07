from modules.unit.Dog import Dog


class Adapter(Dog):
    def draw(self, g):
        return self.draw_unit(g)