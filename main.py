import funcoes
from datacleaning import clean_data
from gustavo import gustavo_plot
import pandas as pd

df = funcoes.collect_data()

df = clean_data(df)