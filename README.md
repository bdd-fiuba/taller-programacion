# Taller VII: Programación con Bases de Datos

## Introducción

En el taller se tratará con dos bases de datos: MongoDB y postgresql.

Se dividirá el proyecto en etapas, de las cuales el estudiante puede elegir hacerlas o no según haya instalado los requerimientos. Se puede utilizar `docker` y `docker-compose` para contar con todos los requerimientos a la vez.

### Utilizando `docker`

1) Instalar `docker` y `docker-compose` en su sistema operativo.
    - [Linux](https://docs.docker.com/engine/install/)
    - [Windows](https://docs.docker.com/docker-for-windows/install/):
    - [Mac](https://docs.docker.com/docker-for-mac/install/)
2) Configurar correctamente los volumenes de `docker` para que pueda acceder a los archivos desde su sistema operativo en el archivo `docker-compose.yaml`.
3) Ejecutar `docker-compose up -d` para iniciar los contenedores.

## Parte 1: Webserver y MongoDB

Editar el archivo `src/mongodb/load_tweet.py` con su IDE para completar la operación requerida.

## Parte 2: Webserver y Postgresql

Verificar que existen 3 archivos en `src/psql`:
- `init.py`
- `load_tweet.py`
- `orm.py`

Editar el archivo `src/psql/load_tweet.py` con su IDE para completar la operación requerida.
Luego, editar el archivo `src/psql/orm.py` para completar la misma operación pero utilizando la interfaz tipo ORM de `sqlalchemy`.

## Parte 3: Transformación de datos con `dbt`

1. Explorar el directorio `/dbt` para ver los archivos de configuración y los modelos.
2. Entrar en la instancia de `dbt` con:
    ```bash
    docker exec -it webserver bash
    ```
3. Ejecutar `dbt run` para ejecutar los modelos.
4. Ejecutar `dbt test` para ejecutar las pruebas.
5. Ejecutar `dbt docs generate` para generar la documentación.
6. Ejecutar `dbt docs serve` para visualizar la documentación en el navegador.
