import numpy as np
import pandas as pd
from funcoes import collect_data
from datacleaning import clean_data

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, StrMethodFormatter

df = clean_data(collect_data())

df_estados = df.groupby('Sigla Unidade Federativa')['Qtd Valores Apreendidos'].sum().reset_index()
df_estados = df_estados.rename(columns={'Qtd Valores Apreendidos': 'Total Valores Apreendidos'})

print(df_estados)

plt.figure(figsize=(10, 6))
plt.bar(df_estados['Sigla Unidade Federativa'], df_estados['Total Valores Apreendidos'])

money_format = FuncFormatter(lambda x, _: 'R${:,.2f}'.format(x))
plt.gca().yaxis.set_major_formatter(money_format)

plt.xlabel('Estados')
plt.ylabel('Valores Apreendidos')
plt.title('Valores Apreendidos por Estado')

plt.gca().get_yaxis().set_major_formatter(StrMethodFormatter('{x:,.2f}'))

plt.show()