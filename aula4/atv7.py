import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('usuarios_100.csv')
print(df.head())

# Dados categóricos

# Calcule:

# ● frequência;

frequencia_so= df['sistema_operacional'].value_counts()
frequencia_lp= df['linguagem_preferida'].value_counts()

print(frequencia_so)
print(frequencia_lp)

# ● frequência relativa;

frequencia_so_relativa = df['sistema_operacional'].value_counts(normalize=True) * 100
frequencia_lp_relativa = df['linguagem_preferida'].value_counts(normalize=True) * 100

print(frequencia_so_relativa)
print(frequencia_lp_relativa)

# ● gráfico de barras.

frequencia_so.plot(kind="bar")

plt.title("Sistemas Operacionais")
plt.xlabel("Frequencia")
plt.ylabel("Sistema")

plt.show()

#################

frequencia_lp.plot(kind="bar")

plt.title("Linguagem preferida")
plt.xlabel("Frequencia")
plt.ylabel("Linguagens")

plt.show()


# Dados numéricos

frequencia_i= df['idade'].value_counts()
frequencia_td= df['tempo_uso_diario'].value_counts()

# Crie:

# ● histograma;

frequencia_i.plot(kind="hist")

plt.title("Idade")
plt.xlabel("Frequencia")
plt.ylabel("Idades")

plt.show()

###################

frequencia_td.plot(kind="hist")

plt.title("Tempo de uso Diario")
plt.xlabel("Frequencia")
plt.ylabel("Tempo de uso")

plt.show()

# ● boxplot.

frequencia_i.plot(kind="box")

plt.title("Idade")
plt.xlabel("Frequencia")
plt.ylabel("Idades")

plt.show()

####################

frequencia_td.plot(kind="box")

plt.title("Tempo de uso Diario")
plt.xlabel("Frequencia")
plt.ylabel("Tempo de uso")

plt.show()