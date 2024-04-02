# %%
# Questão 6
# Um grupo de 60 leitores fez uma avaliação de três livros de romance e, ao final, 
# escolheram uma das três opções. Teste a hipótese nula de que não há preferência 
# dos leitores, com nível de significância de 5%.

# Eventos	Livro A	Livro B	Livro C	Total
# Frequência	 29	     15      16	   60

# Teste qui-quadrado (nominal ou ordinal)
import numpy as np
from scipy import stats
# %%
# Criando a tabela de contingência
obs = np.array([29, 15, 16])

# %%
res4 = stats.chisquare(obs)
res4.pvalue