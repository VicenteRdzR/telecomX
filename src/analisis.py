import pandas as pd
import matplotlib.pyplot as plt
from etl import cargar_datos

ruta = "TelecomX_Data.json"
df = cargar_datos(ruta)

# Aplanar columnas anidadas
columnas_anidadas = ['customer', 'phone', 'internet', 'account']
for col in columnas_anidadas:
    if col in columnas_anidadas:
        nuevas_columnas = pd.json_normalize(df[col])
        nuevas_columnas.columns = [f"{col}_{subcol}" for subcol in nuevas_columnas.columns]
        df = pd.concat([df.drop(columns=[col]), nuevas_columnas], axis=1)
        
# Limpieza basica
df.replace(['No internet service', 'No phone service'], 'No', inplace=True)

# Mapear columnas binarias
map_si_no = {'Yes': 1, 'No': 0}
columnas_si_no = [
    'Churn', 'customer_Partner', 'customer_Dependents',
    'phone_PhoneService', 'phone_MultipleLines',
    'internet_OnlineSecurity', 'internet_OnlineBackup', 'internet_DeviceProtection',
    'internet_TechSupport', 'internet_StreamingTV', 'internet_StreamingMovies',
    'account_PaperlessBilling'
]

for col in columnas_si_no:
    if col in df.columns:
        df[col] = df[col].map(map_si_no).fillna(0).astype(int)
        
# Convertir campos numericos
df['account_Charges.Total'] = pd.to_numeric(df['account_Charges.Total'], errors='coerce')
df['account_Charges.Total'].fillna(df['account_Charges.Total'].median(), inplace=True)

# Analisis Descriptivo
print("--- Estadistias descriptivas ---")
print(df.describe())

# Distribucion de evasion
churn_counts = df['Churn'].value_counts()
plt.figure()
plt.bar(churn_counts.index.astype(str), churn_counts.values, color=['green', 'red'])
plt.title("Distribucion de Evasion (Churn)")
plt.xlabel("Churn (0 = No, 1 = Si)")
plt.ylabel("Numero de clientes")
plt.tight_layout()
plt.savefig("plots/distribucion_churn.png")
plt.show()

# Recuento de evasion por variable categorica
variables_categoricas = ['customer_gender', 'account_Contract', 'account_PaymentMethod']

for var in variables_categoricas:
    if var in df.columns:
        plt.figure()
        df.groupby([var])['Churn'].mean().plot(kind='bar')
        plt.title(f"Tasa de Evasion por {var}")
        plt.ylabel("Proporcion de evasion")
        plt.xlabel(var)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"plots/churn_{var}.png")
        plt.show()
        
# Recuento de evasion por variables numericas
variables_numericas = ['account_Charges.Total', 'account_Charges.Monthly', 'customer_tenure']

for var in variables_numericas:
    if var in df.columns:
        plt.figure()
        df[df['Churn'] == 0][var].plot(kind='hist', alpha=0.5, label='No Churn')
        df[df['Churn'] == 1][var].plot(kind='hist', alpha=0.5, label='Churn')
        plt.title(f"Distribucion de {var} por Evasion")
        plt.xlabel(var)
        plt.ylabel("Frecuencia")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"plots/distribucion_{var}.png")
        plt.show()