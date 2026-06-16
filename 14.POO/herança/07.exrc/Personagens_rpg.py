from abc import ABC, abstractmethod
from random import randint, randrange
class Personagens(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    
    def atacar(self, alvo, forca=50):
        if self.vida > 0 and alvo.vida > 0: 
            golpe = self.golpes[randrange(0, len(self.golpes))]
            print(f"{self.nome} atacou atacou {alvo.nome} com um {golpe}")
            alvo.receber_danos(forca)
        else:
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer")
            #O parametro de um metodo pode ser instancia de um objeto


    def receber_danos(self, dano):
        fator = randint(1, dano)
        self.vida -= fator
        if self.vida <= 0:
            self.vida = 0
            print("GAMEOVER")
        print(f"O {self.nome} recebeu um dano de {fator}")


    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagens):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes =["Soco", "Golpe de machado", "Pulo giratorio"]

    def curar(self):
        fator = randint(0, 100)
        self.vida += fator
        print(f"O {self.nome} enrolou uma atacura no ferimento e recuperou {fator} pontos de vida")

class Mago(Personagens):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de fogo", "Raio de luz", "Magia estatica"]
        

    
    def curar(self):
        fator = randint(0, 100)
        self.vida += fator
        print(f"O {self.nome} fez um feitiço de cura e recuperou {fator} pontps de vida")
