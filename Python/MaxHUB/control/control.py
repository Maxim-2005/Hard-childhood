__author__ = "Maxim"

from PySide6.QtWidgets import QApplication, QMainWindow

from view.user import Ui_user
from view.message import Ui_message

from control.user import User
from control.message import Message

from model.user import User as ModelUser
from model.message import Message as ModelMessage

#from model.socket.socket import Socket # (перенести в control)

class Control(QMainWindow):
    def __init__(self, model, view, parent=None):
        super(Control, self).__init__(parent)
        #self.socket = Socket() # Исправить потоки (перенести в control)
        self.model = model
        self.view = view
        self.view.setupUi(self)

        self.countUser = 0 # Временно для теста
        self.countMessage = 0 # Временно для теста
        
        self.view.nameButton.clicked.connect(self.nameButton) # Создать/изменить имя
        self.view.btn_1.clicked.connect(self.btn_1) # Кнопка 1 - ?
        self.view.btn_2.clicked.connect(self.btn_2) # Кнопка 2 - ?
        self.view.btn_3.clicked.connect(self.btn_3) # Кнопка 3 - ?
        self.view.btn_4.clicked.connect(self.btn_4) # Кнопка 4 - ?
        self.view.sendButton.clicked.connect(self.sendButton) # Отправка (надо еще поEnter)
        # nameEdit # Поле для ввода имени
        # listUser # Список пользователей
        # listMessages # Список сообщений
        # textEdit # Поле ввода сообщения

    # Создать/изменить имя
    def nameButton(self):
        # Добавить проверку имени != "undefined"
        if self.view.nameButton.text() == 'name':
            text = self.view.nameEdit.text()
            self.model.json.editJSON(text)
            name = self.model.json.readJSON()['name']
            self.setWindowTitle(u"HUB messager - " + name)
            self.view.nameEdit.setEnabled(False)
            self.view.nameEdit.setText("Пользователь: " + name)
            self.view.nameButton.setText(u"edit")
        else:
            self.setWindowTitle(u"HUB messager - введите новое имя")
            self.view.nameEdit.setText("")
            self.view.nameEdit.setEnabled(True)
            self.view.nameButton.setText(u"name")
    
    # Кнопка 1 - временно иммитирует подключение пользователей
    def btn_1(self):
        self.countUser += 1
        user = User('192.168.0.' + str(self.countUser))
        user.nameLabel = 'VASYA'
        self.view.listUser.addWidget(user)

    # Кнопка 2 - временно иммитирует выход всех пользователей
    def btn_2(self):
        while self.view.listUser.count() > 0:
            item = self.view.listUser.takeAt(0)
            item.widget().deleteLater()
    
    # Кнопка 3 - временно иммитирует новое сообщение
    def btn_3(self):
        # Прием сообщения с socket
        self.countMessage += 1
        user = "user-" + str(self.countMessage) # Временно (будет из socket)
        text = "Всем привет!" # Временно (будет из socket)
        modelMessage = ModelMessage(user, text)
        message = Message(modelMessage)
        self.model.addMessage(message)
        self.view.listMessage.addWidget(message)

    # Кнопка 4 - временно иммитирует очистку всех сообщений
    def btn_4(self):
        while self.view.listMessage.count() > 0:
            item = self.view.listMessage.takeAt(0)
            item.widget().deleteLater()

    # Отправка ИСПРАВИТЬ ОБНОВЛЕНИЕ ИМЕНИ КЛИЕНТА
    def sendButton(self):
        user = self.model.json.readJSON()['name']
        text = self.view.textEdit.toPlainText()
        modelMessage = ModelMessage(user, text)
        # message.ui.messageText.setText(text)
        message = Message(modelMessage)
        self.model.addMessage(message)
        self.view.listMessage.addWidget(message)
        self.view.textEdit.setPlainText("")
