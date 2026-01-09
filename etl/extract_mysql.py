import pandas as pd
from sqlalchemy import create_engine

# 1) Configuración
USER = "root"          # ej: "root"
PASSWORD = "hoplita1990"
HOST = "localhost"
PORT = 3306
DB = "baterias_nano"

# 2) Conexión
engine = create_engine(
    f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
)

# 3) Extract
query = "SELECT * FROM ventas_baterias;"
df = pd.read_sql(query, engine)

print("Filas:", len(df))
print(df.head(10))

# 4) Guardar snapshot (opcional, buenísimo para ETL)
df.to_csv("ventas_baterias_raw.csv", index=False, encoding="utf-8")
print("OK -> ventas_baterias_raw.csv generado")
