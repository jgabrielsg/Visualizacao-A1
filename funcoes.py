"""Módulo que contém as funções com utilidade generalizada."""

import pandas as pd
import os

def collect_data(pasta = 'dados'):
    """Coleta os dados do CSV e une eles em apenas um dataframe

    Parameters
    ----------
    pasta : _type_, optional
        A pasta que contém os CSVs, by default pasta

    Returns
    -------
    pandas.Dataframe
        O dataframe com os dados dos CSVs

    Example
    -------
    >>> df = collect_data('dados')
    >>> df.shape[1]
    27
    >>> df.shape[0]
    10268
    """
    arquivos_csv = [arquivo for arquivo in os.listdir(pasta) if arquivo.endswith('.csv')]

    dataframes = []

    for csv in arquivos_csv:
        caminho_arquivo = os.path.join(pasta, csv)
        df = pd.read_csv(caminho_arquivo, encoding='latin1', sep=";")
        dataframes.append(df)

    df = pd.concat(dataframes, ignore_index=True)

    return df

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

       
    Example
    -------
    >>> df_filtrado = filtrar_colunas(collect_data(), "Atuacao em Territorio de Fronteira")
    >>> df_filtrado.shape[1]
    1
    """
    try:
        df_filtrado = df[list(colunas)]
        return df_filtrado
    
    except KeyError as erro:
        print("Coluna não encontrada.")
        print(type(erro), erro.__class__.mro(), end ="\n\n")
    except Exception as erro:
        print("Erro ao rodar a função.")
        print(type(erro), erro.__class__.mro(), end ="\n\n")
    
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

    Example
    -------
    >>> df_filtrado = filtrar_estado(collect_data(), "RS")
    >>> df_filtrado.shape[1]
    809
    """
    try:
        if type(UF) != str:
            raise KeyError
        
        df_estado = df[df['Sigla Unidade Federativa'] == UF]

        if df_estado.empty:
            raise Exception
        
        return df_estado
    
    except KeyError as erro:
        print("\nDados inseridos não seguem o formato desejado.")
        print(type(erro), erro.__class__.mro(), end ="\n\n")
    except Exception as erro:
        print("Nenhum dado encontrado para a sigla escolhida.")
        print(type(erro), erro.__class__.mro(), end ="\n\n")

def contar_repeticoes(df, *colunas):
    """
    Conta o número de repetições da(s) coluna(s) especificada(s) de um DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame que contém os dados a serem contados.
    *colunas : str
        Uma ou mais colunas que vão ter as repetições contadas.

    Returns
    -------
    pandas.DataFrame
        DataFrame original com uma coluna adicional "QUANTIDADE" indicando o número de repetições.
    
    Example
    -------
    >>> df_repeticoes = contar_repeticoes(collect_data(), "Sigla Unidade Federativa")
    >>> df_repeticoes.shape[0]
    27
    >>> df_repeticoes.shape[1]
    1
    """
    try:
        df_copia = df.copy()
        repeticoes = df_copia.groupby(list(colunas)).size().reset_index(name = "QUANTIDADE")
        df_copia = df_copia.merge(repeticoes, on = list(colunas), how = "left")
        df_copia = df_copia.drop_duplicates(subset = list(colunas), keep = "first")
        df_copia = df_copia[list(colunas) + ["QUANTIDADE"]]
        df_copia = df_copia.set_index(list(colunas)).sort_values("QUANTIDADE", ascending=True)
        return df_copia
    
    except KeyError as erro:
        print("\nDados inseridos não seguem o formato desejado.")
        print(type(erro), erro.__class__.mro(), end ="\n\n")

    except Exception as erro:
        print("Alguns dos dados passados não foram encontrados.")
        print(type(erro), erro.__class__.mro(), end ="\n\n")

def valores_unicos(df, coluna):
    """
    Retorna uma lista de valores únicos de uma coluna específica de um DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame que contém os dados a serem analisados.
    coluna : str
        Coluna que vai ter seus valores únicos analisados.

    Returns
    -------
    list
        Uma lista contendo os valores únicos da coluna especificada.

    Example
    -------
    >>> valores_unicos(collect_data(), "Sigla Unidade Federativa")
    ['RR', 'MG', 'PI', 'RS', 'PR', 'MS', 'RJ', 'AC', 'AM', 'CE', 'GO', 'SP', 'RO', 'PE', 'BA', 'MT', 'ES', 'PA', 'SE', 'AL', 'SC', 'PB', 'DF', 'RN', 'TO', 'MA', 'AP']
    """
    try:
        lista_de_valores_unicos = []
        for unico in df[coluna].unique():
            lista_de_valores_unicos.append(unico)
        return lista_de_valores_unicos
    
    except Exception as erro:
        print(f"Ocorreu um erro ao buscar valores únicos:")
        print(type(erro), erro.__class__.mro(), end ="\n\n")