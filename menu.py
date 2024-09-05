from cliente import Cliente
from servidor import Servidor
from informacionPC import Info
class Menu():
    def menu(self):
        
        continuar=True
        while continuar:        
        
            print("""
            # {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
            # {}________                     __           .__                    .___               {}
            # {}\______ \    ____    _______/  |_ _______ |__|______ _____     __| _/ ____ _______  {}
            # {} |    |  \ _/ __ \  /  ___/\   __\\_  __ \|  |\____ \\__  \   / __ | /  _ \\_  __ \ {}
            # {} |    `   \\  ___/  \___ \  |  |   |  | \/|  ||  |_> >/ __ \_/ /_/ |(  <_> )|  | \/ {}
            # {}/_______  / \___  >/____  > |__|   |__|   |__||   __/(____  /\____ | \____/ |__|    {}
            # {}        \/      \/      \/                    |__|        \/      \/                {}
            # {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}      
            
            1) Establecer Servidor 
            2) Establecer Cliente
            3) Información del PC
            0) Salir\n
            """)
            try:
                opc=int(input("Escribe la opción: "))
                
                if opc==1:
                    puerto=int(input("Escribe el número del puerto en donde correra el servidor: "))
                    servidor=Servidor(puerto)
                    servidor.start()
                elif opc==2:
                    puerto=int(input("Escribe el número del puerto en donde esta corriendo el servidor: "))
                    servidor=input("Escribe la dirección IP donde esta corriendo el servidor: ")
                    print(" para cerrar conexión escribe: !DESCONECTAR")
                    
                    cliente=Cliente(puerto, servidor)
                    mensaje=input("Escribe el mensaje dirijido al servidor: ")
                    cliente.send(mensaje)
                elif opc==3:
                    informacion = Info()
                    informacion.getInfo()
                elif opc==0:
                    continuar=False
                else:
                    print("Opción no válida...")
            except ValueError:
                print("Solo puede introducir números!!!!!!!!!!!")
            except KeyboardInterrupt:
                print("Adiós")
                continuar=False