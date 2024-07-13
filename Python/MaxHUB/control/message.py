__author__ = "Maxim"

from PySide6.QtWidgets import QWidget

from view.message import Ui_message

class Message(QWidget):

    def __init__(self, modelMessage, parent=None):
        super(Message, self).__init__(parent)
        self.ui = Ui_message()
        self.ui.setupUi(self)
        self.ui.timeLabel.setText(str(modelMessage.data))
        self.ui.userLabel.setText(modelMessage.user)
        self.ui.messageText.setText(modelMessage.text)
