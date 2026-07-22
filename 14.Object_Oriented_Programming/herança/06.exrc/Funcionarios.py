from abc import ABC, abstractmethod

class Funcionarios(ABC):
    salario_min = 1612
    inss = 0.075
    def __init__(self, nome):
        self.nome = nome
        self.salario = 0
        
    
    @abstractmethod
    def calcular_salario(self):
        pass


    def analisar_salario(self):
        base = self.salario / self.salario_min
        print(f"{"Analise de salario":-^50}")
        print(f"O salario de {self.nome} é de {self.salario:.2f}")
        print(f"E isso é equi valente a {base:.2f} do salario minimo")
        print("-"*50)



class Horista(Funcionarios):
    def __init__(self, nome, valor_hora =7.37 , horas_trabalhadas=220):
        super().__init__(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
        self.salario_brutof = horas_trabalhadas * valor_hora

    
    def calcular_salario(self):
        self.salario = self.salario_brutof - (self.salario_brutof * self.inss)
       


class Mensalista(Funcionarios):
    def __init__(self, nome, salario_bruto = Funcionarios.salario_min):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    
    def calcular_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * self.inss)
