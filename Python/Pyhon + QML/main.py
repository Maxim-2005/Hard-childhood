import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

class Control(QObject):
    connect = Signal(str)
    add_item = Signal(str)

    @Slot(str)
    def press_button(self, message):
        print("PYTHON: " + message)
        self.connect.emit("ТЕКСТ ИЗ PYTHON: " + message)
        self.add_item.emit("ТЕКСТ ИЗ PYTHON: " + message)

control = Control()
engine.rootContext().setContextProperty("control", control)

engine.load("view.qml")
sys.exit(app.exec())