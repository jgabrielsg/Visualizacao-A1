import pandas as pd

pd.set_option('display.max_columns', None)

def clean_data(df):
    """Recebe o dataframe e limpa ele, corrigindo tipos e colunas e linhas

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe ainda "sujo"

    Returns
    -------
    pandas.DataFrame
        Dataframe com as correções
    """

    try:
        df.drop(columns=["Monit Eletronica"], inplace=True)
        df.drop(columns=["Recol Domic Noturno"], inplace=True)
        df.drop(columns=["Qtd Internacao Prov"], inplace=True)
        df.drop(columns=["Comparecimento Juizo"], inplace=True)
        df.drop(columns=["Qtd Valores Apreendidos i11"], inplace=True)
        df.drop(columns=["Proib Ausentar Comarca"], inplace=True)
        df.drop(columns=["Proib Acesso ou Freq"], inplace=True)
        df.drop(columns=["Proib Contato"], inplace=True)
    
    except Exception as error:
        print("!! Erro !!\n")
        print("Erro limpar o dataframe!\n")
        print(error)

    # Remove linhas vazias
    df.dropna(axis=0, how='all', inplace=True)
    # Remove colunas vazias 
    df.dropna(axis=1, how='all', inplace=True)

    df = arrumar_tipos(df)
    df["Area"] = df["Area"].str.rstrip()
    df = arrumar_escrita(df)

    return df

def format_currency(value):
    if pd.notna(value):
        value = value/1000000
        return "${:,.2f}M".format(value)
    else:
        return 0.0
    
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

    colunas_datas = ["Data do Inicio", "Data da Deflagracao"]
    colunas_dinheiro = ["Qtd Valores Apreendidos", "Qtd Valores Descapitalizados", "Qtd Prejuizos Causados a Uniao"]

    # Arruma os tipos das colunas de data
    for coluna in colunas_datas:
        try:
            df[coluna] = pd.to_datetime(df[coluna], format='%d/%m/%Y')
        except KeyError as erro:
            print("A coluna:", coluna, ", não está presente no dataframe!")
        except Exception as erro:
            print("Não foi possível converter a coluna", coluna, "em data!")

    # Arruma os tipos das colunas de valores monetários
    for coluna in colunas_dinheiro:
        try: 
            mask = df[coluna].notna()
            df.loc[mask, coluna] = df.loc[mask, coluna].str.replace('R$', '', regex=False).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
            df[coluna] = df[coluna].fillna(0).astype(float)
        except KeyError as erro:
            print("A coluna:", coluna, ", não está presente no dataframe!")
        except Exception as erro:
            print("Não foi possível converter a coluna", coluna, "em float!")

    return df

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
        df[coluna] = df[coluna].replace(nome_correto)
    except Exception:
        print("Não deu para arrumar os nomes da coluna 'Area': ", coluna)

    return df