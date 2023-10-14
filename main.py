from funcoes import collect_data
from datacleaning import clean_data
import graficos

df = collect_data()
df = clean_data(df)

fig_vinicius = graficos.make_plot_vinicius(df)
fig_vinicius.savefig('graficos/graficovinicius.png')
fig_guilherme = graficos.make_plot_guilherme(df)
fig_guilherme.savefig('graficos/graficoguilherme.png')
fig_gustavo = graficos.make_gustavo_plot(df)
fig_gustavo.savefig('graficos/graficogustavo.png')
fig_joao = graficos.make_plot_joao(df)
fig_joao.savefig('graficos/graficojoao.png')