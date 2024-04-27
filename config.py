from kafka import KafkaConsumer
import os

# Configuración del consumidor global
server = os.getenv('KAFKA-SERVER')
consumidor = KafkaConsumer(bootstrap_servers=server)