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

colors = ['green' if i > 21 else 'gray' for i in range(len(df_estados))]

def graph_currency(value, pos):
    if value >= 1e6: 
        return f'${value/1e6:.0f}M'  
    else:
        return f'${value:.0f}' 

plt.figure(figsize=(10, 6))
plt.bar(df_estados['Sigla Unidade Federativa'], df_estados['Total Valores Apreendidos'], color=colors)

plt.legend(['Valores Apreendidos'], loc='upper left')

plt.axvspan(21.5, 26.5, color='red', alpha=0.3, label='Valores acima de 500 milhões')

plt.text(15, 1000000000, 'Valores > 500M', fontsize=12, color='black', fontweight='bold')

bars = plt.bar(df_estados['Sigla Unidade Federativa'], df_estados['Total Valores Apreendidos'], color=colors)

total_sum = df_estados['Total Valores Apreendidos'].sum()

for bar in bars:
    height = bar.get_height()
    percentage = (height / total_sum) * 100
    plt.text(bar.get_x() + bar.get_width() / 2, height / 2, f'{percentage:.2f}%', ha='center', va='baseline', rotation=90, fontsize=8, fontweight='bold', color='#010101', linespacing=0.9)


plt.axhline(y=1000000, color='r', linestyle='--', label='Limiar de 1 milhão')
plt.fill_between(df_estados['Sigla Unidade Federativa'], 0, df_estados['Total Valores Apreendidos'], alpha=0.2)
plt.title('Valores Apreendidos por Estado em 2022')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.text(0.02, 0.92, 'Dados de 2022', transform=plt.gcf().transFigure)

plt.xlabel('Estados')
plt.ylabel('Valores Apreendidos')
plt.title('Valores Apreendidos por Estado')

formatter = FuncFormatter(graph_currency)
plt.gca().yaxis.set_major_formatter(formatter)

plt.savefig('graficos/graficojoao.png')
