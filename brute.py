from builtins import enumerate, filter, input, int, len, print, range, max, sum
from itertools import product
import pandas as pd
import time
from itertools import product

def knapsack_bruteforce_solver(values, weights, capacity):
    n = len(values)
    max_value = 0
    selected_items = []

    # Reduzir o espaço de busca apenas para combinações com peso total <= capacidade
    valid_combinations = filter(lambda c: sum(weights[i] * c[i] for i in range(n)) <= capacity, product([0, 1], repeat=n))

    for combo in valid_combinations:
        total_value = sum(v * combo[i] for i, v in enumerate(values))

        if total_value > max_value:
            max_value = total_value
            selected_items = [i for i, x in enumerate(combo) if x == 1]

    return max_value, selected_items

# Restante do seu código...

# Carregando o arquivo CSV
csv_file_path = 'final_book_dataset_kaggle2.csv'  # Substitua pelo caminho do seu arquivo CSV
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
print(f"Valor máximo obtido (método de força bruta otimizada): {max_value_bruteforce}")
print("Itens selecionados:")
for item in selected_items_bruteforce:
    print(f"  - {df.loc[item, 'title']}")

# Medindo o tempo total de execução
total_end_time = time.time()
print(f"Tempo total de execução (método de força bruta otimizada): {total_end_time - total_start_time} segundos")
