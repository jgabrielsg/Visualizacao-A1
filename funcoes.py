import pandas as pd
import os

pasta = 'dados'

def collect_data(pasta = pasta):
    arquivos_csv = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith('.csv')]

    dataframes = []

    for csv in arquivos_csv:
        caminho_arquivo = os.path.join(pasta, csv)
        df = pd.read_csv(caminho_arquivo, encoding='latin-1', sep=";")
        dataframes.append(df)

    df = pd.concat(dataframes, ignore_index=True)

    return df

print(collect_data(pasta))

def filtrar_colunas(df,coluna1,coluna2):
    try:
        df_filtrado = df[[coluna1, coluna2]]
    except NameError:
        print("Coluna não encontrada.")
    return df_filtrado