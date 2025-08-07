from etl import cargar_datos
import pandas as pd

ruta = "TelecomX_Data.json"
df = cargar_datos(ruta)

# Conocer conjunto de datos
print("Informacion de DataFrame:")
df.info()

print("Descripcion rapida estadistica de variables numericas:")
print(df.describe())

print("Primeras filas:")
print(df.head())

print("Columnas:")
print(df.columns.tolist())

# Comprobacion de incoherencias en los datos
print("Valores faltantes por columna:")
print(df.isnull().sum())

# Aplanar columnas anidadas
columnas_anidadas = ['customer', 'phone', 'internet', 'account']

for col in columnas_anidadas:
    if col in df.columns:
        nuevas_columnas = pd.json_normalize(df[col])
        nuevas_columnas.columns = [f"{col}_{subcol}" for subcol in nuevas_columnas.columns] 
        df = pd.concat([df.drop(columns=[col]), nuevas_columnas], axis=1)
        
print("Columnas actuales del DataFrame:")
print(df.columns.tolist())

# Filas duplicadas
print("Numero de filas duplicadas:")
print(df.duplicated().sum())

# Convertir a numérico y rellenar TotalCharges
if 'TotalCharges' in df.columns:
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    median_total = df['TotalCharges'].median()
    df['TotalCharges'] = df['TotalCharges'].fillna(median_total)
    print(f"Valores nulos en TotalCharges rellenados con la mediana: {median_total}")

# Convertir a numérico y rellenar account_Charges.Total
if 'account_Charges.Total' in df.columns:
    df['account_Charges.Total'] = pd.to_numeric(df['account_Charges.Total'], errors='coerce')
    median_account_total = df['account_Charges.Total'].median()
    df['account_Charges.Total'] = df['account_Charges.Total'].fillna(median_account_total)
    print(f"Valores nulos en account_Charges.Total rellenados con la mediana: {median_account_total}")

# Mapeo para convertir Yes/No a 1/0
map_si_no = {'Yes': 1, 'No': 0}

# Lista de columnas binarias a transformar
columnas_si_no = [
    'Churn',
    'customer_Partner',
    'customer_Dependents',
    'phone_PhoneService',
    'phone_MultipleLines',
    'internet_OnlineSecurity',
    'internet_OnlineBackup',
    'internet_DeviceProtection',
    'internet_TechSupport',
    'internet_StreamingTV',
    'internet_StreamingMovies',
    'account_PaperlessBilling'
]

# Reemplazar "No internet service" y "No phone service" por "No"
valores_no_servicio = ['No internet service', 'No phone service']
df.replace(valores_no_servicio, 'No', inplace=True)

for col in columnas_si_no:
    if col in df.columns:
        df[col] = df[col].map(map_si_no).fillna(0).astype(int)

print("\nDatos transformados (primeras filas):")
print(df.head())

print("\nTipos de datos actuales:")
print(df.dtypes)