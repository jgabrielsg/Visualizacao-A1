"""Módulo que contém as funções que criam os gráficos de cada aluno."""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from funcoes import collect_data, filtrar_colunas, contar_repeticoes, criar_df_guilherme
from datacleaning import clean_data
from matplotlib.ticker import FuncFormatter

def make_plot_vinicius(df):
    """ Cria um gráfico de barras que exibe a quantidade de apreensões por estado em 2022.

    Parameters
    ----------
    df : DataFrame
        O DataFrame contendo os dados dos valores apreendidos por estado.

    Returns
    -------
    Figure
        Um objeto de figura do Matplotlib contendo o gráfico gerado.
    """
    # Limpeza pessoal do Dataset
    df_estados = filtrar_colunas(df, "Sigla Unidade Federativa")
    df_estados = contar_repeticoes(df_estados, "Sigla Unidade Federativa")
    df_estados = df_estados.rename_axis(index = "ESTADOS")

    # Plotagem do gráfico
    regioes_cores = {"Norte": (["AC", "AM", "AP", "PA", "RO", "RR", "TO"], "green"),
                    "Nordeste": (["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"], "red"),
                    "Centro-Oeste": (["DF", "GO", "MS", "MT"], "orange"),
                    "Sudeste": (["ES", "MG", "RJ", "SP"], "yellow"),
                    "Sul": (["PR", "RS", "SC"], (1, 0, 1))}

    barras = plt.barh(df_estados.index, df_estados["QUANTIDADE"], height = 0.5)
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
            plt.text(largura - 70, barra.get_y() + barra.get_height() / 2, f"{porcentagem:.2f}%", ha = "center",
                    va = "center", fontsize=8, fontweight = "bold", color = "#010101", linespacing = 0.9)

    # Legenda
    for regiao, (siglas, cor) in regioes_cores.items():
        plt.bar(0, 0, color = cor, label = regiao)
    plt.legend(loc = "lower right")

    # Personalização do gráfico
    plt.xlabel("Quantidade")
    plt.ylabel("Estados")
    plt.title("Quantidade de Apreensões por Estado")
    plt.grid(axis = "x", linestyle = "--", alpha=0.6)

    return plt

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
    
    Example
    -------
    Exemplo de uso:

    >>> df = clean_data(collect_data())
    >>> fig = make_plot_guilherme(df)
    >>> fig.savefig('graficos/graficoguilherme.png')
    """
    #Previne que o df original seja modificado.
    df_copia = df.copy()
    df_copia = filtrar_colunas(df_copia, 'Atuacao em Territorio Indigena','Qtd Valores Apreendidos','Sigla Unidade Federativa')

    #Remove os estados sem atuação em território indigena.
    estados_ap_ind = df_copia[df_copia['Atuacao em Territorio Indigena'] == 'Sim'].groupby('Sigla Unidade Federativa').size().index
    df_ap_ind = df_copia[df_copia['Sigla Unidade Federativa'].isin(estados_ap_ind)]

    df_agrupado = df_ap_ind.groupby(['Atuacao em Territorio Indigena','Sigla Unidade Federativa'])['Qtd Valores Apreendidos'].mean().reset_index(name="Média")
    df_pivot = df_agrupado.pivot_table(values='Média',  columns=['Atuacao em Territorio Indigena'], index = 'Sigla Unidade Federativa', fill_value=0)

    plt.style.use("Solarize_Light2")
    df_pivot.plot(kind='bar', edgecolor='white', linewidth=1)
    plt.yscale("log")

    plt.xlabel('Estado (UF)', fontsize=8)
    plt.xticks(rotation=90)
    plt.ylabel('Quantidade Apreendida (log)', fontsize=8)
    plt.grid(axis='y', linestyle='--', alpha=0.3)

    plt.title('Quantidade Apreendida em Território Indigena', fontsize=12)
    legenda = ['Não','Sim']
    plt.legend(legenda, title='Atuação em território indigena', title_fontsize=10, fontsize=8)

    return plt

def make_gustavo_plot(df):
    """ Cria um stackplot das operações policiais ao longo do tempo

    Parameters
    ----------
    df : DataFrame
        O DataFrame com os dados necessários.

    Returns
    -------
    Figure
        Um objeto de figura do Matplotlib contendo o gráfico gerado.
    """

    # Cria uma cópia das colunas necessáras do dataframe
    df_copia = df.copy()
    df_copia = filtrar_colunas(df, "Data da Deflagracao", "Area")

    #Deixando mais curtos os títulos para que a legenda seja mais legível
    df_copia.loc[df_copia["Area"] == "Crimes Ambientais e Contra o Patrimônio Cultural", "Area"] = "Crimes Ambientais"
    df_copia.loc[df_copia["Area"] == "Crimes de Ódio e Pornografia Infantil", "Area"] = "Crimes de Ódio e Porn. Infantil"
    
    #Evita que um aviso do pandas apareca criando um novo df
    df_copia = df_copia.copy()
    df_copia["Data de Deflagracao"] = df_copia['Data da Deflagracao'].dt.strftime('%m/%Y')

    # Usado para saber as áreas de atuação das operações mais frequêntes
    contagem_area = df_copia["Area"].value_counts().index

    # Agrupa por mês e área de atuação as operações
    grouped = df_copia.groupby(['Area', 'Data de Deflagracao']).size().unstack(fill_value=0)

    grouped = grouped.loc[contagem_area[:10]]

    colors = ['#9e0142', '#d53e4f', '#f46d43', '#fdae61', '#fee08b',
              '#e6f598', '#abdda4', '#66c2a5', '#3288bd', '#5e4fa2']

    plt.style.use("Solarize_Light2")
    plot = plt.figure(figsize=(14, 8))
    plt.stackplot(grouped.columns, grouped.values, labels=grouped.index, alpha=0.8, colors=colors)
    plt.xticks(range(1, 13), rotation=30)
    plt.xlim(grouped.columns.min(), grouped.columns.max())
    plt.xlabel('Mês')

    plt.ylabel("Quantidade de Operações")
    ax = plt.gca()
    y_intervals = [100, 200, 300, 400, 500, 600, 700, 800, 900]  # Define as quantidades das linhas que cruzam o gráfico
    for y in y_intervals:
        ax.axhline(y=y, color='black', linestyle='--', alpha=0.3)
    
    plt.title("Operações policiais por Área de Atuação em 2022")
    plt.legend(title='Area', title_fontsize='14', loc='upper right', bbox_to_anchor=(1.13, 1))
    # plt.show()

    return plot

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
    df = clean_data(collect_data())

    fig_vinicius = make_plot_vinicius(df)
    fig_vinicius.savefig('graficos/graficovinicius.png')

    fig_guilherme = make_plot_guilherme(df)
    fig_guilherme.savefig('graficos/graficoguilherme.png')

    fig_gustavo = make_gustavo_plot(df)
    fig_gustavo.savefig('graficos/graficogustavo.png')

    fig_joao = make_plot_joao(df)
    fig_joao.savefig('graficos/graficojoao.png')