FROM python:3.9-slim

WORKDIR /app

# Copia requirements.txt desde el directorio raíz
COPY ../requirements.txt requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos necesarios desde el directorio raíz
COPY ../main.py main.py
COPY ../pipeline.py pipeline.py
COPY ../.env .env
COPY ../data/ data/

CMD ["python", "main.py"]

