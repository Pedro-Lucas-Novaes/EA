import pandas as pd

dados = {
    "Nome": ["João", "Maria", "Pedro", "Ana"],
    "Idade": [18, 20, 19, 22]
}

df = pd.DataFrame(dados)

# Exibir o data frame

print("******************************")
print(df) # print(df.head())
print("******************************")
# Contar os registro do dataframe
print(len(df)) # maneira 1
print(df.shape) # maneira 2
print("******************************")
# Vizualizar informações
df.info()
print("******************************")