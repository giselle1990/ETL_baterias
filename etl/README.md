# 🔋 ETL_baterias

Proyecto **ETL (Extract, Transform, Load)** desarrollado en **Python** para la extracción, limpieza y transformación de datos de ventas de baterías automotrices.  
El objetivo es construir una base de datos limpia y consistente que permita análisis posteriores, reportes y visualizaciones (BI).

---

## 📌 Objetivo del proyecto

- Extraer datos de ventas desde una fuente de datos (MySQL / CSV).
- Normalizar y limpiar la información (nombres, formatos, valores nulos).
- Generar un dataset final listo para análisis y/o carga en sistemas de reporting.
- Aplicar buenas prácticas de **Data Engineering** y **control de versiones**.

---

## 🧱 Estructura del proyecto

```text
ETL_baterias/
│
├── etl/
│   ├── README.md                # Documentación específica del proceso ETL
│   ├── extract_mysql.py         # Extracción de datos desde MySQL / fuente externa
│   ├── transform_clean.py       # Limpieza y transformación de datos
│   ├── ventas_baterias_raw.csv  # Datos crudos (ejemplo)
│   └── requirements.txt         # Dependencias del proyecto
│
├── ventas_baterias_clean.csv    # Dataset final limpio



⚙️ Tecnologías utilizadas

Python 3

Pandas

MySQL / CSV

Git & GitHub

🔄 Flujo ETL

Extract

Conexión a base de datos MySQL o lectura de archivos CSV.

Extracción de datos de ventas de baterías.

Transform

Limpieza de datos (nulos, duplicados, formatos).

Normalización de campos (texto, fechas, categorías).

Reglas de negocio para estandarización.

Load

Generación de un archivo CSV limpio.

Listo para análisis, dashboards o carga en BI.

🚀 Cómo ejecutar el proyecto

Clonar el repositorio:

git clone https://github.com/giselle1990/ETL_baterias.git
cd ETL_baterias


Crear y activar entorno virtual (opcional pero recomendado):

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows


Instalar dependencias:

pip install -r etl/requirements.txt


Ejecutar scripts:

python etl/extract_mysql.py
python etl/transform_clean.py

📊 Posibles usos

Análisis de ventas de baterías automotrices.

Integración con dashboards en Power BI / Tableau.

Base para pipelines de datos más complejos.

Proyecto demostrativo de ETL y Data Engineering.

🧩 Próximas mejoras

Carga automática a base de datos (PostgreSQL / MySQL).

Logging y manejo de errores.

Automatización del pipeline.

Integración con herramientas de BI.

👩‍💻 Autora

Giselle San German
└── README.md                    # Documentación general del proyecto

