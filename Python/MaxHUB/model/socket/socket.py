__author__ = "Maxim"

import socket
import threading
import sys

class Socket():
    def __init__(self):
        self.host = '192.168.3.121' # Переделать что-бы бралось с JSON-а
        self.port = 9090            # Переделать что-бы бралось с JSON-а
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        
        # Инициализация потоков
        threadReciver = threading.Thread(target=self.Reciver)
        threadSender = threading.Thread(target=self.Sender)

        # Запуск потоков
        threadReciver.start()
        threadSender.start()

    def Reciver(self):
        while True:
            data = self.sock.recv(1024)
            if data:
                print(data.decode())

    def Sender(self):
        while True:
            message = input()
            if message == "exit":
                self.sock.close()
                sys.exit()
            else:
                self.sock.send(message.encode())
