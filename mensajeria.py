from productor import enviarMensaje
from consumidor import recibirMensajesAnteriores, recibirMensaje
import time
from config import consumidor, terminar, iniciar, cerrar, nuevo, getConsumidor
import threading

def mensajeria(productor, canal, userId):
    print("###### Vienvenidos a nuestra aplicacion de mensajeria ######\n")
    consumidor = nuevo()
    consumidor.subscribe([canal])
    leer = threading.Thread(target=recibirMensaje, args=(consumidor,))
    leer.start()
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
                mensaje = input(f"Escriba un mensaje para el canal '{canal}': ")
                enviarMensaje(productor, canal, mensaje, userId)
                time.sleep(1)
            elif opcion == "2":
                temp = input("Digite el nuevo canal: ")
                canal = temp
                terminar()
                leer.join()
                time.sleep(2)
                consumidor.close()
                consumidor = nuevo()
                consumidor.subscribe([canal])
                iniciar()
                leer = threading.Thread(target=recibirMensaje, args=(consumidor,))
                leer.start()
                time.sleep(1)
            elif opcion == "3":
                recibirMensajesAnteriores(canal)
                time.sleep(3)
            elif opcion == "4":
                leer.join()
                break
            else:
                print("Esto no esta dentro de las opciones.")
        except Exception as e:
            print("Error en el menu de mensajeria.")
    
        
