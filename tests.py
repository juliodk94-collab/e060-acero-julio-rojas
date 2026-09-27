import math
import unittest
from pathlib import Path

import pandas as pd

from e060_data import lookup_result


ROOT = Path(__file__).resolve().parent
BOOK = ROOT / "E060_Acero_Julio_Rojas.xlsx"


class ValidationSheetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = pd.read_excel(BOOK, sheet_name="VALIDACION", engine="openpyxl")

    def test_all_validation_cases(self):
        numeric = ["db_mm", "Diámetro interior mínimo", "Extensión del gancho", "Desarrollo a tracción ld", "Desarrollo con gancho ldg", "Traslape Clase A", "Traslape Clase B"]
        for _, expected in self.cases.iterrows():
            with self.subTest(caso=expected["caso"]):
                actual = lookup_result(expected["Barra"], expected["Tipo de gancho"], BOOK)
                tolerance = float(expected["tolerancia_mm"])
                for field in numeric:
                    ev, av = expected[field], actual[field]
                    if pd.isna(ev):
                        self.assertTrue(pd.isna(av), field)
                    else:
                        self.assertTrue(math.isclose(float(av), float(ev), abs_tol=tolerance), f"{field}: {av} != {ev}")
                self.assertEqual(actual["Unidad"], expected["Unidad"])

    def test_source_files_are_relative_and_present(self):
        self.assertTrue(BOOK.is_file())
        self.assertTrue((ROOT / "lamina_tecnica.svg").is_file())


if __name__ == "__main__":
    unittest.main()
