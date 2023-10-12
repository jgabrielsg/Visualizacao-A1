import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from funcoes import collect_data, filtrar_colunas, contar_repeticoes

# Limpeza pessoal do Dataset
df_estados = filtrar_colunas(collect_data(), "Sigla Unidade Federativa")
df_estados["Sigla Unidade Federativa"] = df_estados["Sigla Unidade Federativa"].str.strip()
df_estados = contar_repeticoes(df_estados, "Sigla Unidade Federativa")
df_estados = df_estados.rename_axis(index = "ESTADOS")
print(df_estados)

# Plotagem do gráfico
regioes_cores = {"Norte": (["AC", "AM", "AP", "PA", "RO", "RR", "TO"], "green"),
                 "Nordeste": (["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"], "red"),
                 "Centro-Oeste": (["DF", "GO", "MS", "MT"], "orange"),
                 "Sudeste": (["ES", "MG", "RJ", "SP"], "yellow"),
                 "Sul": (["PR", "RS", "SC"], "purple")}

barras = plt.barh(df_estados.index, df_estados["QUANTIDADE"], height = 0.4)
total_soma = df_estados["QUANTIDADE"].sum()

for num, barra in enumerate(barras):
    estado = df_estados.index[num]
    for regiao, (siglas, cor) in regioes_cores.items():
        if estado in siglas:
            barra.set_color(cor)

    largura = barra.get_width()
    porcentagem = (largura / total_soma) * 100
    if porcentagem < 10:
        plt.text(largura + 10, barra.get_y() + barra.get_height() / 2, f"{porcentagem:.2f}%", ha = "left",
                 va = "center", fontsize=8, fontweight = "bold", color = "#010101", linespacing = 0.9)
    else:
        plt.text(largura, barra.get_y() + barra.get_height() / 2, f"{porcentagem:.2f}%", ha = "center",
                 va = "center", fontsize=8, fontweight = "bold", color = "#010101", linespacing = 0.9)

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