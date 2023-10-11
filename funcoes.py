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
    """Recebe um DataFrame pandas e retorna um novo com apenas duas colunas desejadas.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame do qual se quer filtrar as colunas.
    coluna1 : str
        Nome da primeira coluna a compor o DataFrame filtrado.
    coluna2 : str
        Nome da segunda coluna a compor o DataFrame filtrado.

    Returns
    -------
    pandas.DataFrame
       DataFrame contendo apenas as duas colunas recebidas.
    """
    try:
        df_filtrado = df[[coluna1, coluna2]]
    except NameError:
        print("Coluna não encontrada.")
    return df_filtrado

def filtrar_estado(df,UF):
    """Recebe um DataFrame pandas e retorna um novo com os dados para um estado específico.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame do qual se quer filtrar as colunas.
    UF : str
        Sigla do estado do qual se deseja isolar os dados.

    Returns
    -------
    pandas.DataFrame
        DataFrame composto apenas pelo estado escolhido.
    """
    try:
        df_estado = df[df['Sigla Unidade Federativa'] == UF]
    except NameError:
        print("Estado não encontrado.")
    return df_estado

df = collect_data()
print(type(df))