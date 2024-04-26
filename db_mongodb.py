from pymongo import MongoClient

def get_mongo_connection():
    try:
        client = MongoClient('localhost', 27017, username='root', password='example')
        db = client['storage']
        return db
    except Exception as e:
        print("Error al conectarse.")
        return None
