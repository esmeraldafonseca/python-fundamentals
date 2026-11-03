from casa import *

def main():

    casa1= Casa(4, 2, 2)
    casa2 = Casa(2, 1, 2)
    casa3 = Casa(6, 4, 5)
    print(casa1.descricao())
    casa_filtrada =Casa.filto_quartos(4)
    for casa in casa_filtrada:
        print()
        print(casa.descricao())

if __name__ == "__main__":
    main()