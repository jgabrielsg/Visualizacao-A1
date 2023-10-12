import numpy as np
import pandas as pd
from funcoes import collect_data, filtrar_colunas, valores_unicos, contar_repeticoes, valores_unicos
from datacleaning import clean_data
import matplotlib.pyplot as plt

df_area = filtrar_colunas(collect_data(), "Area")
df_area["Area"] = df_area["Area"].str.strip()

df_area = contar_repeticoes(df_area, "Area")
df_area = df_area.drop_duplicates(subset = ["Area"], keep = "first")
df_area = df_area.set_index("Area").rename_axis(index = "AREA").sort_values("QUANTIDADE", ascending=True)

print(df_area)