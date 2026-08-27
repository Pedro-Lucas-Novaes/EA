import pandas as pd

alunos = pd.DataFrame({
 "Nome": [
 "Ana", "Bruno", "Carlos", "Daniela",
 "Eduardo", "Fernanda", "Gabriel", "Helena",
 "Igor", "Julia", "Lucas", "Marina"
 ],
 "Idade": [18, 17, 19, 16, 34, 18, 17, 19, 15, 18, 15, 40],
 "Nota": [8, 7, 9, 6, 10, 8, 7, 9, 5, 8, 6, 10]
})
# Calcule a média da população.
media_populacao = alunos["Idade"].mean()
print(f"Média da população: {media_populacao}")

# Selecione aleatoriamente 5 alunos.
amostra = alunos.sample(n=5, random_state=20)

# Calcule a média da amostra.
media_amostra = amostra["Idade"].mean()
print(f"Média da amostra: {media_amostra}")

# Selecione aleatoriamente 10 alunos.
amostra_10 = alunos.sample(n=10, random_state=20)
print(amostra_10)

# Calcule novamente a média.
media_amostra_10 = amostra_10["Idade"].mean()
print(f"Média da amostra com 10: {media_amostra_10}")

# Compare os resultados

print(media_populacao - media_amostra - media_amostra_10)



