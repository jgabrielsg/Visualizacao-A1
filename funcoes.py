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

    # Arruma os tipos das colunas de data
    colunas_datas = ["Data do Inicio", "Data da Deflagracao"]

    for coluna in colunas_datas:
        df_copia[coluna] = pd.to_datetime(df_copia[coluna], format='%d/%m/%Y')

    # Arruma os tipos das colunas de valores monetários, funciona mas vou tentar melhorar dps
    colunas_dinheiro = ["Qtd Valores Apreendidos", "Qtd Valores Apreendidos i11", "Qtd Valores Descapitalizados", "Qtd Prejuizos Causados a Uniao"]

    for coluna in colunas_dinheiro:
        df_copia[coluna] = df_copia[coluna].fillna(0).astype(str)
        mascara = df_copia[coluna].notnull()
        df_copia.loc[mascara, coluna] = df_copia.loc[mascara, coluna].str.replace('R\$', '').str.replace('.', '').str.replace(',', '.')
        df_copia[coluna] = df_copia[coluna].astype(float).astype(int)

    return df_copia

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

df_teste = arrumar_tipos(collect_data(pasta))
print(df_teste["Qtd Valores Apreendidos"]) 
