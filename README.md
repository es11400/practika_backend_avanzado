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




