import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from funcoes import collect_data, filtrar_colunas, remover_espacos
from datacleaning import arrumar_tipos

class DFTests(unittest.TestCase):

    # Aqui sao feitos os unitest com as funcoes criadas, para isso foram criados csv's pequenos
    # e manipulados com as funcoes. Para isso foram criados csv's especificos para se aplicar cada funcao, já que 
    # elas foram pensadas para analisar uma base de dados com colunas especificas em formatos especificos, e foram criados
    # "gabaritos", que sao os dataframes que seriam o resultado correto do output da funcao.    

    def test_collect_data(self):
        self.gabarito = pd.read_csv("testes_dados/collect_data/gabarito_1.csv", encoding='latin1', sep =";")
        self.df = collect_data('testes_dados/collect_data/dados')
        assert_frame_equal(self.gabarito, self.df)

    def test_arrumar_tipos(self):
        self.gabarito = pd.read_csv("testes_dados/arrumar_tipos/gabarito.csv", encoding='latin1', sep =";")
        self.df = pd.read_csv("testes_dados/arrumar_tipos/arrumar_tipos.csv", encoding='latin1', sep =";")
        assert_frame_equal(self.gabarito, arrumar_tipos(self.df))

    def test_remover_espacos(self):
        self.gabarito = pd.read_csv("testes_dados/remover_espacos/gabarito.csv", encoding='latin1', sep =";")
        self.df = pd.read_csv("testes_dados/remover_espacos/espacado.csv", encoding='latin1', sep =";")
        assert_frame_equal(self.gabarito, remover_espacos(self.df, "espaco"))

    # Teste collect_data
    def test_filtrar_colunas(self):
        self.gabarito2 = pd.read_csv("testes_dados/filtrar_colunas/gabarito_2.csv", encoding='latin1', sep =";")
        df_original = pd.read_csv("testes_dados/filtrar_colunas/dados.csv", encoding='latin1', sep =";")
        result_df = filtrar_colunas(df_original,"Nome","Idade")
        self.assertTrue(self.gabarito2.equals(result_df))

if __name__ == '__main__':
    unittest.main()