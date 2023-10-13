import numpy as np
import pandas as pd
from funcoes import filtrar_colunas, valores_unicos, contar_repeticoes, valores_unicos
import matplotlib.pyplot as plt

def gustavo_plot(df):
    df_copia = filtrar_colunas(df, "Data da Deflagracao", "Area")
    df_copia["Mes"] = pd.to_datetime(df_copia['Data da Deflagracao']).dt.strftime('%m/%Y')
    
    # df_copia["Mes"] = df_copia["Mes"].map(meses)

    contagem_area = df_copia["Area"].value_counts().index

    grouped = df_copia.groupby(['Area', 'Mes']).size().unstack(fill_value=0)

    grouped = grouped.loc[contagem_area[:10]]
    # grouped.set_index('Mes', inplace=True)

    colors = ['#9e0142', '#d53e4f', '#f46d43', '#fdae61', '#fee08b',
              '#e6f598', '#abdda4', '#66c2a5', '#3288bd', '#5e4fa2']

    plt.style.use("Solarize_Light2")
    plt.figure(figsize=(14, 8))
    plt.stackplot(grouped.columns, grouped.values, labels=grouped.index, alpha=0.8, colors=colors)
    plt.xticks(range(1, 13), rotation=30)
    plt.xlim(grouped.columns.min(), grouped.columns.max())
    plt.xlabel('mês de 2022')

    plt.ylabel('Número de operações policiais')
    ax = plt.gca()
    y_intervals = [100, 200, 300, 400, 500, 600, 700, 800, 900]  # Define as quantidades das linhas que cruzam o gráfico
    for y in y_intervals:
        ax.axhline(y=y, color='black', linestyle='--', alpha=0.3)
    
    plt.title('Tipos de operações durante 2022')
    plt.legend(title='Area', title_fontsize='14', loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.show()

    return plt