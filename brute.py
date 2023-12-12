from builtins import bin, enumerate, filter, input, int, len, print, range, max, sum
import pandas as pd
import time

def generate_combinations(n):
    # Gera todas as combinações possíveis de 0s e 1s usando contagem binária
    for i in range(2**n):
        yield [int(x) for x in bin(i)[2:].zfill(n)]

def knapsack_bruteforce_solver(values, weights, capacity):
    # Medindo o tempo de inicialização
    start_time = time.time()

    n = len(values)

    max_value = 0
    selected_items = []

    # Iterando sobre todas as combinações possíveis de itens
    for combination in generate_combinations(n):
        current_value = sum(v * combination[i] for i, v in enumerate(values))
        current_weight = sum(w * combination[i] for i, w in enumerate(weights))

        # Verificando se a combinação é válida (dentro da capacidade da mochila)
        if current_weight <= capacity and current_value > max_value:
            max_value = current_value
            selected_items = [i for i, x in enumerate(combination) if x == 1]

    # Medindo o tempo de execução do algoritmo
    end_time = time.time()
    print(f"Tempo de execução do algoritmo: {end_time - start_time} segundos")

    return max_value, selected_items

# Carregando o arquivo CSV
csv_file_path = 'partial.csv'  # Substitua pelo caminho do seu arquivo CSV
df = pd.read_csv(csv_file_path)

# Extraindo valores relevantes das colunas
avg_reviews = df['avg_reviews'].fillna(0).tolist()  # Preenchendo valores ausentes com 0
prices = df['price'].fillna(0).tolist()  # Preenchendo valores ausentes com 0
knapsack_capacity = int(input("Digite a capacidade da mochila em dólares: "))

# Medindo o tempo total de execução
total_start_time = time.time()

# Resolvendo o problema da mochila 0/1 com força bruta otimizada
max_value_bruteforce, selected_items_bruteforce = knapsack_bruteforce_solver(avg_reviews, prices, knapsack_capacity)

# Exibindo resultados
print(f"Total de estrelas obtidas(método de força bruta otimizada): {max_value_bruteforce}")
print(f"Média de estrelas: {max_value_bruteforce / len(selected_items_bruteforce)}")
print("Itens selecionados:")
for item in selected_items_bruteforce:
    print(f"  - {df.loc[item, 'title']}")
