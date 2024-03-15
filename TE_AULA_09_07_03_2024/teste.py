# %%
from scipy import stats
# %%
# Suponha que você tenha uma amostra de dados numéricos
dados = [0.1, 0.2, 0.3, 0.4, 0.5]

# Realize o teste de normalidade Kolmogorov-Smirnov
statistic, p_value = stats.kstest(dados, 'norm')

# Exiba os resultados do teste
print("Estatística de teste:", statistic)
print("Valor P:", p_value)

# %%
# Verifique a hipótese nula (H0)
alpha = 0.05
if p_value > alpha:
    print("Não rejeitar H0: Os dados seguem uma distribuição normal")
else:
    print("Rejeitar H0: Os dados não seguem uma distribuição normal")
