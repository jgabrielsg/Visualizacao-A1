import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from funcoes import collect_data, arrumar_tipos, filtrar_colunas, contar_repeticoes
from datacleaning import clean_data

def make_plot_guilherme(df):
    df_copia = filtrar_colunas(df, 'Atuacao em Territorio Indigena','Qtd Valores Apreendidos','Sigla Unidade Federativa').copy()

    df_agrupado = df_copia.groupby(['Atuacao em Territorio Indigena','Sigla Unidade Federativa'])['Qtd Valores Apreendidos'].mean().reset_index(name="Média")

    df_pivot = df_agrupado.pivot_table(values='Média',  columns=['Atuacao em Territorio Indigena'], index = 'Sigla Unidade Federativa', fill_value=0)

    df_pivot.plot(kind="bar")
    plt.yscale("log")
    # plt.show()
    return plt
    

fig = make_plot_guilherme(clean_data(collect_data()))
fig.savefig('graficos/graficoguilherme.png')