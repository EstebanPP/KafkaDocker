import time
from datetime import datetime
from db_mongodb import get_mongo_connection
from bson import ObjectId

# Configura el servidor de Kafka
def enviarMensaje(productor, canal, mensaje, userId):
    try:
        productor.send(canal, mensaje.encode('utf-8'))
        time.sleep(1)
        productor.flush()
        time.sleep(2)
        db = get_mongo_connection()
        subscription = db[canal]
        subscription.insert_one({"userId":ObjectId(userId), "fecha":datetime.now(),"canal":canal,"mensaje":mensaje.encode('utf-8')})
    except Exception as e:
        print("Error al escribir un mensaje.")
