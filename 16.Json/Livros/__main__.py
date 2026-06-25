from livros import *

def main():
    lista_livro = [
        {"Titulo": "Bananas assassinas",
         "Autor": "Banana Joy"},
        {"Titulo": "Queria ser onde",
         "Autor": "Esqueci lol"},
        {"Titulo": "Morte no nilo",
         "Autor": "Aghata"}
    ]
    guardar_livros(lista_livro)

    livros = carregar_livros()

    for itens in livros:
        print(f'Titulo: {itens["Titulo"]}\nAutor: {itens["Autor"]}')
        print()

if __name__ == "__main__":
    main()