import funcoes
from datacleaning import clean_data
from gustavo import make_gustavo_plot
import pandas as pd

df = funcoes.collect_data()

df = clean_data(df)

make_gustavo_plot(df)