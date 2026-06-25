import json

contatos = [
    {"Nome": "Ana", "Contato": 927184920},
    {"Nome": "Mario", "Contato": 926371908}
]

with open("contatos.json", "w") as ficheiro:
    json.dump(contatos, ficheiro)
    

with open("contatos.json", "r") as ficheiro:
    contatos_py= json.load(ficheiro)

for itens in contatos_py:
    print(f"Nome: {itens['Nome']}\nContatos: {itens['Contato']}")
    print()