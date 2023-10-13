import numpy as np
import pandas as pd
from funcoes import filtrar_colunas
from funcoes import collect_data
from datacleaning import clean_data
import matplotlib.pyplot as plt

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
    df_copia = filtrar_colunas(df, "Data da Deflagracao", "Area")

    #Deixando mais curtos os títulos para que a legenda seja mais legível
    df_copia["Area"] = df_copia["Area"].replace({"Crimes Ambientais e Contra o Patrimônio Cultural": "Crimes Ambientais",
                                                 "Crimes de Ódio e Pornografia Infantil": "Crimes de Ódio e Porn. Infantil"})
    
    df_copia["Mes"] = pd.to_datetime(df_copia['Data da Deflagracao']).dt.strftime('%m/%Y')
    #TODO remover a mensagem de aviso q isso aqui tá dando

    # Usado para saber as áreas de atuação das operações mais frequêntes
    contagem_area = df_copia["Area"].value_counts().index

    # Agrupa por mês e área de atuação as operações
    grouped = df_copia.groupby(['Area', 'Mes']).size().unstack(fill_value=0)

    # print(grouped)

    grouped = grouped.loc[contagem_area[:10]]
    # grouped.set_index('Mes', inplace=True)

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

if __name__ == "__main__":
    fig = make_gustavo_plot(clean_data(collect_data()))
    fig.savefig('graficos/graficogustavo.png')