import pandas as pd
import os  

def title_case(s: pd.Series) -> pd.Series:
    def transform(value):
        if pd.isna(value):
            return value
        return value.strip().lower().title()

    return s.astype("string").apply(transform)

def upper_clean(s: pd.Series) -> pd.Series:
    return s.astype("string").str.strip().str.upper()

def infer_jurisdiccion_simple(zona: pd.Series, jurisdiccion: pd.Series) -> pd.Series:
    j = jurisdiccion.astype("string").str.strip()
    z = zona.astype("string").fillna("").str.strip().str.upper()

    is_blank = j.isna() | (j == "") | (j.str.lower() == "nan")

    pba_keywords = ["PBA", "CASEROS", "SAN FERNANDO", "VILLA RAFFO", "VICENTE", "GARIN", "GBA"]
    is_pba = z.apply(lambda x: any(k in x for k in pba_keywords))

    j_out = j.copy()
    j_out[is_blank & (z != "") & is_pba] = "PBA"
    j_out[is_blank & (z != "") & (~is_pba)] = "CABA"
    return j_out.str.upper()

def main():
    input_file = "etl/ventas_baterias_raw.csv"
    if not os.path.exists(input_file):
        print(f"Error: El archivo '{input_file}' no existe.")
        return

    df = pd.read_csv(input_file)

    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce").dt.date
    df["monto"] = pd.to_numeric(df["monto"], errors="coerce")
    df["monto"] = df["monto"].round(0).astype("Int64")

    df["vehiculo_marca"] = title_case(df.get("vehiculo_marca"))
    df["vehiculo_modelo"] = title_case(df.get("vehiculo_modelo"))
    df["bateria_marca"] = title_case(df.get("bateria_marca"))

    df["bateria_codigo"] = upper_clean(df.get("bateria_codigo"))
    df["dominio"] = upper_clean(df.get("dominio"))

    df["zona"] = df.get("zona").astype("string").fillna("").str.strip().str.title()
    df.loc[df["zona"] == "", "zona"] = pd.NA

    df["jurisdiccion"] = infer_jurisdiccion_simple(df.get("zona"), df.get("jurisdiccion"))

    df["vehiculo_anio"] = pd.to_numeric(df.get("vehiculo_anio"), errors="coerce").astype("Int64")

    cap = df.get("bateria_capacidad_ah").astype("string")
    df["bateria_capacidad_ah"] = pd.to_numeric(cap.str.extract(r"(\d+)")[0], errors="coerce").astype("Int64")

    df["forma_pago"] = df.get("forma_pago").astype("string").str.strip()

    cols = [
        "fecha", "zona", "jurisdiccion", "monto", "forma_pago",
        "vehiculo_marca", "vehiculo_modelo", "vehiculo_anio", "dominio",
        "bateria_marca", "bateria_codigo", "bateria_capacidad_ah"
    ]
    df_clean = df[cols].copy()

    df_clean.to_csv("ventas_baterias_clean.csv", index=False, encoding="utf-8")
    print("OK -> ventas_baterias_clean.csv generado")
    print("Filas:", len(df_clean))
    print(df_clean.head(10))

if __name__ == "__main__":
    main()
