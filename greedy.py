from builtins import input, int, len, print, range, max
import tkinter
import pandas as pd
from tkinter import ttk
from tkinter import filedialog
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
    max_value, selected_items = knapsack_greedy_solver(avg_reviews, prices, knapsack_capacity)

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
