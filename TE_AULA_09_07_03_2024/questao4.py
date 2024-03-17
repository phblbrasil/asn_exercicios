# %%
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

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
# Vamos começar validando se eles seguem uma distribuição normal, para tal faremos o teste KS 
df_col_antes_tratamento = df_colesterol[['ID','Antes_tratamento']]

# Plotando o gráfico de dispersão - Antes do tratamento
sns.kdeplot(data=df_col_antes_tratamento,x='Antes_tratamento')
plt.title('Ditribuição Antes do Tratamento')
plt.show()
# %%
df_col_depois_tratamento = df_colesterol[['ID','Depois_tratamento']]

# Plotando o gráfico de dispersão - Antes do tratamento
sns.kdeplot(data=df_col_depois_tratamento,x='Depois_tratamento')
plt.title('Ditribuição Antes do Tratamento')
plt.show()

# %%
# Teste de Levene para igualdade de variâncias
levene_statistic, p_value_levene = stats.levene(df_col_antes_tratamento['Antes_tratamento'], 
                                                df_col_depois_tratamento['Depois_tratamento'])
print("Teste de Levene:")
print("Estatística de Levene:", levene_statistic)
print("Valor p:", p_value_levene)

# %%
# Teste t de Student emparelhado
t_statistic, p_value = stats.ttest_rel(df_col_antes_tratamento['Antes_tratamento'], 
                                       df_col_depois_tratamento['Depois_tratamento'])
print("Teste t de Student emparelhado:")
print("Estatística t:", t_statistic)
print("Valor p:", p_value)

# %%
# Para fazer um comparativo vamos ver também o teste não paramétrico
# Teste de Wilcoxon
w_statistic, p_value_wilcoxon = stats.wilcoxon(df_col_antes_tratamento['Antes_tratamento'],
                                               df_col_depois_tratamento['Depois_tratamento'])
print("Teste de Wilcoxon:")
print("Estatística W:", w_statistic)
print("Valor p:", p_value_wilcoxon)