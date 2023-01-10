# NOTE Modulo JSON
import json

# Melhor para armazenar obj, dicionário, listas, etc
# Texto é txt, o rsto JSON é melhor

lista_pessoas = [
    {
        "nome": "Maya",
        "raca": "Cachorro"
    },
    {
        "nome": "Victoria",
        "raca": "Humano"
    },
]

retrieved_data = []

with open("/Users/victorialuquet/Desktop/python-course/curso/files/data.json", "w") as data_file:
    json.dump(lista_pessoas, data_file, ensure_ascii=False) 
    # Faz o 'dump' do dado no aruivo json -> converte e guarda
    # ensure_ascii -> guarda do jeito que ta com acento e tal, sem codificacao
    
    retrieved_data = json.load() # Pega os dados do arquivo