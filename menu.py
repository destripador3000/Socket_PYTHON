from cliente import Cliente
from servidor import Servidor
from informacionPC import Info



class Menu():
    def menu(self):
        continuar = True
        while continuar:        
            print("""
                1) Establecer Servidor 
                2) Establecer Cliente
                3) Información del PC
                0) Salir
                """)
            try:
                opc = int(input("Escribe la opción: "))
                
                if opc == 1:
                    puerto = int(input("Escribe el número del puerto en donde correrá el servidor: "))
                    servidor = Servidor(puerto)
                    servidor.start()

                elif opc == 2:
                    puerto = int(input("Escribe el número del puerto en donde está corriendo el servidor: "))
                    servidor_ip = input("Escribe la dirección IP del servidor: ")
                    print("Para cerrar la conexión, escribe: !DESCONECTAR")

                    cliente = Cliente(puerto, servidor_ip)
                    while True:
                        comando = input("Introduce un comando para ejecutar en el servidor: ")
                        if comando.strip().upper() == "!DESCONECTAR":
                            cliente.disconnect()
                            break
                        cliente.send(comando)

                elif opc == 3:
                    informacion = Info()
                    informacion.getInfo()

                elif opc == 0:
                    continuar = False

                else:
                    print("Opción no válida...")

            except ValueError:
                print("Solo puede introducir números!")
            except KeyboardInterrupt:
                print("Adiós")
                continuar = False


if __name__ == "__main__":
    app = Menu()
    app.menu()
