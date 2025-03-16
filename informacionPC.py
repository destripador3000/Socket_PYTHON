import socket
class Info():
    def getInfo(self):
        equipo = socket.gethostname()
        ip = socket.gethostbyname(equipo)
        print(f"El equipo es {equipo}\nLa IP del equipo es: {ip}")



