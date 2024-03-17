# %%
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# Um grupo de 20 consumidores fez um teste de degustação com dois tipos de cerveja 
# (Marca A e Marca B). Ao final, escolheram uma das marcas, como vemos a seguir.
# Teste a hipótese de não há diferença na preferência dos consumidores, ao nível de 
# significância de 5%.

# Tabela de contingência
notas = [[8, 12], [12, 8]]  # Marca A vs Marca B
# %%
# Teste Qui-quadrado
chi2_statistic, p_value_chi2, _, _ = stats.chi2_contingency(notas)
print("Teste Qui-quadrado:")
print("Estatística Qui-quadrado:", chi2_statistic)
print("Valor p:", p_value_chi2)

# %%
# Também vamos fazer o teste binomial

# Número total de consumidores
total_consumers = 20

# Número de consumidores que escolheram a Marca A
marca_a = 8

# Proporção esperada sob a hipótese nula
p = 0.5

# %%
# Teste binomial
p_value_binomial = stats.binom_test(marca_a, n=total_consumers, p=p, alternative='two-sided')
print("Teste Binomial:")
print("Valor p:", p_value_binomial)


# Eventos	Marca A	Marca B	Total
# Frequência	8	12	20

# No R 
# Binário:
# binom.test(8, 20, p = 0.5, conf.level = 0.95)
 
# Exact binomial test 
# data:  8 and 20
# number of successes = 8, number of trials = 20, p-value = 0.5034
# alternative hypothesis: true probability of success is not equal to 0.5
# 95 percent confidence interval:
#   0.1911901 0.6394574
# sample estimates:
#   probability of success 
# 0.4 

# binom.test(12, 20, p = 0.5, conf.level = 0.95)
# Exact binomial test
# data:  12 and 20
# number of successes = 12, number of trials = 20, p-value = 0.5034
# alternative hypothesis: true probability of success is not equal to 0.5
# 95 percent confidence interval:
#   0.3605426 0.8088099
# sample estimates:
#   probability of success 
# 0.6
 
# Não paramétrico uma amostra Teste Qui-quadrado
# preferencia <- c(8, 12)
# chisq.test(preferencia)
 
# Chi-squared test for given probabilities
 
# data:  preferencia
# X-squared = 0.8, df = 1, p-value = 0.3711

# De acordo com os testes acima, podemos afirmar, que não há preferência entre as marcas.
