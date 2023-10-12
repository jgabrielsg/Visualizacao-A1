import numpy as np
import pandas as pd
from funcoes import filtrar_colunas, valores_unicos, contar_repeticoes, valores_unicos
import matplotlib.pyplot as plt

def gustavo_plot(df):
    #Agrupa as colunas escolhidas e conta a frequência 
    grouped = df.groupby(['Area', 'Tipo de Operacao']).size()

    #Cria listas como os valores na mesma ordem que eles aparecem na Series
    areas = grouped.index.get_level_values('Area')
    operation_types = grouped.index.get_level_values('Tipo de Operacao')
    counts = grouped.values

    #Cria listas com os valores únicos de Área e Tipo de operação
    unique_areas = sorted(areas.unique())
    unique_operation_types = sorted(operation_types.unique())

    width = 0.8

    fig, ax = plt.subplots()
    bottom = np.zeros(len(unique_areas))

    #Checa se um determinado tipo de operação foi executado em uma dada árae, e se foi, sua contagem é adicionada ào plot
    for operation_type in unique_operation_types:
        operation_counts = []
        for area in unique_areas:
            if (area, operation_type) in grouped.index:
                operation_counts.append(counts[grouped.index == (area, operation_type)][0])
            else:
                operation_counts.append(0)
        
        p = ax.bar(unique_areas, operation_counts, width, label=operation_type, bottom=bottom)
        bottom += operation_counts

    ax.set_title("grafico")
    ax.legend(loc="upper right")

    # plt.show()