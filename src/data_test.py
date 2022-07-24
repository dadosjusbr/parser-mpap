from data import load
import unittest


STATUS_DATA_UNAVAILABLE = 4


class TestData(unittest.TestCase):
    def test_validate_existence(self):
        file_names = [
            "src/output_test/sheets/membros-ativos-contracheque-07-2019.xls",
            "src/output_test/sheets/membros-ativos-indenizatorias-07-2019.xls",
        ]
        with self.assertRaises(SystemExit) as cm:
            dados = load(file_names, "2021", "01", "src/output_test/sheets") # mês e ano alterados para simular erro
            dados.validate("src/output_test/sheets/")
        self.assertEqual(cm.exception.code, STATUS_DATA_UNAVAILABLE)

    def test_validate_existence_05_2022(self):
        file_names = ['src/output_test/sheets/membros-ativos-contracheque-05-2022.xls',
            "src/output_test/sheets/membros-ativos-indenizatorias-05-2022.xls"]
        with self.assertRaises(SystemExit) as cm:
            dados = load(file_names, '2022', '06', "src/output_test/sheets") # mês alterado para simular erro
            dados.validate("src/output_test/sheets")
        self.assertEqual(cm.exception.code, STATUS_DATA_UNAVAILABLE)


if __name__ == "__main__":
    unittest.main()
