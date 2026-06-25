import json

def guardar_contatos(contatos):
    with open("Contatos.json", "w", encoding="utf-8") as f:
        json.dump(contatos, f, indent=4)

def carregar_contatos():
    try:
        with open("Contatos.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        print("Ficheiro não encontrado, a começar do zero.")
        

def atualiza_numero(nome, novo_numero):
    contatos = carregar_contatos()
    for item in contatos:
        if item["Nome"] == nome:
            item["Contato"] = novo_numero
    guardar_contatos(contatos)
        

def apagar_contatos(nome):
    contatos = carregar_contatos()
    nova_lista=[]
    for item in contatos:
        if item["Nome"] != nome:
            nova_lista.append(item["Nome"])
    

    guardar_contatos(nova_lista)

        
