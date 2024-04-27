# Importaciones
from kafka import KafkaConsumer
import os

# Configuración del consumidor global
server = os.getenv('KAFKA-SERVER')
consumidor = KafkaConsumer(bootstrap_servers=server)

# Bandera para el consumidor
bandera = True

# Colocar la bandera en false
def terminar():
    global bandera
    bandera = False

# Colocar la bandera en true
def iniciar():
    global bandera
    bandera = True

# Tomamos la bandera
def getBandera():
    global bandera
    return bandera

# Creamos un nuevo consumidor
def nuevo():
    return KafkaConsumer(bootstrap_servers=server)


