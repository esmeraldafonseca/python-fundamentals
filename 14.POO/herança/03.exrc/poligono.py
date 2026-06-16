from abc import ABC,abstractmethod
from math import pi
class Poligono(ABC):

    LADOS_QUANTIDADE =4

    @abstractmethod
    def Perimetro(self):
        pass

    @abstractmethod
    def Area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def Perimetro(self):
        return self.lado * self.LADOS_QUANTIDADE
   
    def Area(self):
        return self.lado **2
        
    

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    def Perimetro(self):
        return (2*pi) * self.raio
       
    def Area(self):
        return pi * (self.raio**2)


