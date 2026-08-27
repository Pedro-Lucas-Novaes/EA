import pandas as pd

clientes = pd.DataFrame({
    "Cliente": [
        "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
        "Fernanda", "Gabriel", "Helena", "Igor", "Julia",
        "Lucas", "Marina", "Nicolas", "Olivia", "Pedro",
        "Rafaela", "Samuel", "Tatiana", "Victor", "Yasmin",
        "Alice", "Bernardo", "Camila", "Diego", "Elisa",
        "Felipe", "Giovana", "Henrique", "Isabela", "Joao",
        "Karen", "Leonardo", "Manuela", "Nathan", "Paula",
        "Ricardo", "Sofia", "Thiago", "Valentina", "William",
        "Amanda", "Bianca", "Caio", "Debora", "Enzo",
        "Flavia", "Gustavo", "Heloisa", "Ivan", "Jasmin",
        "Kevin", "Larissa", "Marcelo", "Natalia", "Otavio",
        "Priscila", "Rafael", "Sara", "Tomás", "Vanessa",
        "Arthur", "Beatriz", "Cesar", "Diana", "Elias",
        "Fabiana", "Guilherme", "Isis", "Jonas", "Karina",
        "Luan", "Mirela", "Noah", "Patricia", "Renato",
        "Silvia", "Tales", "Ursula", "Vinicius", "Wesley",
        "Adriana", "Breno", "Clara", "Douglas", "Estela",
        "Fernando", "Gabriela", "Hugo", "Ingrid", "Jorge",
        "Kelly", "Luiz", "Monica", "Nelson", "Otavio",
        "Priscila", "Roberto", "Simone", "Tiago", "Viviane"
    ],
    "Idade": [
        18, 22, 35, 29, 41,
        26, 33, 45, 19, 24,
        31, 38, 27, 52, 34,
        23, 47, 30, 36, 28,
        21, 43, 32, 25, 39,
        18, 29, 44, 37, 26,
        33, 48, 22, 31, 40,
        35, 27, 46, 24, 53,
        20, 34, 42, 29, 23,
        38, 31, 50, 26, 36,
        28, 45, 33, 21, 47,
        30, 39, 25, 54, 32,
        19, 41, 27, 35, 49,
        23, 37, 44, 29, 31,
        26, 43, 20, 52, 34,
        38, 28, 46, 33, 24,
        40, 22, 36, 51, 27,
        45, 30, 39, 25, 48,
        32, 21, 42, 29, 35,
        47, 26, 53, 31, 44
    ],
    "Valor": [
        120, 250, 180, 320, 450,
        210, 390, 520, 150, 275,
        340, 480, 225, 610, 375,
        190, 550, 300, 425, 260,
        175, 490, 315, 230, 580,
        140, 360, 470, 290, 215,
        395, 625, 185, 330, 445,
        510, 270, 355, 600, 420,
        160, 385, 530, 245, 195,
        410, 345, 575, 280, 465,
        225, 540, 310, 170, 495,
        365, 590, 255, 430, 200,
        135, 460, 295, 375, 515,
        180, 405, 625, 250, 335,
        290, 480, 155, 570, 345,
        415, 265, 535, 390, 220,
        450, 310, 185, 525, 350,
        275, 440, 600, 230, 490,
        365, 205, 555, 320, 475,
        290, 510, 340, 165, 580
    ]
})

# Calcule o gasto médio da população.
gasto_medio = clientes["Valor"].mean()
print(f"Gasto Médio geral: {gasto_medio}\n")

# Retire uma amostra aleatória de 10 clientes.
amostra_10 = clientes.sample(n=10, random_state=20)
print(f"Amostra Aleatória de 10 clientes:\n {amostra_10}\n")

# Calcule o gasto médio da amostra.
gasto_medio_10 = amostra_10["Valor"].mean()
print(f"Gasto Médio da amostra:{gasto_medio_10}\n")

# Retire uma amostra de 30 clientes.
amostra_30 = clientes.sample(n=30, random_state=20)
print(f"Amostra Aleatória de 30 clientes:\n {amostra_30}\n")

gasto_medio_30 = amostra_30["Valor"].mean()

# Compare as duas estimativas.

print(f"Amostra 10: {gasto_medio - gasto_medio_10}")

print(f"Amostra 30: {gasto_medio - gasto_medio_30}")

