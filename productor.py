# Importaciones
import time
from datetime import datetime
from db_mongodb import get_mongo_connection
from bson import ObjectId

# Configura producdor te kafka
def enviarMensaje(productor, canal, mensaje, userId):
    try:
        # Enviamos el mensaje al servidor
        productor.send(canal, mensaje.encode('utf-8'))
        time.sleep(1)
        # Guardamos el mensaje en mongo
        db = get_mongo_connection()
        subscription = db[canal]
        subscription.insert_one({"userId":ObjectId(userId), "fecha":datetime.now(),"canal":canal,"mensaje":mensaje.encode('utf-8')})
    except Exception as e:
        print("Error al escribir un mensaje.")
