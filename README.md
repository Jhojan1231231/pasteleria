# Dulce Encanto - Pastelería

Aplicación web desarrollada con Django para administrar una pastelería.

## Funcionalidades

- Catálogo público de productos.
- Búsqueda por nombre y filtro por línea.
- Visualización de detalles y fotografías.
- Registro de encargos sin necesidad de iniciar sesión.
- Validación de datos del cliente.
- Control automático del stock.
- Comprobantes con código único.
- Administración de productos, líneas y encargos desde Django Admin.

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML y CSS

## Instalación

1. Clonar o descargar el repositorio.
2. Crear un entorno virtual:

   `python -m venv .venv`

3. Activar el entorno virtual en Windows:

   `.venv\Scripts\activate`

4. Instalar dependencias:

   `pip install -r requirements.txt`

5. Ejecutar las migraciones:

   `python manage.py migrate`

6. Iniciar el servidor:

   `python manage.py runserver`

7. Abrir en el navegador:

   `http://127.0.0.1:8000/`

## Administración

El panel administrativo se encuentra en:

`http://127.0.0.1:8000/admin/`

Se debe utilizar un usuario administrador previamente creado.