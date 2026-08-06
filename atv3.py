import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Produto": ["Teclado", "Mouse", "Monitor", "Fone"],
    "Preco": [56.20, 25.00, 850.99, 85.00],
    "Quantidade": [10, 45, 12, 200]
}

df = pd.DataFrame(dados)

plt.plot(
    df["Preco"], df["Quantidade"],
    #width=1,
    color="#6f0ac7"
    )

plt.title("Quantidade dos Produtos")
plt.xlabel("Preco")
plt.ylabel("Quantidade")

plt.show()



