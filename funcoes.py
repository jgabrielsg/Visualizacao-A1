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
    """Funcao que retorna um dataframe com os tipos de dados das colunas adequados.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame inicial com os dados lidos.

    Returns
    -------
    pandas.DataFrame
       DataFrame com
    """

    df_copia = df

    colunas_datas = ["Data do Inicio", "Data da Deflagracao"]

    for coluna in colunas_datas:
        df_copia[coluna] = pd.to_datetime(df_copia[coluna], format='%d/%m/%Y')

    return df_copia

def filtrar_colunas(df, *colunas):
    """Recebe um DataFrame Pandas e retorna um novo com as colunas desejadas.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame do qual se quer filtrar as colunas.
    *colunas : str
        Nomes das colunas a compor o DataFrame filtrado.

    Returns
    -------
    pandas.DataFrame
       DataFrame contendo apenas as colunas recebidas.
    """
    try:
        df_filtrado = df[list(colunas)]
        return df_filtrado
    except KeyError as erro:
        print(f"Coluna não encontrada: {erro}")
    
    

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
        if df_estado.empty:
            raise ValueError
        return df_estado
    except ValueError as erro:
        print(f"Nenhum dado encontrado para a sigla escolhida: {erro}")

# df = collect_data()
# df_teste = filtrar_colunas(df,"Data da Deflagracao",'Data do Inicia')
