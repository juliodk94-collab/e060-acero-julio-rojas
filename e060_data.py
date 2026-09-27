from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent
WORKBOOK_PATH = ROOT / "E060_Acero_Julio_Rojas.xlsx"


def load_results(path: Path = WORKBOOK_PATH) -> pd.DataFrame:
    if not path.is_file():
        raise FileNotFoundError(f"No se encontró la fuente de datos: {path.name}")
    return pd.read_excel(path, sheet_name="RESULTADOS", engine="openpyxl")


def lookup_result(barra: str, gancho: str, path: Path = WORKBOOK_PATH) -> pd.Series:
    data = load_results(path)
    match = data[(data["Barra"] == barra) & (data["Tipo de gancho"] == gancho)]
    if len(match) != 1:
        raise ValueError("La combinación seleccionada no existe de forma única en RESULTADOS.")
    return match.iloc[0]
