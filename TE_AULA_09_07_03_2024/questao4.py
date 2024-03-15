# %%
import pandas as pd
from scipy.stats import kstest, norm, levene, ttest_ind
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# Questão 3

# Deseja-se comparar o tempo médio de espera para atendimento (min) em 2 hospitais. 
# Para isso, coletou-se uma amostra com 20 pacientes em cada hospital. Os dados estão 
# disponíveis no arquivo Hospitais.xlsx. Verifique se há diferença entre os tempos 
# médios de espera nos dois hospitais. Considere um nível de significância de 1%.

# lendo a base
df_colesterol = pd.read_excel('dados/Colesterol.xlsx')
df_colesterol.head(5)
# %%
# Obter os nomes únicos dos hospitais
hospitais = df_hospitais['Hospital'].unique()

# Dicionário para armazenar os resultados
resultados_ks = {}

# Loop para realizar o teste em cada hospital
for hospital in hospitais:
    # Filtrar dados por hospital
    dados = df_hospitais[df_hospitais['Hospital'] == hospital]['Tempo_Atendimento']
    
    # Calcular a média e o desvio padrão
    media, desvio_padrao = norm.fit(dados)
    
    # Realizar o teste de Kolmogorov-Smirnov
    estatistica, p_valor = kstest(dados, 'norm', args=(media, desvio_padrao))
    
    # Armazenar os resultados
    resultados_ks[hospital] = {'estatistica': estatistica, 'p_valor': p_valor}

resultados_ks

# %%
# Vamos plotar os histogramas para saber se temos o mesmo sentimento de atender uma normal
hospital_1 = df_hospitais[df_hospitais['Hospital'] == 'Hospital_1']
sns.kdeplot(data=hospital_1,x='Tempo_Atendimento')
plt.title('Tempo de Atendimento do Hospital 1')
plt.show()

# %%
# Vamos plotar os histogramas para saber se temos o mesmo sentimento de atender uma normal
hospital_2 = df_hospitais[df_hospitais['Hospital'] == 'Hospital_2']
sns.kdeplot(data=hospital_2,x='Tempo_Atendimento')
plt.title('Tempo de Atendimento do Hospital 2')
plt.show()


# %%
# Agora vamos partir para a análise das variancias das amostras
# vamos isolar os tempos de atendimento de cada hospital
tempo_atendimento_h1 = hospital_1['Tempo_Atendimento']
tempo_atendimento_h2 = hospital_2['Tempo_Atendimento']

# Após, vamos realizar o teste F de Levene para comparar as variâncias
estatistica_levene, p_valor_levene = levene(tempo_atendimento_h1, 
                                            tempo_atendimento_h2, 
                                            center='mean')

estatistica_levene, p_valor_levene

# %%
# Vamos plotar o boxplot para uma leitura visual dos dados também
sns.boxplot(df_hospitais,x='Hospital',y='Tempo_Atendimento')
plt.title('Tempo de Atendimento  nos Hospitais')
plt.show()


# %%
# Fazendo o teste T para duas amostras independentes com um nível de significância de 1%
estatistica_t, p_valor_t = ttest_ind(tempo_atendimento_h1,
                                     tempo_atendimento_h2,
                                     equal_var=True)

#print(estatistica_t)
print(f"""O p-valor do teste T para duas amostras com variância homogeneidade 
      de variâncias e com significacia de 1% (0.01) foi de: {p_valor_t}""")


