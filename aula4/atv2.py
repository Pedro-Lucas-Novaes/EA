import pandas as pd
import matplotlib.pyplot as plt

linguagens = [
    "Python", "JavaScript", "TypeScript", "Java", "C#", 
    "C++", "C", "JavaScript", "Rust", "PHP", 
    "Python", "Kotlin", "Swift", "TypeScript", "SQL", 
    "Scala", "JavaScript", "Elixir", "Haskell", "Java", 
    "Python", "Julia", "Clojure", "TypeScript", "Assembly", 
    "Shell/Bash", "JavaScript", "Groovy", "TypeScript", "Java"
]

serie = pd.Series(linguagens)

#frequencia de cada linguagem

frequencia_absoluta = serie.value_counts()
print("Frequencia Absoluta")
print(frequencia_absoluta)

#frequencia relativa

frequencia_relativa = serie.value_counts(normalize=True)
print("Frequencia Relativa")
print(frequencia_relativa)

#frequencia mais frequente

print("Linguagem mais Frequente")
print(frequencia_absoluta.idxmax(), frequencia_absoluta.max())

#Depois Crie um gráfico de barras

frequencia_absoluta.plot(kind="bar")

plt.title("linguagem de programação")

plt.show()