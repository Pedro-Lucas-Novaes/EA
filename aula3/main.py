import pandas as pd

df = pd.read_csv("dados.csv")


nAmostra = 1000
amostra = df.sample(n=nAmostra, random_state=15)

medPopulacao = df["idade"].mean()
print(f"Média população:{medPopulacao}")

medAmostra = amostra["idade"].mean()
print(f"Média da amostra: {medAmostra}")

print(f"Erro amostral: {medPopulacao - medAmostra}")