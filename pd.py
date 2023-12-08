from builtins import input, int, len, print, range, max
import pandas as pd
import time

def knapsack_pd_solver(values, weights, capacity):
    n = len(values)
    # Inicializando a tabela de programação dinâmica
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Medindo o tempo de inicialização
    start_time = time.time()

    # Preenchendo a tabela de programação dinâmica
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Tratando valores ausentes e verificando se o peso do item cabe na capacidade
            if not pd.isna(weights[i - 1]) and int(weights[i - 1]) <= w:
                # Escolhendo o valor máximo entre incluir ou não o item na mochila
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - int(weights[i - 1])])
            else:
                # Caso o peso do item seja maior que a capacidade disponível
                dp[i][w] = dp[i - 1][w]

    # Medindo o tempo de execução do algoritmo
    end_time = time.time()
    print(f"Tempo de execução do algoritmo: {end_time - start_time} segundos")

    # Rastreando os itens selecionados
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            # Incluindo o índice do item selecionado
            selected_items.append(i - 1)
            # Atualizando a capacidade disponível
            if not pd.isna(weights[i - 1]):
                w -= int(weights[i - 1])
        i -= 1

    # Retornando o valor máximo e os índices dos itens selecionados
    return dp[n][capacity], selected_items

# Carregando o arquivo CSV
csv_file_path = 'final_book_dataset_kaggle2.csv'  # Substitua pelo caminho do seu arquivo CSV
df = pd.read_csv(csv_file_path)

# Extraindo valores relevantes das colunas
avg_reviews = df['avg_reviews'].fillna(0).tolist()  # Preenchendo valores ausentes com 0
prices = df['price'].fillna(0).tolist()  # Preenchendo valores ausentes com 0
knapsack_capacity = int(input("Digite a capacidade da mochila em dólares: "))

# Medindo o tempo total de execução
total_start_time = time.time()

# Resolvendo o problema da mochila 0/1
max_value, selected_items = knapsack_pd_solver(avg_reviews, prices, knapsack_capacity)

# Exibindo resultados
print(f"Valor máximo obtido: {max_value}")
print("Itens selecionados:")
for item in selected_items:
    print(f"  - {df.loc[item, 'title']}")

# Medindo o tempo total de execução
total_end_time = time.time()
print(f"Tempo total de execução: {total_end_time - total_start_time} segundos")
