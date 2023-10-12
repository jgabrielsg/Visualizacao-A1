import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from funcoes import collect_data, filtrar_colunas, contar_repeticoes

# Limpeza pessoal do Dataset
df_estados = filtrar_colunas(collect_data(), "Sigla Unidade Federativa")
df_estados["Sigla Unidade Federativa"] = df_estados["Sigla Unidade Federativa"].str.strip()
df_estados = contar_repeticoes(df_estados, "Sigla Unidade Federativa")
df_estados = df_estados.drop_duplicates(subset = ["Sigla Unidade Federativa"], keep = "first")
df_estados = df_estados.set_index("Sigla Unidade Federativa").rename_axis(index = "ESTADOS").sort_values("QUANTIDADE", ascending=True)

# Plotagem do gráfico
regioes_cores = {"Norte": (["AC", "AM", "AP", "PA", "RO", "RR", "TO"], "green"),
                 "Nordeste": (["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"], "red"),
                 "Centro-Oeste": (["DF", "GO", "MS", "MT"], "orange"),
                 "Sudeste": (["ES", "MG", "RJ", "SP"], "yellow"),
                 "Sul": (["PR", "RS", "SC"], "purple")}

barras = plt.barh(df_estados.index, df_estados["QUANTIDADE"])
total_soma = df_estados["QUANTIDADE"].sum()

for num, barra in enumerate(barras):
    estado = df_estados.index[num]
    for regiao, (siglas, cor) in regioes_cores.items():
        if estado in siglas:
            barra.set_color(cor)

    largura = barra.get_width()
    percentage = (largura / total_soma) * 100
    plt.text(largura, barra.get_y() + barra.get_height() / 2, f"{percentage:.2f}%", ha = "left", 
             va = "center", fontsize=8, fontweight = "bold", color = "#010101", linespacing=0.9)

# Legenda
for regiao, (siglas, cor) in regioes_cores.items():
    plt.bar(0, 0, color=cor, label=regiao)
plt.legend(loc = "lower right")

# Personalização do gráfico
plt.xlabel("Quantidade")
plt.ylabel("Estados")
plt.title("Quantidade de Apreensões por Estado")
plt.grid(axis = "x", linestyle = "--", alpha=0.6)

plt.savefig("graficos/graficovinicius.png")