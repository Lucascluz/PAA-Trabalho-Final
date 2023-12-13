from builtins import enumerate, input, int, len, print, range, max, sum
import tkinter
import pandas as pd
from tkinter import ttk
from tkinter import filedialog
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
    max_value, selected_items = knapsack_bruteforce_solver(avg_reviews, prices, knapsack_capacity)

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