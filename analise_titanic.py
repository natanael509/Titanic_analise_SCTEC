# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt


# LENDO O ARQUIVO CSV

# Lê o arquivo titanic.csv (deve estar na mesma pasta)
df = pd.read_csv("titanic_dataset.csv")

# Mostra as 5 primeiras linhas
print("Primeiras linhas do dataset:")
print(df.head())

# Mostra informações gerais
print("\nInformações do dataset:")
print(df.info())

# Mostra estatísticas básicas
print("\nEstatísticas descritivas:")
print(df.describe())

# 2 VERIFICANDO VALORES NULOS

print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Preenchendo valores nulos da idade com a média
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Preenchendo valores nulos de Embarked com o valor mais frequente
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# 3 ANÁLISE EXPLORATÓRIA

# Taxa geral de sobrevivência
taxa_sobrevivencia = df["Survived"].mean()
print("\nTaxa geral de sobrevivência:", taxa_sobrevivencia)

# Sobrevivência por sexo
print("\nSobrevivência por sexo:")
print(df.groupby("Sex")["Survived"].mean())

# Sobrevivência por classe
print("\nSobrevivência por classe:")
print(df.groupby("Pclass")["Survived"].mean())

# 4 CRIANDO UM GRÁFICO SIMPLES

# Contagem de sobreviventes
sobreviventes = df["Survived"].value_counts()

plt.bar(["Não Sobreviveu", "Sobreviveu"], sobreviventes)
plt.title("Quantidade de Sobreviventes")
plt.xlabel("Situação")
plt.ylabel("Quantidade")

# Salva o gráfico
plt.savefig("grafico_sobreviventes.png")

# Mostra o gráfico na tela
plt.show()

print("\nAnálise finalizada!")
