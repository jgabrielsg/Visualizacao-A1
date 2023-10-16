"""Módulo que contém as funções que criam os gráficos de cada aluno."""

import matplotlib.pyplot as plt
import gerar_dataframes
from datacleaning import clean_data
from funcoes import collect_data, graph_currency
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

    Example
    -------
    Exemplo de uso:

    >>> df = clean_data(collect_data())
    >>> df_vinicius = gerar_dataframes.criar_dataframe_vinicius(df)
    >>> fig = make_plot_vinicius(df_vinicius)
    >>> fig.savefig('graficos/graficovinicius.png')
    """

    #Definindo o estilo do gráfico
    plt.style.use("Solarize_Light2")

    # Plotagem do gráfico
    regioes_cores = {"Norte": (["AC", "AM", "AP", "PA", "RO", "RR", "TO"], "green"),
                    "Nordeste": (["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"], "red"),
                    "Centro-Oeste": (["DF", "GO", "MS", "MT"], "orange"),
                    "Sudeste": (["ES", "MG", "RJ", "SP"], "yellow"),
                    "Sul": (["PR", "RS", "SC"], (1, 0, 1))}

    barras = plt.barh(df.index, df["QUANTIDADE"], height = 0.5)
    total_soma = df["QUANTIDADE"].sum()

    for num, barra in enumerate(barras):
        estado = df.index[num]
        for regiao, (siglas, cor) in regioes_cores.items():
            if estado in siglas:
                barra.set_color(cor) # Separação por cores de acordo com a região

        largura = barra.get_width()
        porcentagem = (largura / total_soma) * 100
        if porcentagem < 10:
            plt.text(largura + 10, barra.get_y() + barra.get_height() / 2, f"{porcentagem:.2f}%", ha = "left",
                    va = "center", fontsize=8, fontweight = "bold", color = "#010101", linespacing = 0.9)
        else:
            # Aqui, coloquei as porcentagem para "dentro" da barra, pois antes elas estavam atravessando o limite do gráfico.
            plt.text(largura - 70, barra.get_y() + barra.get_height() / 2, f"{porcentagem:.2f}%", ha = "center",
                    va = "center", fontsize=8, fontweight = "bold", color = "#010101", linespacing = 0.9)

    # Legenda
    for regiao, (siglas, cor) in regioes_cores.items():
        plt.bar(0, 0, color = cor, label = regiao)
    plt.legend(loc = "lower right")

    # Personalização do gráfico
    plt.xlabel("Quantidade de Apreensões")
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
    >>> df_guilherme = gerar_dataframes.criar_dataframe_guilherme(df)
    >>> fig = make_plot_guilherme(df_guilherme)
    >>> fig.savefig('graficos/graficoguilherme.png')
    """

    plt.style.use("Solarize_Light2")
    df.plot(kind='bar', edgecolor='white', linewidth=1)
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

    >>> df = clean_data(collect_data())
    >>> df_gustavo = gerar_dataframes.criar_dataframe_gustavo(df)
    >>> fig = make_plot_gustavo(df_gustavo)
    >>> fig.savefig('graficos/graficogustavo.png')
    """

    colors = ['#9e0142', '#d53e4f', '#f46d43', '#fdae61', '#fee08b',
              '#e6f598', '#abdda4', '#66c2a5', '#3288bd', '#5e4fa2']

    plt.style.use("Solarize_Light2")
    plot = plt.figure(figsize=(14, 8))
    plt.stackplot(df.columns, df.values, labels=df.index, alpha=0.8, colors=colors)
    plt.xticks(range(1, 13), rotation=30)
    plt.xlim(df.columns.min(), df.columns.max())
    plt.xlabel('Mês')

    plt.ylabel("Quantidade de Operações")
    ax = plt.gca()
    y_intervals = [100, 200, 300, 400, 500, 600, 700, 800, 900]  # Define as quantidades das linhas que cruzam o gráfico
    for y in y_intervals:
        ax.axhline(y=y, color='black', linestyle='--', alpha=0.3)
    
    plt.title("Operações policiais por Área de Atuação em 2022")
    plt.legend(title='Area', title_fontsize='14', loc='upper right', bbox_to_anchor=(1.13, 1))

    return plot

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
    >>> df_joao = gerar_dataframes.criar_dataframe_joao(df)
    >>> fig = make_plot_joao(df_joao)
    >>> fig.savefig('graficos/graficojoao.png')
    """

    colors = ['green' if i > 21 else 'gray' for i in range(len(df))]

    plot = plt.figure(figsize=(10, 6))
    plt.bar(df['Sigla Unidade Federativa'], df['Total Valores Apreendidos'], color=colors)

    plt.legend(['Valores Apreendidos'], loc='upper left')

    plt.axvspan(21.5, 26.5, color='red', alpha=0.3, label='Valores acima de 500 milhões')

    plt.text(15, 1000000000, 'Valores > 500M', fontsize=12, color='black', fontweight='bold')

    bars = plt.bar(df['Sigla Unidade Federativa'], df['Total Valores Apreendidos'], color=colors)

    total_sum = df['Total Valores Apreendidos'].sum()

    for bar in bars:
        height = bar.get_height()
        percentage = (height / total_sum) * 100
        plt.text(bar.get_x() + bar.get_width() / 2, height / 2, f'{percentage:.2f}%', ha='center', va='baseline', rotation=90, fontsize=8, fontweight='bold', color='#010101', linespacing=0.9)

    plt.axhline(y=1000000, color='r', linestyle='--', label='Limiar de 1 milhão')
    plt.fill_between(df['Sigla Unidade Federativa'], 0, df['Total Valores Apreendidos'], alpha=0.2)
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
    df = collect_data()
    df = clean_data(df)

    df_vinicius = gerar_dataframes.criar_dataframe_vinicius(df)
    fig_vinicius = make_plot_vinicius(df_vinicius)
    fig_vinicius.savefig('graficos/graficovinicius.png')

    df_guilherme = gerar_dataframes.criar_dataframe_guilherme(df)
    fig_guilherme = make_plot_guilherme(df_guilherme)
    fig_guilherme.savefig('graficos/graficoguilherme.png')

    df_gustavo = gerar_dataframes.criar_dataframe_gustavo(df)
    fig_gustavo = make_gustavo_plot(df_gustavo)
    fig_gustavo.savefig('graficos/graficogustavo.png')

    df_joao = gerar_dataframes.criar_dataframe_joao(df)
    fig_joao = make_plot_joao(df_joao)
    fig_joao.savefig('graficos/graficojoao.png')