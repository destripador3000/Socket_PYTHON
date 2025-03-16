import socket
import threading
import subprocess

class Servidor():
    def __init__(self, puerto):
        self.HEADER = 64
        self.PORT = puerto
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DESCONECTAR"
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        print("[INICIANDO] Servidor está iniciando...")

    def handle_client(self, conn, addr):
        print(f"[NUEVA CONEXIÓN] {addr} conectado.")
        while True:
            try:
                msg_longitud = conn.recv(self.HEADER).decode(self.FORMAT)
                if not msg_longitud:
                    break
                msg_longitud = int(msg_longitud)
                msg = conn.recv(msg_longitud).decode(self.FORMAT)

                if msg == self.DISCONNECT_MESSAGE:
                    break
                
                print(f"[{addr}] Comando recibido: {msg}")

                # Ejecutar el comando y capturar la salida
                resultado = subprocess.run(msg, shell=True, capture_output=True, text=True)
                
                # Enviar la salida de vuelta al cliente
                salida = resultado.stdout if resultado.stdout else resultado.stderr
                salida = salida[:1024]  # Limitar tamaño para evitar desbordamientos
                conn.send(salida.encode(self.FORMAT))

            except Exception as e:
                print(f"[ERROR] Problema con {addr}: {e}")
                break

        conn.close()
        print(f"[DESCONECTADO] {addr} se ha desconectado.")

    def start(self):
        self.server.listen()
        print(f"[ESCUCHANDO] El servidor está escuchando en {self.SERVER}:{self.PORT}")
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[CONEXIONES ACTIVAS] {threading.active_count() - 1}")

