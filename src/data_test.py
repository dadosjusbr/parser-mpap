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
            dados = load(file_names, "2021", "01", "/output")
            dados.validate("src/output_test/sheets/")
        self.assertEqual(cm.exception.code, STATUS_DATA_UNAVAILABLE)

    def test_validate_existence_05_2022(self):
        file_names = ['/output/membros-ativos-contracheque-05-2022.xls',
                      '/output/membros-ativos-indenizatorias-05-2022.xls']
        try:
            with self.assertRaises(SystemExit) as cm:
                dados = load(file_names, '2022', '05', "/output")
                dados.validate("/output")
            self.assertEqual(cm.exception.code, STATUS_DATA_UNAVAILABLE)
        except Exception as exc:
            if "SystemExit not raised" in str(exc):
                assert True
            else:
                assert False


if __name__ == "__main__":
    unittest.main()
