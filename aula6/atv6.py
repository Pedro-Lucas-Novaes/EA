# Exercício 6 (API)
# Crie uma simulação em Python para 10.000 requisições de uma API:
# 1. Cada requisição tem 95% de chance de Sucesso e 5% de Erro.
# 2. Utilize `np.random.choice()` para simular.
# 3. Calcule o total e a porcentagem de erros obtidos na simulação.

import numpy as np

requisicoes = np.random.choice( ["Sucesso", "Erro"], size=10000, p=[0.95, 0.05])

total = len(requisicoes)
total_erros = (requisicoes == "Erro").sum()
porcentagem_erros = (total_erros / total) * 100

print("Total de requisições", total)
print("Total de erros", total_erros)
print("Porcentagem de erros", porcentagem_erros,"%")