import socket


class Cliente():
    def __init__(self, puerto, servidor):
        self.HEADER=64
        self.PORT = puerto
        self.FORMAT= 'utf-8'
        self.DISCONNECT_MESSAGE ="!DESCONECTAR"
        self.SERVER=servidor
        self.ADDR=(self.SERVER, self.PORT)
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente.connect(self.ADDR)

    def send(self,msg):
        mensaje = msg.encode(self.FORMAT)
        mensaje_longitud=len(mensaje)
        enviar_longitud = str(mensaje_longitud).encode(self.FORMAT)
        enviar_longitud += b' '* (self.HEADER-len(enviar_longitud))
        self.cliente.send(enviar_longitud)
        self.cliente.send(mensaje)
    
    
