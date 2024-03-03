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
print(preco_range)