import socket


class Info():
    def getInfo(self):
        self.equipo=socket.gethostname()
        self.ip=socket.gethostbyname(self.equipo)
        print(f"El equipo es {self.equipo}\nLa Ip del equipo es:{self.ip}")



