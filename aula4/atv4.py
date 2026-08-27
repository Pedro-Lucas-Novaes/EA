import pandas as pd
import matplotlib.pyplot as plt

dados = [
    162, 146, 166, 188, 144, 144, 189, 169, 138, 163,
    138, 138, 156, 102, 106, 135, 124, 157, 127, 114,
    186, 144, 151, 114, 136, 152, 121, 159, 134, 142,
    134, 196, 149, 123, 170, 119, 155, 101, 116, 154,
    168, 154, 147, 142, 113, 132, 138, 176, 158, 105
]

serie = pd.Series(dados)


# 1. Calcule a frequência.

frequencia_absoluta = serie.value_counts()
print(frequencia_absoluta)

# 2. Crie um histograma.

frequencia_absoluta.plot(kind="hist")

plt.title("Dados")

plt.show()

# 3. Utilize diferentes quantidades de bins.

frequencia_absoluta.plot(kind="hist", bins=5)

plt.title("Dados")

plt.show()


# 4. Compare os histogramas.

