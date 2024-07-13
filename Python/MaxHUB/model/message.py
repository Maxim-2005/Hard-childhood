__author__ = "Maxim"

from datetime import datetime

class Message():
    def __init__(self, user = "", text = ""):
        self.user = user
        self.text = text
        self.data = datetime.now().strftime("%H:%M:%S")
        # self.like = 0 # счетчик лайков