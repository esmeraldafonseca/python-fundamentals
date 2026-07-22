from Personagens_rpg import *
from rich import inspect, print

def main():
    p1 = Guerreiro("Pikachu", 1000)
    p1.receber_danos(1000)
    
    p2 = Mago("Gandalf", 2000)

    p1.atacar(p2, 20000)
    p2.atacar(p1)

if __name__ == "__main__":
    main()