def area(largura, comprimento):
    a = largura * comprimento
    print(f'A area de um terreno com {largura}m e {comprimento} é de {a}m²')


#programa principal
largura = float(input("Largura(m): "))
comprimento = float(input("Comprimento(m): "))
area(largura, comprimento)