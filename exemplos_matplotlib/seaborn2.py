import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
tips = sns.load_dataset("tips") # gorjetas em restaurante
print(sns.get_dataset_names()) # lista completa
print(tips.head())

'''5.2 lineplot
O lineplot agrupa por x e calcula automaticamente média e intervalo de confiança (ou desvio padrão)
do y. Ótimo para séries temporais.'''
# Adiciona o título
plt.title("Relação entre Ano e Passageiros")
flights = sns.load_dataset("flights") # passageiros por mês/ano
sns.lineplot(data=flights, x="year", y="passengers", errorbar="sd")
# errorbar: 'ci', 'sd', 'se', ('pi', 95), None
plt.show()


# 6. Gráficos de distribuição
# Servem para entender como os dados estão distribuídos: forma, dispersão, caudas, assimetria,
# presença de multimodalidade.
# 6.1 histplot

penguins = sns.load_dataset("penguins") # pinguins de Palmer
sns.histplot(
data=penguins, x="flipper_length_mm",
hue="species", kde=True,
element="step", # step | bars | poly
stat="count", # count | frequency | density | probability
bins=25,
)
plt.show()

# 6.2 kdeplot
# O kdeplot estima a densidade de probabilidade por kernel. Aceita 1 ou 2 variáveis (nesse caso vira um
# mapa de contorno).
sns.kdeplot(data=penguins, x="bill_length_mm", y="bill_depth_mm",
hue="species", fill=True, alpha=0.5, thresh=0.05)
plt.show()