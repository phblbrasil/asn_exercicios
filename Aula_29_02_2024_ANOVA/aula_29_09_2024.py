# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# carregando o banco de dados das notas
chocolates = pd.read_excel("notas_precos.xlsx", sheet_name="preco_nota")

# carregando a relação dos grupos e das faixas de preço
preco_range = pd.read_excel("notas_precos.xlsx", sheet_name="range_vlr_venda")

# %%
range_preco_chocolate = {
    'g1':'0 a 5 reais',
    'g2':'5 a 10 reais',
    'g3':'10 a 15 reais',
    'g4':'15 a 20 reais',
    'g5':'20 a 25 reais',
    'g6':'25 a 30 reais'
}

# %%
chocolates['range_preco'] = chocolates['faixa_preco'].map(range_preco_chocolate)
chocolates = chocolates[['faixa_preco', 'range_preco', 'notas']]
# %%
print(chocolates)
# %%
# Aqui temos um experimento onde vários indivíduos independentes deram notas para alguns chocolates.
# Em cada linha da tabela temos um chocolate diferente que foi avaliado
#  Bom trabalho =] : 
# 
# a.	Fazer uma análise descritiva das duas variáveis sozinhas
# b.	pense em um gráfico interessante para verificar se existe alguma relação entre as notas dadas e o preço do chocolate
# c.	o que pode ser feito para detectar se existe alguma interação?
# d.	Faça a anova e verifique se as médias das notas, por faixa de preço são iguais.
# e.	Crie as equações para chegar no chute sofisticada (ychapeu). 
# i.	Quantas equações podem ser criadas?
# ii.	Descreva cada uma dessas equações
# f.	Calcule SQT, SQM e SQE
# g.	Calcule R2 e interprete
# h.	Observe as equações que você criou e me conte se algo te chamou a atenção.
# %%
# a.Fazer uma análise descritiva das duas variáveis sozinhas
# %%
# describe chocolates
descritivo = chocolates.describe()
print(descritivo)
# %%
# quartis das notas
sns.boxplot(data=chocolates, 
            x="faixa_preco", 
            y="notas",
            color='.8',
            #linecolor="#000",
            linewidth=.75)

# %%
# distribuição das observações no histograma
sns.histplot(data=chocolates, 
             x='notas', 
             bins= 30,
             kde=True)

# %%
# b.pense em um gráfico interessante para verificar se existe alguma relação
# entre as notas dadas e o preço do chocolate

sns.scatterplot(data = chocolates, x = 'notas', y = 'faixa_preco', hue = 'range_preco', )

# %%
# c.o que pode ser feito para detectar se existe alguma interação?

# %%
# d.Faça a anova e verifique se as médias das notas, por faixa de preço são iguais.

# %%
# e.Crie as equações para chegar no chute sofisticada (ychapeu). 

# %%
# i.Quantas equações podem ser criadas?

# %%
# ii.Descreva cada uma dessas equações

# %%
# f.Calcule SQT, SQM e SQE

# %%
# g.Calcule R2 e interprete

# %%
# h.Observe as equações que você criou e me conte se algo te chamou a atenção.
