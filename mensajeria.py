# Importaciones
from productor import enviarMensaje
from consumidor import recibirMensajesAnteriores, recibirMensaje
import time
from config import terminar, iniciar, nuevo
import threading

# Funcion de menu para la aplicacion 
def mensajeria(productor, canal, userId):
    print("###### Vienvenidos a nuestra aplicacion de mensajeria ######\n")
    # Creamos un nuevo consumidor 
    consumidor = nuevo()
    consumidor.subscribe([canal])
    # Creamos el hilo para el consumidor
    leer = threading.Thread(target=recibirMensaje, args=(consumidor,))
    leer.start()
    # Iniciamos el menu
    while True:
        try:
            print("--------------------")
            opcion = input("Escoje entre las opciones (Escriba el numero):\
                            \n 1. Enviar mensaje.\
                            \n 2. Cambiar canal de lectura y escritura.\
                            \n 3. Mensajes anteriores.\
                            \n 4. Cerrar la aplicacion.\
                            \n Opcion: ")
            print("--------------------\n")
            if opcion == "1":
                # Pedimos el mensaje y lo enviamos mediante el productor
                mensaje = input(f"Escriba un mensaje para el canal '{canal}': ")
                enviarMensaje(productor, canal, mensaje, userId)
                time.sleep(1)
            elif opcion == "2":
                # Pedimos el nuevo canal
                temp = input("Digite el nuevo canal: ")
                canal = temp
                # Terminamos el consumidor actual
                terminar()
                leer.join()
                time.sleep(2)
                # Creamos un nuevo consumidor
                consumidor.close()
                consumidor = nuevo()
                consumidor.subscribe([canal])
                iniciar()
                leer = threading.Thread(target=recibirMensaje, args=(consumidor,))
                leer.start()
                time.sleep(1)
                # Recuperamos el historial
                recibirMensajesAnteriores(canal)
            elif opcion == "3":
                # Recuperamos el historial
                recibirMensajesAnteriores(canal)
                time.sleep(3)
            elif opcion == "4":
                # Terminamos el consumidor y salimos del menu
                terminar()
                leer.join()
                consumidor.close()
                break
            else:
                print("Esto no esta dentro de las opciones.")
        except Exception as e:
            print("Error en el menu de mensajeria.")
    
        
