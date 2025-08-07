# telecomX
Telecom X - Análisis de Evasión de Clientes

Este proyecto realiza un análisis exploratorio de datos de una empresa de telecomunicaciones, enfocado en identificar patrones relacionados con la pérdida de clientes (**churn**). Se aplican técnicas de ETL (extracción, transformación y carga) y visualización de datos para generar hallazgos útiles para el negocio.

##  📁 Estructura del Proyecto

telecomX/

├── data/

│ └── TelecomX_Data.json

├── plots/

│ ├── churn_account_Contract.png

│ ├── churn_account_PaymentMethod.png

│ ├── churn_customer_gender.png

│ ├── distribucion_account_Charges.Monthly.png

│ ├── distribucion_account_Charges.Total.png

│ ├── distribucion_churn.png

│ └── distribucion_customer_tenure.png

├── src/

│ ├── analisis.py

│ ├── etl.py

│ └── transform.py

├── requirements.txt

└── README.md


## ⚙️ Instalación

### 1. Clonar el repositorio
'''bash

git clone https://github.com/VicenteRdzR/telecomX.git

cd telecomX

pip install -r requirements.txt

## ⚙️ Ejecucion

### 1. Ejecutar script de extracción
python src/etl.py

### 2. Ejecutar script de transformacion
python src/transform.py

### 3. Ejecutar script de analisis
python src/analisis.py

## 📫 Contacto

Vicente Rodríguez

jvicente.rdz.r@gmail.com