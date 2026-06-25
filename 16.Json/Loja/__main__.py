from loja import *

def main():
    produtos=[
        {"Nome":"Tv", "Preco": 295},
        {"Nome":"Computador portatil", "Preco": 1699},
        {"Nome":"Mouse", "Preco": 17},
        {"Nome":"Mouse pad", "Preco":19}]
    
    guardar_produto(produtos)
    produto= carregar_produto()

    prod_caro = produto_mais_caro(produto)
    print(f"Produto mais caro: {prod_caro['Nome']} - {prod_caro['Preco']}€")

    print()

    actualizar_preco("Tv", 300)
    produto = carregar_produto()
    print(produto)

if __name__ == "__main__":
    main()