from kafka import KafkaProducer
import time

# Configura el servidor de Kafka


def enviarMensaje(productor, canal, mensaje):
    try:
        productor.send(canal,   mensaje.encode('utf-8'))
    except Exception as e:
        print("Error al escribir un mensaje.")
