import pandas as pd
from funcoes import collect_data, arrumar_tipos

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

    arrumar_tipos(df)

    # df['Qtd Valores Apreendidos'] = df['Qtd Valores Apreendidos'].apply(format_currency)
    # df['Qtd Valores Descapitalizados'] = df['Qtd Valores Descapitalizados'].apply(format_currency)
    # df['Qtd Prejuizos Causados a Uniao'] = df['Qtd Prejuizos Causados a Uniao'].apply(format_currency)

    return df

# old_df = collect_data()
# print(clean_data(old_df))

def format_currency(value):
    if pd.notna(value):
        value = value/1000000
        return "${:,.2f}M".format(value)
    else:
        return 0.0

print(clean_data(collect_data()))