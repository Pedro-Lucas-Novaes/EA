import pandas as pd

tabela = pd.read_csv('dados.csv')

serie = tabela["cidade"]

frequencia = serie.value_counts()
frequencia_acumulada = frequencia.cumsum()

tabela = pd.DataFrame({
    'Frequencia': frequencia,
    'Frequencia_Relativa': frequencia / len(serie),
    'Frequencia_Acumulada': frequencia_acumulada
})

print(tabela)