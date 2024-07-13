__author__ = "Maxim"

import random

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal

from view.user import Ui_user

class User(QWidget):
    delete = Signal(int)

    def __init__(self, id_widget: int, parent=None):
        super(User, self).__init__(parent)
        self.ui = Ui_user()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.userID.setTitle(str(id_widget))
        name = random.choice(['Бульбазавр', 'Ивизавр', 'Венузавр', 'Чармандер', 'Чармелеон',
            'Чаризард', 'Сквиртл', 'Вартортл', 'Бластойз', 'Катерпи', 'Метапод',
            'Баттерфри', 'Видл', 'Какуна', 'Бидрилл', 'Пиджи', 'Пиджеотто',
            'Пиджит', 'Раттата', 'Ратикэйт', 'Спироу', 'Фироу', 'Эканс', 'Эрбок',
            'Пикачу', 'Райчу', 'Сэндшру', 'Сэндслэш', 'Нидоран', 'Нидорина',
            'Нидоквин', 'Нидоран', 'Нидорино', 'Нидокинг', 'Клефейри', 'Клефейбл',
            'Вульпикс', 'Найнтейлс', 'Джигглипуф', 'Вигглитаф', 'Зубат', 'Голбат',
            'Оддиш', 'Глум', 'Вайлплум', 'Парас', 'Парасект', 'Венонат', 'Веномот',
            'Диглетт', 'Дагтрио'])
        self.ui.nameLabel.setText(name) # Временно, для теста

    @Slot()
    def press_del(self):
        self.delete.emit(self.id_widget)