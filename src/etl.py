import pandas as pd
import os

def cargar_datos(nombre_archivo: str) -> pd.DataFrame:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # telecomX/
    ruta_archivo = os.path.join(base_dir, "data", nombre_archivo)

    try:
        df = pd.read_json(ruta_archivo)
        print("Datos cargados localmente")
        return df
    except Exception as e:
        print(f"Error al leer el archivo local: {e}")
        return pd.DataFrame()