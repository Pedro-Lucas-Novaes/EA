import pandas as pd
import matplotlib.pyplot as plt

notas = [
 7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 9, 8, 10
 ]
# 1. Criar uma Series.
serie = pd.Series(notas)

# 2. Calcular a frequência absoluta.
fab = serie.value_counts()

# 3. Calcular a frequência relativa.
fr = serie.value_counts(normalize=True)

# 4. Calcular a frequência acumulada.

fac = fab.cumsum()

# 5. Criar uma tabela.

tabela = pd.DataFrame({
    "F_Absoluta": fab,
    "F_Relativa": fr,
    "F_Acumulativa": fac
})

# 6. Criar um gráfico de barras.

fab.plot(kind="bar")

plt.title("Frequencias das notas")
plt.xlabel("Notas")
plt.ylabel("Frequencia")

plt.show()

# 7. Criar um gráfico de pizza.

fab.plot(kind="pie", autopct="%1.1f%%")

plt.title("Frequencias das notas")

plt.show()