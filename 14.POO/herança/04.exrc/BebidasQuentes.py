from abc import ABC, abstractmethod

class BebidasQuentes(ABC):

    def preparar(self):
        print(f"{"A inicializar o processo":-^50} \n")
        print(self.ferver_agua())
        print(self.misturar())
        print(self.servir())
        print()
        print(f"{"Bebida pronta!":-^50}")

    def ferver_agua(self):
        return "1- A ferver a agua a 100 graus Celsius."

    @abstractmethod
    def servir(self):
        pass


    @abstractmethod
    def misturar(self):
        pass

class cafe(BebidasQuentes):
    def __init__(self):
        super().__init__()
    

    def misturar(self):
        return "2- A passar a agua quente pelo po de cafe moido."
    
    
    def servir(self):
        return "3- Servindo em um xicara pequena."
    

class cha(BebidasQuentes):
    def __init__(self):
        super().__init__()
    

    def misturar(self):
        return "2- Colocar e tirar a saqueta de cha na agua quente\n   7 vezes."
    
    
    def servir(self):
        return "3- Servir em uma chavena."

class leite(BebidasQuentes):
    def __init__(self):
        super().__init__()
    
    def misturar(self):
        return "Dissolver o leite em po instantanio na agua quente"
    
    
    def servir(self):
        return "Servir em uma caneca."


