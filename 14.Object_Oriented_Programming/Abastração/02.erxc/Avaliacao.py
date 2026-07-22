class Avaliacao():
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota


#metodos acessores
    def get_nota(self): #metodo setter
        return self._nota


    def set_nota(self, valor): #metodo getter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Valor invalido")