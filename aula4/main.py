import pandas as pd

notas = [
 7, 8, 6, 9, 7,
 5, 8, 7, 10, 6,
 8, 9, 7, 5, 6,
 8, 7, 9, 8, 10
]

serie = pd.Series(notas)

frequencia = serie.value_counts().sort_index()
frequencia_acumulada = frequencia.cumsum()

tabela = pd.DataFrame({
    'Frequencia': frequencia,
    'Frequencia_Relativa': frequencia / len(serie),
    'Frequencia_Acumulada': frequencia_acumulada
})

print(tabela)