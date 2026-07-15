import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


tips = sns.load_dataset("tips")
sns.set_style("whitegrid") # aplica globalmente
with sns.axes_style("dark"): # apenas dentro do bloco
 sns.scatterplot(data=tips, x="total_bill", y="tip")
sns.set_context("talk") # tamanho: paper|notebook|talk|poster
sns.despine() # remove bordas superiores/direitas
plt.show()

sns.color_palette("Set2") # retorna a paleta
sns.palplot(sns.color_palette("mako", 8))
sns.set_palette("colorblind") # define globalmente
plt.show()

'''5. Gráficos relacionais
Mostram a relação entre duas variáveis numéricas. As duas funções principais são scatterplot
(pontos) e lineplot (linhas com estatística).
5.1 scatterplot'''
# Adiciona o título
plt.title("Relação entre Total da Conta e Gorjeta")
sns.scatterplot(
data=tips, x="total_bill", y="tip",
hue="time", # cor por categoria
size="size", # tamanho por variável
sizes=(20, 180), # faixa de tamanhos
style="smoker", # forma do marcador
)
plt.tight_layout() #gráfico com informação cortada use essa linha 
plt.show()