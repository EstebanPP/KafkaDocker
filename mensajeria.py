from productor import enviarMensaje
import time

# Menu para manejar los mensajes y los canales
def mensajeria(productor, canal, consumidor):
    print("###### Vienvenidos a nuestra aplicacion de mensajeria ######\n")
    while True:
        try:
            print("--------------------")
            opcion = input("Escoje entre las opciones (Escriba el numero):\
                            \n 1. Enviar mensaje.\
                            \n 2. Cambiar canal de lectura y escritura.\
                            \n 3. Cerrar la aplicacion.\
                            \n Opcion: ")
            print("--------------------\n")
            if opcion == "1":
                mensaje = input(f"Escriba un mensaje para el canal '{canal}': ")
                enviarMensaje(productor, canal, mensaje)
                time.sleep(3)
            elif opcion == "2":
                temp = input("Digite el nuevo canal: ")
                canal = temp
                consumidor.subscribe([canal])
                time.sleep(3)
            elif opcion == "3":
                break
            else:
                print("Esto no esta dentro de las opciones.")
        except Exception as e:
            print("Error en el menu de mensajeria.")
    
        
