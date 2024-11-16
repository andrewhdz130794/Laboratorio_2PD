# Laboratorio 2PD

## Descripción
Este proyecto implementa un pipeline Batch y una API para procesar datos y generar predicciones. El pipeline Batch procesa archivos `.parquet` en una carpeta específica y genera predicciones guardándolas en formato `.xlsx`. La API permite realizar predicciones en tiempo real mediante solicitudes HTTP.

---

## Estructura del Proyecto
Laboratorio_2PD/ ├── API/ │ ├── main.py # Archivo principal para ejecutar la API │ ├── pipeline.py # Lógica de predicción para la API │ ├── requirements.txt # Dependencias necesarias para la API │ ├── .env # Variables de entorno para configurar la API ├── Batch/ │ ├── main.py # Archivo principal para ejecutar el Batch │ ├── pipeline.py # Lógica de predicción para el Batch │ ├── requirements.txt # Dependencias necesarias para el Batch │ ├── .env # Variables de entorno para configurar el Batch │ ├── data/ # Carpeta de datos │ ├── input/ # Archivos de entrada (.parquet) │ └── output/ # Resultados generados (.xlsx) └── README.md # Documentación del proyecto


---

## Requisitos
1. **Docker** instalado en tu sistema.
2. **Python 3.9+** (opcional si decides probar sin Docker).
3. Librerías necesarias especificadas en `requirements.txt`.

## IMPORTANTE!! 

1. Inicia Docker Desktop antes de Ejecutar los comandos de este archivo

2. Si realizas algùn cambio a los archivos para asegurarte que los cambios los tome deberas de
ejectuar nuevamente:
docker build -t automl-dockerizer-api .
docker build -t automl-dockerizer-batch .

3. Asegúrate de que las rutas en el archivo .env coincidan con la estructura de tu proyecto.

4. Verifica que los puertos utilizados por Docker estén disponibles (por defecto, 8000 para la API).
---

## Ejecución del Proyecto

# Modo Batch

#### **Paso 1: Navega a la Carpeta Batch**
Abre tu terminal y navega a la carpeta `Batch`:

cd Laboratorio_2PD
cd Batch

#### ** Paso 2 Construye la imagen Docker para el pipeline Batch**
docker build -t automl-dockerizer-batch .

#### ** Paso 3 Configura el Archivo .env**

DATASET=data/input/dataset.parquet
INPUT_FOLDER=data/input
OUTPUT_FOLDER=data/output
TARGET=Churn
#### ** Paso 4 Coloca tus archivos .parquet en la carpeta data/input.**
#### ** Paso 5 Ejecuta el Contenedor**
docker run --env-file .env -v "$(pwd)/data:/app/data" automl-dockerizer-batch
#### **Paso 6: Verifica los Resultados **
Los resultados se generarán en data/output como archivos .xlsx.

# Modo API

#### **Paso 1: Navega a la Carpeta API**
Abre tu terminal y navega a la carpeta `API`:

cd Laboratorio_2PD
cd API

#### ** Paso 2 Construye la imagen Docker para el pipeline API**
docker build -t automl-dockerizer-api .
#### ** Paso 3 Configura el Archivo .env**

Asegúrate de que el archivo .env en la carpeta API tenga el siguiente contenido:
TARGET=Churn

#### **Paso 4: Ejecuta el Contenedor**
Ejecuta el contenedor para la API:
docker run --env-file .env -p 8000:8000 automl-dockerizer-api


#### **Paso 5: Verifica que la API Funciona**
Accede a la API en tu navegador: http://localhost:8000

Visita la documentación interactiva: http://localhost:8000/docs

