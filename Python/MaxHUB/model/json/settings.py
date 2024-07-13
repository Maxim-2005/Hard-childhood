__author__ = "Maxim"

import os.path
import json

from datetime import datetime

#### Лучше разделить на 3 файла JSON: для server, для user и для настроек GUI.
class Json():
    def __init__(self):
        self.file = os.getcwd() + "//settings.json"
        # self.file = "model\json\settings.json"
        self.serv = "192.168.3.121"
        self.port = "9090"
        self.them = "light"

    # Создание JSON и заполнение по умолчанию
    def createJSON(self, name, mail, icon):
        if not os.path.exists(self.file):
            data = {
                "serv": self.serv,
                "port": self.port,
                "name": name,
                "mail": mail,
                "icon": icon,
                "them": self.them,
                "last": datetime.now().strftime("%H:%M:%S")
            }
            with open(self.file, "w") as file:
                json.dump(data, file)
    
    # Чтение файла JSON
    def readJSON(self):
        with open(self.file, "r") as file:
            data = json.load(file)
        return data
    
    # Редактирование JSON
    def editJSON(self, name = "undefined", mail = "undefined", icon = "default"):
        data = self.readJSON()
        for i in data:
            if i == "name" and name != "undefined":
                data['name'] = name
            if i == "mail" and mail != "undefined":
                data['mail'] = mail
            if i == "icon" and icon != "default":
                data['icon'] = icon
        with open(self.file, "w") as file:
            json.dump(data, file)

    # Удаление JSON
    def deleteJSON(self):
        with open(self.file, 'w') as file:
            json.dump({}, file)


#### ТЕСТИРОВАНИЕ (УДАЛИТЬ И ЛИКВИДИРОВАТЬ ВСЕХ, КТО ВИДЕЛ ЭТОТ КОД)
'''
j = Json()
j.createJSON()
print("1")
print(j.readJSON())
print("2")
j.editJSON("Ишкильдык", "google@gmail.com", "ava.jpg") #УДАЛЯЕТ ВСЕ
print(j.readJSON())
print("3")
j.deleteJSON()
print(j.readJSON())
'''
