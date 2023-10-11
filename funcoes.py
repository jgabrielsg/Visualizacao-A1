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

def arrumar_tipos(df):
    # função que vai arrumar os dtypes das colunas

    df_copia = df

    colunas_datas = ["Data do Inicio", "Data da Deflagracao"]

    for coluna in colunas_datas:
        df_copia[coluna] = pd.to_datetime(df_copia[coluna], format='%d/%m/%Y')

    return df_copia

df = arrumar_tipos(collect_data(pasta))

print(df["Data do Inicio"])
print(df["Data do Inicio"].dtype)


def filtrar_colunas(df,coluna1,coluna2):
    try:
        df_filtrado = df[[coluna1, coluna2]]
    except NameError:
        print("Coluna não encontrada.")
    return df_filtrado

def filtrar_estado(df,UF):
    try:
        df_estado = df[df['Sigla Unidade Federativa'] == UF]
    except NameError:
        print("Estado não encontrado.")
    return df_estado

# df = collect_data()
# print(filtrar_estado(df,"PR")['Sigla Unidade Federativa'])