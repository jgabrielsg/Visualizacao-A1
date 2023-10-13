import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from funcoes import collect_data, arrumar_tipos, filtrar_colunas, contar_repeticoes
from datacleaning import clean_data


def make_plot_guilherme(df):
    """Cria um gráfico de barras que exibe de forma comparativa os valores apreendidos em territórios indigenas e não-indigenas por estado.

    Esta função recebe um DataFrame contendo os dados de valores apreendidos por estado e
    gera um gráfico de barras que mostra os valores apreendidos por estado em territórios indigenas e não-indigenas.


    Parameters
    ----------
    df : DataFrame
        O DataFrame contendo os dados dos valores apreendidos por estado.

    Returns
    -------
    Figure
        Um objeto de figura do Matplotlib contendo o gráfico gerado.
    """
    df_copia = filtrar_colunas(df, 'Atuacao em Territorio Indigena','Qtd Valores Apreendidos','Sigla Unidade Federativa').copy()

    #Remove os estados sem atuação em território indigena
    estados_ap_ind = df_copia[df_copia['Atuacao em Territorio Indigena'] == 'Sim'].groupby('Sigla Unidade Federativa').size().index
    df_ap_ind = df_copia[df_copia['Sigla Unidade Federativa'].isin(estados_ap_ind)]

    df_agrupado = df_ap_ind.groupby(['Atuacao em Territorio Indigena','Sigla Unidade Federativa'])['Qtd Valores Apreendidos'].mean().reset_index(name="Média")

    df_pivot = df_agrupado.pivot_table(values='Média',  columns=['Atuacao em Territorio Indigena'], index = 'Sigla Unidade Federativa', fill_value=0)

    df_pivot.plot(kind='bar', edgecolor='white', linewidth=1)
    plt.yscale("log")

    plt.title('Quantidade Apreendida em Território Indigena', fontsize=12)
    plt.xlabel('Estado (UF)', fontsize=8)
    plt.ylabel('Quantidade Apreendida (log)', fontsize=8)
    plt.grid(axis='y', linestyle='--', alpha=0.3)

    legenda = ['Sim', 'Não']
    plt.legend(legenda, title='Atuação em território indigena', title_fontsize=10, fontsize=8)
    
    return plt
    

fig = make_plot_guilherme(clean_data(collect_data()))
# fig.show()
fig.savefig('graficos/graficoguilherme.png')