import pandas as pd

alunos = pd.DataFrame({
 "Nome": [
 "Ana", "Bruno", "Carlos", "Daniela",
 "Eduardo", "Fernanda", "Gabriel", "Helena",
 "Igor", "Julia", "Lucas", "Marina"
 ],
 "Nota": [8, 7, 9, 6, 10, 8, 7, 9, 5, 8, 6, 10]
})

# Verifique o tamanho da população
print(alunos.shape[0])
print(len(alunos))

# Calcule a média da população
media_populacao = alunos["Nota"].mean()
print(media_populacao)

# Retire uma amostra de 5 alunos

amostra = alunos.sample(n=5, random_state=42)

# Calcule as duas médias.
media_amostra = amostra["Nota"].mean()
print(media_amostra)

# Compare as duas médias
print(media_populacao - media_amostra)

# Repita utilizando uma amostra de 8 alunos
amostra_8 = alunos.sample(n=8, random_state=42)
media_amostra_8 = amostra_8["Nota"].mean()
print(media_populacao - media_amostra_8)
