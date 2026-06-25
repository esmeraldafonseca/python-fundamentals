class Casa:
    todas_as_casas =[]
    def __init__(self, quantidade_quartos, quantidade_banheiro, vagas_garagem):
        self.quantidade_quartos = quantidade_quartos
        self.quantidade_banheiro = quantidade_banheiro
        self.vagas_garagem = vagas_garagem

        self.todas_as_casas.append(self)#recebe o proprio objeto

    def descricao(self):
        return f'Quartos: {self.quantidade_quartos}\nBanheiros: {self.quantidade_banheiro}\nVagas na garagem: {self.vagas_garagem}'


    @classmethod
    def filto_quartos(cls, quantidade_quartos):
        casa_filtrada =[]

        for itens in cls.todas_as_casas:
            if itens.quantidade_quartos >= quantidade_quartos:
                casa_filtrada.append(itens)

        return casa_filtrada

