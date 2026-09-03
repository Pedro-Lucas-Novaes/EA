import pandas as pd

tempos = pd.Series([120, 130, 125, 140, 120, 150, 125, 120, 135, 125])

print(f"Media: {tempos.mean()}")

print(f"Mediana: {tempos.median()}")

#print(f"Moda: {tempos.mode()[0]}")

print("Moda: ")
print(tempos.mode())

print(f"Minimo: {tempos.min()} Maximo: {tempos.max()}")
