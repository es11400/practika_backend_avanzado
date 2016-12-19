# practika_django
Práctica de Python, Django y REST

##Instalacción

Clonamos el repo.

```bash
$ git clone https://github.com/es11400/practika_django.git
```


Despues hay un script de instalación ```install.sh``` que: 

1. Crea el entorno virtual
2. Instala las dependencias en el mismo
3. Crea un usuario con privilegios de administrador

Para ejecutar el instalador, sitúate en la carpeta del proyecto desde el terminal y ejecuta:

```
$ ./install.sh
```

## Arranque de la app

### Servidor web

Para arrancar el servidor, hay que *activar el entorno virtual* y luego *arrancar el servidor* de desarrollo de Django.

Desde la carpeta del proyecto y en el terminal, ejecuta:

```
$ source env/bin/activate
(env)$ python manage.py runserver
```

### Celery (servicio de procesamiento en background)

Para arrancar Celery, hay que *activar el entorno virtual* y luego *arrancar el Celery*.

Desde la carpeta del proyecto y en el terminal, ejecuta:

```
$ source env/bin/activate
(env)$ celery -A cuentame worker -l info
```






nota: El instalador y el readme.md, están basados en la sabidurida de @kas.


## Contenido de la prática.

### Internacionalización.

Se añade la posibilidad de añadir idiomas, en este caso hemos añadido Inglés.

### Integración con terceros

Ofrecemos integración con terceros.

Puede probar el correcto funcionamiento de esta con la aplicación de Heroku ofrecida por Django-Oauth-Toolkit.

http://django-oauth-toolkit.herokuapp.com/consumer/exchange/

Para ver ver o crear las aplicaciones del usuario, debe estar autenticado en la plataforma.

```
http://127.0.0.1:8000/oauth/applications
```


Obtención de tokens, para ello deberá para los siguiente información

    grant_type    : authorization_code
   
    code          : 
   
    client_id     :
   
    client_secret :
   
    redirect_uri  :

```
http://127.0.0.1:8000/oauth/token
```
Para revocar o refrescar el token

```
http://127.0.0.1:8000/oauth/revoke_token
```


### Login Social

Se añade acceso y registro de usuarios mediante Facebook y Twitter.
    

### Autenticacion del API basada en tokens JWT

Añadimos el uso de tokens JWT para todos los endpoints que requieren seguridad, el tiempo standard es de 5 minutos, siendo este configurable en el settings.

```
JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=3),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(minutes=5),
}
```


### API SUBIDA DE ARCHIVOS Y GENERACION DE THUMBNAILS E IMAGENES RESPONSIVE

Para esta opción se ha optado por utilizar un sistema de tareas en background con Kombu o RabbitMQ y Celery.

Para el uso de  Rabbitmq es necesario tenerlo instaldo, por defecto el settings viene configuración para trabajar con Kombu

BROKER_URL = 'django://'

Para instalar Rabbitmq

http://www.rabbitmq.com/download.html

Y cambiar en el settings el parámetro BROKER_URL

BROKER_URL = 'amqp://guest:guest@localhost:5672//'

El formato minimo es de 3600px y se generan 3 tamaños por cada imagen añadida.

    small  ->  500
    medium ->  750
    large  -> 1000

### NOTIFICACIONES DE RESPUESTA Y MENCIONES

Pendiente de realizar