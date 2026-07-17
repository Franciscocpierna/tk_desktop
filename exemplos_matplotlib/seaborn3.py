import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

''' 
 3. Datasets integrados
O Seaborn traz vários datasets prontos para prática, baixados sob demanda:
tips = sns.load_dataset("tips") # gorjetas em restaurante
iris = sns.load_dataset("iris") # medidas de pétalas
penguins = sns.load_dataset("penguins") # pinguins de Palmer
flights = sns.load_dataset("flights") # passageiros por mês/ano
titanic = sns.load_dataset("titanic") # passageiros do Titanic
print(sns.get_dataset_names()) # lista completa
print(tips.head())
Os exemplos desta apostila usam tips, penguins, iris e flights.
'''

# 6.3 Outros de distribuição
# tips = sns.load_dataset("tips") # gorjetas em restaurante
# penguins = sns.load_dataset("penguins") # pinguins de Palmer
# sns.ecdfplot(data=penguins, x="body_mass_g", hue="species") # ECDF
# sns.rugplot(data=tips, x="total_bill") # "tapete" de marcas
# sns.displot(data=tips, x="total_bill", kind="hist") # figure-level
# plt.show()



# 7. Gráficos categóricos
# Quando o eixo x (ou y) é uma variável categórica. Cada função enfatiza um aspecto:
# • boxplot / violinplot: distribuição resumida.
# • barplot: valor agregado (média por padrão).
# • countplot: contagem de ocorrências.
# • stripplot / swarmplot: pontos individuais.
# • pointplot: média com intervalo de confiança.
# 7.1 boxplot e violinplot
tips = sns.load_dataset("tips") # gorjetas em restaurante
sns.boxplot(data=tips, x="day", y="total_bill", hue="smoker")
sns.violinplot(data=tips, x="day", y="total_bill",
hue="sex", split=True, inner="quart")
plt.show()