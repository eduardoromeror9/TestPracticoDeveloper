# Resumen de lo que hice, paso a paso

1. Creo un entorno virtual: `python3 -m venv venv`
2. instalar django: `pip install django`
3. Iniciar el proyecto: `django-admin startproject app`
4. Crear la app: `manage.py startapp app_bike`
5. Crear la tabla en postgreSQL
6. Cambiar los settings para conectar la DB
7. Instalar el adaptador para bd de python: `pip install psycopg2-binary`
8. Hacer las migraciones iniciales: `manage.py migrate`
9. Crear super usuario para entrar al admin de Django: `manage.py createsuperuser`

## MODELS.PY

1. Cree un modelo con 3 campos, con su metodo str para que muestre la info de la estacion.
2. Cree la clase meta que sirve para llamar en plural a las estaciones.
3 Termino definiendo los campos a buscar.

## VIEWS.PY

1. Importe el modelo Estacion y el file utils.
2. Cree una funcion de vista para que obtenga datos de la consulta que hace a la url desde el utils.py.
3. En la vista del template, filtre los datos por nombre para que no muestre repetidos.
4. Despues fui creando un objeto Estación para cada estación y lo guarda en la base de datos.
5. al final, crea el template llamado bikes.html con el contexto de estaciones.

## UTILS.PY

1. Este file lo cree para tener la funcion de consulta a la API y traer los datos en un json.
2. Despues la importe en la vista (views.py)

## URLS.PY

1. Aqui imoporte la vista que cree en mi app.
2. Le agregue la ruta en los path

## SETTINGS

1. En los settings le cambie la configuracion de la BD para conectar postgreSQL.
2. Le agregue la hora local de santiago al proyecto.
3. Agregue la app creada.

## TEMPLATE

1. hice un template basico con unos estilos de css.
    - Comprobe si habian estaciones disponibles y si no habia mostratia un mensaje error.
    - Fui recorriendo las estaciones para despues ir mostrando los name, free_bike y los empty_slots.

## ADMIN.PY

1. Cree una clase en el admin para mostrar el resultado que guardaba en mi modelo Estacion.
    - Importe los modelos el modelo de Estacion
2. Al admin tambien le agregue la opcion de buscar por nombre para mejorar la visualizacion de los datos.
3. En la vista de admin deje todos los datos de la BD.

## Proyecto BikeSantiago

    Este proyecto es una aplicación web desarrollada en Django que utiliza la API pública de BikeSantiago para mostrar información de las estaciones de bicicletas   disponibles en Santiago, Chile.

## Requisitos

    Para poder ejecutar este proyecto, es necesario tener instalado:

    Django (4.1.7)
    psycopg2
    requests

## Instalación

    Para instalar los paquetes necesarios, puedes utilizar el archivo requirements.txt incluido en este repositorio. Para hacerlo, simplemente abre una terminal en la carpeta raíz del proyecto y escribe el siguiente comando:

    `pip install -r requirements.txt`

### Ejecución

    Para utilizar la aplicación, debes ejecutar el servidor de Django. Para hacerlo, abre una terminal en la carpeta raíz del proyecto y escribe el siguiente comando:

    `python manage.py runserver`

    Después de ejecutar este comando, podrás acceder a la aplicación en tu navegador web ingresando la dirección http://localhost:8000/bikes/.

## Autor: Eduardo Romero
