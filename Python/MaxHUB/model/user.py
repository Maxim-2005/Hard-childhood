__author__ = "Maxim"

class User():
    def __init__(self, usn = "", uid = "", uip = "", key = ""):
        self.name = usn
        self.userID = uid
        self.userIP = uip
        self.pubKey = key
        self.status = False