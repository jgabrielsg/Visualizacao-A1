import funcoes
import datacleaning
from gustavo import make_gustavo_plot
from vinicius import make_vinicius_plot

df = funcoes.collect_data()

df = datacleaning.clean_data(df)
# print(df)

make_gustavo_plot(df)
make_vinicius_plot()