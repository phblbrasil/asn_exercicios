# %%
import pandas as pd
from scipy.stats import kstest, norm, levene, ttest_ind
import seaborn as sns
import matplotlib.pyplot as plt

# %%
# Um grupo de 20 consumidores fez um teste de degustação com dois tipos de cerveja 
# (Marca A e Marca B). Ao final, escolheram uma das marcas, como vemos a seguir.
# Teste a hipótese de não há diferença na preferência dos consumidores, ao nível de 
# significância de 5%.

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
