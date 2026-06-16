#from rich import print
from Transportes import *

def main():
    distancia  = 4

    veiculo = Drone(distancia)
    print(f"O frete de {type(veiculo).__name__} para uma distancia de {veiculo.distancia}km é de {veiculo.calcular_frete()}")


if __name__ == "__main__":
    main()