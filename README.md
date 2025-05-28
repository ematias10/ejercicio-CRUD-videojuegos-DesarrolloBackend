# MisJuegos

Este proyecto es una aplicación para gestionar y explorar juegos, desarrollada con Django.

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- (Opcional) Entorno virtual recomendado

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/misjuegos.git
    cd misjuegos
    ```

2. (Opcional) Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

Para aplicar migraciones y ejecutar el servidor de desarrollo:
```bash
python manage.py migrate
python manage.py runserver
```

## Estructura del proyecto

- `/misjuegos`: Código fuente principal del proyecto Django
- `/videojuegos`: Aplicación para gestionar los videojuegos y su CRUD (Crear, Leer, Actualizar, Borrar). 

## Notas
- Asegúrate de tener configurada la base de datos en `settings.py`.
- Puedes crear un superusuario para acceder al panel de administración con:
    ```bash
    python manage.py createsuperuser
    ```
- Accede al panel de administración en `http://localhost:8000/admin` con las credenciales del superusuario.
- Para explorar los videojuegos, visita `http://localhost:8000/videojuegos/`.




