# Taller VII: Programación con Bases de Datos

## Introducción

En el taller se tratará con dos bases de datos: MongoDB y postgresql.

La ejecución es posible para dos tipos de instalaciones: con `docker` (y `docker-compose`) o de forma local, contando necesariamente con `python` y `postgresql` instalados.

## Entorno de desarrollo con `docker`

Teniendo `docker` y `docker-compose` instalados en su sistema operativo ejecutar:

1. Bases de datos:
    ```bash
    docker-compose up -d mongodb postgresql
    ```
2. Servidor de la API:
    ```bash
    docker-compose up --build webserver
    ```
    En este punto, debería ver logs de instalación y ejecución en su terminal.
3. Conexión al container del webserver con la instalación de python.
    ```bash
    docker-compose exec -it webserver bash
    ```
4. Una vez aquí, se podrán ejecutar comandos con la instalación de python. 

### Ejecución de carga de datos

Para testear su api, puede utilizar:
```bash
python carga_datos.py [cantidad] // Tal vez python3, según su instalación
```

## Parte 1: MongoDB

Moverse a la rama `docker/parte-1`:
```bash
git checkout docker/parte-1
```

Completar el archivo `webserver/src/database.py` para que:

1. Se conecte a la base de datos.
2. Se haga la carga de un tweet.
3. Se pueda consultar por un tweet por `id`.
4. Utilizar la rama `docker/parte-1-pydantic` para verificar cómo se construye en capa de negocio una solución a la verificación del esquema de datos.

## Parte 2: PostgreSQL

Ir a la rama `docker/parte-2` con:

```bash
git checkout docker/parte-2
```

## Parte 3: PostgreSQL con ORM

Ir a la rama `docker/parte-3` con:

```bash
git checkout docker/parte-3
```
