# Importaciones
from bson import ObjectId
from db_mongodb import get_mongo_connection
from config import getBandera

# Recibe un mensaje del servidor de kafka mediante un consumidor
def recibirMensaje(consumidor):
    try:
        # Obtenemos el canal del consumidor
        canal = consumidor.subscription().pop()
        print(f"Se ingreso en el canal de '{canal}'.")
        # Mientras este activo el consumidor
        while getBandera():
            # Recibimos los mensajes de los isguientes segundos
            mensajes = consumidor.poll(timeout_ms=3000)
            # Si hay mensajes
            if mensajes != {}:
                # Tomamos los mensajes y los imprimimos
                for topic_partition, lista_mensajes in mensajes.items():
                    for mensaje in lista_mensajes:
                        print("__ Nuevo Mensaje __")
                        canal = consumidor.subscription().pop()
                        print(f"Mensaje recibido de '{canal}': {mensaje.value.decode('utf-8')}\n")
        # Se sale del consumidor
        canal = consumidor.subscription().pop()
        print(f"Se salio en el canal de '{canal}'.")
    except Exception as e:
        print("Error al recibir un mensaje.")

# Funcion para tomar los mensajes de mongo
def recibirMensajesAnteriores(canal):
    try:
        # Tomamos la conexcion
        db = get_mongo_connection()
        subscription = db[canal]
        # Buscamos el doumento
        Mensajes = subscription.find({})
        user = db['users']
        # Imprimimos los datos de los mensajes 
        print("__ Historial __")
        for mensaje in Mensajes:
            usuario = user.find_one({'_id': ObjectId(mensaje['userId'])},{'_id': 0, 'name': 1})
            print(f"Usuario: {usuario['name']}")
            print(f"Canal: {mensaje['canal']}")
            print(f"Mensaje: {mensaje['mensaje'].decode('utf-8')}")
            print(f"Fecha: {mensaje['fecha']}\n")
    except Exception as e:
        print("Error al recibir los mensajes.")
        