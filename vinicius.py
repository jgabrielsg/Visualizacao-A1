import numpy
import pandas
from funcoes import collect_data, filtrar_colunas, valores_unicos, contar_repeticoes, valores_unicos
from datacleaning import clean_data
import matplotlib.pyplot as plt

df_area = filtrar_colunas(collect_data(), "Area")
df_area["Area"] = df_area["Area"].str.strip()

df_area = contar_repeticoes(df_area, "Area")

print(df_area)
print(valores_unicos(df_area, "Area"))