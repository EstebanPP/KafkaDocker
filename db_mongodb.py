from pymongo import MongoClient
import os

def get_mongo_connection():
    try:
        client = MongoClient(os.getenv('MONGO-HOST'),
                             int(os.getenv('MONGO-PORT')),
                                username=os.getenv('MONGO-USERNAME'),
                                password=os.getenv('MONGO-PASSWORD'))
        db = client['storage']
        return db
    except Exception as e:
        print("Error al conectarse.")
        return None
