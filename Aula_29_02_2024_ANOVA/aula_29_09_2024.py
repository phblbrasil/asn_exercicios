# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
from scipy.stats import kstest

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
chocolates = chocolates.rename(
    columns={
        'faixa_preco': 'Faixa de Preço',
        'range_preco': 'Intervalo do Valor do Chocolate',
        'notas': 'Notas Recebidas'
    }
)

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
            x='Faixa de Preço', 
            y='Notas Recebidas',
            color='.8',
            #linecolor="#000",
            linewidth=.75)
plt.title('Comportamento das notas por Faixa de Preço')
plt.show()
# %%
# distribuição das observações no histograma
sns.histplot(data=chocolates, 
             x='Notas Recebidas', 
             bins= 20,
             kde=True)
plt.title('Distribuição das Notas')
plt.show()

# %%
# criando o gráfico de densidade
sns.displot(chocolates,
            x='Notas Recebidas',
            kind='kde')
plt.title('Densidades das Notas')
plt.show()
# %%
# b.pense em um gráfico interessante para verificar se existe alguma relação
# entre as notas dadas e o preço do chocolate
sns.scatterplot(data = chocolates, 
                x = 'Faixa de Preço', 
                y = 'Notas Recebidas', 
                hue = 'Intervalo do Valor do Chocolate')
plt.title('Relação Faixa de Preço x Notas')
plt.show()
# %%
# c. O que pode ser feito para detectar se existe alguma interação?

# %%
# d.Faça a anova e verifique se as médias das notas, por faixa de preço são iguais.
# começando temos que fazer o passo a passo para podermos fazer a ANOVA, são eles:
# 1) Teste de normalidade da base
# 2) 
# 3) 
# 4) 

# %%
teste_normal = pd.DataFrame(chocolates_medias['Notas Recebidas'])
sns.displot(teste_normal,
            x='Notas Recebidas',
            kind='kde')
# %%
resultado_ks, p_valor = kstest(teste_normal,'norm')
print("Estatística de teste KS:", resultado_ks)
print("P-valor:", p_valor)
# %%
g1_g2_dist = chocolates_medias[
    (chocolates_medias['Faixa de Preço'] == 'g1') |
    (chocolates_medias['Faixa de Preço'] == 'g2')
    ]
sns.displot(g1_g2_dist,
            x='Notas Recebidas',
            kind='kde')
plt.title('Distribuição G1 e G2')
plt.show()


# %%
g3_dist = chocolates_medias[chocolates_medias['Faixa de Preço'] == 'g3']
sns.displot(g1_g2_dist,
            x='Notas Recebidas',
            kind='kde')
plt.title('Distribuição G3')
plt.show()

# %%
g4_dist = chocolates_medias[chocolates_medias['Faixa de Preço'] == 'g4']

sns.displot(g1_g2_dist,
            x='Notas Recebidas',
            kind='kde')
plt.title('Distribuição G4')
plt.show()
# %%
g5_g6_dist = chocolates_medias[
    (chocolates_medias['Faixa de Preço'] == 'g5') |
    (chocolates_medias['Faixa de Preço'] == 'g6')
    ]
sns.displot(g5_g6_dist,
            x='Notas Recebidas',
            kind='kde')
plt.title('Distribuição G1 e G2')
plt.show()

# %%
# e.Crie as equações para chegar no chute sofisticada (ychapeu). 
# primeiramente vamos definir as médias por grupos:
medias_grupos = chocolates.groupby('Faixa de Preço')['Notas Recebidas'].mean().round(2)
print(medias_grupos)
# %%
media_faixa_preco = {
    'g1':'1.0',
    'g2':'1.0',
    'g3':'3.0',
    'g4':'7.0',
    'g5':'9.0',
    'g6':'9.0'
}

# %%
# adicionar a media na tabela chocolates por faixa de frupo
chocolates_medias = chocolates
# %%
# %%
chocolates_medias['faixa_preco'] = {}
chocolates_medias['media_grupo'] = {}
# %%
chocolates_medias['faixa_preco'] = chocolates_medias['Faixa de Preço'].map(media_faixa_preco)
chocolates_medias = chocolates_medias.drop(columns=['media_grupo'])

# %%
chocolates_medias['media_global'] = chocolates_medias['Notas Recebidas'].mean()

# %%

chocolates_medias.head(10)

# %%

chocolates_medias.to_csv('chocolate_tratado.csv', sep=',', index=False)
# i.Quantas equações podem ser criadas?

# %%
# ii.Descreva cada uma dessas equações

# %%
# f.Calcule SQT, SQM e SQE

# %%
# g.Calcule R2 e interprete

# %%
# h.Observe as equações que você criou e me conte se algo te chamou a atenção.
