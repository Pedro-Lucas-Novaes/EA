import pandas as pd

notas = pd.Series([7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 
9, 8, 10])

print(f"Media: {notas.mean()}")
print(f"Mediana: {notas.median()}")
print("Moda: ")
print(notas.mode())
print(f"Minimo: {notas.min()} Maximo: {notas.max()}")