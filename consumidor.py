from bson import ObjectId
from db_mongodb import get_mongo_connection
from config import getConsumidor , getBandera

# Recibe un mensaje del servidor de kafka
def recibirMensaje(consumidor):
    try:
        print(f"Se ingreso en el canal de {consumidor.subscription()}")
        while getBandera():
            mensajes = consumidor.poll(timeout_ms=3000)
            if mensajes != {}:
                print("__ Nuevo Mensaje __")
                print(f"Mensaje recibido de {consumidor.subscription()}: {mensajes}\n")
        print(f"Se salio en el canal de {consumidor.subscription()}")
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
        