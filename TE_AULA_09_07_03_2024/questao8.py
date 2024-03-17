# %%

# Questão 8
# Um grupo de 15 consumidores avaliou o nível de satisfação (1=baixo, 2=médio, 3=alto) 
# de três serviços bancários diferentes. Os resultados estão na tabela Banco.xlsx. 
# Verifique se há diferença entre os três serviços. Considere nível de significância 
# de 5%.

# %%
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# %%
consumidores = pd.read_excel('dados/Banco.xlsx')
print(consumidores)

# %%
# teste ANOVA de um fator

f_statistic, p_value = stats.f_oneway(consumidores['A'],
                                      consumidores['B'],
                                      consumidores['C'])

# %%
print("Teste ANOVA:")
print("Estatística F:", f_statistic)
print("Valor p:", p_value)