from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel

# Inicializar la aplicación FastAPI
app = FastAPI()

# Modelo de entrada para predicciones
class PredictionInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    # Agrega más campos según las características de tu modelo

# Ruta para verificar que la API está funcionando
@app.get("/")
def read_root():
    return {"message": "La API está funcionando correctamente"}

# Ruta para realizar predicciones
@app.post("/predict")
def predict(input_data: PredictionInput):
    # Aquí cargarías el modelo y harías predicciones
    # Por ejemplo, simulando una predicción:
    prediction = 1  # Cambia esto con la lógica real de predicción
    return {"prediction": prediction}

def start_api():
    """
    Función para iniciar la API.
    """
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
