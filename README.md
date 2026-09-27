# E060 Acero — Julio Rojas

Herramienta educativa en Streamlit para consultar dimensiones de ganchos, longitudes de desarrollo y traslapes. No es apta para diseño estructural. Los resultados deben verificarse contra la Norma E.060 vigente y por un profesional responsable.

## Fuente y trazabilidad

`E060_Acero_Julio_Rojas.xlsx` es la única fuente de valores, coeficientes, fórmulas legibles, unidades, referencias y estados de trazabilidad usados por la aplicación. `app.py` solo carga y presenta la información del libro; no contiene valores normativos.

El libro fue estructurado a partir de la Norma E.060 suministrada, especialmente las secciones 7.1, 7.2, 12.2, 12.5 y 12.15. Las hipótesis del caso educativo están identificadas en `PARAMETROS`; no deben interpretarse como valores obligatorios para un proyecto real.

## Estructura

- `app.py`: aplicación Streamlit.
- `E060_Acero_Julio_Rojas.xlsx`: fuente única de datos normativos y casos de validación.
- `lamina_tecnica.svg`: lámina técnica mostrada dentro de la app.
- `tests.py`: reproduce los casos de la hoja `VALIDACION`.
- `requirements.txt`: dependencias fijadas para despliegue reproducible.
- `.streamlit/config.toml`: configuración visual sin secretos.

Las rutas se resuelven desde la ubicación de `app.py`, por lo que funcionan localmente y en Streamlit Community Cloud sin depender del directorio de ejecución.

## Ejecución local

```bash
python -m pip install -r requirements.txt
python tests.py
streamlit run app.py
```

## Despliegue en Streamlit Community Cloud

1. Publicar estos archivos en un repositorio de GitHub, sin secretos ni credenciales.
2. En Streamlit Community Cloud, elegir el repositorio, la rama principal y `app.py` como archivo de entrada.
3. No se necesitan variables secretas para esta versión.
4. Confirmar visualmente la carga del Excel y de `lamina_tecnica.svg` después del primer despliegue.

## Limitaciones

El escenario incluido usa hipótesis educativas documentadas en el Excel. La selección no reemplaza la verificación de resistencia de materiales, recubrimiento, espaciamiento, posición de barras, tratamiento epóxico, concreto liviano, responsabilidad sísmica ni condiciones particulares del proyecto.
