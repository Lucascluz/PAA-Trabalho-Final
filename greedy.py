from builtins import input, int, len, print, range
import pandas as pd
import time

def knapsack_greedy_solver(values, weights, capacity):
    n = len(values)
    
    # Criando uma lista de índices ordenados pelo valor por peso em ordem decrescente
    start_time = time.time()
    sorted_indices = sorted(range(n), key=lambda i: values[i] / weights[i] if weights[i] != 0 else 0, reverse=True)
    end_time = time.time()
    print(f"Tempo de ordenação: {end_time - start_time} segundos")

    max_value = 0
    selected_items = []

    start_time = time.time()
    for i in sorted_indices:
        if weights[i] != 0 and int(weights[i]) <= capacity:
            # Se o peso do item couber na capacidade, adiciona o valor do item ao máximo
            max_value += values[i]
            # Reduz a capacidade disponível
            capacity -= int(weights[i])
            # Adiciona o índice do item selecionado à lista
            selected_items.append(i)
    end_time = time.time()
    print(f"Tempo de execução do algoritmo: {end_time - start_time} segundos")

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

# Resolvendo o problema da mochila 0/1 com abordagem gananciosa
max_value, selected_items = knapsack_greedy_solver(avg_reviews, prices, knapsack_capacity)

# Exibindo resultados
print(f"Valor máximo obtido (método guloso): {max_value}")
print("Itens selecionados:")
for item in selected_items:
    print(f"  - {df.loc[item, 'title']}")

# Medindo o tempo total de execução
total_end_time = time.time()
print(f"Tempo total de execução: {total_end_time - total_start_time} segundos")
