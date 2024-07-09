import socket 
import threading

class Servidor():
    def __init__(self, puerto):
        self.HEADER=64
        self.PORT = puerto
        self.SERVER=socket.gethostbyname(socket.gethostname())
        self.ADD =(self.SERVER, self.PORT)
        self.FORMAT= 'utf-8'
        self.DISCONNECT_MESSAGE ="!DESCONECTAR"
        self.server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADD)

    def handle_client(self,conn, addr):
        print(f"[NUEVA CONEXIÓN] {addr} conectado.")
        conexion = True
        while conexion:
            msg_longitud =  conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_longitud:
                msg_longitud = int(msg_longitud)
                msg = conn.recv(msg_longitud).decode(self.FORMAT)
                if msg == self.DISCONNECT_MESSAGE:
                    conexion = False
                print(f"[{addr}] {msg}")  
        conn.close()
    def start(self):
        self.server.listen()
        print(f"[ESCUCHANDO] El servidor esta escuchando en {self.SERVER}")
        while True:
            conn, addr =self.server.accept()
            thread =threading.Thread(target=self.handle_client, args=(conn,addr))
            thread.start()
            print(f"[CONEXIONES ACTIVAS] {threading.active_count()-1}")

    print("[INICIANDO] Servidor esta iniciando...")

