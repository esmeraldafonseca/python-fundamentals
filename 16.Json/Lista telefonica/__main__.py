from contato import *
def main():

    Contatos = [
    {"Nome": "Ana", "Contato": 927184920},
    {"Nome": "Mario", "Contato": 926371908},
    {"Nome": "Debora", "Contato":925109878}
]

    guardar_contatos(Contatos)
    atualiza_numero("Ana", 936775292)
    apagar_contatos("Mario")



    contato = carregar_contatos()
    print(contato)

if __name__ == "__main__":
    main()