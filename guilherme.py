import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from funcoes import collect_data, arrumar_tipos, filtrar_colunas, contar_repeticoes
from datacleaning import clean_data

def make_plot_guilherme(df):
    df_copia = filtrar_colunas(df, 'Atuacao em Territorio Indigena','Qtd Valores Apreendidos','Sigla Unidade Federativa').copy()

    #Remove os estados sem atuação em território indigina, ou valores muito baixos
    estados_ap_ind = df_copia[df_copia['Atuacao em Territorio Indigena'] == 'Sim'].groupby('Sigla Unidade Federativa').size().index
    
    df_ap_ind = df_copia[df_copia['Sigla Unidade Federativa'].isin(estados_ap_ind)]

    df_agrupado = df_ap_ind.groupby(['Atuacao em Territorio Indigena','Sigla Unidade Federativa'])['Qtd Valores Apreendidos'].mean().reset_index(name="Média")

    df_pivot = df_agrupado.pivot_table(values='Média',  columns=['Atuacao em Territorio Indigena'], index = 'Sigla Unidade Federativa', fill_value=0)

    df_pivot.plot(kind="bar")
    plt.yscale("log")
    return plt
    

fig = make_plot_guilherme(clean_data(collect_data()))
fig.show()
fig.savefig('graficos/graficoguilherme.png')