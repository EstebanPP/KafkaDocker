# Importaciones
from db_mongodb import get_mongo_connection
from mensajeria import mensajeria
from kafka import KafkaProducer
import threading
import os

# Se toma el host
server = os.getenv('KAFKA-SERVER')

# Se crean los dos servicios
productor = KafkaProducer(bootstrap_servers=server)

# Solicitamos el nombre del usuario
print("###### Para ingreasar a nuestra aplicacion de mensajeria ######\n")
usuario = input("Nombre usuario: ")
db = get_mongo_connection()
user = db['users']
userId=user.insert_one({"name":usuario}).inserted_id

# Tomamos el canal inicial de lectura y escritura
canal = input("Ingrese el canal del que desea leer y escirbir: ")
print("\n")

# Crear subprocesos para leer y escribir mensajes
escribir = threading.Thread(target=mensajeria, args=(productor, canal, userId,))

# Iniciar los subprocesos
escribir.start()

# Esperar a que los subprocesos terminen 
escribir.join()

