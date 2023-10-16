from funcoes import collect_data
from datacleaning import clean_data
import graficos
import gerar_dataframes

df = collect_data()
df = clean_data(df)

df_vinicius = gerar_dataframes.criar_dataframe_vinicius(df)
fig_vinicius = graficos.make_plot_vinicius(df_vinicius)
fig_vinicius.savefig('graficos/graficovinicius.png')

df_guilherme = gerar_dataframes.criar_dataframe_guilherme(df)
fig_guilherme = graficos.make_plot_guilherme(df_guilherme)
fig_guilherme.savefig('graficos/graficoguilherme.png')

df_gustavo = gerar_dataframes.criar_dataframe_gustavo(df)
fig_gustavo = graficos.make_gustavo_plot(df_gustavo)
fig_gustavo.savefig('graficos/graficogustavo.png')

df_joao = gerar_dataframes.criar_dataframe_joao(df)
fig_joao = graficos.make_plot_joao(df_joao)
fig_joao.savefig('graficos/graficojoao.png')