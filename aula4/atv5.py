import pandas as pd
import matplotlib.pyplot as plt

tempos = [ 110, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185,
 190, 195, 200, 205, 210, 220, 230, 250, 300, 500 ]

serie = pd.Series(tempos)
frequencia = serie.value_counts()



# 1. Histograma.

# frequencia.plot(kind="hist")
# plt.tilte("Tempos")
# plt.show()

# 2. Boxplot.

plt.boxplot(tempos)
plt.title("Tempos")
plt.show()

# Depois responda:
# ● Existem valores que parecem diferentes?

# SIM

# ● Qual região concentra a maior parte dos dados?

# 150

# ● O valor 500 parece seguir o comportamento dos demais?

# NÃO