from enum import Enum
from terran import Terran
from zerg import Zerg
from protoss import Protoss


class Factory(object):
    """Фабричный метод"""

    class Race(Enum):
        """Вложенный класс"""
        TERRAN = 0,
        ZERG = 1,
        PROTOSS = 2

    factory_dict = {
        Race.TERRAN: Terran,
        Race.ZERG: Zerg,
        Race.PROTOSS: Protoss
    }

    def new_unit(self, race):
        return self.factory_dict[race]()