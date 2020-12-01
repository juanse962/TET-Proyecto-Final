import pandas as pd
import numpy as np

df = pd.read_csv('covid-pre-procesado.csv')
new_df = pd.DataFrame(df)
new_df = new_df.dropna()

new_df.to_csv('covid-limpio.csv',index=False) 