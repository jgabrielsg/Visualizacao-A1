import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from funcoes import collect_data, arrumar_tipos, filtrar_colunas, contar_repeticoes
from datacleaning import clean_data


df = clean_data(collect_data())
df_copia = filtrar_colunas(df, 'Atuacao em Territorio Indigena','Qtd Valores Apreendidos','Sigla Unidade Federativa').copy()

# df_area_ind = df[df['Atuacao em Territorio Indigena'] == "Sim"]
# df_area_Nind = df[df['Atuacao em Territorio Indigena'] == "Nao"]
# media_ind = df_area_ind['Qtd Valores Apreendidos'].mean()
# media_Nind = df_area_Nind['Qtd Valores Apreendidos'].mean()

gr = df_copia.groupby(['Atuacao em Territorio Indigena','Sigla Unidade Federativa'])['Qtd Valores Apreendidos'].mean().reset_index(name="Média")

piv = gr.pivot_table(values='Média',  columns=['Atuacao em Territorio Indigena'],  
                        index = 'Sigla Unidade Federativa', fill_value=0)

piv.plot(kind="bar")

plt.show()
    


# guilherme_plot(df)