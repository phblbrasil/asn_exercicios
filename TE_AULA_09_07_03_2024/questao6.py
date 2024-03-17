# %%
# Questão 6
# Um grupo de 60 leitores fez uma avaliação de três livros de romance e, ao final, 
# escolheram uma das três opções. Teste a hipótese nula de que não há preferência 
# dos leitores, com nível de significância de 5%.

# Eventos	Livro A	Livro B	Livro C	Total
# Frequência	 29	     15      16	   60

# Teste qui-quadrado (nominal ou ordinal)
import numpy as np
from scipy.stats import chi2_contingency
# %%
# Criando a tabela de contingência
obs = np.array([29, 15, 16])

# %%
obs2 = np.array([[29, 15, 70]])
# %%
res = chi2_contingency(obs)


# %%
res2 = chi2_contingency(obs2)
res2.pvalue

# %%

obs3 = np.array(
    [[[[12, 17],
       [11, 16]],
      [[11, 12],
       [15, 16]]],
     [[[23, 15],
       [30, 22]],
      [[14, 17],
       [15, 16]]]])
res3 = chi2_contingency(obs3)
res3.pvalue
# %%
res.pvalue
# %%
# Teste Qui-quadrado
chi2_statistic, p_value_chi2, _, _ = chi2_contingency(obs)
print("Teste Qui-quadrado:")
print("Estatística Qui-quadrado:", chi2_statistic)
print("Valor p:", p_value_chi2)

