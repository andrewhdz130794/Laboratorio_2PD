FROM python:3.9-slim

WORKDIR /app

# Copiar el archivo de dependencias
COPY ../requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar archivos necesarios desde la raíz del proyecto
COPY ../main.py main.py
COPY ../pipeline.py pipeline.py
COPY ../.env .env
COPY ../data/ data/

# Configurar el comando para el modo Batch
CMD ["python", "main.py"]



