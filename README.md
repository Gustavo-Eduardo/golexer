# Analizador de codigo GO

## Para correr este proyecto necesitas
- `pip install "fastapi[all]"` Esto instalará FastAPI junto con Uvicorn para usar como server de la app.
- `pip install pydantic` Para instalar la libreria que permite recibir el Request body del cliente.
- `uvicorn main:app` Para iniciar el server desde el archivo main.py. Tambien puedes usar la _flag_ `--reload` para refrescar el servidor con cada cambio en el código, no usar para producción.

## Una vez lanzado el proyecto puedes
- Acceder a la api desde `http://127.0.0.1:8000/<endpoint>` para acceder a los endpoints de la api.
- Acceder a la documentación en SwaggerUI desde `http://127.0.0.1:8000/docs`.