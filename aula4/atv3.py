import pandas as pd
import matplotlib.pyplot as plt

sistema = [
    "Windows", 
    "Linux",
    "macOS",
    "Android",
    "iOS",
    "Windows",
    "Linux",
    "macOS",
    "Android",
    "iOS",
    "Windows",
    "Linux",
    "macOS",
    "Android",
    "iOS",
    "Windows",
    "Linux",
    "macOS",
    "Android",
    "iOS",
    "Windows",
    "Linux",
    "macOS",
    "Android",
    "iOS",
    "Windows",
    "Linux",
    "macOS",
    "Android",
    "iOS",
    "Windows",
    "Linux",
    "macOS",
    "Android",
    "iOS",
    "Windows","Linux","macOS", "Android",
    "iOS","Windows", "Linux",
    "macOS", "Windows",
    "Windows",
]

serie = pd.Series(sistema)

# 1. Calcule a frequência.

frequencia_absoluta = serie.value_counts()
print(frequencia_absoluta)

# 2. Calcule a porcentagem.

frequencia_relativa = serie.value_counts(normalize=True) * 100
print(frequencia_relativa)

# 3. Identifique o sistema mais frequente.
print(frequencia_absoluta.idxmax(), frequencia_absoluta.max())

# 4. Crie um gráfico de barras.

frequencia_absoluta.plot(kind="bar")

plt.title("Sistema operacional")

plt.show()

# 5. Crie um gráfico de pizza.

frequencia_absoluta.plot(kind="pie", autopct="%1.1f%%")

plt.title("linguagem de programação")

plt.show()