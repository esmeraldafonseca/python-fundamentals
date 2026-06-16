from poligono import Quadrado, Circulo
from rich import print 
def main():
    circulo1 = Circulo(12)
    print(f"O perimetro de um circulo com {circulo1.raio}cm de raio é de {circulo1.Perimetro():.1f}cm")
    print(f"A area de um circulo com {circulo1.raio}cm de raio é de {circulo1.Area():.1f}cm²")
    print()

    quadrado = Quadrado(8)
    print(f"O perimetro de um quadrado com {quadrado.lado}cm de raio é de {quadrado.Perimetro():.1f}cm")
    print(f"A area de um quadrado com {quadrado.lado}cm de raio é de {quadrado.Area():.1f}cm²")
    
if __name__ == "__main__":
    main()