from kafka import KafkaConsumer
import os

# Configuración del consumidor global
server = os.getenv('KAFKA-SERVER')
consumidor = KafkaConsumer(bootstrap_servers=server)
bandera = True

def terminar():
    global bandera
    bandera = False

def iniciar():
    global bandera
    bandera = True

def getBandera():
    global bandera
    return bandera

def cerrar():
    global consumidor
    consumidor.close()

def nuevo():
    return KafkaConsumer(bootstrap_servers=server)

def getConsumidor():
    global consumidor
    return consumidor

