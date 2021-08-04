from random import randint as r


class Units(object):
    """Супер-класс"""
    def __init__(self, file):
        """Конструктор"""
        self.file = file
        self.pos = r(20, 450), r(20, 390)

    def console(self):
        print("Юнит:", self.__class__.__name__)