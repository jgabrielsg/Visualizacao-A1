"""Módulo que contém as funções que criam os dataframes que cada aluno usa na criação dos gráficos."""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from funcoes import collect_data, filtrar_colunas, contar_repeticoes
from datacleaning import clean_data
from matplotlib.ticker import FuncFormatter

def criar_dataframe_guilherme(df):
    """Gera um dataframe para analise e visualização.   

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame original limpo após ser retirado do site do governo federal e tratado.

    Returns
    -------
    pandas.DataFrame
        Tabela dinâmica baseada na média das quantidades apreendidas 
        em território indigena e não indigena para um estado
    """
    try:
        #Previne que o df original seja modificado.
        df_copia = df.copy()
        df_copia = filtrar_colunas(df_copia, 'Atuacao em Territorio Indigena','Qtd Valores Apreendidos','Sigla Unidade Federativa')

        #Remove os estados sem atuação em território indigena.
        estados_ap_ind = df_copia[df_copia['Atuacao em Territorio Indigena'] == 'Sim'].groupby('Sigla Unidade Federativa').size().index
        df_ap_ind = df_copia[df_copia['Sigla Unidade Federativa'].isin(estados_ap_ind)]

        df_agrupado = df_ap_ind.groupby(['Atuacao em Territorio Indigena','Sigla Unidade Federativa'])['Qtd Valores Apreendidos'].mean().reset_index(name="Média")
        df_pivot = df_agrupado.pivot_table(values='Média',  columns=['Atuacao em Territorio Indigena'], index = 'Sigla Unidade Federativa', fill_value=0)
    except Exception as erro:
        print("Erro! DataFrame não é valido para o DataFrame final desejado com a função criar_dataframe_guilherme!")
        print(type(erro), erro.__class__.mro(), end ="\n\n")
        df_pivot = {}
    return df_pivot

def criar_dataframe_gustavo(df):
    try:
        # Cria uma cópia das colunas necessáras do dataframe
        df_copia_gustavo = df.copy()
        df_copia_gustavo = filtrar_colunas(df, "Data da Deflagracao", "Area")

        #Deixando mais curtos os títulos para que a legenda seja mais legível
        df_copia_gustavo.loc[df_copia_gustavo["Area"] == "Crimes Ambientais e Contra o Patrimônio Cultural", "Area"] = "Crimes Ambientais"
        df_copia_gustavo.loc[df_copia_gustavo["Area"] == "Crimes de Ódio e Pornografia Infantil", "Area"] = "Crimes de Ódio e Porn. Infantil"
        
        #Evita que um aviso do pandas apareca criando um novo df
        df_copia_gustavo = df_copia_gustavo.copy()
        df_copia_gustavo["Data de Deflagracao"] = df_copia_gustavo['Data da Deflagracao'].dt.strftime('%m/%Y')

        # Usado para saber as áreas de atuação das operações mais frequêntes
        contagem_area = df_copia_gustavo["Area"].value_counts().index

        # Agrupa por mês e área de atuação as operações
        grouped = df_copia_gustavo.groupby(['Area', 'Data de Deflagracao']).size().unstack(fill_value=0)

        grouped = grouped.loc[contagem_area[:10]]
    except Exception as erro:
        print("Erro! DataFrame não é valido para o DataFrame final desejado com a função criar_dataframe_gustavo!")
        print(type(erro), erro.__class__.mro(), end ="\n\n")
        grouped = {}
    return grouped

def criar_dataframe_joao(df):
    try:
        df_copia_joao = df.copy()
        df_estados_joao = df_copia_joao.groupby('Sigla Unidade Federativa')['Qtd Valores Apreendidos'].sum().reset_index()
        df_estados_joao = df_estados_joao.rename(columns={'Qtd Valores Apreendidos': 'Total Valores Apreendidos'})
        df_estados_joao = df_estados_joao.sort_values(by='Total Valores Apreendidos', ascending=True)
    except Exception as erro:
        print("Erro! DataFrame não é valido para o DataFrame final desejado com a função criar_dataframe_joao!")
        print(type(erro), erro.__class__.mro(), end ="\n\n")
        df_estados_joao = {}
    return df_estados_joao

def criar_dataframe_vinicius(df):
    try:
        df_copia_vinicius = df.copy()
        df_estados_vinicius = filtrar_colunas(df_copia_vinicius, "Sigla Unidade Federativa")
        df_estados_vinicius = contar_repeticoes(df_estados_vinicius, "Sigla Unidade Federativa")
        df_estados_vinicius = df_estados_vinicius.rename_axis(index = "ESTADOS")
    except Exception as erro:
        print("Erro! DataFrame não é valido para o DataFrame final desejado com a função criar_dataframe_vinicius!")
        print(type(erro), erro.__class__.mro(), end ="\n\n")
        df_estados_vinicius = {}
    return df_estados_vinicius

if __name__ == "__main__":
    df = clean_data(collect_data())
    criar_dataframe_guilherme(df)
    criar_dataframe_gustavo(df)
    criar_dataframe_joao(df)
    criar_dataframe_vinicius(df)