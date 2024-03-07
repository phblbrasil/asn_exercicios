# carregando os pacotes
library(readxl)
library(haven)
library(tidyverse)
library(car) #teste F de levene

# carregando a base de dados
chocolates <- read.csv2('Aula_29_02_2024_ANOVA/chocolate_tratado.csv', sep=',')

class(chocolates$Notas.Recebidas)
chocolates$Notas.Recebidas <- as.integer(chocolates$Notas.Recebidas)

class(chocolates$Notas.Recebidas)

chocolates_normal <- chocolates$Notas.Recebidas
# Teste de kolmogorov - Smirnov (KS)
# H0: amostra provem de uma populacao normal
# H1: amostra nao provem de uma populacao normal
ks.test (chocolates_normal, "pnorm", mean(chocolates_normal),sd(chocolates_normal))

# fazendo teste de variancia para saber se sao iguais ou nao
leveneTest(Notas.Recebidas ~ Faixa.de.Preço, data=chocolates)

# Como resultado temos:
# Levene's Test for Homogeneity of Variance (center = median)
#       Df F value Pr(>F)
# group  5  0.7364 0.5995
#       54 


# Agora vamos fazer a ANOVA
anova_chocolates = aov(Notas.Recebidas ~ Faixa.de.Preço, data=chocolates)
summary(anova_chocolates)
