from abc import ABC, abstractmethod



class Transportes(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calcular_frete():
        return


class Mota(Transportes):
    fator=1.20
    def __init__(self, distancia):
        super().__init__(distancia)


    def calcular_frete(self):
        return self.distancia * self.fator


class Caminhao(Transportes):
    fator=1.20
    def __init__(self, distancia):
        super().__init__(distancia)


    def calcular_frete(self):
        if self.distancia < 50:
            return "0£. So são feitas entregas de caminhão para uma distancia superior a 50km"
        else:
            return self.distancia * self.fator


class Drone(Transportes):
    fator= 9.50
    def __init__(self, distancia):
        super().__init__(distancia)


    def calcular_frete(self):
        if self.distancia > 10:
            return "0. So são feitas entregas de drone para uma distancia inderior a 10km"
        
        else:
            return self.distancia * self.fator