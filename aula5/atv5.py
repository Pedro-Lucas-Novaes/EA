import pandas as pd
import matplotlib.pyplot as plt

Linguagens = ['Python', 'Java', 'Python', 'JavaScript', 'Python', 'C#', 
'Java', 'Python', 'C#', 'Python']


# 1. Converta a lista de linguagens em uma Series do Pandas.

serie = pd.Series(Linguagens)

# 2. Calcule a frequência absoluta de cada uma e descubra qual linguagem é a Moda do conjunto.

freq = serie.value_counts()
print("Frequencia absoluta")
print(freq)
print("lista da frequencia")
moda = serie.mode()
print(moda)

# 3. Calcule a frequência relativa em porcentagem para cada categoria registrada.

freq_rel = serie.value_counts(normalize=True) * 100
print("Frequencia relativa em porcentagem")
print(freq_rel)

# 4. Crie um Gráfico de Barras com Matplotlib mostrando a preferência das linguagens

freq.plot(kind='bar')
plt.title('Preferencia das linguagens')
plt.show()