import numpy as np
import pandas as pd
from funcoes import collect_data
from datacleaning import clean_data

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def graph_currency(value, pos):
    """
    Formata valores em milhões para uso em legendas de gráficos.

    Esta função formata o valor para exibir em formato de moeda, indicando milhões
    se o valor for maior ou igual a 1 milhão.

    Parameters
    ----------
    value : int
        O valor a ser formatado.
    pos : int
        Argumento obrigatório da função FuncFormatter.

    Returns
    -------
    str
        A representação formatada do valor em milhões, no formato "$X.XXM" se o valor
        for maior ou igual a 1 milhão, caso contrário, no formato "$X".

    Example
    -------
    Exemplo de uso:

    >>> graph_currency(1500000, 0)
    '$1.5M'

    >>> graph_currency(50, 0)
    '$50'
    """
    if value >= 1e6: 
        return f'${value/1e6:.0f}M'  
    else:
        return f'${value:.0f}' 

def make_plot_joao(df):
    """
    Cria um gráfico de barras que exibe os valores apreendidos por estado em 2022.

    Esta função recebe um DataFrame contendo os dados de valores apreendidos por estado e
    gera um gráfico de barras que mostra os valores apreendidos por estado em 2022.

    Parameters
    ----------
    df : DataFrame
        O DataFrame contendo os dados dos valores apreendidos por estado.

    Returns
    -------
    Figure
        Um objeto de figura do Matplotlib contendo o gráfico gerado.

    Example
    -------
    Exemplo de uso:

    >>> df = clean_data(collect_data())
    >>> fig = make_plot_joao(df)
    >>> fig.savefig('graficos/graficojoao.png')
    """
    df_estados = df.groupby('Sigla Unidade Federativa')['Qtd Valores Apreendidos'].sum().reset_index()
    df_estados = df_estados.rename(columns={'Qtd Valores Apreendidos': 'Total Valores Apreendidos'})
    df_estados = df_estados.sort_values(by='Total Valores Apreendidos', ascending=True)

    colors = ['green' if i > 21 else 'gray' for i in range(len(df_estados))]

    plot = plt.figure(figsize=(10, 6))
    plt.bar(df_estados['Sigla Unidade Federativa'], df_estados['Total Valores Apreendidos'], color=colors)

    plt.legend(['Valores Apreendidos'], loc='upper left')

    plt.axvspan(21.5, 26.5, color='red', alpha=0.3, label='Valores acima de 500 milhões')

    plt.text(15, 1000000000, 'Valores > 500M', fontsize=12, color='black', fontweight='bold')

    bars = plt.bar(df_estados['Sigla Unidade Federativa'], df_estados['Total Valores Apreendidos'], color=colors)

    total_sum = df_estados['Total Valores Apreendidos'].sum()

    for bar in bars:
        height = bar.get_height()
        percentage = (height / total_sum) * 100
        plt.text(bar.get_x() + bar.get_width() / 2, height / 2, f'{percentage:.2f}%', ha='center', va='baseline', rotation=90, fontsize=8, fontweight='bold', color='#010101', linespacing=0.9)

    plt.axhline(y=1000000, color='r', linestyle='--', label='Limiar de 1 milhão')
    plt.fill_between(df_estados['Sigla Unidade Federativa'], 0, df_estados['Total Valores Apreendidos'], alpha=0.2)
    plt.title('Valores Apreendidos por Estado em 2022')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.text(0.02, 0.92, 'Dados de 2022', transform=plt.gcf().transFigure)

    plt.xlabel('Estados')
    plt.ylabel('Valores Apreendidos')
    plt.title('Valores Apreendidos por Estado')

    formatter = FuncFormatter(graph_currency)
    plt.gca().yaxis.set_major_formatter(formatter)

    return plot

if __name__ == "__main__":
    fig = make_plot_joao(clean_data(collect_data()))
    fig.savefig('graficos/graficojoao.png')
