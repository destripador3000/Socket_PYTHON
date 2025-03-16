import socket

class Cliente():
    def __init__(self, puerto, servidor):
        self.HEADER = 64
        self.PORT = puerto
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DESCONECTAR"
        self.SERVER = servidor
        self.ADDR = (self.SERVER, self.PORT)
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.cliente.connect(self.ADDR)
            print(f"[CONECTADO] Conectado a {self.SERVER}:{self.PORT}")
        except Exception as e:
            print(f"[ERROR] No se pudo conectar al servidor: {e}")

    def send(self, msg):
        try:
            mensaje = msg.encode(self.FORMAT)
            mensaje_longitud = str(len(mensaje)).encode(self.FORMAT)
            mensaje_longitud += b' ' * (self.HEADER - len(mensaje_longitud))
            self.cliente.send(mensaje_longitud)
            self.cliente.send(mensaje)
            
            # Recibir la respuesta del servidor
            respuesta = self.cliente.recv(1024).decode(self.FORMAT)
            print(f"[SERVIDOR]: {respuesta}")

        except Exception as e:
            print(f"[ERROR] No se pudo enviar el mensaje: {e}")

    def disconnect(self):
        self.send(self.DISCONNECT_MESSAGE)
        self.cliente.close()


