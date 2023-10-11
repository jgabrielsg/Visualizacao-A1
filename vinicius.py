import numpy
import pandas
from funcoes import collect_data, filtrar_colunas

pasta = "dados"
df = collect_data(pasta)

print(filtrar_colunas(df, "Area", "Sigla Unidade Federativa"))
