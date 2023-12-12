from builtins import input, int, len, print, range, max
import tkinter
import pandas as pd
from tkinter import ttk
from tkinter import filedialog
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

# Função para resolver o problema da mochila 0/1 com a interface gráfica
def solve_knapsack():
    # Carregando o arquivo CSV
    file_path = filedialog.askopenfilename(title="Selecione o arquivo CSV")
    df = pd.read_csv(file_path)

    # Extraindo valores relevantes das colunas
    avg_reviews = df['avg_reviews'].fillna(0).tolist()
    prices = df['price'].fillna(0).tolist()

    # Obtendo a capacidade da mochila através da interface gráfica
    knapsack_capacity = int(capacity_entry.get())

    # Resolvendo o problema da mochila 0/1
    max_value, selected_items = knapsack_pd_solver(avg_reviews, prices, knapsack_capacity)

    # Exibindo resultados na interface gráfica
    num_result_label.config(text=f"Quantidade de Livros selecionados: {len(selected_items)}")
    result_label.config(text=f"Total de estrelas obtidas (programação dinâmica): {max_value}")
    avg_stars_label.config(text=f"Média de estrelas: {max_value / len(selected_items)}")
    items_label.config(text="Itens selecionados:\n" + "\n".join([f"  - {df.loc[item, 'title']}" for item in selected_items]))

# Configuração da interface gráfica
root = tkinter.Tk()
root.title("Resolutor de Mochila 0/1 (Programação Dinâmica)")

# Botão para carregar o arquivo CSV
load_button = ttk.Button(root, text="Carregar Arquivo CSV", command=solve_knapsack)
load_button.pack(pady=10)

# Entrada para a capacidade da mochila
capacity_entry = ttk.Entry(root)
capacity_entry.pack(pady=5)
capacity_entry.insert(0, "100")

# Rótulos para os resultados
num_result_label = ttk.Label(root, text="")
num_result_label.pack(pady=5)

result_label = ttk.Label(root, text="")
result_label.pack(pady=5)

avg_stars_label = ttk.Label(root, text="")
avg_stars_label.pack(pady=5)

items_label = ttk.Label(root, text="")
items_label.pack(pady=5)

# Iniciar a interface gráfica
root.mainloop()