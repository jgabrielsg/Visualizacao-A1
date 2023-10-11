import numpy as np
import pandas as pd
from funcoes import collect_data
from datacleaning import clean_data

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df = clean_data(collect_data())

df_estados = df.groupby('Sigla Unidade Federativa')['Qtd Valores Apreendidos'].sum().reset_index()
df_estados = df_estados.rename(columns={'Qtd Valores Apreendidos': 'Total Valores Apreendidos'})
df_estados = df_estados.sort_values(by='Total Valores Apreendidos', ascending=True)

print(df_estados)

def graph_currency(value, pos):
    if value >= 1e6: 
        return f'${value/1e6:.0f}M'  
    else:
        return f'${value:.0f}' 

plt.figure(figsize=(10, 6))
plt.bar(df_estados['Sigla Unidade Federativa'], df_estados['Total Valores Apreendidos'])

plt.xlabel('Estados')
plt.ylabel('Valores Apreendidos')
plt.title('Valores Apreendidos por Estado')

formatter = FuncFormatter(graph_currency)
plt.gca().yaxis.set_major_formatter(formatter)

plt.savefig('graficos/graficojoao.png')
