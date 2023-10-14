import unittest
import pandas as pd
from funcoes import collect_data

class DFTests(unittest.TestCase):

    def setUp(self):
        self.gabarito1 = pd.read_csv("testes_dados/collect_data/gabarito_1.csv", encoding='latin1', sep =";")
        # self.gabarito2 = ... 
        
    # Teste collect_data
    def test1(self):
        result_df = collect_data('testes_dados/collect_data/dados')
        self.assertTrue(self.gabarito1.equals(result_df))

if __name__ == '__main__':
    unittest.main()