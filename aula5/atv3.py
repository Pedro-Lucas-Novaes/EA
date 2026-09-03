import pandas as pd

salarios = pd.Series([2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 
2800, 20000])

print(f"Media: {salarios.mean()}")

print(f"Mediana: {salarios.median()}")

tamanho = len(salarios)
tamanho_moda = len(salarios.mode())

print("Moda: ")
if tamanho_moda == tamanho:
    print("Amodal")
else:
    print(salarios.mode())


print(f"Minimo: {salarios.min()} Maximo: {salarios.max()}")