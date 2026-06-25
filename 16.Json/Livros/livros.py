import json

def guardar_livros(lista):

    with open("livros.json", "w") as f:
        json.dump(lista, f)

def carregar_livros():
    with open("livros.json", "r") as f:
        return json.load(f)
    