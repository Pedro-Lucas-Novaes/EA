import numpy as  np
import pandas as pd

np.random.seed(15)

dados = {"Notas" : np.random.normal(70, 10, 10000)}

df = pd.DataFrame(dados)

amostra = df.sample(n=100, random_state=42)

media_populacao = df["Notas"].mean()
media_amostra = amostra["Notas"].mean()

#print(f"Média da população: {media_populacao}")

#print(f"Média da amostra: {media_amostra}")

for tamanho in [10, 50, 100, 500, 1000]:
    amostra = df.sample(n=tamanho, random_state=42)
    media = amostra["Notas"].mean()

    print(tamanho, media)