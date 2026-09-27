from __future__ import annotations

import pandas as pd
import streamlit as st

from e060_data import ROOT, WORKBOOK_PATH, load_results, lookup_result

LAMINA_PATH = ROOT / "lamina_tecnica.svg"


def result_block(label: str, value: object, unit: str, formula: str, reference: str, status: str) -> None:
    is_unverified = status == "NO VERIFICADO" or pd.isna(value)
    color = "#B91C1C" if is_unverified else "#92400E"
    background = "#FEE2E2" if is_unverified else "#FEF3C7"
    shown = "NO VERIFICADO" if pd.isna(value) else f"{float(value):,.2f} {unit}"
    st.markdown(
        f"""<div class="result" style="border-left-color:{color};background:{background}">
        <div class="result-title">{label}</div><div class="result-value" style="color:{color}">{shown}</div>
        <div><b>Fórmula:</b> {formula}</div><div><b>Unidades:</b> {unit}</div>
        <div><b>Referencia:</b> {reference}</div><div><b>Trazabilidad:</b> <span style="color:{color};font-weight:700">{status}</span></div>
        </div>""",
        unsafe_allow_html=True,
    )


st.set_page_config(page_title="E060 Acero — Julio Rojas", page_icon="🏗️", layout="wide")
st.markdown("""<style>
div[data-testid="stAppViewContainer"]{padding-top:5.2rem}.fixed-warning{position:fixed;top:0;left:0;right:0;z-index:999999;background:#7F1D1D;color:white;padding:12px 24px;text-align:center;font-weight:700;box-shadow:0 2px 8px #0004}.result{border-left:7px solid;padding:14px 16px;margin:10px 0;border-radius:6px}.result-title{font-weight:700}.result-value{font-size:1.55rem;font-weight:800;margin:4px 0 8px}
</style><div class="fixed-warning">Herramienta educativa. No apta para diseño estructural.<br>Los valores deben verificarse contra la Norma E.060 vigente.</div>""", unsafe_allow_html=True)
st.title("E060 Acero — Julio Rojas")

try:
    data = load_results()
except Exception as exc:
    st.error(str(exc))
    st.stop()

tab_calc, tab_sheet, tab_trace = st.tabs(["Consulta", "Lámina técnica", "Trazabilidad"])
with tab_calc:
    c1, c2 = st.columns(2)
    barra = c1.selectbox("Diámetro de barra", data["Barra"].drop_duplicates().tolist())
    gancho = c2.selectbox("Tipo de gancho", data["Tipo de gancho"].drop_duplicates().tolist())
    row = lookup_result(barra, gancho)
    st.caption(row["Nota de trazabilidad"])
    reference = row["Referencia"]
    status = row["Estado"]
    a, b = st.columns(2)
    with a:
        result_block("Diámetro interior mínimo", row["Diámetro interior mínimo"], row["Unidad"], row["Fórmula dimensiones"], reference, status)
        result_block("Longitud de desarrollo a tracción ld", row["Desarrollo a tracción ld"], row["Unidad"], row["Fórmula ld"], reference, status)
        result_block("Traslape Clase A", row["Traslape Clase A"], row["Unidad"], row["Fórmula traslape"], reference, status)
    with b:
        result_block("Extensión del gancho", row["Extensión del gancho"], row["Unidad"], row["Fórmula dimensiones"], reference, status)
        result_block("Desarrollo con gancho ldg", row["Desarrollo con gancho ldg"], row["Unidad"], row["Fórmula ldg"], reference, status)
        result_block("Traslape Clase B", row["Traslape Clase B"], row["Unidad"], row["Fórmula traslape"], reference, status)
with tab_sheet:
    if LAMINA_PATH.is_file():
        st.image(str(LAMINA_PATH), use_container_width=True)
    else:
        st.error(f"No se encontró {LAMINA_PATH.name}.")
with tab_trace:
    st.dataframe(data[["Barra", "Tipo de gancho", "Referencia", "Estado", "Nota de trazabilidad"]], hide_index=True, use_container_width=True)
    st.info("Las hipótesis del caso educativo están documentadas en la hoja PARAMETROS del Excel. La aplicación no contiene coeficientes ni valores normativos.")
