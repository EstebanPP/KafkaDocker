from kafka import KafkaConsumer

# Recibe un mensaje del servidor de kafka
def recibirMensaje(consumidor, canal):
    try:
        for mensaje in consumidor:
            print("__ Nuevo Mensaje __")
            print(f"Mensaje recibido de {consumidor.subscription()}: {mensaje.value.decode('utf-8')}\n")
    except Exception as e:
        print("Error al recibir un mensaje.")
        