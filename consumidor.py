from bson import ObjectId
from db_mongodb import get_mongo_connection
from config import consumidor

# Recibe un mensaje del servidor de kafka
def recibirMensaje():
    try:
        while True:
            consumidor.poll(timeout_ms=1000)
            for mensaje in consumidor:
                print("__ Nuevo Mensaje __")
                print(f"Mensaje recibido de {consumidor.subscription()}: {mensaje.value.decode('utf-8')}\n")
    except Exception as e:
        print("Error al recibir un mensaje.")

def recibirMensajesAnteriores(canal):
    try:
        db = get_mongo_connection()
        subscription = db[canal]
        Mensajes = subscription.find({})
        user = db['users']
        for mensaje in Mensajes:
            usuario = user.find_one({'_id': ObjectId(mensaje['userId'])},{'_id': 0, 'name': 1})
            print(f"Usuario: {usuario['name']}")
            print(f"Canal: {mensaje['canal']}")
            print(f"Mensaje: {mensaje['mensaje']}")
            print(f"Fecha: {mensaje['fecha']}\n")
    except Exception as e:
        print("Error al recibir los mensajes.")
        