from db_mongodb import get_mongo_connection
from consumidor import recibirMensaje
from mensajeria import mensajeria
from kafka import KafkaProducer
import threading
import os


# Se toma el host
server = os.getenv('KAFKA-SERVER')

# Se crean los dos servicios
productor = KafkaProducer(bootstrap_servers=server)


# Solicitamos el canal
usuario = input("Nombre usuario: ")
db = get_mongo_connection()
user = db['users']
userId=user.insert_one({"name":usuario}).inserted_id

canal = input("Ingrese el canal del que desea leer y escirbir: ")

# Crear subprocesos para leer y escribir mensajes
#leer = threading.Thread(target=recibirMensaje)
escribir = threading.Thread(target=mensajeria, args=(productor, canal, userId,))

# Iniciar los subprocesos
#leer.start()
escribir.start()

# Esperar a que los subprocesos terminen 
#leer.join()
escribir.join()

