# KafkaDocker

Aplicacion para gestionar un sistema de mensajeria con Kafka y el almacenamiento de los mensajes con mongo.

## Usar

* Para iniciar la aplicacion se deben seguir los siguientes pasos:
    1. Clonar el repositorio de "<https://github.com/EstebanPP/KafkaDocker.git>".
    2. Crear el contenedor con "docker-compose up -d --build".
    3. Ejecutar la aplicacion con "docker exec -it app python app.py".

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

* Para la arquitectura de la aplicacion se deciden implementar hilos, estos hilos se inician en app.py y controlan paralelamente el recibimiento de mensajes y a su vez un menu para las diferentes opciones de la app.
* Se tiene el consumidor de manera global en config.py para poder hacer uso de el dentro de toda la aplicacio.
* Para el menu se usa mensajeria.py la cual tiene las opciones para mandar un mensaje, cambiar el canal actual y ademas el ver el historial de mensajes, se implemento por aparte para tener una forma mas sencilla de acceder al historial en cualquier momento y no solo entrando en el chat.

## Kafka

* kafka se utiliza como sistema de mensajeria, lo que permite al usuario suscribirse a un canal y poder enviar y recibir mesajes del mismo canal.
* En productor.py se tiene el metodo enviarMensaje el cual mendiante un productor envia el mensaje al canal deseado.
* En consumidor.py se tiene el metodo de recibirMensaje el cual esta constantemente leyendo la entrada de mensajes del consumidor.
* Ademas se manera un consumidor global para poder hacer las modificaiones de los canales sin problema alguno.
* Kafka permite paralelamente poder enviar un mensaje por el primer hilo "escribir" y luego recibirlo en el hilo de "leer", esto como si fueran dos aplicaciones separadas, una enviando el mensaje y la otra lo recibe.

## Mongo

* Mongo se utiliza para almacenar a los usuarios y los mensajes que fueron pasados por los canales.
* En el app.py se guarda el dato del usuario y se pasa el Id generado a mensajeria para posteriormente pasarlo a productor.
* En productor se guarda los datos del mensaje (fecha, userId, canal y mensaje) en la colección correspondiente al canal que se este utilizando.
* En consumidor cuando se llama a ver todos los mensajes de un canal, primero se buscan los mismos y luego se utiliza el idUser para buscar los datos del usuario en el collection users e imprimirlos junto con el el mensaje correspondiente.
