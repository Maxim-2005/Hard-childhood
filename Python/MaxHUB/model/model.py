__author__ = "Maxim"

from model.json.settings import Json
from model.sql.dataBase import Sqlite

class Model():
    def __init__(self):
        self.json = Json()
        self.json.createJSON("undefined", "undefined", "default")
        self.sql = Sqlite() # Загатовка для сохранения чата и т.д.
        self.listUsers = [] # Заполняется с JSON
        self.listMessages = [] # Заполняется с JSON

    ## ПОЛЬЗОВАТЕЛИ
    # Добавить пользователя
    def addUser(self, user):
        self.listUsers.append(user)
        # Совпадение имен не проверяем, т. к. с сервера будут разные id
    
    # Удалить пользователя (в сообщениях останется unknown)
    def delUser(self, user):
        self.listUsers.remove(user)

    # Смена имени или других данных
    def editUser(self, user):
        # Дописать редактирование
        return user
    
    # Активность пользователя (онлайн/оффлайн)
    def statusUser(self, user, status):
        user.status = status
        return user
    
    # Вывод онлайн-пользователей
    def usersOnline(self):
        online = []
        for user in self.listUsers:
            if user.status:
                online.append(user)
        return online
    
    ## СООБЩЕНИЯ
    # Добавить сообщение
    def addMessage(self, message):
        self.listMessages.append(message)
    
    # Редактировать сообщение (Включает удаление)
    def editMessage(self, message):
        # Дописать редактирование
        return message
    
    # История сообщений
    def actualMessage(self):
        actual = self.listMessages
        # Выборка последних сообщений (20, 50, 100, ..., ?)
        return actual