import pandas as pd
import os

pasta = 'dados'

def collect_data(pasta = pasta):
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

def arrumar_tipos(df):
    """Funcao que retorna um dataframe com os tipos de dados das colunas adequados.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame inicial com os dados lidos.

    Returns
    -------
    pandas.DataFrame
       DataFrame com os tipos corrigidos
    """

    df_copia = df

    colunas_datas = ["Data do Inicio", "Data da Deflagracao"]
    colunas_dinheiro = ["Qtd Valores Apreendidos", "Qtd Valores Descapitalizados", "Qtd Prejuizos Causados a Uniao"]


    # Arruma os tipos das colunas de data
    for coluna in colunas_datas:
        try:
            df_copia[coluna] = pd.to_datetime(df_copia[coluna], format='%d/%m/%Y')

        except KeyError as erro:
            print("!! ERRO !!\n")
            print("A coluna:", coluna, ", não está presente no dataframe!\n")
            print(type(erro), erro.__class__.mro())

    # Arruma os tipos das colunas de valores monetários
    for coluna in colunas_dinheiro:
        try: 
            mask = df[coluna].notna()
            df.loc[mask, coluna] = df.loc[mask, coluna].str.replace('R$', '', regex=False).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
            df[coluna] = df[coluna].fillna(0).astype(float)
        
        except KeyError as erro:
            print("!! ERRO !!\n")
            print("A coluna:", coluna, ", não está presente no dataframe!\n")
            print(type(erro), erro.__class__.mro())

        except Exception as erro:
            print("!! Erro !!\n")
            print(type(erro), erro.__class__.mro(), end ="\n\n")

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
    
    
    """
    try:
        repeticoes = df.groupby(list(colunas)).size().reset_index(name = "QUANTIDADE")
        df = df.merge(repeticoes, on = list(colunas), how = "left")
        df = df.drop_duplicates(subset = list(colunas), keep = "first")
        df = df.set_index(list(colunas)).sort_values("QUANTIDADE", ascending=True)
        return df
    
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
    """
    try:
        lista_de_valores_unicos = []
        for unico in df[coluna].unique():
            lista_de_valores_unicos.append(unico)
        return lista_de_valores_unicos
    
    except Exception as erro:
        print(f"Ocorreu um erro ao buscar valores únicos:")
        print(type(erro), erro.__class__.mro(), end ="\n\n")
    
def remover_espaços(df, coluna = "Area"):
    """
    Função que remove os espaços extras que existem na coluna "Area" do dataframe, ou outra coluna se especificada.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame que contém a coluna em questão.
    coluna : str
        Coluna que vai ter seus espaços extrar removidos.

    Returns
    -------
    pandas.DataFrame
        O data frame com a coluna especificada sem os espaços extras.
    """
    df_copia = df

    try:
        df_copia[coluna] = df_copia[coluna].str.rstrip()

    except KeyError as erro:
        print("!! ERRO !!\n")
        print("A coluna:", coluna, ", não está presente no dataframe!\n")
    
    except Exception as error:
        print("!! ERRO !!\n")
        print("Não deu pra remover os espaços da coluna: ", coluna)
    
    return df_copia

def arrumar_escrita(df, coluna = "Area"):
    """
    Função que arruma bugs do dataframe em específico, em que, somente em algumas linhas caractéres como "á" estão bugados.
    Exemplo: "Fraudes Bancï¿½rias" ao invés de "Fraudes Bancárias"

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame com a coluna "Area" não corrigida
    coluna : str
        Coluna que vai ser corrigida, normalmente a coluna "Area".

    Returns
    -------
    pandas.DataFrame
        O data frame com a coluna especificada arrumada.
    """
    df_copia = df

    nome_correto = {"Crimes de ï¿½dio e Pornografia Infantil": "Crimes de Ódio e Pornografia Infantil",
                    "Fraudes Bancï¿½rias": "Fraudes Bancárias",
                    "Trï¿½fico de Drogas": "Tráfico de Drogas",
                    "Crimes Fazendï¿½rios": "Crimes Fazendários",
                    "Crimes Contra o Patrimï¿½nio": "Crimes Contra o Patrimônio",
                    "Crimes de Corrupï¿½ï¿½o": "Crimes de Corrupção",
                    "Crimes Previdenciï¿½rios": "Crimes Previdenciários",
                    "Trï¿½fico de Armas": "Tráfico de Armas",
                    "Crimes Ambientais e Contra o Patrimï¿½nio Cultural": "Crimes Ambientais e Contra o Patrimônio Cultural"}

    try:
        df_copia[coluna] = df_copia[coluna].replace(nome_correto)
    
    except Exception:
        print("!! ERRO !!\n")
        print("Não deu para arrumar os nomes da coluna 'Area': ", coluna)

    return df_copia