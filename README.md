# KafkaDocker

Aplicacion para gestionar un sistema de mensajeria con Kafka y el almacenamiento de los mensajes con mongo.

## Usar

* Instalar "pip install git+https://github.com/dpkp/kafka-python.git"
* Instalar "pip install kafka-python"
* Ejecutar "app.py"

## Manual
* Tras una correcta ejecución por medio de la terminal se le solictiara el nombre y seguidamente se le solicitara el nombre del canal al que desea sucribirse 
* Una vez ingresado esos datos se desplegara un menú con 4 opciones 
    1. Enviar mensaje.
    2. Cambiar canal de lectura y escritura.
    3. Mensajes anteriores.
    4. Cerrar la aplicacion.
* Enviar mensaje: Se le solicitara que ingrese el mensaje a enviar.
* Cambiar canal de lectura y escritura: Si desea ingresar a otro canal.
* Mensajes anteriores: Muestra los mensajes del canal almacenados en mongo.
* Cerrar la aplicacion: Termina la ejecución.

## Arquitectura

## Kafka

## Mongo
* Mongo se utiliza para almacenar a los usuarios y los mensajes que fueron pasados por los canales.
* En el app.py se guarda el dato del usuario y se pasa el Id generado a mensajeria para posteriormente pasarlo a productor.
* En productor se guarda los datos del mensaje (fecha, userId, canal y mensaje) en la colección correspondiente al canal que se este utilizando.
* En consumidor cuando se llama a ver todos los mensajes de un canal, primero se buscan los mismos y luego se utiliza el idUser para buscar los datos del usuario en el collection users e imprimirlos junto con el el mensaje correspondiente. 