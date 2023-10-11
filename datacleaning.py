import pandas as pd
from funcoes import collect_data

pd.set_option('display.max_columns', None)

def clean_data(df):
    df.drop(columns=["Monit Eletronica"], inplace=True)
    df.drop(columns=["Recol Domic Noturno"], inplace=True)
    df.drop(columns=["Qtd Internacao Prov"], inplace=True)
    df.drop(columns=["Comparecimento Juizo"], inplace=True)
    df.drop(columns=["Qtd Valores Apreendidos i11"], inplace=True)
    df.drop(columns=["Proib Ausentar Comarca"], inplace=True)
    df.drop(columns=["Proib Acesso ou Freq"], inplace=True)
    df.drop(columns=["Proib Contato"], inplace=True)

    # Remove linhas vazias
    df.dropna(axis=0, how='all', inplace=True)
    # Remove colunas vazias 
    df.dropna(axis=1, how='all', inplace=True)

    df['Qtd Valores Apreendidos'] = df['Qtd Valores Apreendidos'].str.replace('R\$', '').str.replace('.', '').str.replace(',', '.').astype(float)

    return df

old_df = collect_data()

print(clean_data(old_df))