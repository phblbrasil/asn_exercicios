# %%

# Questão 7
# Um grupo de 20 adolescentes fez a dieta dos pontos por um período de 1 mês. 
# Verifique se houve redução de peso depois da dieta. Arquivo Dieta.xlsx. 
# Considere nível de significância de 5%.

# %%
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# %%
adolescentes = pd.read_excel('dados/Dieta.xlsx')
adolescentes.head(5)
# %%
# primeiro passo é ver se a base segue uma distribuição normal
# como temos uma base pequenna, usaremos o Teste de Shapiro Wilk (4 <= n <= 2000)

# Teste de Shapiro-Wilk
statistic, p_value_shapiro = stats.shapiro(adolescentes['Antes'])
print("Teste de Shapiro-Wilk:")
print("Estatística de teste:", statistic)
print("Valor p:", p_value_shapiro)

# vamos protar o gráfico para o antes
# Plotando o gráfico de dispersão - Antes do tratamento
sns.kdeplot(data=adolescentes,x='Antes')
plt.title('Ditribuição Antes da Dieta')
plt.show()

# %%
# base depois

# Teste de Shapiro-Wilk
statistic, p_value_shapiro = stats.shapiro(adolescentes['Depois'])
print("Teste de Shapiro-Wilk:")
print("Estatística de teste:", statistic)
print("Valor p:", p_value_shapiro)

# vamos protar o gráfico para o antes
# Plotando o gráfico de dispersão - Antes do tratamento
sns.kdeplot(data=adolescentes,x='Depois')
plt.title('Ditribuição Depois da Dieta')
plt.show()

# %%
# Segundo os testes acima, os dados não seguem uma distruição normal. 
# Desta forma, partiremos para utilizar um teste não paramétrico. 
# Usaremos o teste McNemar:

# %%
# Determinando se houve mudança
mudanca = [adolescentes['Antes'][i] != adolescentes['Depois'][i] for i in range(len(adolescentes['Antes']))]
print(mudanca)

# %%
# Criando o data frame com a mudança
df_mudanca = pd.DataFrame({"Antes": adolescentes['Antes'], "Depois": adolescentes['Depois'], "Mudança": mudanca})

# %%
# Criando a tabela de contingência
tabela_contingencia = pd.crosstab(df_mudanca["Mudança"], df_mudanca["Mudança"])

# %%
# Teste de McNemar
chi2_statistic, p_value, _, _ = stats.chi2_contingency(tabela_contingencia)
print("Teste de McNemar:")
print("Estatística Qui-quadrado:", chi2_statistic)
print("Valor p:", p_value)

