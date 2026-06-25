import json

def guardar_produto(produto):
    with open("produtos.json", "w") as f:
        json.dump(produto, f)

def carregar_produto():
    with open("produtos.json", "r") as f:
        return json.load(f)

def produto_mais_caro(prdutos):
    return max(prdutos, key=lambda item: item["Preco"])

def actualizar_preco(nome, novo_preco):
    produtos = carregar_produto()

    for itens in produtos:
        if itens["Nome"] == nome:
            itens["Preco"] = novo_preco

    guardar_produto(produtos)

def apagar_produto(nome):
    produtos = carregar_produto()
    nova_lista=[]

    for itens in produtos:
        if itens["Nome"] != nome:
            nova_lista.append(itens)

    produtos = nova_lista
    guardar_produto(produtos)
    