import funcoes
from datacleaning import clean_data
from gustavo import gustavo_plot

df = funcoes.collect_data()

df = clean_data(df)

gustavo_plot(df)