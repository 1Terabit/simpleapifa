# Simple API FastAPI

Este es un proyecto de ejemplo que utiliza FastAPI para crear una API RESTful. La aplicación está estructurada de manera modular, lo que facilita su mantenimiento y escalabilidad.

## Estructura del Proyecto
```python
simpleapifa/
├── app/
│   ├── __init__.py
│   ├── main.py                # Archivo principal donde se inicia la aplicación FastAPI
│   ├── database.py            # Configuración de la base de datos
│   ├── models/                # Modelos de la base de datos
│   │   ├── __init__.py
│   │   ├── user.py            # Modelo de usuario
│   │   ├── item.py            # Modelo de ítem
│   │   └── comment.py         # Modelo de comentario
│   ├── schemas/               # Esquemas de Pydantic para validación
│   │   ├── __init__.py
│   │   ├── user.py            # Esquema de usuario
│   │   ├── item.py            # Esquema de ítem
│   │   └── comment.py         # Esquema de comentario
│   ├── services/              # Lógica de negocio
│   │   ├── __init__.py
│   │   ├── user_service.py     # Servicios para usuarios
│   │   ├── item_service.py     # Servicios para ítems
│   │   └── comment_service.py  # Servicios para comentarios
│   └── api/                   # Rutas de la API
│       ├── __init__.py
│       └── endpoints/         # Endpoints de la API
│           ├── __init__.py
│           ├── users.py       # Endpoints para usuarios
│           ├── items.py       # Endpoints para ítems
│           └── comments.py     # Endpoints para comentarios
├── tests/                     # Pruebas de la aplicación
│   ├── __init__.py
│   ├── conftest.py            # Archivo de configuración de pruebas y fixtures
│   ├── test_users.py          # Pruebas para usuarios
│   ├── test_items.py          # Pruebas para ítems
│   └── test_comments.py       # Pruebas para comentarios
├── requirements.txt           # Dependencias del proyecto
├── .env
└── README.md                  # Documentación del proyecto
```

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/simpleapifa.git
   cd simpleapifa
   ```

2. Crea un entorno virtual y actívalo:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate  # En Windows
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` en la raíz del proyecto y configura tus variables de entorno:

   ```plaintext
   DB_USER=tu_usuario
   DB_PASSWORD=tu_contraseña
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=tu_base_de_datos
   ```

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
uvicorn app.main:app --reload
```

La aplicación estará disponible en `http://127.0.0.1:8000`.

## Pruebas

Para ejecutar las pruebas, utiliza el siguiente comando:

```bash
pytest
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

