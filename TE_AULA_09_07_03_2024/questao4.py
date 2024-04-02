# %%
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# %%
# Questão 3

# Trinta adolescentes com nível de colesterol total acima do permitido foram 
# submetidos a um tratamento que consistia em dieta e atividade física. A planilha 
# Colesterol.xlsx apresenta os índices de colesterol LDL (mg/dL) antes e depois 
# do tratamento. Verifique se o tratamento é eficaz (com nível de significância de 5%).

# Teste T para duas amostras Emparelhada

# Se não paramétricos = teste Wilcoxon

# lendo a base
df_colesterol = pd.read_excel('dados/Colesterol.xlsx')
df_colesterol.head(5)
# %%
# Plotando o gráfico de distribuição - Antes do tratamento
sns.kdeplot(data=df_colesterol,x=df_colesterol['Antes_tratamento'])
plt.title('Ditribuição Antes do Tratamento')
plt.show()

# %%
# Teste de Shapiro-Wilk
p_value_shapiro = stats.shapiro(df_colesterol['Antes_tratamento'])
print("Teste de Shapiro-Wilk:")
print("Valor p:", p_value_shapiro)

# %%
# Teste de Shapiro-Wilk - Depois tratamento
p_value_shapiro = stats.shapiro(df_colesterol['Depois_tratamento'])
print("Teste de Shapiro-Wilk:")
print("Valor p:", p_value_shapiro)
# %%
# Plotando o gráfico de distribuição - Depois do tratamento
sns.kdeplot(data=df_colesterol,x=df_colesterol['Depois_tratamento'])
plt.title('Ditribuição Depois do Tratamento')
plt.show()
# %%
# Teste de Levene para igualdade de variâncias
levene_statistic, p_value_levene = stats.levene(df_colesterol['Antes_tratamento'], 
                                                df_colesterol['Depois_tratamento'])
print("Teste de Levene:")
print("Estatística de Levene:", levene_statistic)
print("Valor p:", p_value_levene)

# %%
# Teste t de Student emparelhado
t_statistic, p_value = stats.ttest_rel(df_colesterol['Antes_tratamento'], 
                                       df_colesterol['Depois_tratamento'])
print("Teste t de Student emparelhado:")
print("Estatística t:", t_statistic)
print("Valor p:", p_value)

# %%
# Vamos testar agora se o valor é maior ou menor que a média antes do tratamento:
referencia = df_colesterol['Antes_tratamento'].mean()
# %%
# Realizando o teste t de Student para uma amostra (unicaudal)
t_statistic, p_value = stats.ttest_1samp(df_colesterol['Depois_tratamento'], 
                                         referencia, 
                                         alternative='less')

print("Teste t de Student para uma amostra (unicaudal - menor):")
print("Estatística t:", t_statistic)
print("Valor p:", p_value)

# %%

# Verificando se o valor p é menor que o nível de significância (por exemplo, 0.05)
if p_value < 0.05:
    print("O colesterol após o tratamento é significativamente menor do que o valor de referência (220).")
else:
    print("""Não há evidências suficientes para concluir que o colesterol após o tratamento é 
          significativamente menor do que o valor de referência (220).""")

# %%
# Para fazer um comparativo vamos ver também o teste não paramétrico
# Teste de Wilcoxon
w_statistic, p_value_wilcoxon = stats.wilcoxon(df_colesterol['Antes_tratamento'],
                                               df_colesterol['Depois_tratamento'])
print("Teste de Wilcoxon:")
print("Estatística W:", w_statistic)
print("Valor p:", p_value_wilcoxon)
