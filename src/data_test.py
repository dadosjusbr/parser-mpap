from data import load
import os
import unittest

month = '05'
year = '2022'
file_names = [f'src/output_test/sheets/membros-ativos-contracheque-{month}-{year}.xls',
              f'src/output_test/sheets/membros-ativos-indenizatorias-{month}-{year}.xls']


class TestData(unittest.TestCase):
    def test_validate_existence(self):
        STATUS_DATA_UNAVAILABLE = 4
        with self.assertRaises(SystemExit) as cm:
            dados = load(file_names, year, month, "")
            dados.validate("")
        self.assertEqual(cm.exception.code, STATUS_DATA_UNAVAILABLE)


if __name__ == "__main__":
    unittest.main()
