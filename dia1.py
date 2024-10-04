import pandas as pd
from matplotlib import pyplot as plt
import os

df_ipea = pd.read_csv('dataset/ipeadata[04-10-2024-03-44].csv', skiprows=1)

df = df_ipea[['Município', '2022']]
df.columns = ['MUNICIPIO','2022']
df = df.dropna()

df2022_ordenado = df.sort_values(by='2022', ascending=False).reset_index(drop=True)

ranks = df2022_ordenado.index + 1
values = df2022_ordenado['2022']
zipf_values = values.max() / ranks

fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
# ax.plot(ranks, values, marker = 'x')
ax.scatter(ranks, values, marker = 'x', color = 'red')
ax.plot(ranks, zipf_values)
ax.set_xscale('log')
ax.set_yscale('log')
ax.label()

os.makedirs('results')
fig.savefig('results/fig1.png')