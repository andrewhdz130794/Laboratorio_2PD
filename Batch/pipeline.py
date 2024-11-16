import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def preprocess_data(file_path, target_column):
    """
    Función para preprocesar los datos.
    Carga los datos desde un archivo y separa las características de la columna objetivo.

    Args:
        file_path (str): Ruta del archivo.
        target_column (str): Nombre de la columna objetivo.

    Returns:
        X (DataFrame): Características.
        y (Series): Columna objetivo.
    """
    data = pd.read_parquet(file_path)
    if target_column not in data.columns:
        raise KeyError(f"La columna objetivo '{target_column}' no se encuentra. Columnas disponibles: {data.columns.tolist()}")
    X = data.drop(columns=[target_column])
    y = data[target_column]
    return X, y

def train_model(X, y):
    """
    Función para entrenar un modelo Random Forest.

    Args:
        X (DataFrame): Características.
        y (Series): Columna objetivo.

    Returns:
        model (RandomForestClassifier): Modelo entrenado.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def predict(model, data_file, target_column):
    """
    Función para realizar predicciones en nuevos datos.

    Args:
        model (RandomForestClassifier): Modelo entrenado.
        data_file (str): Ruta del archivo con nuevos datos.
        target_column (str): Nombre de la columna objetivo.

    Returns:
        predictions (ndarray): Predicciones del modelo.
    """
    new_data = pd.read_parquet(data_file)
    if target_column in new_data.columns:
        new_data = new_data.drop(columns=[target_column])
    predictions = model.predict(new_data)
    return predictions

def run_pipeline():
    """
    Función principal para ejecutar el pipeline en modo Batch.
    """
    print("Iniciando el pipeline Batch...")
    print(f"DATASET: {os.getenv('DATASET')}")
    print(f"INPUT_FOLDER: {os.getenv('INPUT_FOLDER')}")
    print(f"OUTPUT_FOLDER: {os.getenv('OUTPUT_FOLDER')}")

    # Leer variables de entorno
    dataset_path = os.getenv("DATASET")
    target_column = os.getenv("TARGET")
    input_folder = os.getenv("INPUT_FOLDER")
    output_folder = os.getenv("OUTPUT_FOLDER")

    # Preprocesar datos
    print(f"Cargando datos desde {dataset_path}...")
    X, y = preprocess_data(dataset_path, target_column)

    # Entrenar el modelo
    print("Entrenando el modelo...")
    model = train_model(X, y)

    # Procesar archivos en modo Batch
    print(f"Procesando archivos en la carpeta {input_folder}...")
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".parquet"):
            input_path = os.path.join(input_folder, file_name)
            print(f"Procesando archivo: {input_path}...")

            # Realizar predicciones
            predictions = predict(model, input_path, target_column)

            # Guardar las predicciones como Excel
            output_file = os.path.join(output_folder, f"predictions_{file_name.replace('.parquet', '.xlsx')}")
            pd.DataFrame(predictions, columns=["Prediction"]).to_excel(output_file, index=False)
            print(f"Predicciones guardadas en {output_file}")
