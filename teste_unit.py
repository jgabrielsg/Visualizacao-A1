import unittest
import pandas as pd
from funcoes import collect_data, filtrar_colunas

class DFTests(unittest.TestCase):

    def setUp(self):
        self.gabarito1 = pd.read_csv("testes_dados/collect_data/gabarito_1.csv", encoding='latin1', sep =";")
        self.gabarito2 = pd.read_csv("testes_dados/filtrar_colunas/gabarito_2.csv", encoding='latin1', sep =";")
        
    # Teste collect_data
    def test_collect_data(self):
        result_df = collect_data('testes_dados/collect_data/dados')
        self.assertTrue(self.gabarito1.equals(result_df))

    # Teste collect_data
    def test_filtrar_colunas(self):
        df_original = pd.read_csv("testes_dados/filtrar_colunas/dados.csv", encoding='latin1', sep =";")
        result_df = filtrar_colunas(df_original,"Nome","Idade")
        self.assertTrue(self.gabarito2.equals(result_df))

if __name__ == '__main__':
    unittest.main()