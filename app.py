from consumidor import recibirMensaje
from productor import enviarMensaje
from mensajeria import mensajeria
from kafka import KafkaProducer
from kafka import KafkaConsumer
import threading

# Se toma el host
server = "localhost:9092"

# Se crean los dos servicios
productor = KafkaProducer(bootstrap_servers=server)
consumidor = KafkaConsumer(bootstrap_servers=server)

# Solicitamos el canal
canal = input("Ingrese el canal del que desea leer y escirbir: ")
consumidor.subscribe([canal])

# Crear subprocesos para leer y escribir mensajes
leer = threading.Thread(target=recibirMensaje, args=(consumidor, canal))
escribir = threading.Thread(target=mensajeria, args=(productor, canal, consumidor))

# Iniciar los subprocesos
leer.start()
escribir.start()

# Esperar a que los subprocesos terminen (esto no debería suceder en un programa de consola)
leer.join()
escribir.join()

