from ContaBancaria import *

def main():
    conta1 = ContaBancaria(920, "Rui", 2000)
    conta1.sacar(2700)
    print(conta1)

if __name__ == "__main__":
    main()