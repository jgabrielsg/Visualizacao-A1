import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from funcoes import collect_data, filtrar_colunas, contar_repeticoes

df_estados = filtrar_colunas(collect_data(), "Sigla Unidade Federativa")
df_estados["Sigla Unidade Federativa"] = df_estados["Sigla Unidade Federativa"].str.strip()

df_estados = contar_repeticoes(df_estados, "Sigla Unidade Federativa")
df_estados = df_estados.drop_duplicates(subset = ["Sigla Unidade Federativa"], keep = "first")
df_estados = df_estados.set_index("Sigla Unidade Federativa").rename_axis(index = "ESTADOS").sort_values("QUANTIDADE", ascending=True)

x = df_estados.index
y = df_estados["QUANTIDADE"]

plt.barh(x, y)
plt.xlabel("Quantidade")
plt.ylabel("Estados")
plt.title("Quantidade de apreensões por estado")

plt.show()
plt.savefig('graficos/graficovinicius.png')